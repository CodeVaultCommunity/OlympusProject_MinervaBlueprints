"""Regression checks for Minerva declarations and their assessment limits."""
import ast
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
from minerva_blueprints.loading import InputError, read_yaml, safe_path
from minerva_blueprints.validation import validate
from minerva_blueprints.code_inspection import resolve_python_symbol

EDITION = Path(__file__).resolve().parents[1]


class TestBlueprint(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='minerva-test-')
        self.root = Path(self.tmp.name) / 'ecosystem'
        shutil.copytree(EDITION / 'examples/minimal', self.root)
        self.path = self.root / 'docs/L2_MinervaBlueprints/blueprint.yaml'
        self.data = read_yaml(self.path)

    def tearDown(self):
        self.tmp.cleanup()

    def result(self, code=None, exit_code=1, **options):
        self.path.write_text(yaml.safe_dump(self.data, sort_keys=False, allow_unicode=True), encoding='utf-8')
        result = validate(self.path, self.root, **options)
        self.assertEqual(exit_code, result['exit_code'], result['diagnostics'])
        if code:
            self.assertIn(code, {item['code'] for item in result['diagnostics']}, result['diagnostics'])
        return result

    def test_minimal_covers_official_request_case(self):
        report = self.result(exit_code=0)
        self.assertEqual(1, report['counts']['cases'])
        self.assertEqual(7, report['counts']['criteria'])
        self.assertEqual('UC-REQUEST-SUBMIT', self.data['adpm']['cases'][0]['id'])
        self.assertEqual('opaque_bytes_and_declared_catalog', report['source_check'])

    def test_all_official_examples_and_revisions(self):
        from run_examples import EXAMPLES
        for name, (directory, filename) in EXAMPLES.items():
            with self.subTest(name=name):
                root = EDITION / directory
                report = validate(root / filename, root)
                self.assertEqual(0, report['exit_code'], report['diagnostics'])

    def test_unknown_source_entity(self):
        self.data['adpm']['entities'][0]['source_entity_id'] = 'ENT-NOT-DECLARED'
        self.result('SOURCE_REF_UNRESOLVED')

    def test_entity_invariants_have_correct_kind_and_owner(self):
        rule = self.data['adpm']['rules'][0]
        rule['kind'] = 'transition'
        self.result('ENTITY_INVARIANT')
        rule['kind'] = 'invariant'
        rule['owner_ref'] = 'ENT-CALLER-CONTEXT'
        self.result('ENTITY_INVARIANT')

    def test_wrong_source_entity_kind(self):
        self.data['adpm']['entities'][0]['source_entity_id'] = 'ACT-REQUESTER'
        self.result('SOURCE_REF_WRONG_TYPE')

    def test_unknown_rule_origin(self):
        self.data['adpm']['rules'][0]['origin_refs'] = ['VLD-NOT-DECLARED']
        self.result('SOURCE_REF_UNRESOLVED')

    def test_rule_origin_cannot_be_empty(self):
        self.data['adpm']['rules'][0]['origin_refs'] = []
        self.result('RULE_ORIGIN_MISSING')

    def test_added_rule_can_reference_a_decision(self):
        self.data['adpm']['rules'][0]['origin_refs'] = ['DEC-CALLER-CONTEXT']
        self.result(exit_code=0)

    def test_actor_must_be_permitted_for_source_case(self):
        self.data['source_l1']['catalog'].append({'ref': 'ACT-OTHER', 'kind': 'actor', 'statement': 'Another role.'})
        self.data['adpm']['cases'][0]['permission']['allowed_actor_refs'] = ['ACT-OTHER']
        self.result('ACTOR_CASE_PERMISSION')

    def test_unknown_actor(self):
        self.data['adpm']['cases'][0]['permission']['allowed_actor_refs'] = ['ACT-MISSING']
        self.result('ACTOR_REF')

    def test_source_case_actor_reference_is_typed(self):
        item = next(x for x in self.data['source_l1']['catalog'] if x['kind'] == 'case')
        item['actor_refs'] = ['ENT-REQUEST']
        self.result('SOURCE_REF_WRONG_TYPE')

    def test_duplicate_source_identity(self):
        self.data['source_l1']['catalog'].append(copy.deepcopy(self.data['source_l1']['catalog'][0]))
        self.result('L1_DUPLICATE')

    def test_catalogue_namespace_is_distinct(self):
        self.assertIn(self.data['adpm']['cases'][0]['id'], [x['ref'] for x in self.data['source_l1']['catalog']])
        self.result(exit_code=0)

    def test_source_model_is_not_interpreted(self):
        source = self.root / 'source.bin'
        source.write_bytes(b'\x00\xffopaque source format; no Atlas reader')
        self.data['source_l1'].update(model='Another L1 model', model_version='draft-3', artifact='source.bin', sha256=hashlib.sha256(source.read_bytes()).hexdigest())
        report = self.result(exit_code=0)
        self.assertTrue(any('fidelity' in text for text in report['limitations']))

    def test_missing_source_is_operational(self):
        self.data['source_l1']['artifact'] = 'missing.bin'
        self.result('L1_IO', exit_code=3)

    def test_changed_source_bytes(self):
        source = self.root / self.data['source_l1']['artifact']
        source.write_bytes(source.read_bytes() + b'\n')
        self.result('L1_HASH')

    def test_reviewed_source_requires_hash(self):
        self.data['source_l1']['sha256'] = None
        self.result('L1_HASH_REQUIRED')

    def test_unknown_trace_source(self):
        self.data['traceability'][0]['source_ref'] = 'RF-MISSING'
        self.result('SOURCE_REF_UNRESOLVED')

    def test_unknown_trace_target(self):
        self.data['traceability'][0]['target_refs'] = ['UC-MISSING']
        self.result('REF_UNRESOLVED')

    def test_unmapped_obligation(self):
        self.data['traceability'] = [x for x in self.data['traceability'] if x['source_ref'] != 'RF-REQUEST-01']
        self.result('SOURCE_OBLIGATION_UNMAPPED')

    def test_one_program_case_per_source_case(self):
        extra = copy.deepcopy(self.data['adpm']['cases'][0]); extra['id'] = 'UC-EXTRA'
        self.data['adpm']['cases'].append(extra)
        self.result('CASE_BIJECTION')

    def test_missing_behavioral_test(self):
        self.data['advs']['behavioral_tests'] = []
        self.result('TEST_BIJECTION')

    def test_duplicate_behavioral_test(self):
        extra = copy.deepcopy(self.data['advs']['behavioral_tests'][0]); extra['id'] = 'BT-EXTRA'
        self.data['advs']['behavioral_tests'].append(extra)
        self.result('TEST_BIJECTION')

    def test_wrong_case_test_reference(self):
        self.data['advs']['behavioral_tests'][0]['case_ref'] = 'ENT-REQUEST'
        self.result('REF_WRONG_TYPE')

    def test_duplicate_model_identity(self):
        self.data['adpm']['entities'].append(copy.deepcopy(self.data['adpm']['entities'][0]))
        self.result('ID_DUPLICATE')

    def test_missing_advs_is_structural_error(self):
        del self.data['advs']
        self.result('SCHEMA_INVALID')

    def test_uncovered_criterion(self):
        for scenario in self.data['advs']['behavioral_tests'][0]['scenarios']:
            scenario['criteria_refs'] = [ref for ref in scenario['criteria_refs'] if ref != 'AC-REQUEST-06']
        self.result('CRITERION_UNCOVERED')

    def test_nonapplicable_scenario_does_not_count(self):
        for scenario in self.data['advs']['behavioral_tests'][0]['scenarios']:
            if 'AC-REQUEST-06' in scenario['criteria_refs']:
                scenario['applicability'] = 'not_applicable'
                scenario['rationale'] = 'Disabled by this negative fixture.'
        self.result('CRITERION_UNCOVERED')

    def test_all_denial_categories_required(self):
        for scenario in self.data['advs']['behavioral_tests'][0]['scenarios']:
            if scenario['actor_context'] == 'unknown': scenario['actor_context'] = 'unresolved'
        self.result('AUTH_COVERAGE')

    def test_repeated_denial_category(self):
        self.data['adpm']['cases'][0]['permission']['deny_contexts'].append('unknown')
        self.result('AUTH_DENIALS')

    def test_context_input_must_exist(self):
        self.data['adpm']['cases'][0]['permission']['context_input'] = 'missing'
        self.result('AUTH_INPUT')

    def test_entities_cannot_consume_tools(self):
        self.data['adpm']['entities'][0]['dependencies'] = ['TOL-REQUEST-STORE']
        self.result('REF_WRONG_TYPE')

    def test_tool_cannot_revalidate_entity_invariants(self):
        self.data['adpm']['tools'][0]['operations'][0]['revalidates_rule_refs'] = ['VLD-REQUEST-QUANTITY']
        self.result('ENTITY_REVALIDATION')

    def test_graph_edge_must_resolve_locally(self):
        self.data['adpm']['graphs'][0]['edges'][0]['to'] = 'N-MISSING'
        self.result('GRAPH_EDGE')

    def test_unreachable_graph_node(self):
        self.data['adpm']['graphs'][0]['nodes'].append({'id':'N-UNREACHABLE','kind':'action','description':'Disconnected.'})
        self.result('GRAPH_UNREACHABLE')

    def test_legitimate_graph_cycle(self):
        graph = self.data['adpm']['graphs'][0]; node = graph['entry']
        graph['edges'].append({'id':'E-REPEAT','from':node,'to':node,'condition':'Wait for another input event.','action':''})
        self.result(exit_code=0)

    def test_composition_requires_forwarding(self):
        root = EDITION / 'examples/composition'
        self.data = read_yaml(root / 'docs/L2_MinervaBlueprints/blueprint.yaml')
        shutil.copyfile(root / self.data['source_l1']['artifact'], self.root / self.data['source_l1']['artifact'])
        dep = next(x for x in self.data['adpm']['dependencies'] if x['provider_ref'] == 'UC-BOOKING-LOOKUP')
        dep['context_forwarding'] = None
        self.result('CASE_CONTEXT')

    def test_shared_quality_support_is_canonical(self):
        root = EDITION / 'examples/composition'; data = read_yaml(root / 'docs/L2_MinervaBlueprints/blueprint.yaml')
        check = next(x for x in data['advs']['supporting_checks'] if x['id'] == 'CHK-RNF-BOOKING-CREATE-RESPONSE')
        self.assertEqual({'UC-BOOKING-CREATE','UC-BOOKING-CANCEL'}, set(check['case_refs']))
        self.assertEqual(2, len(check['behavioral_test_refs']))
        self.assertNotIn('minerva_shared_criteria', (root / data['source_l1']['artifact']).read_text(encoding='utf-8'))

    def test_missing_support_reciprocity(self):
        self.data['advs']['supporting_checks'][0]['behavioral_test_refs'] = []
        self.result('SUPPORT_RECIPROCITY')

    def test_execution_requires_report(self):
        self.data['advs']['executions'] = [{'id':'EXEC-FAKE','check_refs':['BT-REQUEST-SUBMIT'],'implementation_revision':'unavailable','environment':'test','result':'passed','observed_at':'2026-10-28T12:00:00Z','report':'missing.txt','limitations':[]}]
        self.result('EVIDENCE_MISSING')

    def test_empty_reviewed_model(self):
        self.data['source_l1']['case_ids'] = []; self.data['adpm']['cases'] = []; self.data['advs']['behavioral_tests'] = []
        self.result('ADMV_EMPTY')

    def test_draft_is_inconclusive(self):
        self.data['document']['status'] = 'draft'
        self.result('DRAFT_INCOMPLETE',exit_code=4)

    def test_unsupported_profile(self):
        self.data['profile_version'] = '2.0.0'
        self.result('PROFILE_UNSUPPORTED',exit_code=2)

    def test_json_cli_and_structure_scope(self):
        proc = subprocess.run([sys.executable,'-B',str(EDITION/'validator/minerva_validate.py'),str(self.path),'--root',str(self.root),'--structure-only','--json'],capture_output=True,text=True)
        self.assertEqual(0,proc.returncode,proc.stderr)
        self.assertEqual('not_assessed',json.loads(proc.stdout)['layer_coverage'])

    def test_task_board_revision_delta(self):
        base=EDITION/'examples/task-board/revisions'
        earlier=read_yaml(base/'revision-2/docs/L2_MinervaBlueprints/blueprint.yaml')
        later=read_yaml(base/'revision-3/docs/L2_MinervaBlueprints/blueprint.yaml')
        self.assertEqual(earlier['source_l1']['case_ids'],later['source_l1']['case_ids'])
        def criterion(data): return next(x for x in data['source_l1']['catalog'] if x['ref']=='AC-TASK-LIST-EMPTY')['statement']
        self.assertNotEqual(criterion(earlier),criterion(later))
        self.assertIn('revision',criterion(later))


