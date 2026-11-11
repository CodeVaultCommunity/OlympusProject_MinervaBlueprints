from __future__ import annotations

import re


def words(value: str) -> list[str]:
    return [part for part in re.split(r"[^A-Za-z0-9]+", value) if part]


def pascal(value: str) -> str:
    return "".join(part[:1].upper() + part[1:].lower() for part in words(value)) or "Unnamed"


def snake(value: str) -> str:
    return "_".join(part.lower() for part in words(value)) or "unnamed"


def text(value: object) -> str:
    if isinstance(value, dict):
        return str(value.get("text", ""))
    return str(value)


def prose(blocks: object) -> str:
    if not isinstance(blocks, list):
        return text(blocks)
    parts: list[str] = []
    for block in blocks:
        if isinstance(block, dict):
            if "text" in block:
                parts.append(str(block["text"]))
            elif block.get("type") == "list":
                parts.extend(str(item.get("text", "")) for item in block.get("items", []))
    return " ".join(part for part in parts if part)
