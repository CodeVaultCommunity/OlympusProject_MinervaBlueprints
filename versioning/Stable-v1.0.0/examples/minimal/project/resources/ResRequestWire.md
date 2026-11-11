---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: RES-REQUEST-WIRE
kind: resource
source_refs:
- RES-REQUEST-WIRE
generation:
  mode: documentation_only
---

# RES-REQUEST-WIRE

Preserves Atlas resource RES-REQUEST-WIRE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "RES-REQUEST-WIRE",
  "source_uri": null,
  "path": "assets/request-form.svg",
  "media_type": "image/svg+xml",
  "sha256": "f5a97fb7cb43af9681b2083fe1deebe38bb3eda24adb947c3314317fc8a24de9",
  "size": 1663,
  "caption": [
    {
      "type": "paragraph",
      "text": "Request form wireframe: Request code, Quantity, and Submit request."
    }
  ],
  "alt": [
    {
      "type": "paragraph",
      "text": "A form with a Request code field, a Quantity field, and a Submit request button. A result area reports confirmation, invalid data, duplicate code, or tool failure."
    }
  ],
  "embedded_text": [
    {
      "text": "Request code"
    },
    {
      "text": "Quantity"
    },
    {
      "text": "Submit request"
    }
  ],
  "drawing_source": {
    "path": "assets/request-form.svg",
    "revision": "1",
    "tool": "scripts/build_examples.py"
  },
  "variants": [
    {
      "path": "assets/request-form.png",
      "media_type": "image/png",
      "sha256": "5dd57bf8bccc9bcd9b68e1be1ea50163777caf93d83f6fbfec1a099eb1d84347",
      "size": 22242,
      "relation": "publication",
      "derived_from": "assets/request-form.svg",
      "producer": "scripts/build_examples.py"
    }
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
