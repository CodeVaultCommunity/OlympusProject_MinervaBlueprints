---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: UC-BOOKING-CREATE
kind: use_case
source_refs:
- UC-BOOKING-CREATE
generation:
  mode: code
  language: python
  path: apps/BookingDesk/usecases/Main/UseCase_CreateBooking.py
  symbol: UseCase_CreateBooking
---

# Create booking

Create one active booking and confirm its stored state.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "UC-BOOKING-CREATE",
  "name": {
    "text": "Create booking"
  },
  "objective": [
    {
      "type": "paragraph",
      "text": "Create one active booking and confirm its stored state."
    }
  ],
  "actors": [
    {
      "actor": "ACT-BOOKING-CLERK",
      "permission": {
        "text": "Permitted to create bookings."
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
      "text": "A clerk supplies a code and title."
    }
  ],
  "context": [
    {
      "type": "paragraph",
      "text": "The desk creates a booking in the shared store."
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
          "text": "The code to create."
        }
      ],
      "required": true
    },
    {
      "name": {
        "text": "Title"
      },
      "type": "text",
      "meaning": [
        {
          "type": "paragraph",
          "text": "The booking title."
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
        "VLD-BOOKING-CODE",
        "VLD-BOOKING-TITLE"
      ],
      "purpose": [
        {
          "type": "paragraph",
          "text": "Validate the code and form the active booking."
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
          "text": "Persist the new booking."
        }
      ]
    }
  ],
  "calls": [],
  "outcomes": [
    {
      "id": "OUT-BOOKING-CREATE-DONE",
      "kind": "success",
      "description": [
        {
          "type": "paragraph",
          "text": "The active booking is created."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "One new booking is retained."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CREATE-INVALID",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The code or title is invalid."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No save and no retained booking."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CREATE-CONFLICT",
      "kind": "failure",
      "description": [
        {
          "type": "paragraph",
          "text": "The store reports a version conflict or unavailability."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No created booking is reported."
        }
      ]
    },
    {
      "id": "OUT-BOOKING-CREATE-DENIED",
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
      "id": "RF-BOOKING-CREATE-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case applies VLD-BOOKING-CODE and refuses an invalid code without saving."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CREATE"
      ],
      "flow_refs": [
        "N-BOOK-CREATE-CODE",
        "N-BOOK-CREATE-CODEC",
        "N-BOOK-CREATE-INVALID",
        "E-BOOK-CREATE-3"
      ]
    },
    {
      "id": "RF-BOOKING-CREATE-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case creates an active booking and calls OP-BOOKING-SAVE with version 0."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-BOOKING-CREATE",
        "OP-BOOKING-SAVE"
      ],
      "flow_refs": [
        "N-BOOK-CREATE-SAVE",
        "E-BOOK-CREATE-4",
        "E-BOOK-CREATE-7"
      ]
    },
    {
      "id": "RF-BOOKING-CREATE-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "VERSION_CONFLICT and STORE_UNAVAILABLE are reported as failures, never as a created booking."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-BOOKING-CREATE",
        "OP-BOOKING-SAVE"
      ],
      "flow_refs": [
        "N-BOOK-CREATE-DUP",
        "N-BOOK-CREATE-FAIL",
        "E-BOOK-CREATE-5",
        "E-BOOK-CREATE-6"
      ]
    },
    {
      "id": "RF-BOOKING-CREATE-04",
      "statement": [
        {
          "type": "paragraph",
          "text": "A successful result returns the created active booking."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CREATE"
      ],
      "flow_refs": [
        "N-BOOK-CREATE-DONE",
        "E-BOOK-CREATE-7"
      ]
    },
    {
      "id": "RF-BOOKING-CREATE-TITLE",
      "statement": [
        {
          "type": "paragraph",
          "text": "After a valid code, apply VLD-BOOKING-TITLE. Refuse invalid title before creating a ready active Booking or invoking save."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CREATE"
      ],
      "flow_refs": [
        "N-BOOK-CREATE-TITLE",
        "N-BOOK-CREATE-TITLEVALID",
        "E-BOOK-CREATE-TITLE-2",
        "E-BOOK-CREATE-TITLE-3"
      ]
    },
    {
      "id": "RF-BOOKING-CREATE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Require this case's permission in the trusted authenticated caller context. Deny missing, unresolved, expired or insufficient context before any validation, tool call, composed use-case call or effect. Anonymous execution is forbidden."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-BOOKING-CREATE"
      ],
      "flow_refs": [
        "N-BOOKING-CREATE-AUTH",
        "N-BOOKING-CREATE-DENIED",
        "E-BOOKING-CREATE-ALLOW",
        "E-BOOKING-CREATE-DENY"
      ]
    }
  ],
  "nonfunctional_requirements": [
    {
      "id": "RNF-BOOKING-CREATE-RESPONSE",
      "scope": "interaction",
      "applies_to": [
        "UC-BOOKING-CREATE"
      ],
      "statement": [
        {
          "type": "paragraph",
          "text": "The boundary presents the result of a creation within 2 seconds of the stimulus for inputs within the declared limits."
        }
      ],
      "criterion": [
        {
          "type": "paragraph",
          "text": "Visible result time is at most 2 seconds."
        }
      ],
      "verification": [
        {
          "type": "paragraph",
          "text": "Run 30 creation requests against the declared configuration and record elapsed time."
        }
      ],
      "metric": {
        "name": {
          "text": "Visible result time"
        },
        "unit": {
          "text": "seconds"
        },
        "target": "2",
        "operator": "<="
      },
      "measurement": {
        "start": [
          {
            "type": "paragraph",
            "text": "The creation stimulus is accepted."
          }
        ],
        "end": [
          {
            "type": "paragraph",
            "text": "The result is visible."
          }
        ]
      },
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
    "main": "GRAPH-BOOKING-CREATE",
    "subflows": []
  },
  "flow_text": [
    {
      "type": "paragraph",
      "text": "Resolve and authorize the initiating caller first (RF-BOOKING-CREATE-AUTH). Denial terminates before any subsequent step."
    },
    {
      "type": "paragraph",
      "text": "Validate the code with VLD-BOOKING-CODE (RF-BOOKING-CREATE-01)."
    },
    {
      "type": "paragraph",
      "text": "Apply title validity after code validity; refuse invalid title without saving (RF-BOOKING-CREATE-TITLE)."
    },
    {
      "type": "paragraph",
      "text": "Create the active booking and save through OP-BOOKING-SAVE (RF-BOOKING-CREATE-02)."
    },
    {
      "type": "paragraph",
      "text": "A save failure is reported as failure (RF-BOOKING-CREATE-03); a success returns the created booking (RF-BOOKING-CREATE-04)."
    }
  ],
  "acceptance_criteria": [
    {
      "id": "AC-BOOKING-CREATE-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "A valid code creates an active booking and a later lookup returns it."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-04"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "An invalid code is refused with no retained booking."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-01"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "A version conflict is never presented as a created booking."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-03"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-TITLE",
      "statement": [
        {
          "type": "paragraph",
          "text": "A whitespace-only title is refused and OP-BOOKING-SAVE is not invoked."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-TITLE"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-AUTH"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-QUALITY",
      "statement": [
        {
          "type": "paragraph",
          "text": "In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim."
        }
      ],
      "verifies": [
        "RNF-BOOKING-CREATE-RESPONSE"
      ]
    }
  ],
  "traceability": [
    {
      "id": "TRC-BOOKING-CREATE-01",
      "source": "RF-BOOKING-CREATE-01",
      "targets": [
        "VLD-BOOKING-CODE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Shared validation also used by lookup."
        }
      ]
    },
    {
      "id": "TRC-BOOKING-CREATE-02",
      "source": "RF-BOOKING-CREATE-02",
      "targets": [
        "OP-BOOKING-SAVE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Shared tool operation also used by cancellation."
        }
      ]
    },
    {
      "id": "TRC-BOOKING-CREATE-ORIGIN",
      "source": "SRC-BOOKING-BRIEF",
      "targets": [
        "RF-BOOKING-CREATE-01",
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-03",
        "RF-BOOKING-CREATE-04",
        "RF-BOOKING-CREATE-TITLE",
        "RF-BOOKING-CREATE-AUTH",
        "RNF-BOOKING-CREATE-RESPONSE"
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
    "path": "apps/BookingDesk/usecases/Main/UseCase_CreateBooking.py",
    "symbol": "UseCase_CreateBooking"
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
      "purpose": "Persist the new booking."
    }
  ],
  "methods": [
    {
      "name": "execute",
      "visibility": "public",
      "trigger": "A clerk supplies a code and title.",
      "parameters": [
        {
          "name": "booking_code",
          "type": "text",
          "required": true
        },
        {
          "name": "title",
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
        "Resolve and authorize the initiating caller first (RF-BOOKING-CREATE-AUTH). Denial terminates before any subsequent step.",
        "Validate the code with VLD-BOOKING-CODE (RF-BOOKING-CREATE-01).",
        "Apply title validity after code validity; refuse invalid title without saving (RF-BOOKING-CREATE-TITLE).",
        "Create the active booking and save through OP-BOOKING-SAVE (RF-BOOKING-CREATE-02).",
        "A save failure is reported as failure (RF-BOOKING-CREATE-03); a success returns the created booking (RF-BOOKING-CREATE-04)."
      ],
      "returns": [
        {
          "outcome_ref": "OUT-BOOKING-CREATE-DONE",
          "kind": "success"
        },
        {
          "outcome_ref": "OUT-BOOKING-CREATE-INVALID",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-BOOKING-CREATE-CONFLICT",
          "kind": "failure"
        },
        {
          "outcome_ref": "OUT-BOOKING-CREATE-DENIED",
          "kind": "refusal"
        }
      ],
      "source_refs": [
        "UC-BOOKING-CREATE",
        "RF-BOOKING-CREATE-01",
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-03",
        "RF-BOOKING-CREATE-04",
        "RF-BOOKING-CREATE-TITLE",
        "RF-BOOKING-CREATE-AUTH"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-BOOKING-CREATE"
  ]
}
```
