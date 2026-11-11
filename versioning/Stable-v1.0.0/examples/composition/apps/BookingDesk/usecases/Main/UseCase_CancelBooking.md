---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: UC-BOOKING-CANCEL
kind: use_case
source_refs:
- UC-BOOKING-CANCEL
generation:
  mode: code
  language: python
  path: apps/BookingDesk/usecases/Main/UseCase_CancelBooking.py
  symbol: UseCase_CancelBooking
---

# Cancel booking

Retain the booking and change its status to cancelled when cancellation is allowed.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "UC-BOOKING-CANCEL",
  "name": {
    "text": "Cancel booking"
  },
  "objective": [
    {
      "type": "paragraph",
      "text": "Retain the booking and change its status to cancelled when cancellation is allowed."
    }
  ],
  "actors": [
    {
      "actor": "ACT-BOOKING-CLERK",
      "permission": {
        "text": "Permitted to cancel bookings."
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
      "text": "A clerk requests cancellation by code."
    }
  ],
  "context": [
    {
      "type": "paragraph",
      "text": "Cancellation reuses lookup and the shared store."
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
          "text": "The booking to cancel."
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
        "VLD-BOOKING-CANCEL"
      ],
      "purpose": [
        {
          "type": "paragraph",
          "text": "Check that the located booking may move from active to cancelled."
        }
      ]
    }
  ],
  "tools": [
    {
      "tool": "TOL-BOOKING-STORE",
      "operation": "OP-BOOKING-SAVE",
      "purpose": [
        {
          "type": "paragraph",
          "text": "Persist the cancelled status."
        }
      ]
    }
  ],
  "calls": [
    {
      "use_case": "UC-BOOKING-LOOKUP",
      "contract": [
        {
          "type": "paragraph",
          "text": "Receives the located booking or the lookup refusal/failure."
        }
      ],
      "authorization": [
        {
          "type": "paragraph",
          "text": "The cancellation actor must also be permitted to locate bookings."
        },
        {
          "type": "paragraph",
          "text": "Preserve the concrete principal and trusted caller context in the lookup invocation. Lookup independently checks its own permission; cancellation permission never bypasses it."
        }
      ]
    }
  ],
  "outcomes": [
    {
      "id": "OUT-BOOKING-CANCEL-DONE",
      "kind": "success",
      "description": [
        {
          "type": "paragraph",
          "text": "The booking is cancelled and retained."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "The booking status becomes cancelled."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CANCEL-ALREADY",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The booking is already cancelled."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No save and no data change."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CANCEL-NOTFOUND",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The lookup did not find the booking."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No save and no data change."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CANCEL-FAILURE",
      "kind": "failure",
      "description": [
        {
          "type": "paragraph",
          "text": "The store or lookup failed."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No cancellation is claimed."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CANCEL-INVALID",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "Lookup refused an invalid code."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No save or data change."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CANCEL-DENIED",
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
      "id": "RF-BOOKING-CANCEL-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case calls UC-BOOKING-LOOKUP and preserves its not-found and invalid-code refusals."
        },
        {
          "type": "paragraph",
          "text": "Preserve the caller context and propagate lookup denial before any save."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CANCEL"
      ],
      "flow_refs": [
        "N-BOOK-CANCEL-LOOK",
        "N-BOOK-CANCEL-FOUND",
        "N-BOOK-CANCEL-NOTFOUND",
        "N-BOOK-CANCEL-INVALID",
        "N-BOOK-CANCEL-LOOKDENIED",
        "E-BOOK-CANCEL-3",
        "E-BOOK-CANCEL-4",
        "E-BOOK-CANCEL-INVALID",
        "E-BOOK-CANCEL-LOOKDENIED",
        "N-BOOK-REFUSE-NOTFOUND",
        "E-BOOK-REFUSE-2"
      ]
    },
    {
      "id": "RF-BOOKING-CANCEL-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case applies VLD-BOOKING-CANCEL to the located booking before any save."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CANCEL"
      ],
      "flow_refs": [
        "N-BOOK-CANCEL-VALIDATE",
        "N-BOOK-CANCEL-VALID",
        "E-BOOK-CANCEL-5"
      ]
    },
    {
      "id": "RF-BOOKING-CANCEL-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "An already-cancelled booking produces the already-cancelled refusal with no save and no effect."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CANCEL"
      ],
      "flow_refs": [
        "N-BOOK-CANCEL-ALREADY",
        "E-BOOK-CANCEL-6",
        "N-BOOK-REFUSE-START",
        "N-BOOK-REFUSE-ALREADY",
        "E-BOOK-REFUSE-1"
      ]
    },
    {
      "id": "RF-BOOKING-CANCEL-04",
      "statement": [
        {
          "type": "paragraph",
          "text": "A passing transition sets status cancelled and calls OP-BOOKING-SAVE with the observed version."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-BOOKING-CANCEL",
        "OP-BOOKING-SAVE"
      ],
      "flow_refs": [
        "N-BOOK-CANCEL-SAVE",
        "N-BOOK-CANCEL-DONE",
        "E-BOOK-CANCEL-7",
        "E-BOOK-CANCEL-9"
      ]
    },
    {
      "id": "RF-BOOKING-CANCEL-05",
      "statement": [
        {
          "type": "paragraph",
          "text": "A store failure is reported distinctly and does not claim cancellation."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-BOOKING-CANCEL",
        "OP-BOOKING-SAVE"
      ],
      "flow_refs": [
        "N-BOOK-CANCEL-ERROR",
        "E-BOOK-CANCEL-8",
        "E-BOOK-CANCEL-LOOKERROR"
      ]
    },
    {
      "id": "RF-BOOKING-CANCEL-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Require this case's permission in the trusted authenticated caller context. Deny missing, unresolved, expired or insufficient context before any validation, tool call, composed use-case call or effect. Anonymous execution is forbidden."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CANCEL"
      ],
      "flow_refs": [
        "N-BOOKING-CANCEL-AUTH",
        "N-BOOKING-CANCEL-DENIED",
        "E-BOOKING-CANCEL-ALLOW",
        "E-BOOKING-CANCEL-DENY"
      ]
    }
  ],
  "nonfunctional_requirements": [
    {
      "id": "RNF-BOOKING-CANCEL-RESPONSE",
      "reference_to": "RNF-BOOKING-CREATE-RESPONSE",
      "scope": "interaction",
      "applies_to": [
        "UC-BOOKING-CANCEL"
      ],
      "references": [
        "SRC-BOOKING-BRIEF"
      ],
      "applicability": [
        {
          "type": "paragraph",
          "text": "Origin: SRC-BOOKING-BRIEF. This is a synthetic teaching obligation; any numeric target and scenario count are illustrative assumptions, not an accepted production SLA or a measurement made by this repository."
        }
      ]
    }
  ],
  "flows": {
    "main": "GRAPH-BOOKING-CANCEL",
    "subflows": [
      "GRAPH-BOOKING-CANCEL-REFUSAL"
    ]
  },
  "flow_text": [
    {
      "type": "paragraph",
      "text": "Resolve and authorize the initiating caller first (RF-BOOKING-CANCEL-AUTH). Denial terminates before any subsequent step."
    },
    {
      "type": "paragraph",
      "text": "Call UC-BOOKING-LOOKUP (RF-BOOKING-CANCEL-01). Its refusals and failures remain observable."
    },
    {
      "type": "paragraph",
      "text": "Apply VLD-BOOKING-CANCEL to the located booking (RF-BOOKING-CANCEL-02)."
    },
    {
      "type": "paragraph",
      "text": "An already-cancelled booking reaches the refusal subflow (RF-BOOKING-CANCEL-03) with no save."
    },
    {
      "type": "paragraph",
      "text": "On pass, set status cancelled and save with the observed version (RF-BOOKING-CANCEL-04). A save failure is reported (RF-BOOKING-CANCEL-05)."
    },
    {
      "type": "paragraph",
      "text": "A composed lookup denial terminates cancellation before save. A lookup failure is propagated as failure, never collapsed into not found."
    }
  ],
  "acceptance_criteria": [
    {
      "id": "AC-BOOKING-CANCEL-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "Cancelling an active booking returns cancelled and retains the code."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-02",
        "RF-BOOKING-CANCEL-04"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "Cancelling an already-cancelled booking is refused with no data change."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "A lookup not-found is distinguishable from an already-cancelled refusal."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-01",
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-FAILURE",
      "statement": [
        {
          "type": "paragraph",
          "text": "An unavailable lookup or save remains a failure; an unknown write is not reported as no change, success, or retried automatically."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-05"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-CONTEXT",
      "statement": [
        {
          "type": "paragraph",
          "text": "A caller allowed to cancel but not to locate is denied by the composed lookup, with the same principal preserved and no save."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-AUTH"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-QUALITY",
      "statement": [
        {
          "type": "paragraph",
          "text": "In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim."
        }
      ],
      "verifies": [
        "RNF-BOOKING-CANCEL-RESPONSE"
      ]
    }
  ],
  "traceability": [
    {
      "id": "TRC-BOOKING-CANCEL-01",
      "source": "RF-BOOKING-CANCEL-02",
      "targets": [
        "VLD-BOOKING-CANCEL",
        "TRN-BOOKING-CANCEL"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Transition validation and entity transition."
        }
      ]
    },
    {
      "id": "TRC-BOOKING-CANCEL-02",
      "source": "RNF-BOOKING-CANCEL-RESPONSE",
      "targets": [
        "RNF-BOOKING-CREATE-RESPONSE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Explicit shared obligation reference."
        }
      ]
    },
    {
      "id": "TRC-BOOKING-CANCEL-ORIGIN",
      "source": "SRC-BOOKING-BRIEF",
      "targets": [
        "RF-BOOKING-CANCEL-01",
        "RF-BOOKING-CANCEL-02",
        "RF-BOOKING-CANCEL-03",
        "RF-BOOKING-CANCEL-04",
        "RF-BOOKING-CANCEL-05",
        "RF-BOOKING-CANCEL-AUTH",
        "RNF-BOOKING-CANCEL-RESPONSE"
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
    "path": "apps/BookingDesk/usecases/Main/UseCase_CancelBooking.py",
    "symbol": "UseCase_CancelBooking"
  },
  "class_kind": "use_case",
  "consumed_entities": [
    "ENT-BOOKING"
  ],
  "injected_tools": [
    {
      "abstract_tool_ref": "TOL-BOOKING-STORE",
      "operation_ref": "OP-BOOKING-SAVE",
      "injected_concrete_tool_ref": "CTL-BOOKING-STORE",
      "purpose": "Persist the cancelled status."
    }
  ],
  "methods": [
    {
      "name": "execute",
      "visibility": "public",
      "trigger": "A clerk requests cancellation by code.",
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
        "Resolve and authorize the initiating caller first (RF-BOOKING-CANCEL-AUTH). Denial terminates before any subsequent step.",
        "Call UC-BOOKING-LOOKUP (RF-BOOKING-CANCEL-01). Its refusals and failures remain observable.",
        "Apply VLD-BOOKING-CANCEL to the located booking (RF-BOOKING-CANCEL-02).",
        "An already-cancelled booking reaches the refusal subflow (RF-BOOKING-CANCEL-03) with no save.",
        "On pass, set status cancelled and save with the observed version (RF-BOOKING-CANCEL-04). A save failure is reported (RF-BOOKING-CANCEL-05).",
        "A composed lookup denial terminates cancellation before save. A lookup failure is propagated as failure, never collapsed into not found."
      ],
      "returns": [
        {
          "outcome_ref": "OUT-BOOKING-CANCEL-DONE",
          "kind": "success"
        },
        {
          "outcome_ref": "OUT-BOOKING-CANCEL-ALREADY",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-BOOKING-CANCEL-NOTFOUND",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-BOOKING-CANCEL-FAILURE",
          "kind": "failure"
        },
        {
          "outcome_ref": "OUT-BOOKING-CANCEL-INVALID",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-BOOKING-CANCEL-DENIED",
          "kind": "refusal"
        }
      ],
      "source_refs": [
        "UC-BOOKING-CANCEL",
        "RF-BOOKING-CANCEL-01",
        "RF-BOOKING-CANCEL-02",
        "RF-BOOKING-CANCEL-03",
        "RF-BOOKING-CANCEL-04",
        "RF-BOOKING-CANCEL-05",
        "RF-BOOKING-CANCEL-AUTH"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-BOOKING-CANCEL",
    "GRAPH-BOOKING-CANCEL-REFUSAL"
  ]
}
```
