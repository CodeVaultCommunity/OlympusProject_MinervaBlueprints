"""Meaningful positive, negative, portability and read-only checks for this edition."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

from minerva_blueprints.validation import read_yaml, validate

EDITION = Path(__file__).resolve().parents[1]


class TestBlueprintValidation(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='minerva-test-')
        self.root = Path(self.tmp.name) / 'ecosystem'
        shutil.copytree(EDITION / 'examples/task-board-ecosystem', self.root)
        self.path = self.root / 'docs/L2_MinervaBlueprints/blueprint.yaml'
        self.data = read_yaml(self.path)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self):
        self.path.write_text(yaml.safe_dump(self.data, sort_keys=False, allow_unicode=True), encoding='utf-8')

    def result(self, code=None, exit_code=1, **kwargs):
        self.write()
        report = validate(self.path, self.root, **kwargs)
        self.assertEqual(exit_code, report['exit_code'], report['diagnostics'])
        if code:
            self.assertIn(code, {x['code'] for x in report['diagnostics']}, report['diagnostics'])
        return report

    def test_full_blueprint_has_three_cases_and_eleven_criteria(self):
        report = self.result(exit_code=0)
        self.assertEqual(3, report['counts']['cases'])
        self.assertEqual(3, report['counts']['behavioral_tests'])
        self.assertEqual(11, report['counts']['criteria'])
        self.assertEqual(16, report['counts']['documents'])
        self.assertEqual('not_requested', report['code_check'])

    def test_minimal_and_planned_validate_before_code(self):
        for name in ('minimal', 'planned'):
            with self.subTest(name=name):
                root = EDITION / 'examples' / name
                report = validate(root / 'docs/L2_MinervaBlueprints/blueprint.yaml', root)
                self.assertEqual(0, report['exit_code'], report['diagnostics'])
                self.assertEqual(1, report['counts']['cases'])

    def test_starter_is_draft_not_full_model(self):
        path = EDITION / 'implementations/yaml/starter.minerva.yaml'
        self.assertEqual(4, validate(path, EDITION)['exit_code'])
        self.assertEqual(0, validate(path, EDITION, structure_only=True)['exit_code'])

    def test_reviewed_empty_model_is_not_coverage(self):
        self.data['source_l1']['case_ids'] = []
        self.data['adpm']['cases'] = []
        self.data['advs']['behavioral_tests'] = []
        self.result('ADMV_EMPTY')

    def test_missing_advs(self):
        del self.data['advs']
        self.result('SCHEMA_INVALID')

    def test_duplicate_direct_behavioral_test(self):
        duplicate = copy.deepcopy(self.data['advs']['behavioral_tests'][0])
        duplicate['id'] = 'BT-TASK-DUPLICATE'
        self.data['advs']['behavioral_tests'].append(duplicate)
        self.result('TEST_BIJECTION')

    def test_extra_program_case(self):
        duplicate = copy.deepcopy(self.data['adpm']['cases'][0])
        duplicate['id'] = 'UC-TASK-EXTRA'
        self.data['adpm']['cases'].append(duplicate)
        self.result('CASE_BIJECTION')

    def test_duplicate_identity(self):
        self.data['adpm']['entities'].append(copy.deepcopy(self.data['adpm']['entities'][0]))
        self.result('ID_DUPLICATE')

    def test_unknown_criterion(self):
        self.data['advs']['behavioral_tests'][0]['scenarios'][0]['criteria_refs'].append('AC-DOES-NOT-EXIST')
        self.result('CRITERION_REF')

    def test_uncovered_criterion(self):
        criterion = 'AC-TASK-001-PERSISTENCE'
        for bt in self.data['advs']['behavioral_tests']:
            for scenario in bt['scenarios']:
                scenario['criteria_refs'] = [x for x in scenario['criteria_refs'] if x != criterion]
        for support in self.data['advs']['supporting_checks']:
            support['criteria_refs'] = [x for x in support['criteria_refs'] if x != criterion]
        self.result('CRITERION_UNCOVERED')

    def test_wrong_case_criterion(self):
        self.data['advs']['behavioral_tests'][0]['scenarios'][0]['criteria_refs'].append('AC-TASK-002-EMPTY')
        self.result('CRITERION_OWNER')

    def test_missing_denial_scenario(self):
        bt = self.data['advs']['behavioral_tests'][0]
        bt['scenarios'] = [s for s in bt['scenarios'] if s['actor_context'] != 'unresolved']
        self.result('AUTH_COVERAGE')

    def test_unknown_actor(self):
        self.data['adpm']['cases'][0]['permission']['allowed_actor_refs'] = ['ACT-UNKNOWN']
        self.result('ACTOR_REF')

    def test_context_input_must_be_declared(self):
        self.data['adpm']['cases'][0]['permission']['context_input'] = 'missing'
        self.result('AUTH_INPUT')

    def test_entity_reference_cannot_resolve_to_tool(self):
        self.data['adpm']['cases'][0]['outputs'][0]['type'] = {'kind': 'entity', 'ref': 'TOL-TASK-STORE'}
        self.result('REF_WRONG_TYPE')

    def test_entity_cannot_depend_on_tool(self):
        self.data['adpm']['entities'][0]['dependencies'].append('TOL-TASK-STORE')
        self.result('REF_WRONG_TYPE')

    def test_tool_cannot_repeat_entity_invariants(self):
        self.data['adpm']['tools'][0]['operations'][0]['revalidates_rule_refs'] = ['RULE-TASK-TITLE']
        self.result('ENTITY_REVALIDATION')

    def test_case_composition_requires_forwarded_context(self):
        dep = copy.deepcopy(self.data['adpm']['dependencies'][0])
        dep.update(id='DEP-COMPOSE-NEGATIVE', consumer_ref='UC-TASK-001', provider_ref='UC-TASK-002', context_forwarding=None)
        self.data['adpm']['dependencies'].append(dep)
        self.result('CASE_CONTEXT')

    def test_case_composition_preserves_independent_permissions(self):
        dep = copy.deepcopy(self.data['adpm']['dependencies'][0])
        dep.update(id='DEP-COMPOSE-POSITIVE', consumer_ref='UC-TASK-001', provider_ref='UC-TASK-002',
                   context_forwarding='Forward the same trusted actor_context; called list case still requires tasks:read.')
        self.data['adpm']['dependencies'].append(dep)
        self.result(exit_code=0)

    def test_graph_edge_requires_declared_node(self):
        self.data['adpm']['graphs'][0]['edges'][0]['to'] = 'NODE-NOT-DECLARED'
        self.result('GRAPH_EDGE')

    def test_legitimate_state_machine_self_loop(self):
        graph = next(g for g in self.data['adpm']['graphs'] if g['kind'] == 'state_machine')
        self.assertTrue(any(e['from'] == e['to'] for e in graph['edges']))
        self.result(exit_code=0)

    def test_unreachable_node_is_reported(self):
        self.data['adpm']['graphs'][0]['nodes'].append({'id': 'NODE-UNREACHABLE', 'kind': 'state', 'description': 'Unreachable declaration.'})
        self.result('GRAPH_UNREACHABLE')

    def test_uncovered_channel_obligation(self):
        self.data['advs']['channel_obligations'].append({'id': 'CHANNEL-HTTP-NEW', 'case_refs': ['UC-TASK-001'],
            'source': 'L4 interaction design review', 'statement': 'Successful request produces declared HTTP representation.'})
        self.result('CHANNEL_UNCOVERED')

    def test_observed_execution_needs_evidence(self):
        self.data['advs']['executions'].append({'id': 'EXEC-UNSUPPORTED-CLAIM', 'check_refs': ['BT-TASK-001'],
            'implementation_revision': 'unknown', 'environment': 'test', 'result': 'passed',
            'observed_at': None, 'report': None, 'limitations': []})
        self.result('EXECUTION_EVIDENCE')

    def test_unsupported_l1_adapter_is_distinct(self):
        self.data['source_l1']['model_version'] = 'Stable-v9.0.0'
        self.result('L1_PROFILE_UNSUPPORTED', exit_code=2)

    def test_unsupported_yaml_profile_is_distinct(self):
        self.data['profile_version'] = '9.0.0'
        self.result('PROFILE_UNSUPPORTED', exit_code=2)

    def test_source_content_pin(self):
        self.data['source_l1']['sha256'] = '0' * 64
        self.result('L1_HASH')

    def test_source_identity_pin(self):
        self.data['source_l1']['revision'] = '999'
        self.result('L1_IDENTITY')

    def test_missing_l1_is_operational_error(self):
        self.data['source_l1']['artifact'] = 'missing.json'
        self.result('L1_IO', exit_code=3)

    def test_malformed_l1_is_validation_error(self):
        source_path = self.root / self.data['source_l1']['artifact']
        origin = json.loads(source_path.read_text())
        origin['atlas']['use_cases'] = ['malformed']
        source_path.write_text(json.dumps(origin))
        self.data['source_l1']['sha256'] = None
        self.result('L1_FORMAT')

    def test_escaping_path_is_rejected(self):
        self.data['source_l1']['artifact'] = '../escape.json'
        self.result('SCHEMA_INVALID')

    def test_mirror_preserves_source_extension(self):
        relative = self.data['mirror']['documents'][0]
        changed = relative.replace('.py.yaml', '.yaml')
        (self.root / relative).rename(self.root / changed)
        self.data['mirror']['documents'][0] = changed
        self.result('MIRROR_PATH')

    def test_duplicate_yaml_keys(self):
        self.path.write_text(self.path.read_text() + '\nkind: blueprint\n')
        report = validate(self.path, self.root)
        self.assertEqual(1, report['exit_code'])
        self.assertIn('YAML_INVALID', {x['code'] for x in report['diagnostics']})

    def test_tags_and_aliases_are_data_errors(self):
        for text in ('value: !!python/object/apply:os.system [echo forbidden]', 'value: &anchor text\ncopy: *anchor'):
            with self.subTest(text=text):
                self.path.write_text(text)
                report = validate(self.path, self.root)
                self.assertEqual(1, report['exit_code'])
                self.assertEqual('YAML_INVALID', report['diagnostics'][0]['code'])

    def test_predictable_scalar_subset(self):
        self.path.write_text('a: true\nb: false\nc: null\nd: yes\ne: 2026-10-28\nf: 1e3\ng: 012\n')
        data = read_yaml(self.path)
        self.assertIs(data['a'], True)
        self.assertIs(data['b'], False)
        self.assertIsNone(data['c'])
        self.assertEqual('yes', data['d'])
        self.assertEqual('2026-10-28', data['e'])
        self.assertEqual(1000.0, data['f'])
        self.assertEqual('012', data['g'])

    def test_code_absence_is_explicitly_inconclusive_when_requested(self):
        self.result('CODE_UNAVAILABLE', exit_code=4, verify_code=True)
        self.result(exit_code=0)

    def test_legacy_multi_unit_record_is_not_admv_claim(self):
        root = EDITION / 'examples/legacy'
        path = root / 'docs/L2_MinervaBlueprints/apps/LegacyReports/reports.py.yaml'
        self.assertGreater(len(read_yaml(path)['units']), 1)
        report = validate(path, root)
        self.assertEqual(0, report['exit_code'], report['diagnostics'])
        self.assertEqual('source_record_only', report['layer_coverage'])

    def test_qualified_support_symbol_requires_correct_owner(self):
        self.data = read_yaml(EDITION / 'examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml')
        code = self.root / 'apps/Support/Test.py'
        code.parent.mkdir(parents=True)
        code.write_text('class Expected:\n    pass\n\nclass Other:\n    def testRun(self):\n        pass\n')
        self.data['advs']['supporting_checks'][0]['reference'] = {
            'path': 'apps/Support/Test.py', 'symbol': 'Expected.testRun', 'status': 'observed'}
        self.result('CHECK_SYMBOL', verify_code=True)
        self.data['advs']['supporting_checks'][0]['reference']['symbol'] = 'Other.testRun'
        self.result(exit_code=0, verify_code=True)

    def test_alternative_document_root_preserves_mirror_mapping(self):
        old_root = self.root / 'docs/L2_MinervaBlueprints'
        new_root = self.root / 'design/program'
        new_root.parent.mkdir(parents=True)
        old_root.rename(new_root)
        self.path = new_root / 'blueprint.yaml'
        self.data['mirror']['root'] = 'design/program'
        self.data['mirror']['documents'] = [x.replace('docs/L2_MinervaBlueprints/', 'design/program/', 1) for x in self.data['mirror']['documents']]
        self.result(exit_code=0)

    def test_shared_criterion_links_existing_behavioral_tests(self):
        source_path = self.root / self.data['source_l1']['artifact']
        source = json.loads(source_path.read_text())
        source['atlas'].setdefault('extensions', {})['minerva_shared_criteria'] = [
            {'id': 'AC-SHARED-ROUNDTRIP', 'case_ids': ['UC-TASK-001', 'UC-TASK-002'],
             'statement': 'A created task is readable by a permitted listing call in the same store.'}]
        source_path.write_text(json.dumps(source))
        self.data['source_l1']['sha256'] = hashlib.sha256(source_path.read_bytes()).hexdigest()
        support = copy.deepcopy(self.data['advs']['supporting_checks'][0])
        support.update(id='CHECK-SHARED-ROUNDTRIP', behavioral_test_refs=['BT-TASK-001', 'BT-TASK-002'],
                       criteria_refs=['AC-SHARED-ROUNDTRIP'], case_refs=['UC-TASK-001', 'UC-TASK-002'])
        self.data['advs']['supporting_checks'].append(support)
        for bt in self.data['advs']['behavioral_tests'][:2]:
            bt['criteria_refs'].append('AC-SHARED-ROUNDTRIP')
            bt['supporting_check_refs'].append('CHECK-SHARED-ROUNDTRIP')
        report = self.result(exit_code=0)
        self.assertEqual(3, report['counts']['behavioral_tests'])
        self.assertEqual(12, report['counts']['criteria'])
        support['behavioral_test_refs'].remove('BT-TASK-002')
        self.result('SHARED_CRITERION_LINK')

    def test_public_counterexamples_match_documented_expectations(self):
        process = subprocess.run([sys.executable, str(EDITION / 'examples/counterexamples/check.py'), '--json'], capture_output=True, text=True)
        self.assertEqual(0, process.returncode, process.stderr)
        report = json.loads(process.stdout)
        self.assertTrue(report['passed'])
        self.assertEqual(13, report['fixture_count'])

    def test_source_behavior_can_reference_its_local_graph(self):
        relative = next(p for p in self.data['mirror']['documents'] if p.endswith('/Entity_Task.py.yaml'))
        path = self.root / relative
        source = read_yaml(path)
        unit = source['units'][0]
        source['graphs'].append({'id': 'GRAPH-LOCAL-TASK', 'owner_ref': unit['id'], 'kind': 'flow',
            'summary': 'Local terminal result for this source unit.', 'entry': 'NODE-LOCAL-RETURN',
            'nodes': [{'id': 'NODE-LOCAL-RETURN', 'kind': 'end', 'description': 'Return the described local result.'}], 'edges': []})
        unit['operations'][0]['behavior']['graph_refs'].append('GRAPH-LOCAL-TASK')
        path.write_text(yaml.safe_dump(source, sort_keys=False))
        report = self.result(exit_code=0)
        self.assertEqual(5, report['counts']['graphs'])

    def test_cli_json_distinguishes_success_draft_and_operational_error(self):
        targets = ((self.path, 0), (EDITION / 'implementations/yaml/starter.minerva.yaml', 4), (self.root / 'missing.yaml', 3))
        for path, expected in targets:
            with self.subTest(expected=expected):
                completed = subprocess.run([sys.executable, str(EDITION / 'validator/minerva_validate.py'), str(path), '--root', str(self.root), '--json'], capture_output=True, text=True)
                self.assertEqual(expected, completed.returncode, completed.stderr)
                report = json.loads(completed.stdout)
                self.assertEqual(expected, report['exit_code'])
                self.assertIn('diagnostics', report)


class TestReadOnlyCodeInspection(unittest.TestCase):
    def test_inspection_never_imports_and_detects_changed_bytes(self):
        with tempfile.TemporaryDirectory(prefix='minerva-read-only-') as folder:
            root = Path(folder)
            code = root / 'apps/Demo/Example.py'
            code.parent.mkdir(parents=True)
            code.write_text("raise RuntimeError('must never run')\n\nclass Example:\n    def run(self):\n        return 1\n")
            path = root / 'docs/L2_MinervaBlueprints/apps/Demo/Example.py.yaml'
            path.parent.mkdir(parents=True)
            behavior = {'summary': 'Return the integer one.', 'steps': ['Return one.'], 'preconditions': [], 'postconditions': ['Result is one.'], 'effects': [], 'graph_refs': []}
            document = {'format': 'minerva-yaml', 'model_version': 'Alpha-v0.1.0', 'profile_version': '0.1.0', 'kind': 'source',
                'document_id': 'FILE-DEMO-EXAMPLE', 'source': {'path': 'apps/Demo/Example.py', 'app': 'Demo', 'language': 'python',
                'state': 'observed', 'sha256': hashlib.sha256(code.read_bytes()).hexdigest(), 'purpose': 'Read-only inspection fixture.', 'observation': 'Bytes created by this test.'},
                'units': [{'id': 'UNIT-DEMO-EXAMPLE', 'code_name': 'Example', 'kind': 'class', 'role': 'support', 'model_refs': [],
                'description': 'A class behind top-level code that would raise if imported.', 'attributes': [], 'operations': [{'id': 'OP-DEMO-RUN', 'code_name': 'run',
                'contract_scope': 'operational', 'native_signature': 'run(self)', 'description': 'Return one.', 'inputs': [], 'outputs': [{'name': 'result', 'description': 'The integer one.', 'type': {'kind': 'primitive', 'name': 'integer'}, 'required': True}],
                'technical_parameters': [], 'behavior': behavior}]}], 'graphs': [], 'dependencies': [], 'limitations': ['Inspection does not establish runtime behavior.']}
            path.write_text(yaml.safe_dump(document, sort_keys=False))
            report = validate(path, root, verify_code=True)
            self.assertEqual(0, report['exit_code'], report['diagnostics'])
            self.assertEqual(1, report['counts']['code_files'])
            code.write_text(code.read_text() + '\n# changed bytes\n')
            report = validate(path, root, verify_code=True)
            self.assertEqual(1, report['exit_code'])
            self.assertIn('CODE_HASH_MISMATCH', {x['code'] for x in report['diagnostics']})


if __name__ == '__main__':
    unittest.main()
