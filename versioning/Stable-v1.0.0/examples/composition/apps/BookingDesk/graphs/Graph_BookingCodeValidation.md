---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-BOOKING-CODE
kind: graph
source_refs:
- GRAPH-VLD-BOOKING-CODE
generation:
  mode: documentation_only
---

# Booking code validation

Preserves Atlas graph GRAPH-VLD-BOOKING-CODE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-BOOKING-CODE",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-BOOKING-CODE"
  },
  "title": {
    "text": "Booking code validation"
  },
  "nodes": [
    {
      "id": "N-VLD-BOOK-CODE-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-READ",
      "type": "action",
      "label": {
        "text": "Read code"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-EMPTY",
      "type": "decision",
      "label": {
        "text": "Non-empty?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-LENGTH",
      "type": "decision",
      "label": {
        "text": "1 to 12 characters?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-CHARS",
      "type": "decision",
      "label": {
        "text": "Uppercase letters or digits?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-PASS",
      "type": "result",
      "label": {
        "text": "Valid"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Invalid code"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-BOOK-CODE-1",
      "from": "N-VLD-BOOK-CODE-START",
      "to": "N-VLD-BOOK-CODE-READ",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CODE-2",
      "from": "N-VLD-BOOK-CODE-READ",
      "to": "N-VLD-BOOK-CODE-EMPTY",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CODE-3",
      "from": "N-VLD-BOOK-CODE-EMPTY",
      "to": "N-VLD-BOOK-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-4",
      "from": "N-VLD-BOOK-CODE-EMPTY",
      "to": "N-VLD-BOOK-CODE-LENGTH",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-5",
      "from": "N-VLD-BOOK-CODE-LENGTH",
      "to": "N-VLD-BOOK-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-6",
      "from": "N-VLD-BOOK-CODE-LENGTH",
      "to": "N-VLD-BOOK-CODE-CHARS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-7",
      "from": "N-VLD-BOOK-CODE-CHARS",
      "to": "N-VLD-BOOK-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-8",
      "from": "N-VLD-BOOK-CODE-CHARS",
      "to": "N-VLD-BOOK-CODE-PASS",
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
    "id": "VLD-BOOKING-CODE"
  },
  "nodes": [
    {
      "id": "N-VLD-BOOK-CODE-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-READ",
      "type": "action",
      "label": {
        "text": "Read code"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-EMPTY",
      "type": "decision",
      "label": {
        "text": "Non-empty?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-LENGTH",
      "type": "decision",
      "label": {
        "text": "1 to 12 characters?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-CHARS",
      "type": "decision",
      "label": {
        "text": "Uppercase letters or digits?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-PASS",
      "type": "result",
      "label": {
        "text": "Valid"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-BOOK-CODE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Invalid code"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-BOOK-CODE-1",
      "from": "N-VLD-BOOK-CODE-START",
      "to": "N-VLD-BOOK-CODE-READ",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CODE-2",
      "from": "N-VLD-BOOK-CODE-READ",
      "to": "N-VLD-BOOK-CODE-EMPTY",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-BOOK-CODE-3",
      "from": "N-VLD-BOOK-CODE-EMPTY",
      "to": "N-VLD-BOOK-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-4",
      "from": "N-VLD-BOOK-CODE-EMPTY",
      "to": "N-VLD-BOOK-CODE-LENGTH",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-5",
      "from": "N-VLD-BOOK-CODE-LENGTH",
      "to": "N-VLD-BOOK-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-6",
      "from": "N-VLD-BOOK-CODE-LENGTH",
      "to": "N-VLD-BOOK-CODE-CHARS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-7",
      "from": "N-VLD-BOOK-CODE-CHARS",
      "to": "N-VLD-BOOK-CODE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-VLD-BOOK-CODE-8",
      "from": "N-VLD-BOOK-CODE-CHARS",
      "to": "N-VLD-BOOK-CODE-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
