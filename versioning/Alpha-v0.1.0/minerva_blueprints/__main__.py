"""Command-line entry point for this explicitly selected edition."""
import argparse
import json
from pathlib import Path
import sys


def main(argv=None):
    parser=argparse.ArgumentParser(description='Read-only Minerva YAML structure and consistency validation.')
    parser.add_argument('document',nargs='?',type=Path)
    parser.add_argument('--root',type=Path,default=Path.cwd(),help='Root against which artifact paths are resolved.')
    parser.add_argument('--json',action='store_true',help='Emit one machine-readable JSON report.')
    parser.add_argument('--structure-only',action='store_true',help='Check only the representation; do not claim ADMV consistency.')
    parser.add_argument('--verify-code',action='store_true',help='Also inspect current source hashes and Python top-level symbols; never execute code.')
    parser.add_argument('--version',action='store_true')
    args=parser.parse_args(argv)
    if args.version:
        print('Minerva Blueprints Alpha-v0.1.0 | YAML 0.1.0 | tool 0.1.0a0'); return 0
    if args.document is None: parser.error('document is required unless --version is used')
    if args.structure_only and args.verify_code: parser.error('--structure-only and --verify-code are mutually exclusive')
    try:
        from .validation import validate
        report=validate(args.document,args.root,structure_only=args.structure_only,verify_code=args.verify_code)
    except ImportError as error:
        report={'status':'operational_error','exit_code':3,'diagnostics':[{'code':'DEPENDENCY_MISSING','severity':'error','document':str(args.document),'element':'$','message':str(error)+'. Install this edition requirements.txt.'}]}
    except Exception as error:
        report={'status':'operational_error','exit_code':3,'diagnostics':[{'code':'INTERNAL_ERROR','severity':'error','document':str(args.document),'element':'$','message':type(error).__name__+': '+str(error)}]}
    if args.json: print(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False))
    else:
        print(report['status'].upper()+': '+str(args.document))
        if 'counts' in report: print(', '.join(f'{k}={v}' for k,v in report['counts'].items()))
        for item in report['diagnostics']:
            print(f"[{item['severity']}:{item['code']}] {item['document']} {item['element']}: {item['message']}")
        print('Result describes requested checks only; it is not OAL certification or proof of behavior.')
    return report['exit_code']


if __name__=='__main__': raise SystemExit(main())