class TestLoadingAndCode(unittest.TestCase):
    def test_restricted_yaml_loader(self):
        with tempfile.TemporaryDirectory(prefix='minerva-yaml-') as directory:
            path=Path(directory)/'input.yaml'
            for text in ['a: 1\na: 2\n','a: &alias 1\nb: *alias\n','a: !!python/object:builtins.object {}\n','1: value\n','a: 1e999\n']:
                with self.subTest(text=text):
                    path.write_text(text,encoding='utf-8')
                    with self.assertRaises((InputError,yaml.YAMLError)):read_yaml(path)
            path.write_text('a: yes\nb: 012\nc: 2026-10-28\nd: true\ne: null\n',encoding='utf-8')
            self.assertEqual({'a':'yes','b':'012','c':'2026-10-28','d':True,'e':None},read_yaml(path))

    def test_paths_cannot_escape(self):
        with tempfile.TemporaryDirectory(prefix='minerva-path-') as directory:
            for value in ['../outside','C:/outside','folder\\file','/outside']:
                with self.subTest(value=value),self.assertRaises(InputError):safe_path(Path(directory),value)

    def test_starter_and_planned_source(self):
        starter=EDITION/'implementations/yaml/starter.minerva.yaml'
        self.assertEqual(0,validate(starter,EDITION,structure_only=True)['exit_code'])
        self.assertEqual(4,validate(starter,EDITION)['exit_code'])
        planned=EDITION/'tests/fixtures/planned'; path=planned/'docs/L2_MinervaBlueprints/apps/RequestRegister/submit.py.yaml'
        self.assertEqual(0,validate(path,planned)['exit_code'])
        self.assertEqual(4,validate(path,planned,verify_code=True)['exit_code'])

    def test_code_inspection_does_not_import(self):
        data=read_yaml(EDITION/'tests/fixtures/planned/docs/L2_MinervaBlueprints/apps/RequestRegister/submit.py.yaml')
        with tempfile.TemporaryDirectory(prefix='minerva-code-') as directory:
            root=Path(directory);code=root/'apps/RequestRegister/submit.py';code.parent.mkdir(parents=True)
            code.write_text("raise RuntimeError('must not execute')\n\ndef submit(actor_context, code, quantity):\n    return None\n",encoding='utf-8')
            data['source'].update(state='observed',sha256=hashlib.sha256(code.read_bytes()).hexdigest())
            path=root/'source.yaml';path.write_text(yaml.safe_dump(data),encoding='utf-8')
            self.assertEqual(0,validate(path,root,verify_code=True)['exit_code'])
            code.write_text(code.read_text(encoding='utf-8')+'\n# drift\n',encoding='utf-8')
            self.assertIn('CODE_HASH_MISMATCH',{x['code'] for x in validate(path,root,verify_code=True)['diagnostics']})

    def test_qualified_symbol_ownership(self):
        tree=ast.parse('class Other:\n def test_run(self): pass\nclass Expected: pass\n')
        self.assertFalse(resolve_python_symbol(tree,'Expected.test_run'))
        self.assertTrue(resolve_python_symbol(tree,'Other.test_run'))


if __name__ == '__main__':
    unittest.main()
