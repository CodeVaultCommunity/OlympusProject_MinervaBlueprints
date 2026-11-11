---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: CMP-BOOKINGDESK
kind: composition
source_refs:
- TOL-BOOKING-STORE
generation:
  mode: code
  language: python
  path: apps/BookingDesk/composition/AppComposition.py
  symbol: AppComposition
---

# BookingDesk composition

Composition root and dependency selection for generated code.

## Preserved Atlas semantics

```atlas-source-json
{
  "source_document_id": "ATLAS-EX-COMPOSITION"
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/BookingDesk/composition/AppComposition.py",
    "symbol": "AppComposition"
  },
  "class_kind": "composition_root",
  "construct": [
    "CTL-BOOKING-STORE"
  ],
  "inject": [
    {
      "abstract_tool_ref": "TOL-BOOKING-STORE",
      "concrete_tool_ref": "CTL-BOOKING-STORE"
    }
  ],
  "boundaries": [
    "BND-BOOKING-CLI"
  ],
  "entrypoints": [
    "cli",
    "http_or_declared_modality"
  ]
}
```
