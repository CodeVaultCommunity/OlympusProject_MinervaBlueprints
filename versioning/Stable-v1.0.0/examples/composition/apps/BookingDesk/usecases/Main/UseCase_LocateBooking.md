---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: UC-BOOKING-LOOKUP
kind: use_case
source_refs:
- UC-BOOKING-LOOKUP
generation:
  mode: code
  language: python
  path: apps/BookingDesk/usecases/Main/UseCase_LocateBooking.py
  symbol: UseCase_LocateBooking
---

# Locate booking

Return the current data of one retained booking.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "UC-BOOKING-LOOKUP",
  "name": {
    "text": "Locate booking"
  },
  "objective": [
    {
      "type": "paragraph",
      "text": "Return the current data of one retained booking."
    }
  ],
  "actors": [
    {
      "actor": "ACT-BOOKING-CLERK",
      "permission": {
        "text": "Permitted to locate bookings."
      },
      "description": [
        {
          "type": "paragraph",
          "text": "The clerk operates the booking desk."
        },
        {
          "type": "paragraph",
          "text": "Resolve this permission from trusted context for the concrete initiating caller; deny absent or unresolved evidence."
        }
      ]
    }
  ],
  "trigger": [
    {
      "type": "paragraph",
      "text": "A clerk requests a booking by code."
    }
  ],
  "context": [
    {
      "type": "paragraph",
      "text": "The lookup is used directly by the desk and by cancellation."
    },
    {
      "type": "paragraph",
      "text": "Caller context must contain a resolved authenticated principal, the relevant case permissions, and a validity status. Its origin is the application's trusted identity-and-permission authority; request fields and caller-supplied role strings are not trusted authorization evidence. Anonymous execution is not permitted. Missing, unresolved, expired or insufficient context is denied before any validation, tool access or effect."
    },
    {
      "type": "paragraph",
      "text": "The initiating actor is ACT-BOOKING-CLERK. The actor is a role; the caller is the concrete principal. The identity/authentication mechanism and channel encoding remain later design decisions."
    }
  ],
  "inputs": [
    {
      "name": {
        "text": "Booking code"
      },
      "type": "text",
      "meaning": [
        {
          "type": "paragraph",
          "text": "The code to locate."
        }
      ],
      "required": true
    }
  ],
  "entry_conditions": [
    {
      "type": "paragraph",
      "text": "Requests may arrive without valid caller context; the explicit denial path handles them before any collaborator is invoked."
    }
  ],
  "entities": [
    {
      "entity": "ENT-BOOKING",
      "validations": [
        "VLD-BOOKING-CODE"
      ],
      "purpose": [
        {
          "type": "paragraph",
          "text": "Validate the code before loading."
        }
      ]
    }
  ],
  "tools": [
    {
      "tool": "TOL-BOOKING-STORE",
      "operation": "OP-BOOKING-LOAD",
      "purpose": [
        {
          "type": "paragraph",
          "text": "Load the retained booking."
        }
      ]
    }
  ],
  "calls": [],
  "outcomes": [
    {
      "id": "OUT-BOOKING-LOOKUP-FOUND",
      "kind": "success",
      "description": [
        {
          "type": "paragraph",
          "text": "The booking is returned."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No persisted change."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-LOOKUP-NOTFOUND",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "No booking has the code."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No persisted change."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-LOOKUP-FAILURE",
      "kind": "failure",
      "description": [
        {
          "type": "paragraph",
          "text": "The store is unavailable."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No persisted change."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-LOOKUP-INVALID",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The booking code is invalid."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No load or data change."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-LOOKUP-DENIED",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The trusted caller context does not authorize this case."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No validation, collaborator call, persisted change, or disclosure of booking existence."
        }
      ]
    }
  ],
  "functional_requirements": [
    {
      "id": "RF-BOOKING-LOOKUP-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case applies VLD-BOOKING-CODE and refuses an invalid code without loading."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-LOOKUP"
      ],
      "flow_refs": [
        "N-BOOK-LOOK-CODE",
        "N-BOOK-LOOK-CODEC",
        "N-BOOK-LOOK-INVALID",
        "E-BOOK-LOOK-3"
      ]
    },
    {
      "id": "RF-BOOKING-LOOKUP-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case calls OP-BOOKING-LOAD and returns the loaded booking when found."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-BOOKING-LOOKUP",
        "OP-BOOKING-LOAD"
      ],
      "flow_refs": [
        "N-BOOK-LOOK-LOAD",
        "N-BOOK-LOOK-FOUND",
        "E-BOOK-LOOK-4",
        "E-BOOK-LOOK-7"
      ]
    },
    {
      "id": "RF-BOOKING-LOOKUP-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "NOT_FOUND is reported as a distinct refusal with no effect."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-BOOKING-LOOKUP",
        "OP-BOOKING-LOAD"
      ],
      "flow_refs": [
        "N-BOOK-LOOK-NOTFOUND",
        "E-BOOK-LOOK-5"
      ]
    },
    {
      "id": "RF-BOOKING-LOOKUP-04",
      "statement": [
        {
          "type": "paragraph",
          "text": "STORE_UNAVAILABLE is reported as a failure, not as not found."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-BOOKING-LOOKUP",
        "OP-BOOKING-LOAD"
      ],
      "flow_refs": [
        "N-BOOK-LOOK-FAIL",
        "E-BOOK-LOOK-6"
      ]
    },
    {
      "id": "RF-BOOKING-LOOKUP-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Require this case's permission in the trusted authenticated caller context. Deny missing, unresolved, expired or insufficient context before any validation, tool call, composed use-case call or effect. Anonymous execution is forbidden."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-LOOKUP"
      ],
      "flow_refs": [
        "N-BOOKING-LOOKUP-AUTH",
        "N-BOOKING-LOOKUP-DENIED",
        "E-BOOKING-LOOKUP-ALLOW",
        "E-BOOKING-LOOKUP-DENY"
      ]
    }
  ],
  "nonfunctional_requirements": [],
  "flows": {
    "main": "GRAPH-BOOKING-LOOKUP",
    "subflows": []
  },
  "flow_text": [
    {
      "type": "paragraph",
      "text": "Resolve and authorize the initiating caller first (RF-BOOKING-LOOKUP-AUTH). Denial terminates before any subsequent step."
    },
    {
      "type": "paragraph",
      "text": "Validate the code (RF-BOOKING-LOOKUP-01). An invalid code is refused before load."
    },
    {
      "type": "paragraph",
      "text": "Load through OP-BOOKING-LOAD (RF-BOOKING-LOOKUP-02). NOT_FOUND is a refusal (RF-BOOKING-LOOKUP-03); STORE_UNAVAILABLE is a failure (RF-BOOKING-LOOKUP-04)."
    }
  ],
  "acceptance_criteria": [
    {
      "id": "AC-BOOKING-LOOKUP-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "A retained code returns the booking and its current status."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-02"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "An unknown code returns not found, not an empty booking."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-03"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "An unavailable store is distinguished from not found."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-04"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-INVALID",
      "statement": [
        {
          "type": "paragraph",
          "text": "A lowercase or punctuated code fails the canonical code rule and no load is invoked."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-01"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-AUTH"
      ]
    }
  ],
  "traceability": [
    {
      "id": "TRC-BOOKING-LOOKUP-01",
      "source": "RF-BOOKING-LOOKUP-01",
      "targets": [
        "VLD-BOOKING-CODE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Shared entity validation."
        }
      ]
    },
    {
      "id": "TRC-BOOKING-LOOKUP-ORIGIN",
      "source": "SRC-BOOKING-BRIEF",
      "targets": [
        "RF-BOOKING-LOOKUP-01",
        "RF-BOOKING-LOOKUP-02",
        "RF-BOOKING-LOOKUP-03",
        "RF-BOOKING-LOOKUP-04",
        "RF-BOOKING-LOOKUP-AUTH"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Versioned synthetic origin for these example obligations."
        }
      ]
    }
  ],
  "assumptions": [],
  "sources": [
    "SRC-BOOKING-BRIEF"
  ],
  "open_issues": []
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/BookingDesk/usecases/Main/UseCase_LocateBooking.py",
    "symbol": "UseCase_LocateBooking"
  },
  "class_kind": "use_case",
  "consumed_entities": [
    "ENT-BOOKING"
  ],
  "injected_tools": [
    {
      "abstract_tool_ref": "TOL-BOOKING-STORE",
      "operation_ref": "OP-BOOKING-LOAD",
      "injected_concrete_tool_ref": "CTL-BOOKING-STORE",
      "purpose": "Load the retained booking."
    }
  ],
  "methods": [
    {
      "name": "execute",
      "visibility": "public",
      "trigger": "A clerk requests a booking by code.",
      "parameters": [
        {
          "name": "booking_code",
          "type": "text",
          "required": true
        }
      ],
      "authorization": {
        "actor_refs": [
          "ACT-BOOKING-CLERK"
        ],
        "before_effects": true
      },
      "algorithm": [
        "Resolve and authorize the initiating caller first (RF-BOOKING-LOOKUP-AUTH). Denial terminates before any subsequent step.",
        "Validate the code (RF-BOOKING-LOOKUP-01). An invalid code is refused before load.",
        "Load through OP-BOOKING-LOAD (RF-BOOKING-LOOKUP-02). NOT_FOUND is a refusal (RF-BOOKING-LOOKUP-03); STORE_UNAVAILABLE is a failure (RF-BOOKING-LOOKUP-04)."
      ],
      "returns": [
        {
          "outcome_ref": "OUT-BOOKING-LOOKUP-FOUND",
          "kind": "success"
        },
        {
          "outcome_ref": "OUT-BOOKING-LOOKUP-NOTFOUND",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-BOOKING-LOOKUP-FAILURE",
          "kind": "failure"
        },
        {
          "outcome_ref": "OUT-BOOKING-LOOKUP-INVALID",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-BOOKING-LOOKUP-DENIED",
          "kind": "refusal"
        }
      ],
      "source_refs": [
        "UC-BOOKING-LOOKUP",
        "RF-BOOKING-LOOKUP-01",
        "RF-BOOKING-LOOKUP-02",
        "RF-BOOKING-LOOKUP-03",
        "RF-BOOKING-LOOKUP-04",
        "RF-BOOKING-LOOKUP-AUTH"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-BOOKING-LOOKUP"
  ]
}
```
