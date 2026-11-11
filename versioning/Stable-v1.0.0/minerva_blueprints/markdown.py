"""Strict Markdown module codec for Minerva Stable-v1.0.0."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


FORMAT = "minerva-markdown/1.0.0"
MODEL_VERSION = "Stable-v1.0.0"
FENCE_RE = re.compile(r"^```(?P<name>atlas-source-json|minerva-design-json)\n(?P<body>.*?)\n```$", re.MULTILINE | re.DOTALL)


class ModuleError(ValueError):
    pass


@dataclass(frozen=True)
class MinervaModule:
    path: Path
    metadata: dict[str, Any]
    atlas_source: Any
    design: dict[str, Any]
    text: str


def _frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ModuleError("module must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ModuleError("frontmatter closing delimiter is missing")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise ModuleError("frontmatter must be a mapping")
    return data, text[end + 5 :]


def load_module(path: Path) -> MinervaModule:
    text = path.read_text(encoding="utf-8")
    metadata, body = _frontmatter(text)
    if metadata.get("format") != FORMAT or metadata.get("model_version") != MODEL_VERSION:
        raise ModuleError(f"{path}: unsupported Minerva format/model version")
    fences: dict[str, Any] = {}
    for match in FENCE_RE.finditer(body):
        name = match.group("name")
        if name in fences:
            raise ModuleError(f"{path}: duplicate {name} fence")
        try:
            fences[name] = json.loads(match.group("body"))
        except json.JSONDecodeError as exc:
            raise ModuleError(f"{path}: invalid {name}: {exc}") from exc
    if set(fences) != {"atlas-source-json", "minerva-design-json"}:
        raise ModuleError(f"{path}: both controlled JSON fences are required")
    if not isinstance(fences["minerva-design-json"], dict):
        raise ModuleError(f"{path}: minerva-design-json must be an object")
    return MinervaModule(path, metadata, fences["atlas-source-json"], fences["minerva-design-json"], text)


def dump_module(metadata: dict[str, Any], title: str, summary: str, source: Any, design: dict[str, Any]) -> str:
    header = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True).rstrip()
    return (
        "---\n"
        + header
        + "\n---\n\n# "
        + title
        + "\n\n"
        + summary.strip()
        + "\n\n## Preserved Atlas semantics\n\n"
        + "```atlas-source-json\n"
        + json.dumps(source, ensure_ascii=False, indent=2)
        + "\n```\n\n## Generation-oriented design\n\n"
        + "```minerva-design-json\n"
        + json.dumps(design, ensure_ascii=False, indent=2)
        + "\n```\n"
    )
