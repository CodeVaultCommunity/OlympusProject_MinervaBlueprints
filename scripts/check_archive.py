"""Verify a complete ZIP or extracted distribution; Git is not required."""
from __future__ import annotations

import argparse
from pathlib import Path
import stat
import sys
import zipfile

# Checking an extracted distribution must not create unlisted Python caches.
sys.dont_write_bytecode = True
from content_inventory import INVENTORY, portable_path, read_file, verify


def read_archive(path: Path) -> dict[str, bytes]:
    if path.is_dir():
        files = {}
        for item in path.rglob("*"):
            if item.is_symlink():
                raise ValueError(f"unsupported symlink: {item.relative_to(path)}")
            if item.is_file():
                name = item.relative_to(path).as_posix()
                files[name] = read_file(path, name)
        return files
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        names = [item.filename for item in entries]
        if len(names) != len(set(names)):
            raise ValueError("duplicate archive paths")
        for item in entries:
            portable_path(item.filename[:-1] if item.is_dir() else item.filename)
            if stat.S_ISLNK(item.external_attr >> 16):
                raise ValueError(f"unsupported symlink: {item.filename}")
        files = {item.filename: archive.read(item) for item in entries if not item.is_dir()}
    # Accept either a root-level manifest or a single enclosing Git-archive folder.
    if INVENTORY not in files:
        manifests = [name for name in files if name.endswith("/" + INVENTORY) and name.count("/") == 1]
        if len(manifests) == 1:
            prefix = manifests[0][:-len(INVENTORY)]
            if not all(name.startswith(prefix) for name in files):
                raise ValueError("files outside the archive root")
            files = {name[len(prefix):]: raw for name, raw in files.items()}
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="ZIP or extracted repository root containing CONTENT-SHA256.json")
    args = parser.parse_args()
    try:
        files = read_archive(args.archive)
        errors = verify(files)
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as error:
        errors = [str(error)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Archive OK: {len(files) - 1} delivery files plus inventory; complete coverage and exact bytes match.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
