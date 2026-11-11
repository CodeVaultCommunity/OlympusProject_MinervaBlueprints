from __future__ import annotations

import json
from pathlib import Path

from minerva_blueprints.validation import validate_project


def main() -> int:
    root = Path(__file__).resolve().parent
    reports = {name: validate_project(root / "examples" / name) for name in ("minimal", "composition", "task-board")}
    print(json.dumps(reports, ensure_ascii=False, indent=2))
    return 0 if all(report["status"] == "passed" for report in reports.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
