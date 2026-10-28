"""Validate Minerva declarations; never interpret a source model or execute code."""
from __future__ import annotations
import ast
import fnmatch
import hashlib
from pathlib import Path
from typing import Any
import yaml
from jsonschema import Draft202012Validator
from . import MODEL_VERSION, PROFILE_VERSION
from .loading import InputError, read_yaml, read_json, safe_path
from .code_inspection import CodeInspectionMixin, resolve_python_symbol

def schema() -> dict:
    path = Path(__file__).resolve().parent / 'schemas' / 'minerva.schema.json'
    return read_json(path)


def walk(value: Any, path='$'):
    if isinstance(value, dict):
        yield value, path
        for key, child in value.items():
            yield from walk(child, path + '/' + key)
    elif isinstance(value, list):
        for index, child in enumerate(value): yield from walk(child, path + '/' + str(index))


class Inspection(CodeInspectionMixin):
    def __init__(self, root, *, structure_only=False, verify_code=False):
        self.root = Path(root).resolve()
        self.structure_only = structure_only
        self.verify_code = verify_code
        self.report = {'tool_version': '0.1.0a0', 'model_version': MODEL_VERSION,
                       'profile_version': PROFILE_VERSION, 'status': 'passed',
                       'exit_code': 0, 'validation_level': 'structure' if structure_only else 'consistency',
                       'layer_coverage': 'not_assessed', 'code_check': 'not_requested',
                       'counts': {'documents': 0, 'cases': 0, 'behavioral_tests': 0,
                                  'criteria': 0, 'scenarios': 0, 'graphs': 0, 'code_files': 0},
                       'diagnostics': [],
                       'limitations': [
                           'Structural and consistency checks do not prove behavioral correctness, sufficient scenarios or OAL conformance.',
                           'Project code and YAML command text are never executed or imported.',
                           'Textual rules, trust policies, algorithm equivalence and contextual-condition adequacy require review.',
                           'Python code inspection, when requested, checks top-level names and hashes; it does not prove runtime behavior.'
                       ]}
        self.all_ids = {}
        self.documents = []
        self.validator = Draft202012Validator(schema())

    def add(self, code, document, element, message, severity='error'):
        self.report['diagnostics'].append({'code': code, 'severity': severity,
            'document': str(document), 'element': str(element), 'message': message})

    def load(self, path):
        try:
            data = read_yaml(path)
        except (OSError, UnicodeError) as error:
            self.add('IO_ERROR', path, '$', str(error)); self.report['exit_code'] = 3; return None
        except (InputError, yaml.YAMLError, RecursionError) as error:
            self.add('YAML_INVALID', path, '$', str(error)); return None
        if data.get('format') != 'minerva-yaml' or data.get('model_version') != MODEL_VERSION or data.get('profile_version') != PROFILE_VERSION:
            self.add('PROFILE_UNSUPPORTED', path, '$', 'This tool supports minerva-yaml, Alpha-v0.1.0, profile 0.1.0 only.')
            self.report['exit_code'] = 2; return None
        if data.get('kind') not in ('blueprint', 'source'):
            self.add('DOCUMENT_KIND', path, '$/kind', 'Expected blueprint or source.'); return None
        selected = dict(self.validator.schema)
        selected.pop('oneOf', None)
        selected['$ref'] = '#/$defs/' + data['kind']
        errors = sorted(Draft202012Validator(selected).iter_errors(data), key=lambda e: str(e.path))
        for error in errors:
            self.add('SCHEMA_INVALID', path, '/'.join(map(str, error.path)), error.message)
        if errors: return None
        self.report['counts']['documents'] += 1
        self.documents.append((path, data))
        return data

    def collect(self, document, data):
        for value, path in walk({key: value for key, value in data.items() if key != 'source_l1'}):
            if 'id' in value:
                identity = value['id']
                if identity in self.all_ids:
                    self.add('ID_DUPLICATE', document, path, f'{identity} is already declared at {self.all_ids[identity][1]}.')
                else: self.all_ids[identity] = (value, path, str(document))
        if data['kind'] == 'source':
            identity = data['document_id']
            if identity in self.all_ids: self.add('ID_DUPLICATE', document, '$/document_id', identity)
            else: self.all_ids[identity] = (data, '$/document_id', str(document))

    def target(self, identity, document, element, allowed=None):
        item = self.all_ids.get(identity)
        if not item:
            self.add('REF_UNRESOLVED', document, element, f'Unknown element {identity}.'); return None
        if allowed is not None and identity not in allowed:
            self.add('REF_WRONG_TYPE', document, element, f'{identity} does not identify the required kind of element.')
            return None
        return item[0]

    def graphs(self, document, graphs, *, owner_ids=None):
        for graph in graphs:
            self.report['counts']['graphs'] += 1
            self.target(graph['owner_ref'], document, graph['id'] + '/owner_ref', owner_ids)
            nodes = {node['id']: node for node in graph['nodes']}
            if graph['entry'] not in nodes:
                self.add('GRAPH_ENTRY', document, graph['id'], 'Entry is not a node of this graph.')
            adjacency = {identity: [] for identity in nodes}
            for edge in graph['edges']:
                if edge['from'] not in nodes or edge['to'] not in nodes:
                    self.add('GRAPH_EDGE', document, edge['id'], 'An edge endpoint is not a node of this graph.')
                else: adjacency[edge['from']].append(edge['to'])
            reachable = set(); pending = [graph['entry']]
            while pending:
                current = pending.pop()
                if current not in reachable:
                    reachable.add(current); pending.extend(adjacency.get(current, []))
            for identity in set(nodes) - reachable:
                self.add('GRAPH_UNREACHABLE', document, identity, 'This node is unreachable from the declared entry.')
            if graph['kind'] == 'flow' and not any(n['kind'] in ('end', 'failure') for n in nodes.values()):
                self.add('GRAPH_TERMINAL', document, graph['id'], 'A supported finite flow declares at least one end or failure node.')
            # Cycles are valid. This structural check is not a termination proof.

    def source_links(self, path, data):
        units = {unit['id'] for unit in data['units']}
        for dependency in data['dependencies']:
            self.target(dependency['from_unit'], path, 'dependencies/from_unit', units)

    def source_l1(self, path, data):
        """Inspect the authored Minerva source catalogue, not the L1 file format.

        The artifact is opaque bytes. Catalogue fidelity to that artifact is a
        separate documented review, even when the SHA-256 matches.
        """
        source = data['source_l1']
        if source['artifact'] is None:
            self.add('L1_MISSING', path, 'source_l1', 'A reviewed blueprint requires a pinned source artifact.')
        else:
            try:
                origin = safe_path(self.root, source['artifact'])
                if source['sha256'] is None:
                    self.add('L1_HASH_REQUIRED', path, 'source_l1/sha256', 'Reviewed source references require a SHA-256.')
                elif hashlib.sha256(origin.read_bytes()).hexdigest() != source['sha256']:
                    self.add('L1_HASH', path, 'source_l1/sha256', 'Pinned source bytes differ.')
            except InputError as error:
                self.add('PATH_INVALID', path, 'source_l1/artifact', str(error))
            except OSError as error:
                self.add('L1_IO', path, 'source_l1/artifact', str(error))
                self.report['exit_code'] = 3
        self.source_elements = {}
        for element in source['catalog']:
            ref = element['ref']
            if ref in self.source_elements:
                self.add('L1_DUPLICATE', path, ref, 'Duplicate source-catalogue identity.')
            self.source_elements[ref] = element
        all_cases = {ref: item for ref, item in self.source_elements.items() if item['kind'] == 'case'}
        actors = {ref: item for ref, item in self.source_elements.items() if item['kind'] == 'actor'}
        selected = source['case_ids']
        if len(selected) != len(set(selected)):
            self.add('L1_SELECTION', path, 'source_l1/case_ids', 'Selected source cases are duplicated.')
        for identity in selected:
            self.source_target(identity, path, 'source_l1/case_ids', {'case'})
        for ref, item in self.source_elements.items():
            for owner in item.get('case_refs', []):
                self.source_target(owner, path, ref, {'case'})
            for actor in item.get('actor_refs', []):
                self.source_target(actor, path, ref, {'actor'})
            if item['kind'] == 'case' and not item.get('actor_refs'):
                self.add('L1_CASE_ACTORS', path, ref, 'Declare the source case permitted actor set.')
            if item['kind'] == 'criterion' and not item.get('case_refs'):
                self.add('L1_CRITERION_SCOPE', path, ref, 'Declare criterion ownership.')
        cases = {ref: all_cases[ref] for ref in selected if ref in all_cases}
        criteria = {ref: set(item['case_refs']) & set(cases)
                    for ref, item in self.source_elements.items()
                    if item['kind'] == 'criterion' and set(item.get('case_refs', [])) & set(cases)}
        self.report['counts']['criteria'] = len(criteria)
        self.report['source_check'] = 'opaque_bytes_and_declared_catalog'
        self.report['limitations'].append('Source catalogue and mappings are authored Minerva declarations. No source-model reader is included; fidelity to the pinned L1 content requires separate review.')
        return cases, criteria, actors

    def source_target(self, identity, document, element, kinds=None):
        item = self.source_elements.get(identity)
        if item is None:
            self.add('SOURCE_REF_UNRESOLVED', document, element, f'Unknown declared source element {identity}.')
        elif kinds is not None and item['kind'] not in kinds:
            self.add('SOURCE_REF_WRONG_TYPE', document, element, f'{identity} has source kind {item["kind"]}; expected {sorted(kinds)}.')
            return None
        return item

    def consistency(self, path, data):
        if data['kind'] == 'source':
            self.collect(path, data); self.graphs(path, data['graphs']); self.source_links(path, data); self.source_code(path, data)
            self.report['layer_coverage'] = 'source_record_only'
            self.add('SOURCE_SCOPE', path, '$', 'A source record alone does not constitute ADMV coverage.', 'info')
            return
        if data['document']['status'] == 'draft':
            self.add('DRAFT_INCOMPLETE', path, 'document/status', 'Draft is structurally readable; complete ADMV consistency has not been claimed.', 'inconclusive')
            self.report['layer_coverage'] = 'draft'; return
        self.collect(path, data)
        adpm, advs = data['adpm'], data['advs']
        sources = []
        for relative in data['mirror']['documents']:
            try: source_path = safe_path(self.root, relative)
            except InputError as error:
                self.add('PATH_INVALID', path, 'mirror/documents', str(error)); continue
            source = self.load(source_path)
            if source is None: continue
            if source['kind'] != 'source':
                self.add('MIRROR_KIND', source_path, '$/kind', 'Mirror documents must be source records.'); continue
            expected = data['mirror']['root'].rstrip('/') + '/' + source['source']['path'] + '.yaml'
            if relative != expected:
                self.add('MIRROR_PATH', source_path, 'source/path', f'Expected {expected}; keep the complete source extension.')
            if any(item[1]['source']['path'] == source['source']['path'] for item in sources):
                self.add('MIRROR_DUPLICATE', source_path, 'source/path', 'A source has multiple mirror records.')
            sources.append((source_path, source)); self.collect(source_path, source)
        cases_l1, criteria, actors = self.source_l1(path, data)
        if not data['source_l1']['case_ids'] or not adpm['cases'] or not advs['behavioral_tests']:
            self.add('ADMV_EMPTY', path, '$', 'A reviewed blueprint declares a nonempty source scope, program cases and behavioral tests.')
        cases = {item['id']: item for item in adpm['cases']}
        entities = {item['id']: item for item in adpm['entities']}
        types = {item['id']: item for item in adpm['types']}
        tools = {item['id']: item for item in adpm['tools']}
        operations = {op['id']: op for tool in adpm['tools'] for op in tool['operations']}
        rules = {item['id']: item for item in adpm['rules']}
        graphs = {item['id']: item for item in adpm['graphs']}
        graph_ids = set(graphs) | {graph['id'] for _, source in sources for graph in source['graphs']}
        tests = {item['id']: item for item in advs['behavioral_tests']}
        supports = {item['id']: item for item in advs['supporting_checks']}
        channels = {item['id']: item for item in advs['channel_obligations']}
        domains = {item['id']: item for item in adpm['domains']}
        model_ids = set(cases)|set(entities)|set(tools)|set(operations)|set(types)|set(rules)
        self.report['counts']['cases'] = len(cases)
        self.report['counts']['behavioral_tests'] = len(tests)
        case_sources = [item['source_case_id'] for item in adpm['cases']]
        test_sources = [item['source_case_id'] for item in advs['behavioral_tests']]
        if sorted(case_sources) != sorted(cases_l1): self.add('CASE_BIJECTION', path, 'adpm/cases', 'Exactly one program case is required for each selected source case, with no extras.')
        if sorted(test_sources) != sorted(cases_l1): self.add('TEST_BIJECTION', path, 'advs/behavioral_tests', 'Exactly one directly linked behavioral test is required for each selected source case, with no extras.')
        for document, structure in self.documents:
            for item, location in walk({key: value for key, value in structure.items() if key != 'source_l1'}):
                if item.get('kind') == 'entity' and 'ref' in item: self.target(item['ref'], document, location, entities)
                if item.get('kind') == 'type' and 'ref' in item: self.target(item['ref'], document, location, types)
                if 'graph_refs' in item:
                    for identity in item['graph_refs']: self.target(identity, document, location, graph_ids)
        for entity in entities.values():
            if entity['source_entity_id'] is not None:
                self.source_target(entity['source_entity_id'], path, entity['id'], {'entity'})
            for identity in entity['invariant_refs']:
                rule = self.target(identity, path, entity['id'], rules)
                if rule and (rule['kind'] != 'invariant' or rule['owner_ref'] != entity['id']):
                    self.add('ENTITY_INVARIANT', path, entity['id'], 'An invariant reference must identify an invariant owned by this entity; transition rules belong to behavior.')
            for identity in entity['dependencies']:
                self.target(identity, path, entity['id'], set(entities)|set(types))
        for rule in rules.values():
            if not rule['origin_refs']:
                self.add('RULE_ORIGIN_MISSING', path, rule['id'], 'An inherited rule or added decision needs an explicit origin.')
            for origin in rule['origin_refs']:
                if origin in {d['id'] for d in data['document']['decisions']}:
                    continue
                self.source_target(origin, path, rule['id'], {'validation', 'requirement', 'field', 'entity', 'case'})
            self.target(rule['owner_ref'], path, rule['id'], set(entities)|set(cases))
        for tool in tools.values():
            for identity in tool['dependencies']: self.target(identity, path, tool['id'], set(tools)|set(entities)|set(types))
            for operation in tool['operations']:
                for identity in operation['canonical_construction_refs']: self.target(identity, path, operation['id'], entities)
                if operation['revalidates_rule_refs']:
                    self.add('ENTITY_REVALIDATION', path, operation['id'], 'Tools cannot repeat entity-internal invariant validation on ready entities.')
        for case in cases.values():
            for identity in case['collaborators']: self.target(identity, path, case['id'], set(tools)|set(operations)|set(entities)|set(cases))
            for identity in case['rule_refs']: self.target(identity, path, case['id'], rules)
            if case['domain_ref'] is not None: self.target(case['domain_ref'], path, case['id'], domains)
            permission = case['permission']
            if len(permission['deny_contexts']) != 4 or set(permission['deny_contexts']) != {'absent','unresolved','unknown','insufficient'}:
                self.add('AUTH_DENIALS', path, case['id'], 'All four denial categories must be declared exactly once.')
            if permission['context_input'] not in {item['name'] for item in case['inputs']}:
                self.add('AUTH_INPUT', path, case['id'], 'Context input must name a declared case input.')
            for actor in permission['allowed_actor_refs']:
                if actor not in actors:
                    self.add('ACTOR_REF', path, case['id'], f'Unknown declared source actor {actor}.')
                elif actor not in cases_l1.get(case['source_case_id'], {}).get('actor_refs', []):
                    self.add('ACTOR_CASE_PERMISSION', path, case['id'], f'{actor} is not permitted by the declared source case.')
        for case in cases.values():
            domain = domains.get(case['domain_ref'])
            if domain and case['id'] not in domain['case_refs']:
                self.add('DOMAIN_RECIPROCITY', path, case['id'], 'Case and domain links disagree.')
        for domain in domains.values():
            for identity in domain['case_refs']:
                case = self.target(identity, path, domain['id'], cases)
                if case and case.get('domain_ref') != domain['id']: self.add('DOMAIN_RECIPROCITY', path, domain['id'], 'Case and domain links disagree.')
        for dep in adpm['dependencies']:
            self.target(dep['consumer_ref'], path, dep['id'], model_ids)
            self.target(dep['provider_ref'], path, dep['id'], model_ids)
            if dep['consumer_ref'] in entities and dep['provider_ref'] not in set(entities)|set(types):
                self.add('ENTITY_DEPENDENCY', path, dep['id'], 'Entities do not depend on cases or tools.')
            if dep['consumer_ref'] in tools and dep['provider_ref'] in cases:
                self.add('TOOL_CASE_DEPENDENCY', path, dep['id'], 'A tool cannot consume an application case.')
            if dep['consumer_ref'] in cases and dep['provider_ref'] in cases and not dep['context_forwarding']:
                self.add('CASE_CONTEXT', path, dep['id'], 'Case composition declares forwarded actor context and preserves called authorization.')
        for lifetime in adpm['composition']['lifetimes']: self.target(lifetime['element_ref'], path, 'composition/lifetimes', model_ids)
        self.graphs(path, adpm['graphs'], owner_ids=model_ids)
        coverage = {identity:set() for identity in criteria}
        scenario_ids=set()
        obligation_coverage=set()
        for bt in tests.values():
            case = self.target(bt['case_ref'], path, bt['id'], cases)
            if case and case.get('source_case_id') != bt['source_case_id']: self.add('TEST_CASE_LINK', path, bt['id'], 'Behavioral test and program case point to different source cases.')
            for identity in bt['supporting_check_refs']:
                check=self.target(identity,path,bt['id'],supports)
                if check and bt['id'] not in check.get('behavioral_test_refs',[]): self.add('SUPPORT_RECIPROCITY',path,bt['id'],'Supporting-check links must be reciprocal.')
            needed={identity for identity, owners in criteria.items() if bt['source_case_id'] in owners}
            if set(bt['criteria_refs']) != needed: self.add('TEST_CRITERIA',path,bt['id'],'Behavioral-test criteria must match the selected source case and its shared criteria.')
            contexts=set()
            for scenario in bt['scenarios']:
                scenario_ids.add(scenario['id']); self.report['counts']['scenarios'] += 1
                if scenario['applicability']=='applicable': contexts.add(scenario['actor_context'])
                for identity in scenario['criteria_refs']:
                    if identity not in criteria: self.add('CRITERION_REF',path,scenario['id'],f'Unknown criterion {identity}.')
                    elif bt['source_case_id'] not in criteria[identity]: self.add('CRITERION_OWNER',path,scenario['id'],'Criterion belongs to another case.')
                    elif scenario['applicability']=='applicable': coverage[identity].add(bt['source_case_id'])
                for identity in scenario['check_refs']: self.target(identity,path,scenario['id'],supports)
                for identity in scenario['obligation_refs']:
                    obligation = self.target(identity,path,scenario['id'],channels)
                    if obligation and bt['case_ref'] not in obligation['case_refs']:
                        self.add('CHANNEL_CASE', path, scenario['id'], 'Channel obligation does not identify this program case.')
                    if scenario['applicability']=='applicable': obligation_coverage.add(identity)
            required_contexts={'allowed','absent','unresolved','unknown','insufficient'}
            if case and case['permission']['anonymous_allowed']: required_contexts.add('anonymous')
            if not required_contexts.issubset(contexts): self.add('AUTH_COVERAGE',path,bt['id'],'Missing applicable actor-context scenarios: '+', '.join(sorted(required_contexts-contexts)))
        for support in supports.values():
            for identity in support['behavioral_test_refs']:
                bt=self.target(identity,path,support['id'],tests)
                if bt and support['id'] not in bt.get('supporting_check_refs',[]): self.add('SUPPORT_RECIPROCITY',path,support['id'],'Supporting-check links must be reciprocal.')
            for identity in support['case_refs']: self.target(identity,path,support['id'],cases)
            for identity in support['criteria_refs']:
                if identity not in criteria: self.add('CRITERION_REF',path,support['id'],f'Unknown criterion {identity}.'); continue
                linked={tests[t]['source_case_id'] for t in support['behavioral_test_refs'] if t in tests}
                if not criteria[identity].issubset(linked): self.add('SHARED_CRITERION_LINK',path,support['id'],'Shared support must link every participating behavioral test.')
                coverage[identity].update(linked & criteria[identity])
            if self.verify_code and support['reference'] and support['reference']['status']=='observed':
                target=safe_path(self.root,support['reference']['path'])
                if not target.is_file(): self.add('CHECK_UNAVAILABLE',path,support['id'],'Observed supporting-check source is unavailable.','inconclusive')
                elif target.suffix=='.py':
                    tree=ast.parse(target.read_text(encoding='utf-8'))
                    if not resolve_python_symbol(tree, support['reference']['symbol']):
                        self.add('CHECK_SYMBOL',path,support['id'],'Referenced qualified Python symbol is absent from its declared lexical owner.')
        for identity, owners in criteria.items():
            if not owners.issubset(coverage[identity]): self.add('CRITERION_UNCOVERED',path,identity,'Criterion lacks applicable declared verification for every participating case.')
        for obligation in channels.values():
            for identity in obligation['case_refs']:
                self.target(identity, path, obligation['id'], cases)
        for identity in set(channels)-obligation_coverage: self.add('CHANNEL_UNCOVERED',path,identity,'Channel obligation lacks an applicable planned scenario.')
        executable_ids=set(tests)|set(supports)|scenario_ids
        for execution in advs['executions']:
            for identity in execution['check_refs']: self.target(identity,path,execution['id'],executable_ids)
            if execution['result'] != 'not_run' and (not execution['observed_at'] or not execution['report']): self.add('EXECUTION_EVIDENCE',path,execution['id'],'An observed result requires timestamp and evidence report.')
            if execution['report']:
                try:
                    report=safe_path(self.root,execution['report'])
                    if not report.is_file(): self.add('EVIDENCE_MISSING',path,execution['id'],'Referenced execution report is absent.')
                except InputError as error: self.add('PATH_INVALID',path,execution['id'],str(error))
        for source_path, source in sources:
            for unit in source['units']:
                for identity in unit['model_refs']: self.target(identity,source_path,unit['id'],model_ids|set(tests)|set(supports))
            self.graphs(source_path, source['graphs']); self.source_links(source_path, source); self.source_code(source_path,source)
        if self.verify_code and data['mirror']['coverage']=='complete':
            expected={item[1]['source']['path'] for item in sources}
            actual=set()
            for pattern in data['mirror']['include_patterns']:
                if Path(pattern).is_absolute() or '..' in Path(pattern).parts: self.add('PATH_INVALID',path,'mirror/include_patterns','Glob must remain within the root.'); continue
                for candidate in self.root.glob(pattern):
                    relative=candidate.relative_to(self.root).as_posix()
                    if candidate.is_file() and not any(fnmatch.fnmatch(relative,x['pattern']) for x in data['mirror']['exclusions']): actual.add(relative)
            if actual-expected: self.add('MIRROR_COVERAGE',path,'mirror', 'Missing source records: '+', '.join(sorted(actual-expected)))
        for link in data['traceability']:
            self.source_target(link['source_ref'], path, 'traceability')
            for target in link['target_refs']:
                self.target(target, path, 'traceability')
        mapped = {link['source_ref'] for link in data['traceability']}
        required_sources = {ref for ref, item in self.source_elements.items()
                            if item['kind'] in {'requirement', 'criterion'}
                            and set(item.get('case_refs', [])) & set(cases_l1)}
        for missing in sorted(required_sources - mapped):
            self.add('SOURCE_OBLIGATION_UNMAPPED', path, missing, 'An in-scope declared obligation needs an explicit L2 mapping.')
        self.report['layer_coverage']='declared_adpm_and_advs'

    def finish(self):
        errors = any(x['severity']=='error' for x in self.report['diagnostics'])
        incomplete = any(x['severity']=='inconclusive' for x in self.report['diagnostics'])
        if self.report['exit_code'] in (2,3): pass
        elif errors: self.report['exit_code']=1
        elif incomplete: self.report['exit_code']=4
        else: self.report['exit_code']=0
        self.report['status']={0:'passed',1:'invalid',2:'unsupported',3:'operational_error',4:'inconclusive'}[self.report['exit_code']]
        if self.verify_code and self.report['code_check']=='requested': self.report['code_check']='checked' if not errors and not incomplete else 'not_established'
        return self.report


def validate(path, root=None, *, structure_only=False, verify_code=False):
    path=Path(path).resolve(); root=Path(root or Path.cwd()).resolve()
    inspection=Inspection(root,structure_only=structure_only,verify_code=verify_code)
    data=inspection.load(path)
    if data is not None and not structure_only:
        try: inspection.consistency(path,data)
        except (InputError, OSError, UnicodeError, SyntaxError) as error:
            inspection.add('INSPECTION_ERROR',path,'$',str(error)); inspection.report['exit_code']=3
    elif data is not None:
        inspection.add('STRUCTURE_ONLY',path,'$','Only the representation schema was checked; ADMV consistency was not evaluated.','info')
    return inspection.finish()
