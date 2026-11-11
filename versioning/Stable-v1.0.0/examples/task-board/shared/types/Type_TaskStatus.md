---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TYP-TASK-STATUS
kind: type
source_refs:
- TYP-TASK-STATUS
generation:
  mode: code
  language: python
  path: apps/TaskBoard/types/Type_TaskStatus.py
  symbol: Type_TaskStatus
---

# Task status

Preserves Atlas type TYP-TASK-STATUS.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "TYP-TASK-STATUS",
  "name": {
    "text": "Task status"
  },
  "definition": [
    {
      "type": "paragraph",
      "text": "Lifecycle state of a Task."
    }
  ],
  "constraints": [
    {
      "type": "paragraph",
      "text": "Exactly open or completed."
    }
  ],
  "examples": [
    {
      "text": "open"
    },
    {
      "text": "completed"
    }
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/TaskBoard/types/Type_TaskStatus.py",
    "symbol": "Type_TaskStatus"
  },
  "class_kind": "value_type",
  "base": null,
  "constraints": [
    {
      "type": "paragraph",
      "text": "Exactly open or completed."
    }
  ]
}
```
