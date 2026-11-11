---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: RES-REQUEST-FLOW
kind: resource
source_refs:
- RES-REQUEST-FLOW
generation:
  mode: documentation_only
---

# RES-REQUEST-FLOW

Preserves Atlas resource RES-REQUEST-FLOW.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "RES-REQUEST-FLOW",
  "source_uri": null,
  "path": "assets/request-flow.svg",
  "media_type": "image/svg+xml",
  "sha256": "71f3a97b667a88041cc5812da8c8e7e1ddaced2f9c835e56c2c7d6d1b4252206",
  "size": 10124,
  "caption": [
    {
      "type": "paragraph",
      "text": "Submission flow with authorization, code and quantity validation, persistence, duplicate refusal and explicit write failure. The edge key identifies every structured edge."
    }
  ],
  "alt": [
    {
      "type": "paragraph",
      "text": "Every node and edge of GRAPH-REQUEST-SUBMIT, with wrapped labels and an edge key. The text and graph records provide the complete accessible description."
    }
  ],
  "embedded_text": [
    {
      "text": "Start"
    },
    {
      "text": "Actor permitted?"
    },
    {
      "text": "Refuse: actor not permitted"
    },
    {
      "text": "Apply VLD-REQUEST-QUANTITY"
    },
    {
      "text": "Quantity valid?"
    },
    {
      "text": "Invalid code or quantity"
    },
    {
      "text": "Store request"
    },
    {
      "text": "Report STORE_UNAVAILABLE"
    },
    {
      "text": "Request confirmed"
    },
    {
      "text": "Duplicate code; no change"
    },
    {
      "text": "Apply code validity"
    },
    {
      "text": "Code valid?"
    },
    {
      "text": "no"
    },
    {
      "text": "yes"
    },
    {
      "text": "fail"
    },
    {
      "text": "pass"
    },
    {
      "text": "stored"
    },
    {
      "text": "STORE_UNAVAILABLE"
    },
    {
      "text": "DUPLICATE_CODE"
    },
    {
      "text": "pass"
    },
    {
      "text": "fail"
    }
  ],
  "drawing_source": {
    "path": "assets/request-flow.svg",
    "revision": "1286331986e92aa70d90981f34da7aaa1dc45b09fa69106b4717745a2a095c0a",
    "tool": "scripts/build_examples.py"
  },
  "variants": [
    {
      "path": "assets/request-flow.png",
      "media_type": "image/png",
      "sha256": "53545111afdda2bcf5b113667ef14dc2233ca3f7e5e730749d3f50473ed81f8b",
      "size": 73547,
      "relation": "publication",
      "derived_from": "assets/request-flow.svg",
      "producer": "scripts/build_examples.py"
    }
  ],
  "derived_from_graph": "GRAPH-REQUEST-SUBMIT"
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
