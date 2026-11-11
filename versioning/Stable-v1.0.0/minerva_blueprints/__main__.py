from __future__ import annotations

import argparse
import json
from pathlib import Path

from .importer import ImportError, import_atlas
from .validation import validate_project


def main_import(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="minerva-import-atlas")
    parser.add_argument("normalized", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--app", required=True)
    parser.add_argument("--language", default="python")
    parser.add_argument("--tool-designs", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    try:
        manifest = import_atlas(args.normalized, args.output, app=args.app, language=args.language, tool_designs_path=args.tool_designs, force=args.force)
    except (ImportError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


def main_validate(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="minerva-validate")
    parser.add_argument("project", type=Path)
    args = parser.parse_args(argv)
    report = validate_project(args.project)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "passed" else 1


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m minerva_blueprints")
    sub = parser.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import-atlas")
    imp.add_argument("args", nargs=argparse.REMAINDER)
    val = sub.add_parser("validate")
    val.add_argument("args", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    return main_import(args.args) if args.command == "import-atlas" else main_validate(args.args)


if __name__ == "__main__":
    raise SystemExit(main())
