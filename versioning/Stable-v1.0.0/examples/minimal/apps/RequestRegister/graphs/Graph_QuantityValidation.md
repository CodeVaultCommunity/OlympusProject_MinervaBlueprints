---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-REQUEST-QUANTITY
kind: graph
source_refs:
- GRAPH-VLD-REQUEST-QUANTITY
generation:
  mode: documentation_only
---

# Quantity validation

Preserves Atlas graph GRAPH-VLD-REQUEST-QUANTITY.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-REQUEST-QUANTITY",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-REQUEST-QUANTITY"
  },
  "title": {
    "text": "Quantity validation"
  },
  "nodes": [
    {
      "id": "N-VLD-REQ-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-READ",
      "type": "action",
      "label": {
        "text": "Read quantity"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-TYPE",
      "type": "decision",
      "label": {
        "text": "Integer?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-MIN",
      "type": "decision",
      "label": {
        "text": "At least 1?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-PASS",
      "type": "result",
      "label": {
        "text": "Valid"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-FAIL-TYPE",
      "type": "refusal",
      "label": {
        "text": "Invalid: not an integer"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-FAIL-MIN",
      "type": "refusal",
      "label": {
        "text": "Invalid: less than 1"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-REQ-1",
      "from": "N-VLD-REQ-START",
      "to": "N-VLD-REQ-READ",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-REQ-2",
      "from": "N-VLD-REQ-READ",
      "to": "N-VLD-REQ-TYPE",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-REQ-3",
      "from": "N-VLD-REQ-TYPE",
      "to": "N-VLD-REQ-FAIL-TYPE",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-REQ-4",
      "from": "N-VLD-REQ-TYPE",
      "to": "N-VLD-REQ-MIN",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-REQ-5",
      "from": "N-VLD-REQ-MIN",
      "to": "N-VLD-REQ-FAIL-MIN",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-REQ-6",
      "from": "N-VLD-REQ-MIN",
      "to": "N-VLD-REQ-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
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
    "id": "VLD-REQUEST-QUANTITY"
  },
  "nodes": [
    {
      "id": "N-VLD-REQ-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-READ",
      "type": "action",
      "label": {
        "text": "Read quantity"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-TYPE",
      "type": "decision",
      "label": {
        "text": "Integer?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-MIN",
      "type": "decision",
      "label": {
        "text": "At least 1?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-PASS",
      "type": "result",
      "label": {
        "text": "Valid"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-FAIL-TYPE",
      "type": "refusal",
      "label": {
        "text": "Invalid: not an integer"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-REQ-FAIL-MIN",
      "type": "refusal",
      "label": {
        "text": "Invalid: less than 1"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-REQ-1",
      "from": "N-VLD-REQ-START",
      "to": "N-VLD-REQ-READ",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-REQ-2",
      "from": "N-VLD-REQ-READ",
      "to": "N-VLD-REQ-TYPE",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-REQ-3",
      "from": "N-VLD-REQ-TYPE",
      "to": "N-VLD-REQ-FAIL-TYPE",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-REQ-4",
      "from": "N-VLD-REQ-TYPE",
      "to": "N-VLD-REQ-MIN",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-REQ-5",
      "from": "N-VLD-REQ-MIN",
      "to": "N-VLD-REQ-FAIL-MIN",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-REQ-6",
      "from": "N-VLD-REQ-MIN",
      "to": "N-VLD-REQ-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
