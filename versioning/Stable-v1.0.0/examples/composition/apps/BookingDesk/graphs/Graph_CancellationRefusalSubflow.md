---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-BOOKING-CANCEL-REFUSAL
kind: graph
source_refs:
- GRAPH-BOOKING-CANCEL-REFUSAL
generation:
  mode: documentation_only
---

# Cancellation refusal subflow

Preserves Atlas graph GRAPH-BOOKING-CANCEL-REFUSAL.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-BOOKING-CANCEL-REFUSAL",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-BOOKING-CANCEL"
  },
  "title": {
    "text": "Cancellation refusal subflow"
  },
  "nodes": [
    {
      "id": "N-BOOK-REFUSE-START",
      "type": "start",
      "label": {
        "text": "Refusal"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "N-BOOK-REFUSE-ALREADY",
      "type": "refusal",
      "label": {
        "text": "Already cancelled: no effect"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "N-BOOK-REFUSE-NOTFOUND",
      "type": "refusal",
      "label": {
        "text": "Not found: no effect"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-REFUSE-1",
      "from": "N-BOOK-REFUSE-START",
      "to": "N-BOOK-REFUSE-ALREADY",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ],
      "label": {
        "text": "already cancelled"
      }
    },
    {
      "id": "E-BOOK-REFUSE-2",
      "from": "N-BOOK-REFUSE-START",
      "to": "N-BOOK-REFUSE-NOTFOUND",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "not found"
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
    "kind": "use_case",
    "id": "UC-BOOKING-CANCEL"
  },
  "nodes": [
    {
      "id": "N-BOOK-REFUSE-START",
      "type": "start",
      "label": {
        "text": "Refusal"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "N-BOOK-REFUSE-ALREADY",
      "type": "refusal",
      "label": {
        "text": "Already cancelled: no effect"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "N-BOOK-REFUSE-NOTFOUND",
      "type": "refusal",
      "label": {
        "text": "Not found: no effect"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-REFUSE-1",
      "from": "N-BOOK-REFUSE-START",
      "to": "N-BOOK-REFUSE-ALREADY",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ],
      "label": {
        "text": "already cancelled"
      }
    },
    {
      "id": "E-BOOK-REFUSE-2",
      "from": "N-BOOK-REFUSE-START",
      "to": "N-BOOK-REFUSE-NOTFOUND",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "not found"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
