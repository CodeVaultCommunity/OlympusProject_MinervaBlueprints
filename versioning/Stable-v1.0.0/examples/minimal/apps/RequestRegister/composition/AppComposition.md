---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: CMP-REQUESTREGISTER
kind: composition
source_refs:
- TOL-REQUEST-STORE
generation:
  mode: code
  language: python
  path: apps/RequestRegister/composition/AppComposition.py
  symbol: AppComposition
---

# RequestRegister composition

Composition root and dependency selection for generated code.

## Preserved Atlas semantics

```atlas-source-json
{
  "source_document_id": "ATLAS-EX-MINIMAL"
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/RequestRegister/composition/AppComposition.py",
    "symbol": "AppComposition"
  },
  "class_kind": "composition_root",
  "construct": [
    "CTL-REQUEST-STORE"
  ],
  "inject": [
    {
      "abstract_tool_ref": "TOL-REQUEST-STORE",
      "concrete_tool_ref": "CTL-REQUEST-STORE"
    }
  ],
  "boundaries": [
    "BND-REQUEST-WEB"
  ],
  "entrypoints": [
    "cli",
    "http_or_declared_modality"
  ]
}
```
