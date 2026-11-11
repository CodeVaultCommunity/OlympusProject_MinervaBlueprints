---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: CMP-TASKBOARD
kind: composition
source_refs:
- TOL-TASK-STORE
generation:
  mode: code
  language: python
  path: apps/TaskBoard/composition/AppComposition.py
  symbol: AppComposition
---

# TaskBoard composition

Composition root and dependency selection for generated code.

## Preserved Atlas semantics

```atlas-source-json
{
  "source_document_id": "DOC-TASK-BOARD"
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/TaskBoard/composition/AppComposition.py",
    "symbol": "AppComposition"
  },
  "class_kind": "composition_root",
  "construct": [
    "CTL-TASK-STORE"
  ],
  "inject": [
    {
      "abstract_tool_ref": "TOL-TASK-STORE",
      "concrete_tool_ref": "CTL-TASK-STORE"
    }
  ],
  "boundaries": [
    "BND-TASK-ILLUSTRATION"
  ],
  "entrypoints": [
    "cli",
    "http_or_declared_modality"
  ]
}
```
