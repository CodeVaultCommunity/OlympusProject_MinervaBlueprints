"""Atlas normalized hand-off to code-shaped Minerva Markdown modules."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

import yaml

from .markdown import dump_module
from .naming import pascal, prose, snake, text


class ImportError(ValueError):
    pass


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _target(app: str, kind: str, name: str, language: str = "python") -> dict[str, Any]:
    ext = {"python": "py", "typescript": "ts", "java": "java"}.get(language, language)
    folders = {
        "entity": "entities",
        "type": "types",
        "abstract_tool": "tools/abstract",
        "concrete_tool": "tools/concrete",
        "use_case": "usecases/Main",
        "boundary": "boundaries",
        "behavioral_test": "tests",
        "composition": "composition",
    }
    prefixes = {
        "entity": "Entity",
        "type": "Type",
        "abstract_tool": "AbstractTool",
        "concrete_tool": "Tool",
        "use_case": "UseCase",
        "boundary": "Boundary",
        "behavioral_test": "Test",
        "composition": "AppComposition",
    }
    symbol = prefixes[kind] + ("" if kind == "composition" else "_" + pascal(name))
    filename = symbol + "." + ext
    return {
        "language": language,
        "path": f"apps/{app}/{folders[kind]}/{filename}",
        "symbol": symbol,
    }


def _metadata(identity: str, kind: str, source_refs: list[str], target: dict | None, mode: str = "code") -> dict:
    generation: dict[str, Any] = {"mode": mode}
    if target:
        generation.update(target)
    return {
        "format": "minerva-markdown/1.0.0",
        "model_version": "Stable-v1.0.0",
        "id": identity,
        "kind": kind,
        "source_refs": source_refs,
        "generation": generation,
    }


def _entity_design(item: dict, app: str, language: str) -> dict:
    name = text(item["name"])
    methods = []
    for validation in item.get("validations", []):
        methods.append(
            {
                "name": "validate_" + snake(text(validation.get("name", validation["id"]))),
                "visibility": "private",
                "trigger": "during canonical construction and state transition",
                "parameters": [{"name": snake(text(x["name"])), "type": x.get("type", "unknown")} for x in validation.get("inputs", [])],
                "returns": [result.get("outcome", "result") for result in validation.get("results", [])],
                "algorithm": prose(validation.get("statement", [])),
                "source_refs": [validation["id"]],
            }
        )
    methods.insert(
        0,
        {
            "name": "create",
            "visibility": "public",
            "trigger": "when raw values enter the domain",
            "parameters": [{"name": snake(text(field["name"])), "type": field.get("type", "unknown")} for field in item.get("fields", [])],
            "returns": [pascal(name)],
            "algorithm": "Construct only after all Atlas entity validations pass; never leave a partially valid entity.",
            "source_refs": [item["id"], *[v["id"] for v in item.get("validations", [])]],
        },
    )
    return {
        "target": _target(app, "entity", name, language),
        "class_kind": "entity",
        "fields": [
            {
                "name": snake(text(field["name"])),
                "type": field.get("type", "unknown"),
                "required": field.get("required", True),
                "source_ref": field.get("id"),
            }
            for field in item.get("fields", [])
        ],
        "methods": methods,
        "dependencies": item.get("relationships", []),
    }


def _abstract_tool_design(item: dict, app: str, language: str) -> dict:
    name = text(item["name"])
    return {
        "target": _target(app, "abstract_tool", name, language),
        "class_kind": "protocol",
        "methods": [
            {
                "name": snake(text(operation["name"])),
                "parameters": [{"name": snake(text(x["name"])), "type": x.get("type", "unknown")} for x in operation.get("inputs", [])],
                "returns": [text(x["name"]) for x in operation.get("results", [])],
                "failures": [x.get("code") for x in operation.get("failures", [])],
                "effects": prose(operation.get("effects", [])),
                "source_refs": [operation["id"]],
            }
            for operation in item.get("operations", [])
        ],
    }


def _concrete_tool_design(item: dict, app: str, language: str, external: dict[str, Any] | None) -> dict:
    abstract_name = text(item["name"])
    external = dict(external or {})
    technology = external.pop("technology", "REQUIRES_EXTERNAL_DESIGN")
    concrete_name = external.pop("name", technology + " " + abstract_name)
    methods = []
    for operation in item.get("operations", []):
        methods.append(
            {
                "name": snake(text(operation["name"])),
                "implements_operation": operation["id"],
                "parameters": [{"name": snake(text(x["name"])), "type": x.get("type", "unknown")} for x in operation.get("inputs", [])],
                "returns": [text(x["name"]) for x in operation.get("results", [])],
                "algorithm": external.get("algorithm", "Translate the protocol call into the selected technology while preserving conditions, failures, effects, and guarantees."),
                "transaction": external.get("transaction", "Technology-specific transaction policy must preserve Atlas outcome certainty."),
                "error_mapping": {failure.get("code", "FAILURE"): failure.get("code", "FAILURE") for failure in operation.get("failures", [])},
            }
        )
    return {
        "target": _target(app, "concrete_tool", concrete_name, language),
        "class_kind": "concrete_tool",
        "implements": [item["id"]],
        "technology": technology,
        "design_status": "complete" if technology != "REQUIRES_EXTERNAL_DESIGN" else "requires_external_design",
        "methods": methods,
        "configuration": external.get("configuration", []),
        "lifecycle": external.get("lifecycle", "application_scope"),
        "dependencies": external.get("dependencies", []),
        "notes": external.get("notes", []),
    }


def _use_case_design(item: dict, app: str, language: str, concrete_by_abstract: dict[str, str]) -> dict:
    name = text(item["name"])
    calls = []
    for tool_use in item.get("tools", []):
        calls.append(
            {
                "abstract_tool_ref": tool_use["tool"],
                "operation_ref": tool_use["operation"],
                "injected_concrete_tool_ref": concrete_by_abstract.get(tool_use["tool"]),
                "purpose": prose(tool_use.get("purpose", [])),
            }
        )
    return {
        "target": _target(app, "use_case", name, language),
        "class_kind": "use_case",
        "consumed_entities": [entry["entity"] for entry in item.get("entities", [])],
        "injected_tools": calls,
        "methods": [
            {
                "name": "execute",
                "visibility": "public",
                "trigger": prose(item.get("trigger", [])),
                "parameters": [{"name": snake(text(x["name"])), "type": x.get("type", "unknown"), "required": x.get("required", True)} for x in item.get("inputs", [])],
                "authorization": {
                    "actor_refs": [actor["actor"] for actor in item.get("actors", [])],
                    "before_effects": True,
                },
                "algorithm": [block.get("text", "") for block in item.get("flow_text", [])],
                "returns": [{"outcome_ref": outcome["id"], "kind": outcome["kind"]} for outcome in item.get("outcomes", [])],
                "source_refs": [item["id"], *[req["id"] for req in item.get("functional_requirements", [])]],
            }
        ],
        "graph_refs": [item.get("flows", {}).get("main"), *item.get("flows", {}).get("subflows", [])],
    }


def _boundary_design(item: dict, app: str, language: str) -> dict:
    name = text(item["name"])
    return {
        "target": _target(app, "boundary", name, language),
        "class_kind": "boundary_adapter",
        "boundary_semantics": "Interaction interface only; never a test case or observation point.",
        "classification": item["classification"],
        "modality": item["modality"],
        "methods": [
            {
                "name": snake(text(interaction["name"])),
                "exposes_use_case": interaction["use_case"],
                "trigger": prose(interaction.get("trigger", [])),
                "input_mapping": interaction.get("input_mapping", []),
                "result_mapping": interaction.get("result_mapping", []),
                "source_refs": [interaction["id"], *interaction.get("requirement_refs", [])],
            }
            for interaction in item.get("interactions", [])
        ],
    }


def _test_design(case: dict, app: str, language: str) -> dict:
    name = text(case["name"])
    scenarios = []
    for criterion in case.get("acceptance_criteria", []):
        scenarios.append(
            {
                "id": "SCN-" + criterion["id"],
                "source_ref": criterion["id"],
                "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
                "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
                "then": prose(criterion.get("statement", [])),
                "observation_points": ["returned_outcome", "declared_effects", "concrete_tool_calls"],
            }
        )
    return {
        "target": _target(app, "behavioral_test", name, language),
        "class_kind": "behavioral_test",
        "tests_use_case": case["id"],
        "scenarios": scenarios,
        "graph_refs": [case.get("flows", {}).get("main"), *case.get("flows", {}).get("subflows", [])],
    }


def import_atlas(normalized_path: Path, output: Path, *, app: str, language: str = "python", tool_designs_path: Path | None = None, force: bool = False) -> dict:
    normalized = json.loads(normalized_path.read_text(encoding="utf-8"))
    if normalized.get("format") != "atlas-normalized/1.1.0":
        raise ImportError("Minerva Stable-v1.0.0 requires atlas-normalized/1.1.0")
    if output.exists() and any(output.iterdir()) and not force:
        raise ImportError(f"output {output} is not empty; pass force only for importer-owned trees")
    output.mkdir(parents=True, exist_ok=True)
    tool_designs = json.loads(tool_designs_path.read_text(encoding="utf-8")) if tool_designs_path else {}
    atlas = normalized["atlas"]
    concepts = normalized["concepts"]
    concept_by_id = {item["id"]: item for item in concepts}
    top = [item for item in concepts if item.get("owner_ref") is None]

    modules: list[str] = []
    coverage: dict[str, str] = {}
    module_ids: dict[str, str] = {}

    def write(relative: str, metadata: dict, title: str, summary: str, source: Any, design: dict) -> None:
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(dump_module(metadata, title, summary, source, design), encoding="utf-8", newline="\n")
        modules.append(relative)
        module_ids[metadata["id"]] = relative

    document_fields = {key: value for key, value in atlas.items() if key not in {
        "actors", "vocabulary", "types", "entities", "tools", "use_cases", "boundaries", "graphs",
        "resources", "assumptions", "decisions", "open_issues", "sources", "history",
    }}
    project_id = "MINERVA-" + "-".join(part.upper() for part in app.replace("_", "-").split("-") if part)
    project_design = {
        "target": None,
        "semantic_role": "distributed_project_metadata",
        "application": app,
        "source_document_id": atlas["document_id"],
        "source_revision": atlas["revision"],
        "language": atlas["language"],
        "rule": "This file is not an Atlas appendix. Atlas concepts live in the code-shaped modules listed by the manifest.",
    }
    write("project/Project.md", _metadata(project_id, "project", [atlas["document_id"]], None, "documentation_only"), text(atlas["title"]), "Project-wide semantics and generation context.", document_fields, project_design)

    path_for_owner: dict[str, str] = {}
    concrete_by_abstract: dict[str, str] = {}
    for concept in top:
        item, kind, identity = concept["content"], concept["kind"], concept["id"]
        if kind == "actor":
            relative = f"shared/actors/Actor_{pascal(text(item['name']))}.md"
            design = {"target": None, "role": "trusted_actor_role", "permissions": item.get("permissions", []), "generation": "referenced_type_or_policy"}
            title = text(item["name"])
        elif kind == "term":
            relative = f"project/vocabulary/Term_{pascal(text(item['term']))}.md"
            design = {"target": None, "role": "ubiquitous_language", "generation": "naming_constraint"}
            title = text(item["term"])
        elif kind == "type":
            title = text(item["name"])
            relative = f"shared/types/Type_{pascal(title)}.md"
            target = _target(app, "type", title, language)
            design = {"target": target, "class_kind": "value_type", "base": item.get("base"), "constraints": item.get("constraints", [])}
        elif kind == "entity":
            title = text(item["name"])
            relative = f"apps/{app}/entities/Entity_{pascal(title)}.md"
            design = _entity_design(item, app, language)
        elif kind == "abstract_tool":
            title = text(item["name"])
            relative = f"apps/{app}/tools/abstract/AbstractTool_{pascal(title)}.md"
            design = _abstract_tool_design(item, app, language)
        elif kind == "use_case":
            title = text(item["name"])
            relative = f"apps/{app}/usecases/Main/UseCase_{pascal(title)}.md"
            design = {}  # completed after concrete tool identities are known
        elif kind == "boundary":
            title = text(item["name"])
            relative = f"apps/{app}/boundaries/Boundary_{pascal(title)}.md"
            design = _boundary_design(item, app, language)
        elif kind == "graph":
            title = text(item.get("title", {"text": identity}))
            relative = f"apps/{app}/graphs/Graph_{pascal(title)}.md"
            design = {"target": None, "class_kind": "control_flow_graph", "owner": item.get("owner"), "nodes": item.get("nodes", []), "edges": item.get("edges", []), "generation": "method_control_flow"}
        else:
            title = text(item.get("title", item.get("name", {"text": identity})))
            folder = {"resource": "resources", "assumption": "assumptions", "decision": "decisions", "open_issue": "open_issues", "source": "sources", "history_entry": "history"}.get(kind, kind + "s")
            relative = f"project/{folder}/{pascal(identity)}.md"
            design = {"target": None, "class_kind": "provenance_or_constraint", "generation": "documentation_or_code_comment"}
        path_for_owner[identity] = relative
        if kind != "use_case":
            write(relative, _metadata(identity, kind, [identity], design.get("target"), "code" if design.get("target") else "documentation_only"), title or identity, prose(item.get("purpose", item.get("description", []))) or f"Preserves Atlas {kind} {identity}.", item, design)

        if kind == "abstract_tool":
            concrete_id = "CTL-" + identity.split("-", 1)[-1]
            concrete_design = _concrete_tool_design(item, app, language, tool_designs.get(identity))
            concrete_title = concrete_design["technology"] + " implementation of " + title
            concrete_relative = f"apps/{app}/tools/concrete/Tool_{pascal(concrete_title)}.md"
            concrete_by_abstract[identity] = concrete_id
            write(concrete_relative, _metadata(concrete_id, "concrete_tool", [identity], concrete_design["target"]), concrete_title, f"Concrete design implementing Atlas abstract tool {identity}; no executable code is stored in Minerva.", item, concrete_design)

    # Use cases are written after the concrete-tool registry exists.
    for concept in [item for item in top if item["kind"] == "use_case"]:
        case = concept["content"]
        identity = concept["id"]
        relative = path_for_owner[identity]
        design = _use_case_design(case, app, language, concrete_by_abstract)
        write(relative, _metadata(identity, "use_case", [identity], design["target"]), text(case["name"]), prose(case.get("objective", [])), case, design)
        test_id = "TST-" + identity.split("-", 1)[-1]
        test_design = _test_design(case, app, language)
        test_relative = f"apps/{app}/tests/BehavioralTest_{pascal(text(case['name']))}.md"
        write(test_relative, _metadata(test_id, "behavioral_test", [identity, *[criterion["id"] for criterion in case.get("acceptance_criteria", [])]], test_design["target"], "test"), f"Behavioral tests for {text(case['name'])}", "Executable-test design derived from Atlas acceptance criteria. Scenario observations are observation_points, never Boundaries.", {"use_case": identity, "acceptance_criteria": case.get("acceptance_criteria", [])}, test_design)

    composition_id = "CMP-" + project_id.split("-", 1)[-1]
    composition_design = {
        "target": _target(app, "composition", app, language),
        "class_kind": "composition_root",
        "construct": sorted(concrete_by_abstract.values()),
        "inject": [{"abstract_tool_ref": abstract, "concrete_tool_ref": concrete} for abstract, concrete in sorted(concrete_by_abstract.items())],
        "boundaries": [item["id"] for item in top if item["kind"] == "boundary"],
        "entrypoints": ["cli", "http_or_declared_modality"],
    }
    write(f"apps/{app}/composition/AppComposition.md", _metadata(composition_id, "composition", list(concrete_by_abstract), composition_design["target"]), f"{app} composition", "Composition root and dependency selection for generated code.", {"source_document_id": atlas["document_id"]}, composition_design)

    # Every nested Atlas concept is covered by its owning module; top-level concepts by their own module.
    for concept in concepts:
        relative = path_for_owner.get(concept["id"]) or path_for_owner.get(concept.get("owner_ref"))
        if relative is None:
            raise ImportError(f"no module owner for Atlas concept {concept['id']}")
        coverage[concept["id"]] = relative

    provenance = output / "provenance"
    provenance.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(normalized_path, provenance / "atlas.normalized.json")
    ledger = {
        "format": "minerva-coverage/1.0.0",
        "source_semantic_sha256": normalized["source"]["semantic_sha256"],
        "concept_count": len(concepts),
        "entries": [
            {
                "source_ref": concept["id"],
                "source_kind": concept["kind"],
                "source_pointer": concept["pointer"],
                "module": coverage[concept["id"]],
            }
            for concept in concepts
        ],
    }
    (provenance / "coverage.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    graph_nodes = [
        {"id": concept["id"], "kind": concept["kind"], "module": coverage[concept["id"]], "layer": "atlas"}
        for concept in concepts
    ]
    graph_nodes.extend(
        {
            "id": f"MOD:{identity}",
            "kind": "minerva_module",
            "module_id": identity,
            "module": relative,
            "layer": "minerva",
        }
        for identity, relative in sorted(module_ids.items())
    )
    graph_edges = [dict(edge, layer="atlas") for edge in normalized.get("relations", [])]
    graph_edges.extend(
        {"from": f"MOD:{concrete}", "to": f"MOD:{abstract}", "relation": "implements", "layer": "minerva"}
        for abstract, concrete in sorted(concrete_by_abstract.items())
    )
    module_id_by_path = {relative: identity for identity, relative in module_ids.items()}
    for entry in ledger["entries"]:
        owner = module_id_by_path[entry["module"]]
        graph_edges.append({"from": entry["source_ref"], "to": f"MOD:{owner}", "relation": "described_by", "layer": "minerva"})
    knowledge = output / "knowledge"
    knowledge.mkdir(parents=True, exist_ok=True)
    (knowledge / "graph.json").write_text(
        json.dumps(
            {
                "format": "minerva-knowledge-graph/1.0.0",
                "model_version": "Stable-v1.0.0",
                "project_id": project_id,
                "nodes": graph_nodes,
                "edges": graph_edges,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )

    manifest = {
        "format": "minerva-project/1.0.0",
        "model_version": "Stable-v1.0.0",
        "project_id": project_id,
        "app": app,
        "source": {
            "format": normalized["format"],
            "document_id": atlas["document_id"],
            "revision": atlas["revision"],
            "semantic_sha256": normalized["source"]["semantic_sha256"],
            "artifact": "provenance/atlas.normalized.json",
        },
        "semantic_authority": "distributed_markdown_modules",
        "modules": sorted(modules),
        "coverage": "provenance/coverage.json",
        "knowledge_graph": "knowledge/graph.json",
    }
    (output / "minerva.project.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8", newline="\n")
    return manifest
