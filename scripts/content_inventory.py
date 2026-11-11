"""Capture every present non-ignored delivery file; verify by path and content."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = "CONTENT-SHA256.json"
SCOPE = "All present non-ignored delivery files reported by Git, using actual working-tree bytes."


def portable_path(name: str) -> str:
    if (not isinstance(name, str) or not name or "\\" in name or ":" in name
            or "\x00" in name or any(part in {"", ".", ".."} for part in name.split("/"))):
        raise ValueError(f"unsupported relative POSIX path: {name!r}")
    return name


def tracked_files(root: Path) -> list[str]:
    raw = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root
    )
    paths = raw.decode("utf-8").split("\0")[:-1]
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate delivery paths reported by Git")
    return sorted(
        portable_path(path) for path in paths
        if path != INVENTORY and (root / Path(*path.split("/"))).is_file()
    )


def read_file(root: Path, name: str) -> bytes:
    path = root
    for part in portable_path(name).split("/"):
        path = path / part
        if path.is_symlink():
            raise ValueError(f"unsupported symlink: {name}")
    if not path.is_file():
        raise ValueError(f"missing file: {name}")
    return path.read_bytes()


def edition(files: dict[str, bytes]) -> str:
    text = files["CITATION.cff"].decode("utf-8")
    matches = re.findall(r"^version:\s*([^\r\n]+)", text, re.M)
    if len(matches) != 1:
        raise ValueError("CITATION.cff must declare exactly one release version")
    value = matches[0].strip().strip("\"'")
    if not re.fullmatch(r"(?:Stable|Alpha)-v\d+\.\d+\.\d+", value):
        raise ValueError("unsupported release version in CITATION.cff")
    return value


def inventory(files: dict[str, bytes]) -> dict:
    return {
        "algorithm": "SHA-256",
        "minerva_edition": edition(files),
        "scope": SCOPE,
        "excluded_paths": [INVENTORY],
        "files": [{"path": portable_path(name), "size_bytes": len(files[name]),
                   "sha256": hashlib.sha256(files[name]).hexdigest()}
                  for name in sorted(files) if name != INVENTORY],
    }


def build(root: Path) -> dict:
    return inventory({name: read_file(root, name) for name in tracked_files(root)})


def verify(files: dict[str, bytes]) -> list[str]:
    """Validate complete coverage, metadata and exact bytes, without needing Git."""
    if INVENTORY not in files:
        return [f"missing file: {INVENTORY}"]
    try:
        for name in files:
            portable_path(name)
        stored = json.loads(files[INVENTORY])
        if not isinstance(stored, dict):
            raise ValueError("inventory must be an object")
        expected_metadata = {"algorithm": "SHA-256", "minerva_edition": edition(files),
                             "scope": SCOPE, "excluded_paths": [INVENTORY]}
        errors = [f"inventory metadata differs: {key}" for key, value in expected_metadata.items()
                  if stored.get(key) != value]
        rows = stored.get("files")
        if not isinstance(rows, list):
            raise ValueError("inventory files must be a list")
        recorded = {}
        for row in rows:
            if not isinstance(row, dict) or set(row) != {"path", "size_bytes", "sha256"}:
                raise ValueError("invalid inventory record fields")
            name = portable_path(row["path"])
            if name == INVENTORY:
                raise ValueError("inventory cannot include itself")
            if name in recorded:
                raise ValueError(f"duplicate inventory path: {name}")
            if type(row["size_bytes"]) is not int or row["size_bytes"] < 0:
                raise ValueError(f"invalid size: {name}")
            if not isinstance(row["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
                raise ValueError(f"invalid SHA-256: {name}")
            recorded[name] = row
        actual = set(files) - {INVENTORY}
        errors += [f"missing file: {name}" for name in sorted(recorded.keys() - actual)]
        errors += [f"added file: {name}" for name in sorted(actual - recorded.keys())]
        for name in sorted(actual & recorded.keys()):
            raw, row = files[name], recorded[name]
            if len(raw) != row["size_bytes"]:
                errors.append(f"size differs: {name}")
            if hashlib.sha256(raw).hexdigest() != row["sha256"]:
                errors.append(f"hash differs: {name}")
        return errors
    except (KeyError, TypeError, ValueError) as error:
        return [f"invalid inventory: {error}"]


def check(root: Path) -> list[str]:
    files = {name: read_file(root, name) for name in tracked_files(root)}
    files[INVENTORY] = read_file(root, INVENTORY)
    return verify(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        if args.write:
            result = build(ROOT)
            (ROOT / INVENTORY).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                                         encoding="utf-8", newline="\n")
            print(f"Wrote {len(result['files'])} files to {INVENTORY}")
        else:
            errors = check(ROOT)
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            print(f"Inventory OK: {len(tracked_files(ROOT))} files (actual bytes)")
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(f"Inventory failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
