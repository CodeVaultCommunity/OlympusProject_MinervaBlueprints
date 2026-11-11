---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-BOOKING-CANCEL
kind: graph
source_refs:
- GRAPH-VLD-BOOKING-CANCEL
generation:
  mode: documentation_only
---

# Cancellation transition validation

Preserves Atlas graph GRAPH-VLD-BOOKING-CANCEL.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-BOOKING-CANCEL",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-BOOKING-CANCEL"
  },
  "title": {
    "text": "Cancellation transition validation"
  },
  "nodes": [
    {
      "id": "N-VLD-BOOK-CANCEL-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-READ",
      "type": "action",
      "label": {
        "text": "Read booking status"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-ACTIVE",
      "type": "decision",
      "label": {
        "text": "Status active?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-PASS",
      "type": "result",
      "label": {
        "text": "Transition allowed"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-FAIL",
      "type": "refusal",
      "label": {
        "text": "Already cancelled"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-BOOK-CANCEL-1",
      "from": "N-VLD-BOOK-CANCEL-START",
      "to": "N-VLD-BOOK-CANCEL-READ",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CANCEL-2",
      "from": "N-VLD-BOOK-CANCEL-READ",
      "to": "N-VLD-BOOK-CANCEL-ACTIVE",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CANCEL-3",
      "from": "N-VLD-BOOK-CANCEL-ACTIVE",
      "to": "N-VLD-BOOK-CANCEL-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CANCEL-4",
      "from": "N-VLD-BOOK-CANCEL-ACTIVE",
      "to": "N-VLD-BOOK-CANCEL-PASS",
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
    "id": "VLD-BOOKING-CANCEL"
  },
  "nodes": [
    {
      "id": "N-VLD-BOOK-CANCEL-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-READ",
      "type": "action",
      "label": {
        "text": "Read booking status"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-ACTIVE",
      "type": "decision",
      "label": {
        "text": "Status active?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-PASS",
      "type": "result",
      "label": {
        "text": "Transition allowed"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CANCEL-FAIL",
      "type": "refusal",
      "label": {
        "text": "Already cancelled"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-BOOK-CANCEL-1",
      "from": "N-VLD-BOOK-CANCEL-START",
      "to": "N-VLD-BOOK-CANCEL-READ",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CANCEL-2",
      "from": "N-VLD-BOOK-CANCEL-READ",
      "to": "N-VLD-BOOK-CANCEL-ACTIVE",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CANCEL-3",
      "from": "N-VLD-BOOK-CANCEL-ACTIVE",
      "to": "N-VLD-BOOK-CANCEL-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CANCEL-4",
      "from": "N-VLD-BOOK-CANCEL-ACTIVE",
      "to": "N-VLD-BOOK-CANCEL-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
