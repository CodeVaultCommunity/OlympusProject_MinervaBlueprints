---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-BOOKING-LOOKUP
kind: graph
source_refs:
- GRAPH-BOOKING-LOOKUP
generation:
  mode: documentation_only
---

# Locate booking

Preserves Atlas graph GRAPH-BOOKING-LOOKUP.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-BOOKING-LOOKUP",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-BOOKING-LOOKUP"
  },
  "title": {
    "text": "Locate booking"
  },
  "nodes": [
    {
      "id": "N-BOOK-LOOK-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-BOOKING-LOOKUP-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ]
    },
    {
      "id": "N-BOOKING-LOOKUP-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no collaborator"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ]
    },
    {
      "id": "N-BOOK-LOOK-CODE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-BOOKING-CODE"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-CODE"
      }
    },
    {
      "id": "N-BOOK-LOOK-CODEC",
      "type": "decision",
      "label": {
        "text": "Code valid?"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ]
    },
    {
      "id": "N-BOOK-LOOK-INVALID",
      "type": "refusal",
      "label": {
        "text": "Refuse: invalid code"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ]
    },
    {
      "id": "N-BOOK-LOOK-LOAD",
      "type": "operation",
      "label": {
        "text": "Load booking"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-BOOKING-LOAD"
      }
    },
    {
      "id": "N-BOOK-LOOK-NOTFOUND",
      "type": "refusal",
      "label": {
        "text": "Refuse: not found"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-03"
      ]
    },
    {
      "id": "N-BOOK-LOOK-FAIL",
      "type": "failure",
      "label": {
        "text": "Report store unavailable"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-04"
      ]
    },
    {
      "id": "N-BOOK-LOOK-FOUND",
      "type": "result",
      "label": {
        "text": "Booking found"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-LOOK-1",
      "from": "N-BOOK-LOOK-START",
      "to": "N-BOOKING-LOOKUP-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-LOOK-2",
      "from": "N-BOOK-LOOK-CODE",
      "to": "N-BOOK-LOOK-CODEC",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-LOOK-3",
      "from": "N-BOOK-LOOK-CODEC",
      "to": "N-BOOK-LOOK-INVALID",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-LOOK-4",
      "from": "N-BOOK-LOOK-CODEC",
      "to": "N-BOOK-LOOK-LOAD",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOK-LOOK-5",
      "from": "N-BOOK-LOOK-LOAD",
      "to": "N-BOOK-LOOK-NOTFOUND",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-03"
      ],
      "label": {
        "text": "NOT_FOUND"
      }
    },
    {
      "id": "E-BOOK-LOOK-6",
      "from": "N-BOOK-LOOK-LOAD",
      "to": "N-BOOK-LOOK-FAIL",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-04"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-BOOK-LOOK-7",
      "from": "N-BOOK-LOOK-LOAD",
      "to": "N-BOOK-LOOK-FOUND",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ],
      "label": {
        "text": "loaded"
      }
    },
    {
      "id": "E-BOOKING-LOOKUP-ALLOW",
      "from": "N-BOOKING-LOOKUP-AUTH",
      "to": "N-BOOK-LOOK-CODE",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-BOOKING-LOOKUP-DENY",
      "from": "N-BOOKING-LOOKUP-AUTH",
      "to": "N-BOOKING-LOOKUP-DENIED",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
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
    "id": "UC-BOOKING-LOOKUP"
  },
  "nodes": [
    {
      "id": "N-BOOK-LOOK-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-BOOKING-LOOKUP-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ]
    },
    {
      "id": "N-BOOKING-LOOKUP-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no collaborator"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ]
    },
    {
      "id": "N-BOOK-LOOK-CODE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-BOOKING-CODE"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-CODE"
      }
    },
    {
      "id": "N-BOOK-LOOK-CODEC",
      "type": "decision",
      "label": {
        "text": "Code valid?"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ]
    },
    {
      "id": "N-BOOK-LOOK-INVALID",
      "type": "refusal",
      "label": {
        "text": "Refuse: invalid code"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ]
    },
    {
      "id": "N-BOOK-LOOK-LOAD",
      "type": "operation",
      "label": {
        "text": "Load booking"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-BOOKING-LOAD"
      }
    },
    {
      "id": "N-BOOK-LOOK-NOTFOUND",
      "type": "refusal",
      "label": {
        "text": "Refuse: not found"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-03"
      ]
    },
    {
      "id": "N-BOOK-LOOK-FAIL",
      "type": "failure",
      "label": {
        "text": "Report store unavailable"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-04"
      ]
    },
    {
      "id": "N-BOOK-LOOK-FOUND",
      "type": "result",
      "label": {
        "text": "Booking found"
      },
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-LOOK-1",
      "from": "N-BOOK-LOOK-START",
      "to": "N-BOOKING-LOOKUP-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-LOOK-2",
      "from": "N-BOOK-LOOK-CODE",
      "to": "N-BOOK-LOOK-CODEC",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-LOOK-3",
      "from": "N-BOOK-LOOK-CODEC",
      "to": "N-BOOK-LOOK-INVALID",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-LOOK-4",
      "from": "N-BOOK-LOOK-CODEC",
      "to": "N-BOOK-LOOK-LOAD",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOK-LOOK-5",
      "from": "N-BOOK-LOOK-LOAD",
      "to": "N-BOOK-LOOK-NOTFOUND",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-03"
      ],
      "label": {
        "text": "NOT_FOUND"
      }
    },
    {
      "id": "E-BOOK-LOOK-6",
      "from": "N-BOOK-LOOK-LOAD",
      "to": "N-BOOK-LOOK-FAIL",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-04"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-BOOK-LOOK-7",
      "from": "N-BOOK-LOOK-LOAD",
      "to": "N-BOOK-LOOK-FOUND",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-02"
      ],
      "label": {
        "text": "loaded"
      }
    },
    {
      "id": "E-BOOKING-LOOKUP-ALLOW",
      "from": "N-BOOKING-LOOKUP-AUTH",
      "to": "N-BOOK-LOOK-CODE",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-BOOKING-LOOKUP-DENY",
      "from": "N-BOOKING-LOOKUP-AUTH",
      "to": "N-BOOKING-LOOKUP-DENIED",
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
