"""Check local documentation links, source snapshots and repository identities."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
IGNORED={'.git','.venv','__pycache__','.pytest_cache','build','dist'}

def anchors(path):
    text=path.read_text(encoding='utf-8')
    ids=set(re.findall(r'<a\s+[^>]*id=[\"\']([^\"\']+)',text))
    counts={}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',text,re.M):
        heading=re.sub(r'<[^>]+>','',heading).strip().lower()
        slug=re.sub(r'[^\w\- ]','',heading).replace(' ','-')
        number=counts.get(slug,0); counts[slug]=number+1
        ids.add(slug if number==0 else f'{slug}-{number}')
    return ids

def check(root):
    errors=[]; local_links=0; markdown=0
    for source in sorted(root.rglob('*.md')):
        if any(part in IGNORED or part.endswith('.egg-info') for part in source.relative_to(root).parts):
            continue
        markdown+=1
        text=source.read_text(encoding='utf-8')
        # Examples in code fences are not repository navigation.
        text=re.sub(r'^(```|~~~).*?^\1\s*$', '', text, flags=re.M|re.S)
        targets=re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',text)
        targets+=re.findall(r'(?:src|href)=[\"\']([^\"\']+)[\"\']',text)
        for target in targets:
            target=target.strip().split(' "',1)[0].strip('<>')
            parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path and not parsed.fragment:
                continue
            local_links+=1
            path=(source.parent/unquote(parsed.path)).resolve() if parsed.path else source
            try:
                path.relative_to(root)
            except ValueError:
                errors.append(f'{source.relative_to(root)}: link leaves repository: {target}')
                continue
            if not path.exists():
                errors.append(f'{source.relative_to(root)}: missing target: {target}')
            elif parsed.fragment and path.is_file() and path.suffix=='.md':
                if unquote(parsed.fragment) not in anchors(path):
                    errors.append(f'{source.relative_to(root)}: missing anchor: {target}')
    snapshots=0
    for source in sorted(root.glob('versioning/*/verification/source-baselines.json')):
        edition=source.parent.parent
        data=json.loads(source.read_text(encoding='utf-8'))
        for item in data['files']:
            target=edition/item['snapshot_path']; snapshots+=1
            if not target.is_file():
                errors.append(f'Missing snapshot: {target.relative_to(root)}'); continue
            raw=target.read_bytes()
            if len(raw)!=item['size_bytes'] or hashlib.sha256(raw).hexdigest()!=item['sha256']:
                errors.append(f'Changed snapshot: {target.relative_to(root)}')
    version=(root/'VERSION').read_text(encoding='utf-8').strip()
    if not (root/'versioning'/version/'README.md').is_file():
        errors.append('VERSION does not identify an edition manual')
    citation=(root/'CITATION.cff').read_text(encoding='utf-8')
    if not re.search(r'^version:\s*[\"\']?'+re.escape(version)+r'[\"\']?\s*$',citation,re.M):
        errors.append('CITATION.cff and VERSION differ')
    return {'status':'failed' if errors else 'passed','markdown_files':markdown,
            'local_links':local_links,'source_snapshots':snapshots,'errors':errors,
            'limits':['External URLs are not fetched.','Structural documentation checks do not prove behavioral correctness.']}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args()
    try:
        report=check(args.root.resolve())
    except (OSError,ValueError,KeyError) as exc:
        report={'status':'failed','errors':[str(exc)]}
    if args.json:
        print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(f"Repository {report['status']}: "+', '.join(f'{k}={report[k]}' for k in ['markdown_files','local_links','source_snapshots'] if k in report))
        for error in report['errors']: print(error,file=sys.stderr)
    return 0 if report['status']=='passed' else 1

if __name__=='__main__':
    raise SystemExit(main())
