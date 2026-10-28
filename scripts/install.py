"""Install the packaged skills without overwriting existing versions."""
from pathlib import Path
import argparse
import hashlib
import os
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]

def fingerprint(folder):
    result = {}
    for path in sorted(folder.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symbolic link is not supported: {path}')
        if path.is_file():
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, default=Path(os.environ.get('CODEX_HOME', Path.home()/'.codex'))/'skills')
    args = parser.parse_args()
    target = args.target.expanduser().resolve()
    sources = sorted(p for p in (ROOT/'skills').iterdir() if p.is_dir() and (p/'SKILL.md').is_file())
    if not sources:
        raise ValueError('No skills found in this package')
    pending = []
    for source in sources:
        dest = target/source.name
        if dest.is_symlink() or not dest.resolve().is_relative_to(target):
            raise ValueError(f'Invalid destination: {dest}')
        desired = fingerprint(source)
        if dest.exists():
            if not dest.is_dir():
                raise ValueError(f'Different existing skill; nothing was installed: {dest}')
            current = fingerprint(dest)
            conflicts = [name for name in desired if name in current and desired[name] != current[name]]
            if conflicts:
                raise ValueError(f'Different existing skill; nothing was installed: {dest}')
            missing = sorted(set(desired) - set(current))
            if missing:
                pending.append((source, dest, missing))
            else:
                print(f'REUSE {source.name}')
        else:
            pending.append((source, dest, sorted(desired)))
    for source, dest, missing in pending:
        for rel in missing:
            target_file = dest/rel
            target_file.parent.mkdir(parents=True, exist_ok=True)
            with (source/rel).open('rb') as reader, target_file.open('xb') as writer:
                shutil.copyfileobj(reader, writer)
        desired, current = fingerprint(source), fingerprint(dest)
        if any(current.get(name) != digest for name, digest in desired.items()):
            raise RuntimeError(f'Copy verification failed: {dest}')
        print(f'INSTALLED {len(missing)} missing files in {dest}')
    print('Installation complete. Skills are available on the next turn.')

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, RuntimeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
