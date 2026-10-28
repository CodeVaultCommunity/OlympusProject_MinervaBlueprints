"""Validate this edition's examples from any working directory."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

EDITION=Path(__file__).resolve().parent
EXAMPLES={
 'minimal':('examples/minimal','docs/L2_MinervaBlueprints/blueprint.yaml'),
 'task-board-ecosystem':('examples/task-board-ecosystem','docs/L2_MinervaBlueprints/blueprint.yaml'),
 'planned':('examples/planned','docs/L2_MinervaBlueprints/blueprint.yaml'),
 'legacy':('examples/legacy','docs/L2_MinervaBlueprints/apps/LegacyReports/reports.py.yaml'),
}


def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('example',nargs='?',choices=sorted(EXAMPLES))
 parser.add_argument('--all',action='store_true')
 parser.add_argument('--list',action='store_true')
 parser.add_argument('--json',action='store_true')
 parser.add_argument('--test',action='store_true')
 args=parser.parse_args()
 if args.list:
  print('\n'.join(EXAMPLES)); return 0
 if args.test:
  return subprocess.call([sys.executable,'-m','unittest','discover','-s',str(EDITION/'tests'),'-p','test_*.py','-v'],cwd=EDITION)
 if args.example is None and not args.all: parser.error('select an example, --all, --list or --test')
 from minerva_blueprints.validation import validate
 selected=list(EXAMPLES) if args.all else [args.example]
 results=[]
 for name in selected:
  directory,filename=EXAMPLES[name]; root=EDITION/directory
  report=validate(root/filename,root)
  results.append({'example':name,**report})
 if args.all:
  starter=validate(EDITION/'implementations/yaml/starter.minerva.yaml',EDITION,structure_only=True)
  results.append({'example':'starter-structure-only',**starter})
 if args.json: print(json.dumps({'results':results,'passed':all(x['exit_code']==0 for x in results)},ensure_ascii=False,indent=2))
 else:
  for result in results:
   print(result['status'].upper()+': '+result['example'])
   for d in result['diagnostics']:
    if d['severity'] not in ('info','warning'): print('  '+d['code']+': '+d['message'])
 return 0 if all(x['exit_code']==0 for x in results) else 1


if __name__=='__main__': raise SystemExit(main())
