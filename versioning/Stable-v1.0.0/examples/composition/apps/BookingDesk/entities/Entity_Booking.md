---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: ENT-BOOKING
kind: entity
source_refs:
- ENT-BOOKING
generation:
  mode: code
  language: python
  path: apps/BookingDesk/entities/Entity_Booking.py
  symbol: Entity_Booking
---

# Booking

Preserves Atlas entity ENT-BOOKING.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "ENT-BOOKING",
  "name": {
    "text": "Booking"
  },
  "meaning": [
    {
      "type": "paragraph",
      "text": "A booking records a named reservation and has a lifecycle status."
    }
  ],
  "identity": {
    "description": [
      {
        "type": "paragraph",
        "text": "Two bookings are the same when their codes are equal."
      }
    ],
    "fields": [
      "FLD-BOOKING-CODE"
    ]
  },
  "fields": [
    {
      "id": "FLD-BOOKING-CODE",
      "name": {
        "text": "Booking code"
      },
      "type": "text",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "A stable uppercase code that identifies the booking."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "1 to 12 uppercase letters or digits."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "BOOK001"
          }
        ],
        "invalid": [
          {
            "text": "book-001"
          }
        ]
      }
    },
    {
      "id": "FLD-BOOKING-TITLE",
      "name": {
        "text": "Title"
      },
      "type": "text",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "A short human-readable title."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "At least one non-whitespace character."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "Annual review"
          }
        ],
        "invalid": [
          {
            "text": "   "
          }
        ]
      }
    },
    {
      "id": "FLD-BOOKING-STATUS",
      "name": {
        "text": "Status"
      },
      "type": "booking-status",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "The lifecycle state of the booking."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "One of active or cancelled."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "active"
          },
          {
            "text": "cancelled"
          }
        ],
        "invalid": [
          {
            "text": "deleted"
          }
        ]
      }
    },
    {
      "id": "FLD-BOOKING-VERSION",
      "name": {
        "text": "Version"
      },
      "type": "integer",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "Concurrency token: zero for a new ready Booking, positive for a retained Booking."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "A non-negative integer; successful save increments it."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "0"
          },
          {
            "text": "1"
          }
        ],
        "invalid": [
          {
            "text": "-1"
          }
        ]
      }
    }
  ],
  "relationships": [],
  "states": [
    {
      "id": "ST-BOOKING-ACTIVE",
      "name": {
        "text": "Active"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "The booking reserves its item."
        }
      ]
    },
    {
      "id": "ST-BOOKING-CANCELLED",
      "name": {
        "text": "Cancelled"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "The booking no longer reserves its item and is retained."
        }
      ]
    }
  ],
  "transitions": [
    {
      "id": "TRN-BOOKING-CANCEL",
      "name": {
        "text": "Cancel"
      },
      "from": "ST-BOOKING-ACTIVE",
      "to": "ST-BOOKING-CANCELLED",
      "description": [
        {
          "type": "paragraph",
          "text": "Cancellation changes status and retains the record."
        }
      ]
    }
  ],
  "validations": [
    {
      "id": "VLD-BOOKING-CODE",
      "name": {
        "text": "Booking code format"
      },
      "scope": "field",
      "statement": [
        {
          "type": "paragraph",
          "text": "The code is valid when it has 1 to 12 characters, all uppercase letters or digits."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Booking code"
          },
          "source": "field",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The value supplied for FLD-BOOKING-CODE."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-VLD-BOOK-CODE-EMPTY",
          "condition": {
            "text": "The code is non-empty."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "An empty code fails."
            }
          ]
        },
        {
          "id": "C-VLD-BOOK-CODE-LEN",
          "condition": {
            "text": "The length is between 1 and 12."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "Longer codes fail."
            }
          ]
        },
        {
          "id": "C-VLD-BOOK-CODE-CHARS",
          "condition": {
            "text": "Every character is A-Z or 0-9."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "Lowercase and punctuation fail."
            }
          ]
        }
      ],
      "results": [
        {
          "outcome": "pass",
          "description": [
            {
              "type": "paragraph",
              "text": "The code is accepted unchanged."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "The code is rejected; the field keeps its previous value."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-BOOKING-CODE"
    },
    {
      "id": "VLD-BOOKING-CANCEL",
      "name": {
        "text": "Cancellation is allowed only from active"
      },
      "scope": "transition",
      "statement": [
        {
          "type": "paragraph",
          "text": "A cancellation transition is valid only when the booking's current status is active."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Current status"
          },
          "source": "state",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The status read from the located booking."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-VLD-BOOK-CANCEL-ACTIVE",
          "condition": {
            "text": "The current status is active."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "A cancelled booking fails this condition."
            }
          ]
        }
      ],
      "results": [
        {
          "outcome": "pass",
          "description": [
            {
              "type": "paragraph",
              "text": "Cancellation may proceed."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "The already-cancelled refusal applies; no save occurs."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-BOOKING-CANCEL"
    },
    {
      "id": "VLD-BOOKING-TITLE",
      "name": {
        "text": "Booking title validity"
      },
      "scope": "field",
      "statement": [
        {
          "type": "paragraph",
          "text": "The title is text with at least one non-whitespace character. Preserve valid text exactly."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Title"
          },
          "source": "field",
          "meaning": [
            {
              "type": "paragraph",
              "text": "FLD-BOOKING-TITLE candidate."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-VLD-BOOK-TITLE-TEXT",
          "condition": {
            "text": "The title has at least one non-whitespace character."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "Empty and whitespace-only titles fail."
            }
          ]
        }
      ],
      "results": [
        {
          "outcome": "pass",
          "description": [
            {
              "type": "paragraph",
              "text": "Accept unchanged."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "Refuse before save."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-BOOKING-TITLE"
    }
  ],
  "examples": [
    {
      "id": "EX-BOOKING-VALID",
      "kind": "valid",
      "description": [
        {
          "type": "paragraph",
          "text": "An active booking with a conforming code."
        }
      ],
      "data": {
        "code": "BOOK001",
        "title": "Annual review",
        "status": "active",
        "version": 0
      }
    },
    {
      "id": "EX-BOOKING-INVALID",
      "kind": "invalid",
      "description": [
        {
          "type": "paragraph",
          "text": "A booking with a lowercase code and unknown status."
        }
      ],
      "data": {
        "code": "book-001",
        "title": "Annual review",
        "status": "deleted",
        "version": 0
      }
    }
  ],
  "assumptions": [],
  "open_issues": []
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/BookingDesk/entities/Entity_Booking.py",
    "symbol": "Entity_Booking"
  },
  "class_kind": "entity",
  "fields": [
    {
      "name": "booking_code",
      "type": "text",
      "required": true,
      "source_ref": "FLD-BOOKING-CODE"
    },
    {
      "name": "title",
      "type": "text",
      "required": true,
      "source_ref": "FLD-BOOKING-TITLE"
    },
    {
      "name": "status",
      "type": "booking-status",
      "required": true,
      "source_ref": "FLD-BOOKING-STATUS"
    },
    {
      "name": "version",
      "type": "integer",
      "required": true,
      "source_ref": "FLD-BOOKING-VERSION"
    }
  ],
  "methods": [
    {
      "name": "create",
      "visibility": "public",
      "trigger": "when raw values enter the domain",
      "parameters": [
        {
          "name": "booking_code",
          "type": "text"
        },
        {
          "name": "title",
          "type": "text"
        },
        {
          "name": "status",
          "type": "booking-status"
        },
        {
          "name": "version",
          "type": "integer"
        }
      ],
      "returns": [
        "Booking"
      ],
      "algorithm": "Construct only after all Atlas entity validations pass; never leave a partially valid entity.",
      "source_refs": [
        "ENT-BOOKING",
        "VLD-BOOKING-CODE",
        "VLD-BOOKING-CANCEL",
        "VLD-BOOKING-TITLE"
      ]
    },
    {
      "name": "validate_booking_code_format",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "booking_code",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "The code is valid when it has 1 to 12 characters, all uppercase letters or digits.",
      "source_refs": [
        "VLD-BOOKING-CODE"
      ]
    },
    {
      "name": "validate_cancellation_is_allowed_only_from_active",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "current_status",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "A cancellation transition is valid only when the booking's current status is active.",
      "source_refs": [
        "VLD-BOOKING-CANCEL"
      ]
    },
    {
      "name": "validate_booking_title_validity",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "title",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "The title is text with at least one non-whitespace character. Preserve valid text exactly.",
      "source_refs": [
        "VLD-BOOKING-TITLE"
      ]
    }
  ],
  "dependencies": []
}
```
