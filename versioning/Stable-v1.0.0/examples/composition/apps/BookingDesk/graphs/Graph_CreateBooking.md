---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-BOOKING-CREATE
kind: graph
source_refs:
- GRAPH-BOOKING-CREATE
generation:
  mode: documentation_only
---

# Create booking

Preserves Atlas graph GRAPH-BOOKING-CREATE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-BOOKING-CREATE",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-BOOKING-CREATE"
  },
  "title": {
    "text": "Create booking"
  },
  "nodes": [
    {
      "id": "N-BOOK-CREATE-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-BOOKING-CREATE-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
      ]
    },
    {
      "id": "N-BOOKING-CREATE-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no collaborator"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
      ]
    },
    {
      "id": "N-BOOK-CREATE-CODE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-BOOKING-CODE"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-CODE"
      }
    },
    {
      "id": "N-BOOK-CREATE-CODEC",
      "type": "decision",
      "label": {
        "text": "Code valid?"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ]
    },
    {
      "id": "N-BOOK-CREATE-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid code or title"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ]
    },
    {
      "id": "N-BOOK-CREATE-SAVE",
      "type": "operation",
      "label": {
        "text": "Save active booking"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-02"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-BOOKING-SAVE"
      }
    },
    {
      "id": "N-BOOK-CREATE-DUP",
      "type": "failure",
      "label": {
        "text": "Report VERSION_CONFLICT"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ]
    },
    {
      "id": "N-BOOK-CREATE-FAIL",
      "type": "failure",
      "label": {
        "text": "Report STORE_UNAVAILABLE"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ]
    },
    {
      "id": "N-BOOK-CREATE-DONE",
      "type": "result",
      "label": {
        "text": "Booking created"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-04"
      ]
    },
    {
      "id": "N-BOOK-CREATE-TITLE",
      "type": "validation",
      "label": {
        "text": "Apply title validity"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-TITLE"
      }
    },
    {
      "id": "N-BOOK-CREATE-TITLEVALID",
      "type": "decision",
      "label": {
        "text": "Title valid?"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-CREATE-1",
      "from": "N-BOOK-CREATE-START",
      "to": "N-BOOKING-CREATE-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CREATE-2",
      "from": "N-BOOK-CREATE-CODE",
      "to": "N-BOOK-CREATE-CODEC",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CREATE-3",
      "from": "N-BOOK-CREATE-CODEC",
      "to": "N-BOOK-CREATE-INVALID",
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-CREATE-4",
      "from": "N-BOOK-CREATE-CODEC",
      "to": "N-BOOK-CREATE-TITLE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-02"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOK-CREATE-5",
      "from": "N-BOOK-CREATE-SAVE",
      "to": "N-BOOK-CREATE-DUP",
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ],
      "label": {
        "text": "VERSION_CONFLICT"
      }
    },
    {
      "id": "E-BOOK-CREATE-6",
      "from": "N-BOOK-CREATE-SAVE",
      "to": "N-BOOK-CREATE-FAIL",
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-BOOK-CREATE-7",
      "from": "N-BOOK-CREATE-SAVE",
      "to": "N-BOOK-CREATE-DONE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-04"
      ],
      "label": {
        "text": "saved"
      }
    },
    {
      "id": "E-BOOK-CREATE-TITLE-1",
      "from": "N-BOOK-CREATE-TITLE",
      "to": "N-BOOK-CREATE-TITLEVALID",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CREATE-TITLE-2",
      "from": "N-BOOK-CREATE-TITLEVALID",
      "to": "N-BOOK-CREATE-INVALID",
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-CREATE-TITLE-3",
      "from": "N-BOOK-CREATE-TITLEVALID",
      "to": "N-BOOK-CREATE-SAVE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOKING-CREATE-ALLOW",
      "from": "N-BOOKING-CREATE-AUTH",
      "to": "N-BOOK-CREATE-CODE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-BOOKING-CREATE-DENY",
      "from": "N-BOOKING-CREATE-AUTH",
      "to": "N-BOOKING-CREATE-DENIED",
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
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
    "id": "UC-BOOKING-CREATE"
  },
  "nodes": [
    {
      "id": "N-BOOK-CREATE-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-BOOKING-CREATE-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
      ]
    },
    {
      "id": "N-BOOKING-CREATE-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no collaborator"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
      ]
    },
    {
      "id": "N-BOOK-CREATE-CODE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-BOOKING-CODE"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-CODE"
      }
    },
    {
      "id": "N-BOOK-CREATE-CODEC",
      "type": "decision",
      "label": {
        "text": "Code valid?"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ]
    },
    {
      "id": "N-BOOK-CREATE-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid code or title"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ]
    },
    {
      "id": "N-BOOK-CREATE-SAVE",
      "type": "operation",
      "label": {
        "text": "Save active booking"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-02"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-BOOKING-SAVE"
      }
    },
    {
      "id": "N-BOOK-CREATE-DUP",
      "type": "failure",
      "label": {
        "text": "Report VERSION_CONFLICT"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ]
    },
    {
      "id": "N-BOOK-CREATE-FAIL",
      "type": "failure",
      "label": {
        "text": "Report STORE_UNAVAILABLE"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ]
    },
    {
      "id": "N-BOOK-CREATE-DONE",
      "type": "result",
      "label": {
        "text": "Booking created"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-04"
      ]
    },
    {
      "id": "N-BOOK-CREATE-TITLE",
      "type": "validation",
      "label": {
        "text": "Apply title validity"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-TITLE"
      }
    },
    {
      "id": "N-BOOK-CREATE-TITLEVALID",
      "type": "decision",
      "label": {
        "text": "Title valid?"
      },
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-CREATE-1",
      "from": "N-BOOK-CREATE-START",
      "to": "N-BOOKING-CREATE-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CREATE-2",
      "from": "N-BOOK-CREATE-CODE",
      "to": "N-BOOK-CREATE-CODEC",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CREATE-3",
      "from": "N-BOOK-CREATE-CODEC",
      "to": "N-BOOK-CREATE-INVALID",
      "requirement_refs": [
        "RF-BOOKING-CREATE-01"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-CREATE-4",
      "from": "N-BOOK-CREATE-CODEC",
      "to": "N-BOOK-CREATE-TITLE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-02"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOK-CREATE-5",
      "from": "N-BOOK-CREATE-SAVE",
      "to": "N-BOOK-CREATE-DUP",
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ],
      "label": {
        "text": "VERSION_CONFLICT"
      }
    },
    {
      "id": "E-BOOK-CREATE-6",
      "from": "N-BOOK-CREATE-SAVE",
      "to": "N-BOOK-CREATE-FAIL",
      "requirement_refs": [
        "RF-BOOKING-CREATE-03"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-BOOK-CREATE-7",
      "from": "N-BOOK-CREATE-SAVE",
      "to": "N-BOOK-CREATE-DONE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-04"
      ],
      "label": {
        "text": "saved"
      }
    },
    {
      "id": "E-BOOK-CREATE-TITLE-1",
      "from": "N-BOOK-CREATE-TITLE",
      "to": "N-BOOK-CREATE-TITLEVALID",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CREATE-TITLE-2",
      "from": "N-BOOK-CREATE-TITLEVALID",
      "to": "N-BOOK-CREATE-INVALID",
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-CREATE-TITLE-3",
      "from": "N-BOOK-CREATE-TITLEVALID",
      "to": "N-BOOK-CREATE-SAVE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-TITLE"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOKING-CREATE-ALLOW",
      "from": "N-BOOKING-CREATE-AUTH",
      "to": "N-BOOK-CREATE-CODE",
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-BOOKING-CREATE-DENY",
      "from": "N-BOOKING-CREATE-AUTH",
      "to": "N-BOOKING-CREATE-DENIED",
      "requirement_refs": [
        "RF-BOOKING-CREATE-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
