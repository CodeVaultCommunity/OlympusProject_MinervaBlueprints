"""Archive the clean committed repository and check its complete inventory."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path, PurePosixPath
import subprocess
import sys

sys.dont_write_bytecode = True
from check_archive import read_archive
from content_inventory import ROOT, check, verify

FORBIDDEN = {".git", ".venv", "__pycache__", ".pytest_cache", "build", "dist"}
TEMP_SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"}


def unwanted(name: str) -> bool:
    path = PurePosixPath(name)
    return (any(part in FORBIDDEN or part.endswith(".egg-info") or part.startswith(("pytest-", ".atlas-pdf-", ".minerva-", ".vulcan-"))
                for part in path.parts) or path.suffix in TEMP_SUFFIXES or name.endswith(".synctex.gz"))


def build(root: Path, output: Path) -> None:
    output = output.resolve()
    if output.exists():
        raise ValueError(f"output already exists: {output}")
    subprocess.run(["git", "diff", "--exit-code", "--quiet", "HEAD", "--"], cwd=root, check=True)
    names = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "-z", "HEAD"], cwd=root).decode("utf-8").split("\0")
    forbidden = [name for name in names if name and unwanted(name)]
    if forbidden:
        raise ValueError("tracked temporary files: " + ", ".join(forbidden))
    errors = check(root)
    if errors:
        raise ValueError("\n".join(errors))
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "archive", "--format=zip", "--prefix=OlympusProject_MinervaBlueprints/", "--output=" + str(output), "HEAD"], cwd=root, check=True)
    files = read_archive(output)
    errors = verify(files)
    if errors:
        raise ValueError("archive verification failed:\n" + "\n".join(errors))
    print(f"Archive: {output}\nFiles: {len(files)}\nSHA-256: {hashlib.sha256(output.read_bytes()).hexdigest()}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        build(ROOT, args.output)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Distribution failed: {error}") from error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
