"""Cross-file validator for distributed Minerva Markdown projects."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import yaml

from .markdown import ModuleError, load_module


def _safe(root: Path, relative: str) -> Path:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {relative}") from exc
    if Path(relative).is_absolute() or "\\" in relative or ".." in Path(relative).parts:
        raise ValueError(f"non-portable project path: {relative}")
    return candidate


def _contains(value: Any, target: Any) -> bool:
    if value == target:
        return True
    if isinstance(value, dict):
        return any(_contains(child, target) for child in value.values())
    if isinstance(value, list):
        return any(_contains(child, target) for child in value)
    return False


def _semantic_hash(atlas: dict) -> str:
    text = json.dumps(atlas, ensure_ascii=False, indent=2, separators=(",", ": "), allow_nan=False) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def validate_project(root: Path) -> dict:
    root = root.resolve()
    errors: list[dict[str, str]] = []

    def error(code: str, location: str, message: str) -> None:
        errors.append({"code": code, "location": location, "message": message})

    manifest_path = root / "minerva.project.yaml"
    if not manifest_path.is_file():
        return {"status": "invalid", "errors": [{"code": "MIN-E-MANIFEST", "location": str(manifest_path), "message": "manifest is missing"}]}
    try:
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return {"status": "invalid", "errors": [{"code": "MIN-E-MANIFEST", "location": str(manifest_path), "message": str(exc)}]}
    if not isinstance(manifest, dict) or manifest.get("format") != "minerva-project/1.0.0" or manifest.get("model_version") != "Stable-v1.0.0":
        error("MIN-E-VERSION", "minerva.project.yaml", "unsupported project format/model version")

    listed = manifest.get("modules", []) if isinstance(manifest, dict) else []
    if not isinstance(listed, list) or len(listed) != len(set(listed)):
        error("MIN-E-MODULES", "minerva.project.yaml", "modules must be a unique list")
        listed = []
    modules = {}
    ids = {}
    targets = {}
    for relative in listed:
        try:
            path = _safe(root, relative)
            module = load_module(path)
        except (ValueError, OSError, UnicodeError, ModuleError) as exc:
            error("MIN-E-MODULE", str(relative), str(exc))
            continue
        modules[relative] = module
        identity = module.metadata.get("id")
        if not isinstance(identity, str) or not identity:
            error("MIN-E-ID", relative, "module id is required")
        elif identity in ids:
            error("MIN-E-ID", relative, f"duplicate module id {identity}")
        else:
            ids[identity] = module
        generation = module.metadata.get("generation", {})
        if not isinstance(generation, dict) or generation.get("mode") not in {"code", "contract_only", "test", "composition", "documentation_only"}:
            error("MIN-E-GENERATION", relative, "generation.mode is invalid")
        target = generation.get("path") if isinstance(generation, dict) else None
        if target:
            if target in targets:
                error("MIN-E-TARGET", relative, f"generation target also owned by {targets[target]}")
            targets[target] = relative
        if "observed_boundary" in module.text or "observed boundary" in module.text.lower():
            error("MIN-E-TERMINOLOGY", relative, "use observation_point; Boundary is reserved for interaction adapters")

    try:
        source_path = _safe(root, manifest["source"]["artifact"])
        normalized = json.loads(source_path.read_text(encoding="utf-8"))
    except (KeyError, ValueError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        error("MIN-E-SOURCE", "minerva.project.yaml/source", str(exc))
        normalized = {}
    if normalized.get("format") != "atlas-normalized/1.1.0":
        error("MIN-E-SOURCE", "provenance/atlas.normalized.json", "Atlas normalized 1.1.0 is required")
    elif _semantic_hash(normalized["atlas"]) != normalized.get("source", {}).get("semantic_sha256"):
        error("MIN-E-SOURCE-HASH", "provenance/atlas.normalized.json", "semantic hash does not match the Atlas payload")
    elif normalized["source"]["semantic_sha256"] != manifest.get("source", {}).get("semantic_sha256"):
        error("MIN-E-SOURCE-HASH", "minerva.project.yaml/source", "manifest and source semantic hashes disagree")

    try:
        coverage_path = _safe(root, manifest["coverage"])
        coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    except (KeyError, ValueError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        error("MIN-E-COVERAGE", "minerva.project.yaml/coverage", str(exc))
        coverage = {}
    concepts = {item["id"]: item for item in normalized.get("concepts", []) if isinstance(item, dict) and "id" in item}
    entries = coverage.get("entries", []) if isinstance(coverage, dict) else []
    entry_refs = [entry.get("source_ref") for entry in entries if isinstance(entry, dict)]
    if set(entry_refs) != set(concepts) or len(entry_refs) != len(set(entry_refs)):
        error("MIN-E-COVERAGE", "provenance/coverage.json", "coverage must map every Atlas concept exactly once")
    for entry in entries:
        if not isinstance(entry, dict) or entry.get("source_ref") not in concepts:
            continue
        relative = entry.get("module")
        module = modules.get(relative)
        if module is None:
            error("MIN-E-COVERAGE-MODULE", str(relative), "coverage points to an unlisted or invalid module")
        elif not _contains(module.atlas_source, concepts[entry["source_ref"]]["content"]):
            error("MIN-E-SEMANTIC-LOSS", relative, f"module does not preserve exact Atlas concept {entry['source_ref']}")

    known_sources = set(concepts)
    if normalized:
        known_sources.add(normalized.get("atlas", {}).get("document_id"))
    for relative, module in modules.items():
        refs = module.metadata.get("source_refs")
        if not isinstance(refs, list) or not refs:
            error("MIN-E-SOURCE-REF", relative, "source_refs must be nonempty")
        else:
            for ref in refs:
                if ref not in known_sources:
                    error("MIN-E-SOURCE-REF", relative, f"unknown Atlas source ref {ref}")

    abstract_tools = {identity for identity, module in ids.items() if module.metadata.get("kind") == "abstract_tool"}
    concrete_tools = {identity: module for identity, module in ids.items() if module.metadata.get("kind") == "concrete_tool"}
    implementations: dict[str, list[str]] = {identity: [] for identity in abstract_tools}
    for identity, module in concrete_tools.items():
        design = module.design
        for abstract in design.get("implements", []):
            if abstract not in abstract_tools:
                error("MIN-E-TOOL", str(module.path), f"concrete tool implements unknown abstract tool {abstract}")
            else:
                implementations[abstract].append(identity)
        if design.get("design_status") != "complete":
            error("MIN-E-TOOL-DESIGN", str(module.path), "Stable examples require complete external concrete-tool design data")
        if not design.get("methods"):
            error("MIN-E-TOOL-DESIGN", str(module.path), "concrete tool must describe its methods")
    for abstract, concrete in implementations.items():
        if not concrete:
            error("MIN-E-TOOL", ids[abstract].path.as_posix(), "every abstract tool needs at least one concrete tool design")

    for identity, module in ids.items():
        kind = module.metadata.get("kind")
        if kind == "boundary":
            if module.design.get("class_kind") != "boundary_adapter" or not module.design.get("methods"):
                error("MIN-E-BOUNDARY", str(module.path), "Boundary must be an interaction adapter exposing use-case methods")
        if kind == "behavioral_test":
            for scenario in module.design.get("scenarios", []):
                if "observation_points" not in scenario:
                    error("MIN-E-OBSERVATION", str(module.path), "test scenarios declare observation_points")

    try:
        graph_path = _safe(root, manifest["knowledge_graph"])
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        if graph.get("format") != "minerva-knowledge-graph/1.0.0":
            error("MIN-E-GRAPH", manifest["knowledge_graph"], "unsupported knowledge graph format")
        if graph.get("model_version") != "Stable-v1.0.0" or graph.get("project_id") != manifest.get("project_id"):
            error("MIN-E-GRAPH", manifest["knowledge_graph"], "knowledge graph identity differs from the project")
        graph_ids = {node["id"] for node in graph.get("nodes", [])}
        if not set(concepts).issubset(graph_ids):
            error("MIN-E-GRAPH", manifest["knowledge_graph"], "knowledge graph omits Atlas concepts")
        if not {f"MOD:{identity}" for identity in ids}.issubset(graph_ids):
            error("MIN-E-GRAPH", manifest["knowledge_graph"], "knowledge graph omits Minerva modules")
        for edge in graph.get("edges", []):
            if edge.get("from") not in graph_ids or edge.get("to") not in graph_ids:
                error("MIN-E-GRAPH", manifest["knowledge_graph"], "knowledge graph edge has an unknown endpoint")
        if not any(edge.get("relation") == "implements" for edge in graph.get("edges", [])) and abstract_tools:
            error("MIN-E-GRAPH", manifest["knowledge_graph"], "knowledge graph omits concrete-tool implementation edges")
    except (KeyError, ValueError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        error("MIN-E-GRAPH", "minerva.project.yaml/knowledge_graph", str(exc))

    return {
        "status": "passed" if not errors else "invalid",
        "model_version": manifest.get("model_version") if isinstance(manifest, dict) else None,
        "counts": {
            "modules": len(modules),
            "atlas_concepts": len(concepts),
            "concrete_tools": len(concrete_tools),
            "generation_targets": len(targets),
        },
        "errors": errors,
    }
