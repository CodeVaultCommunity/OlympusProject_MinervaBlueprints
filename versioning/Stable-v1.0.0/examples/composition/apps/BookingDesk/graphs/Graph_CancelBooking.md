---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-BOOKING-CANCEL
kind: graph
source_refs:
- GRAPH-BOOKING-CANCEL
generation:
  mode: documentation_only
---

# Cancel booking

Preserves Atlas graph GRAPH-BOOKING-CANCEL.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-BOOKING-CANCEL",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-BOOKING-CANCEL"
  },
  "title": {
    "text": "Cancel booking"
  },
  "nodes": [
    {
      "id": "N-BOOK-CANCEL-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-BOOKING-CANCEL-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
      ]
    },
    {
      "id": "N-BOOKING-CANCEL-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no collaborator"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-LOOK",
      "type": "use_case",
      "label": {
        "text": "Call UC-BOOKING-LOOKUP"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "call": {
        "kind": "use_case",
        "id": "UC-BOOKING-LOOKUP"
      }
    },
    {
      "id": "N-BOOK-CANCEL-FOUND",
      "type": "decision",
      "label": {
        "text": "Booking found?"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-NOTFOUND",
      "type": "refusal",
      "label": {
        "text": "Refuse: not found"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-VALIDATE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-BOOKING-CANCEL"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-02"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-CANCEL"
      }
    },
    {
      "id": "N-BOOK-CANCEL-VALID",
      "type": "decision",
      "label": {
        "text": "Transition allowed?"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-02"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-ALREADY",
      "type": "refusal",
      "label": {
        "text": "Refuse: already cancelled"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-SAVE",
      "type": "operation",
      "label": {
        "text": "Save cancelled booking"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-BOOKING-SAVE"
      }
    },
    {
      "id": "N-BOOK-CANCEL-ERROR",
      "type": "failure",
      "label": {
        "text": "Report store failure"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-05"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-DONE",
      "type": "result",
      "label": {
        "text": "Booking cancelled"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid code; no write"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-LOOKDENIED",
      "type": "refusal",
      "label": {
        "text": "Lookup denied; no write"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-CANCEL-1",
      "from": "N-BOOK-CANCEL-START",
      "to": "N-BOOKING-CANCEL-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CANCEL-2",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-FOUND",
      "requirement_refs": [],
      "label": {
        "text": "found / not found"
      }
    },
    {
      "id": "E-BOOK-CANCEL-3",
      "from": "N-BOOK-CANCEL-FOUND",
      "to": "N-BOOK-CANCEL-NOTFOUND",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-BOOK-CANCEL-4",
      "from": "N-BOOK-CANCEL-FOUND",
      "to": "N-BOOK-CANCEL-VALIDATE",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-BOOK-CANCEL-5",
      "from": "N-BOOK-CANCEL-VALIDATE",
      "to": "N-BOOK-CANCEL-VALID",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-02"
      ]
    },
    {
      "id": "E-BOOK-CANCEL-6",
      "from": "N-BOOK-CANCEL-VALID",
      "to": "N-BOOK-CANCEL-ALREADY",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-CANCEL-7",
      "from": "N-BOOK-CANCEL-VALID",
      "to": "N-BOOK-CANCEL-SAVE",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOK-CANCEL-8",
      "from": "N-BOOK-CANCEL-SAVE",
      "to": "N-BOOK-CANCEL-ERROR",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-05"
      ],
      "label": {
        "text": "failure"
      }
    },
    {
      "id": "E-BOOK-CANCEL-9",
      "from": "N-BOOK-CANCEL-SAVE",
      "to": "N-BOOK-CANCEL-DONE",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ],
      "label": {
        "text": "saved"
      }
    },
    {
      "id": "E-BOOK-CANCEL-INVALID",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-INVALID",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "invalid code"
      }
    },
    {
      "id": "E-BOOK-CANCEL-LOOKERROR",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-ERROR",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-05"
      ],
      "label": {
        "text": "lookup failure"
      }
    },
    {
      "id": "E-BOOK-CANCEL-LOOKDENIED",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-LOOKDENIED",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "lookup denied"
      }
    },
    {
      "id": "E-BOOKING-CANCEL-ALLOW",
      "from": "N-BOOKING-CANCEL-AUTH",
      "to": "N-BOOK-CANCEL-LOOK",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-BOOKING-CANCEL-DENY",
      "from": "N-BOOKING-CANCEL-AUTH",
      "to": "N-BOOKING-CANCEL-DENIED",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
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
    "id": "UC-BOOKING-CANCEL"
  },
  "nodes": [
    {
      "id": "N-BOOK-CANCEL-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-BOOKING-CANCEL-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
      ]
    },
    {
      "id": "N-BOOKING-CANCEL-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no collaborator"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-LOOK",
      "type": "use_case",
      "label": {
        "text": "Call UC-BOOKING-LOOKUP"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "call": {
        "kind": "use_case",
        "id": "UC-BOOKING-LOOKUP"
      }
    },
    {
      "id": "N-BOOK-CANCEL-FOUND",
      "type": "decision",
      "label": {
        "text": "Booking found?"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-NOTFOUND",
      "type": "refusal",
      "label": {
        "text": "Refuse: not found"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-VALIDATE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-BOOKING-CANCEL"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-02"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-BOOKING-CANCEL"
      }
    },
    {
      "id": "N-BOOK-CANCEL-VALID",
      "type": "decision",
      "label": {
        "text": "Transition allowed?"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-02"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-ALREADY",
      "type": "refusal",
      "label": {
        "text": "Refuse: already cancelled"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-SAVE",
      "type": "operation",
      "label": {
        "text": "Save cancelled booking"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-BOOKING-SAVE"
      }
    },
    {
      "id": "N-BOOK-CANCEL-ERROR",
      "type": "failure",
      "label": {
        "text": "Report store failure"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-05"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-DONE",
      "type": "result",
      "label": {
        "text": "Booking cancelled"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid code; no write"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "N-BOOK-CANCEL-LOOKDENIED",
      "type": "refusal",
      "label": {
        "text": "Lookup denied; no write"
      },
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-BOOK-CANCEL-1",
      "from": "N-BOOK-CANCEL-START",
      "to": "N-BOOKING-CANCEL-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-BOOK-CANCEL-2",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-FOUND",
      "requirement_refs": [],
      "label": {
        "text": "found / not found"
      }
    },
    {
      "id": "E-BOOK-CANCEL-3",
      "from": "N-BOOK-CANCEL-FOUND",
      "to": "N-BOOK-CANCEL-NOTFOUND",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-BOOK-CANCEL-4",
      "from": "N-BOOK-CANCEL-FOUND",
      "to": "N-BOOK-CANCEL-VALIDATE",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-BOOK-CANCEL-5",
      "from": "N-BOOK-CANCEL-VALIDATE",
      "to": "N-BOOK-CANCEL-VALID",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-02"
      ]
    },
    {
      "id": "E-BOOK-CANCEL-6",
      "from": "N-BOOK-CANCEL-VALID",
      "to": "N-BOOK-CANCEL-ALREADY",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-03"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-BOOK-CANCEL-7",
      "from": "N-BOOK-CANCEL-VALID",
      "to": "N-BOOK-CANCEL-SAVE",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-BOOK-CANCEL-8",
      "from": "N-BOOK-CANCEL-SAVE",
      "to": "N-BOOK-CANCEL-ERROR",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-05"
      ],
      "label": {
        "text": "failure"
      }
    },
    {
      "id": "E-BOOK-CANCEL-9",
      "from": "N-BOOK-CANCEL-SAVE",
      "to": "N-BOOK-CANCEL-DONE",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-04"
      ],
      "label": {
        "text": "saved"
      }
    },
    {
      "id": "E-BOOK-CANCEL-INVALID",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-INVALID",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "invalid code"
      }
    },
    {
      "id": "E-BOOK-CANCEL-LOOKERROR",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-ERROR",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-05"
      ],
      "label": {
        "text": "lookup failure"
      }
    },
    {
      "id": "E-BOOK-CANCEL-LOOKDENIED",
      "from": "N-BOOK-CANCEL-LOOK",
      "to": "N-BOOK-CANCEL-LOOKDENIED",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01"
      ],
      "label": {
        "text": "lookup denied"
      }
    },
    {
      "id": "E-BOOKING-CANCEL-ALLOW",
      "from": "N-BOOKING-CANCEL-AUTH",
      "to": "N-BOOK-CANCEL-LOOK",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-BOOKING-CANCEL-DENY",
      "from": "N-BOOKING-CANCEL-AUTH",
      "to": "N-BOOKING-CANCEL-DENIED",
      "requirement_refs": [
        "RF-BOOKING-CANCEL-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
