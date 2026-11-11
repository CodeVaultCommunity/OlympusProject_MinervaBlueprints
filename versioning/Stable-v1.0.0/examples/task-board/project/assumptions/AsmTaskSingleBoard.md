---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: ASM-TASK-SINGLE-BOARD
kind: assumption
source_refs:
- ASM-TASK-SINGLE-BOARD
generation:
  mode: documentation_only
---

# ASM-TASK-SINGLE-BOARD

Preserves Atlas assumption ASM-TASK-SINGLE-BOARD.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "ASM-TASK-SINGLE-BOARD",
  "statement": [
    {
      "type": "paragraph",
      "text": "Synthetic scope assumes one resolved board per invocation and stable task identifiers within that board."
    }
  ],
  "status": "open",
  "affected": [
    "ENT-TASK",
    "TOL-TASK-STORE",
    "UC-TASK-CREATE",
    "UC-TASK-COMPLETE",
    "UC-TASK-LIST"
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": null,
  "class_kind": "provenance_or_constraint",
  "generation": "documentation_or_code_comment"
}
```
