"""Validate package hashes, primary references, and self-hosted assets."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT/'skills/personal-web-visual-design'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh-manifest', action='store_true', help='Update file hashes after an intentional package edit')
    args = parser.parse_args()
    manifest = json.loads((ROOT/'package-manifest.json').read_text(encoding='utf-8'))
    failures = []
    actual = {}
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if any(part in {'.git', '__pycache__'} for part in rel.parts) or rel.parts[0] in {'dist', '.validation'}:
            continue
        if path.is_symlink():
            failures.append(f'Symbolic link is not allowed: {rel.as_posix()}')
        elif path.is_file() and rel.as_posix() != 'package-manifest.json':
            actual[rel.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if args.refresh_manifest:
        if failures:
            print(json.dumps({'status':'failed','failures':failures}, indent=2))
            return 1
        manifest['files'] = actual
        (ROOT/'package-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    if set(actual) != set(manifest['files']):
        failures.append('Manifest file set differs from package contents')
    for rel, expected in manifest['files'].items():
        path = ROOT/rel
        if not path.resolve().is_relative_to(ROOT) or not path.is_file():
            failures.append(f'Missing or invalid path: {rel}')
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            failures.append(f'Hash mismatch: {rel}')
    for skill in (ROOT/'skills').iterdir():
        if not skill.is_dir():
            continue
        entry = skill/'SKILL.md'
        text = entry.read_text(encoding='utf-8-sig')
        front = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
        if not front or not re.search(r'^name:\s*'+re.escape(skill.name)+r'\s*$', front[1], re.M) or not re.search(r'^description:', front[1], re.M):
            failures.append(f'Invalid skill frontmatter: {skill.name}')
    docs = [ROOT/'README.md', ROOT/'THIRD_PARTY_NOTICES.md', MAIN/'SKILL.md', *sorted((MAIN/'references').rglob('*.md'))]
    anchors = {}
    for doc in docs:
        text = doc.read_text(encoding='utf-8-sig')
        ids = re.findall(r'<a id="([^"]+)"', text)
        if len(ids) != len(set(ids)):
            failures.append(f'Duplicate anchor in {doc.name}')
        anchors[doc.relative_to(ROOT).as_posix()] = ids
        for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z]+://', link):
                continue
            rel, _, anchor = link.partition('#')
            dest = (doc.parent/rel).resolve() if rel else doc
            if not dest.is_file():
                failures.append(f'Broken link in {doc.name}: {link}')
            elif anchor and dest.suffix == '.md':
                body = dest.read_text(encoding='utf-8-sig')
                ids = set(re.findall(r'<a id="([^"]+)"', body))
                if anchor not in ids:
                    failures.append(f'Unknown anchor in {doc.name}: {link}')
    assets = MAIN/'assets'
    for css in assets.rglob('*.css'):
        text = css.read_text(encoding='utf-8')
        for ref in re.findall(r'url\(([^)]+)\)', text):
            rel = ref.strip(' \"\'')
            if re.match(r'^[a-zA-Z]+:', rel) or not (css.parent/rel).resolve().is_file():
                failures.append(f'Nonlocal or missing CSS asset: {css.name}: {rel}')
    preview = assets/'typography-preview.html'
    for ref in re.findall(r'(?:href|src)="([^"]+)"', preview.read_text(encoding='utf-8')):
        if re.match(r'^[a-zA-Z]+:', ref) or not (preview.parent/ref).resolve().is_file():
            failures.append(f'Nonlocal or missing preview asset: {ref}')
    for name in ('web-visual-standards.md', 'data-display.md'):
        if not anchors.get(f'skills/{MAIN.name}/references/{name}'):
            failures.append(f'Missing standard anchors: {name}')
    actual_skills = sorted(p.name for p in (ROOT/'skills').iterdir() if p.is_dir() and (p/'SKILL.md').is_file())
    if manifest['entry_skill'] != MAIN.name or sorted(manifest['skills']) != actual_skills:
        failures.append('Manifest skill identities differ from package contents')
    if 'TODO:' in (MAIN/'SKILL.md').read_text(encoding='utf-8'):
        failures.append('Unfinished primary skill scaffold')
    print(json.dumps({'status':'passed' if not failures else 'failed','files_checked':len(manifest['files']),'entry_skill':MAIN.name,'anchors_checked':sum(map(len, anchors.values())),'failures':failures}, ensure_ascii=False, indent=2))
    return 1 if failures else 0

if __name__ == '__main__':
    sys.exit(main())
