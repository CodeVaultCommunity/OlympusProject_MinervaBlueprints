---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-REQUEST-CODE
kind: graph
source_refs:
- GRAPH-VLD-REQUEST-CODE
generation:
  mode: documentation_only
---

# Request code validity

Preserves Atlas graph GRAPH-VLD-REQUEST-CODE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-REQUEST-CODE",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-REQUEST-CODE"
  },
  "title": {
    "text": "Request code validity"
  },
  "nodes": [
    {
      "id": "N-VLD-REQ-CODE-START",
      "type": "start",
      "label": {
        "text": "Receive code"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-CODE-CHECK",
      "type": "decision",
      "label": {
        "text": "Non-empty text?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-CODE-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-CODE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Invalid code"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-REQ-CODE-1",
      "from": "N-VLD-REQ-CODE-START",
      "to": "N-VLD-REQ-CODE-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-REQ-CODE-2",
      "from": "N-VLD-REQ-CODE-CHECK",
      "to": "N-VLD-REQ-CODE-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-REQ-CODE-3",
      "from": "N-VLD-REQ-CODE-CHECK",
      "to": "N-VLD-REQ-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    }
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": null,
  "class_kind": "control_flow_graph",
  "owner": {
    "kind": "validation",
    "id": "VLD-REQUEST-CODE"
  },
  "nodes": [
    {
      "id": "N-VLD-REQ-CODE-START",
      "type": "start",
      "label": {
        "text": "Receive code"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-CODE-CHECK",
      "type": "decision",
      "label": {
        "text": "Non-empty text?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-CODE-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-CODE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Invalid code"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-REQ-CODE-1",
      "from": "N-VLD-REQ-CODE-START",
      "to": "N-VLD-REQ-CODE-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-REQ-CODE-2",
      "from": "N-VLD-REQ-CODE-CHECK",
      "to": "N-VLD-REQ-CODE-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-REQ-CODE-3",
      "from": "N-VLD-REQ-CODE-CHECK",
      "to": "N-VLD-REQ-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
