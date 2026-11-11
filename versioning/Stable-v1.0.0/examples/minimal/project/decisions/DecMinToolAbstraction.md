---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: DEC-MIN-TOOL-ABSTRACTION
kind: decision
source_refs:
- DEC-MIN-TOOL-ABSTRACTION
generation:
  mode: documentation_only
---

# Keep the store abstract

Preserves Atlas decision DEC-MIN-TOOL-ABSTRACTION.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "DEC-MIN-TOOL-ABSTRACTION",
  "title": {
    "text": "Keep the store abstract"
  },
  "context": [
    {
      "type": "paragraph",
      "text": "The example needs persistence but must not choose a technology."
    }
  ],
  "decision": [
    {
      "type": "paragraph",
      "text": "Define OP-REQUEST-STORE as a tool contract only."
    }
  ],
  "alternatives": [
    {
      "type": "paragraph",
      "text": "Specify SQLite tables and SQL statements."
    }
  ],
  "consequences": [
    {
      "type": "paragraph",
      "text": "Implementations may choose storage, but must satisfy the contract."
    }
  ],
  "status": "accepted",
  "refs": [
    "TOL-REQUEST-STORE"
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
