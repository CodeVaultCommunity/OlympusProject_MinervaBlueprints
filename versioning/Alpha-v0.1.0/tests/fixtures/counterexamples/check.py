"""Apply declared negative-fixture mutations to temporary Minerva documents."""
import argparse
import json
from pathlib import Path
import shutil
import sys
import tempfile
import yaml

HERE = Path(__file__).resolve().parent
EDITION = HERE.parents[2]
sys.path.insert(0, str(EDITION))
from minerva_blueprints.loading import read_yaml
from minerva_blueprints.validation import validate


def replace(document, pointer, value):
    parts = pointer.strip('/').split('/')
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = int(parts[-1]) if isinstance(target, list) else parts[-1]
    target[key] = value


def run():
    manifest = json.loads((HERE / 'expected-results.json').read_text(encoding='utf-8'))
    results = []
    with tempfile.TemporaryDirectory(prefix='minerva-fixtures-') as directory:
        for fixture in manifest['cases']:
            root = Path(directory) / fixture['name']
            shutil.copytree(EDITION / 'examples' / manifest['base_example'], root)
            path = root / 'docs/L2_MinervaBlueprints/blueprint.yaml'
            data = read_yaml(path)
            for patch in fixture.get('patches', []):
                replace(data, patch['path'], patch['value'])
            path.write_text(fixture.get('raw', yaml.safe_dump(data, sort_keys=False)), encoding='utf-8')
            report = validate(path, root)
            codes = [item['code'] for item in report['diagnostics']]
            matched = report['exit_code'] == fixture['expected_exit_code'] and (fixture['expected_diagnostic'] is None or fixture['expected_diagnostic'] in codes)
            results.append({'name':fixture['name'],'matched_expectation':matched,'actual_exit_code':report['exit_code'],'diagnostic_codes':codes})
    return {'passed':all(item['matched_expectation'] for item in results),'fixture_count':len(results),'results':results}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args(); result=run()
    if args.json: print(json.dumps(result,indent=2))
    else:
        for item in result['results']:
            print(('PASS: ' if item['matched_expectation'] else 'FAIL: ')+item['name'])
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
