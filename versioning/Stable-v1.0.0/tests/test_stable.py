from __future__ import annotations

import json
import unittest
from pathlib import Path

import yaml

from minerva_blueprints.markdown import load_module
from minerva_blueprints.validation import validate_project


ROOT = Path(__file__).resolve().parents[1]


class StableContractTests(unittest.TestCase):
    def test_all_maintained_examples_validate(self):
        for name in ("minimal", "composition", "task-board"):
            with self.subTest(name=name):
                report = validate_project(ROOT / "examples" / name)
                self.assertEqual(report["status"], "passed", report["errors"])
                self.assertGreater(report["counts"]["atlas_concepts"], 0)
                self.assertGreater(report["counts"]["generation_targets"], 0)

    def test_manifest_is_discovery_not_semantic_appendix(self):
        root = ROOT / "examples" / "minimal"
        manifest = yaml.safe_load((root / "minerva.project.yaml").read_text(encoding="utf-8"))
        self.assertEqual(manifest["semantic_authority"], "distributed_markdown_modules")
        self.assertNotIn("atlas", manifest)
        self.assertGreater(len(manifest["modules"]), 10)

    def test_use_case_is_generation_ready_and_preserves_atlas(self):
        path = ROOT / "examples/minimal/apps/RequestRegister/usecases/Main/UseCase_SubmitRequest.md"
        module = load_module(path)
        self.assertEqual(module.metadata["kind"], "use_case")
        self.assertEqual(module.design["methods"][0]["name"], "execute")
        self.assertTrue(module.design["methods"][0]["algorithm"])
        self.assertEqual(module.atlas_source["id"], "UC-REQUEST-SUBMIT")
        self.assertTrue(module.design["consumed_entities"])
        self.assertTrue(module.design["injected_tools"])

    def test_boundary_and_observation_point_terms_are_distinct(self):
        root = ROOT / "examples/minimal"
        boundary = load_module(root / "apps/RequestRegister/boundaries/Boundary_RequestRegisterWebForm.md")
        test = load_module(root / "apps/RequestRegister/tests/BehavioralTest_SubmitRequest.md")
        self.assertEqual(boundary.design["class_kind"], "boundary_adapter")
        self.assertTrue(boundary.design["methods"][0]["exposes_use_case"])
        self.assertIn("observation_points", test.design["scenarios"][0])
        self.assertNotIn("observed_boundary", test.text)

    def test_knowledge_graph_contains_tool_lineage_and_all_atlas_ids(self):
        root = ROOT / "examples/task-board"
        graph = json.loads((root / "knowledge/graph.json").read_text(encoding="utf-8"))
        coverage = json.loads((root / "provenance/coverage.json").read_text(encoding="utf-8"))
        node_ids = {node["id"] for node in graph["nodes"]}
        self.assertTrue({entry["source_ref"] for entry in coverage["entries"]} <= node_ids)
        self.assertTrue(any(edge["relation"] == "implements" for edge in graph["edges"]))


if __name__ == "__main__":
    unittest.main()
