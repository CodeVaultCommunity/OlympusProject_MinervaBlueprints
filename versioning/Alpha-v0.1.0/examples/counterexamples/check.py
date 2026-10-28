"""Read each public fixture and compare the actual result with its declared expectation."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
EDITION = ROOT.parents[1]
sys.path.insert(0, str(EDITION))
from minerva_blueprints.validation import validate


def run():
    manifest = json.loads((ROOT / 'expected-results.json').read_text(encoding='utf-8'))
    results = []
    for case in manifest['cases']:
        report = validate(ROOT / case['document'], ROOT, verify_code=case['verify_code'])
        codes = [d['code'] for d in report['diagnostics']]
        matched = report['exit_code'] == case['expected_exit_code'] and (case['expected_diagnostic'] is None or case['expected_diagnostic'] in codes)
        results.append({'name': case['name'], 'matched_expectation': matched, 'actual_exit_code': report['exit_code'], 'expected_exit_code': case['expected_exit_code'], 'diagnostic_codes': codes})
    return {'passed': all(r['matched_expectation'] for r in results), 'fixture_count': len(results), 'results': results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    result = run()
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for item in result['results']:
            print(('PASS' if item['matched_expectation'] else 'FAIL') + ': ' + item['name'] + ' (actual exit ' + str(item['actual_exit_code']) + ')')
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
