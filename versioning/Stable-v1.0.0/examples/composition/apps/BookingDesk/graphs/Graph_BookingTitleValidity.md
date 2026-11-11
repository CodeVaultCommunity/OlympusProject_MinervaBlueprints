---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-BOOKING-TITLE
kind: graph
source_refs:
- GRAPH-VLD-BOOKING-TITLE
generation:
  mode: documentation_only
---

# Booking title validity

Preserves Atlas graph GRAPH-VLD-BOOKING-TITLE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-BOOKING-TITLE",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-BOOKING-TITLE"
  },
  "title": {
    "text": "Booking title validity"
  },
  "nodes": [
    {
      "id": "N-VLD-BOOK-TITLE-START",
      "type": "start",
      "label": {
        "text": "Receive title"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-TITLE-CHECK",
      "type": "decision",
      "label": {
        "text": "Meaningful text?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-TITLE-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-TITLE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Invalid title"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-BOOK-TITLE-1",
      "from": "N-VLD-BOOK-TITLE-START",
      "to": "N-VLD-BOOK-TITLE-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-TITLE-2",
      "from": "N-VLD-BOOK-TITLE-CHECK",
      "to": "N-VLD-BOOK-TITLE-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-BOOK-TITLE-3",
      "from": "N-VLD-BOOK-TITLE-CHECK",
      "to": "N-VLD-BOOK-TITLE-FAIL",
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
    "id": "VLD-BOOKING-TITLE"
  },
  "nodes": [
    {
      "id": "N-VLD-BOOK-TITLE-START",
      "type": "start",
      "label": {
        "text": "Receive title"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-TITLE-CHECK",
      "type": "decision",
      "label": {
        "text": "Meaningful text?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-TITLE-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-TITLE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Invalid title"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-BOOK-TITLE-1",
      "from": "N-VLD-BOOK-TITLE-START",
      "to": "N-VLD-BOOK-TITLE-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-TITLE-2",
      "from": "N-VLD-BOOK-TITLE-CHECK",
      "to": "N-VLD-BOOK-TITLE-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-BOOK-TITLE-3",
      "from": "N-VLD-BOOK-TITLE-CHECK",
      "to": "N-VLD-BOOK-TITLE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
