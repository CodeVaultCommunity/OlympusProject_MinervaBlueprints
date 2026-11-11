"""Validate the shared repository skeleton, documentation, identities, and text bytes."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache", "build", "dist", "work", ".runtime"}
REQUIRED_DIRS = {".github", "assets", "docs", "scripts", "versioning"}
REQUIRED_ROOT_FILES = {
    ".editorconfig", ".gitattributes", ".gitignore", "ACKNOWLEDGEMENTS.md",
    "AGENTS.md", "CITATION.cff", "CLAUDE.md", "CONTENT-SHA256.json",
    "CONTRIBUTING.md", "CONTRIBUTING.pt-br.md", "LICENSE", "README.md",
    "README.pt-br.md", "VERSION",
}
REQUIRED_ASSET_FILES = {
    "README.md", "README.pt-br.md", "asset-metadata.json", "requirements-artwork.txt",
}
REQUIRED_DOC_FILES = {
    "getting-started.md", "getting-started.pt-br.md", "releasing.md", "releasing.pt-br.md",
}
REQUIRED_SCRIPT_FILES = {
    "build_distribution.py", "check_archive.py", "check_repository.py",
    "content_inventory.py", "requirements-dev.txt",
}
REQUIRED_GITIGNORE = {
    "__pycache__/", "*.py[cod]", ".pytest_cache/", ".venv/", "*.egg-info/",
    "build/", "dist/", "work/", "*.sqlite", "*.sqlite3", "*.db", "*.aux",
    "*.log", "*.out", "*.toc", "*.synctex.gz", ".DS_Store",
}
TEXT_SUFFIXES = {".cff", ".json", ".md", ".py", ".sty", ".tex", ".toml", ".txt", ".yaml", ".yml", ".svg"}
TEXT_NAMES = {".editorconfig", ".gitattributes", ".gitignore", "LICENSE", "VERSION"}


def delivery_files(root: Path) -> list[str]:
    raw = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root
    )
    names = raw.decode("utf-8").split("\0")[:-1]
    return sorted(
        set(name for name in names if name != "CONTENT-SHA256.json" and (root / name).is_file())
    )


def exact_bytes(name: str) -> bool:
    path = PurePosixPath(name)
    if name.endswith((".atlas.md", ".atlas.tex")):
        return True
    parts = path.parts
    if len(parts) >= 4 and parts[0] == "versioning" and parts[2] == "verification":
        return parts[3] in {"evidence", "sources", "runs", "reviews"}
    return len(parts) >= 4 and parts[0] == "versioning" and parts[2:4] == ("tests", "fixtures")


def anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    ids = set(re.findall(r'<a\s+[^>]*id=["\']([^"\']+)', text))
    counts: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*$", text, re.M):
        heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        ids.add(slug if number == 0 else f"{slug}-{number}")
    return ids


def check_contract(root: Path) -> list[str]:
    errors: list[str] = []
    for directory in sorted(REQUIRED_DIRS):
        if not (root / directory).is_dir():
            errors.append(f"missing required directory: {directory}/")
    for name in sorted(REQUIRED_ROOT_FILES):
        if not (root / name).is_file():
            errors.append(f"missing required root file: {name}")
    for name in sorted(REQUIRED_ASSET_FILES):
        if not (root / "assets" / name).is_file():
            errors.append(f"missing required asset file: assets/{name}")
    if not (root / "assets" / "sources").is_dir():
        errors.append("missing required asset directory: assets/sources/")
    for name in sorted(REQUIRED_DOC_FILES):
        if not (root / "docs" / name).is_file():
            errors.append(f"missing required document: docs/{name}")
    for name in sorted(REQUIRED_SCRIPT_FILES):
        if not (root / "scripts" / name).is_file():
            errors.append(f"missing required script file: scripts/{name}")
    if not (root / "scripts" / "tests" / "test_content_inventory.py").is_file():
        errors.append("missing inventory tests: scripts/tests/test_content_inventory.py")

    for directory in (root, root / "docs"):
        if directory.is_dir():
            for path in directory.iterdir():
                if path.is_file() and "changelog" in path.name.lower().replace("-", "").replace("_", ""):
                    errors.append(f"changelog is not part of the root contract: {path.relative_to(root)}")

    claude = root / "CLAUDE.md"
    if claude.is_file() and claude.read_text(encoding="utf-8") != "Read and follow [AGENTS.md](AGENTS.md).\n":
        errors.append("CLAUDE.md must contain only the AGENTS.md pointer")

    ignore = root / ".gitignore"
    if ignore.is_file():
        entries = {line.strip() for line in ignore.read_text(encoding="utf-8").splitlines()
                   if line.strip() and not line.lstrip().startswith("#")}
        for missing in sorted(REQUIRED_GITIGNORE - entries):
            errors.append(f".gitignore missing shared entry: {missing}")

    attributes = root / ".gitattributes"
    if attributes.is_file():
        text = attributes.read_text(encoding="utf-8")
        for marker in (
            "* text=auto eol=lf",
            "*.png binary",
            "**/*.atlas.md -text",
            "versioning/*/verification/evidence/** -text",
            "versioning/*/tests/fixtures/** -text",
        ):
            if marker not in text:
                errors.append(f".gitattributes missing byte-policy marker: {marker}")

    return errors


def check_identities(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
        if not re.fullmatch(r"(?:Stable|Alpha)-v\d+\.\d+\.\d+", version):
            errors.append("VERSION has an unsupported edition identity")
        if not (root / "versioning" / version / "README.md").is_file():
            errors.append("VERSION does not identify an edition manual")
        citation = (root / "CITATION.cff").read_text(encoding="utf-8")
        if not re.search(r"^version:\s*[\"\']?" + re.escape(version) + r"[\"\']?\s*$", citation, re.M):
            errors.append("CITATION.cff and VERSION differ")
        metadata = json.loads((root / "assets" / "asset-metadata.json").read_text(encoding="utf-8"))
        if metadata.get("version") != version:
            errors.append("assets/asset-metadata.json and VERSION differ")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        errors.append(f"identity validation failed: {error}")
    return errors


def check_links(root: Path) -> tuple[list[str], int, int]:
    errors: list[str] = []
    local_links = 0
    markdown = 0
    for source in sorted(root.rglob("*.md")):
        relative = source.relative_to(root)
        if any(part in IGNORED_PARTS or part.endswith(".egg-info") for part in relative.parts):
            continue
        markdown += 1
        text = source.read_text(encoding="utf-8")
        text = re.sub(r"^(```|~~~).*?^\1\s*$", "", text, flags=re.M | re.S)
        targets = re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", text)
        targets += re.findall(r'(?:src|href)=["\']([^"\']+)["\']', text)
        for target in targets:
            target = target.strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or (not parsed.path and not parsed.fragment):
                continue
            local_links += 1
            path = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            try:
                path.relative_to(root)
            except ValueError:
                errors.append(f"{relative}: link leaves repository: {target}")
                continue
            if not path.exists():
                errors.append(f"{relative}: missing target: {target}")
            elif parsed.fragment and path.is_file() and path.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(path):
                    errors.append(f"{relative}: missing anchor: {target}")
    return errors, markdown, local_links


def check_snapshots(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    snapshots = 0
    for source in sorted(root.glob("versioning/*/verification/source-baselines.json")):
        edition = source.parent.parent
        data = json.loads(source.read_text(encoding="utf-8"))
        for item in data["files"]:
            target = edition / item["snapshot_path"]
            snapshots += 1
            if not target.is_file():
                errors.append(f"missing snapshot: {target.relative_to(root)}")
                continue
            raw = target.read_bytes()
            if len(raw) != item["size_bytes"] or hashlib.sha256(raw).hexdigest() != item["sha256"]:
                errors.append(f"changed snapshot: {target.relative_to(root)}")
    return errors, snapshots


def check_text_bytes(root: Path) -> list[str]:
    errors: list[str] = []
    for name in delivery_files(root):
        path = root / name
        if exact_bytes(name) or (path.suffix.lower() not in TEXT_SUFFIXES and path.name not in TEXT_NAMES):
            continue
        raw = path.read_bytes()
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"text is not UTF-8: {name}")
            continue
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"UTF-8 BOM is not allowed: {name}")
        if b"\r" in raw:
            errors.append(f"text does not use LF-only line endings: {name}")
        if raw and not raw.endswith(b"\n"):
            errors.append(f"text lacks final newline: {name}")
    return errors


def check(root: Path) -> dict:
    errors = check_contract(root) + check_identities(root)
    link_errors, markdown, local_links = check_links(root)
    snapshot_errors, snapshots = check_snapshots(root)
    errors += link_errors + snapshot_errors + check_text_bytes(root)
    return {
        "status": "failed" if errors else "passed",
        "markdown_files": markdown,
        "local_links": local_links,
        "source_snapshots": snapshots,
        "errors": errors,
        "limits": [
            "External URLs are not fetched.",
            "Structural documentation checks do not prove behavioral correctness.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = check(args.root.resolve())
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        report = {"status": "failed", "errors": [str(error)]}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        metrics = ", ".join(
            f"{key}={report[key]}" for key in ("markdown_files", "local_links", "source_snapshots")
            if key in report
        )
        print(f"Repository {report['status']}: {metrics}")
        for error in report["errors"]:
            print(error, file=sys.stderr)
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
