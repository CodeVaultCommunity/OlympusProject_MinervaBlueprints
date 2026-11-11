---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: BND-BOOKING-CLI
kind: boundary
source_refs:
- BND-BOOKING-CLI
generation:
  mode: code
  language: python
  path: apps/BookingDesk/boundaries/Boundary_BookingDeskCommandLine.py
  symbol: Boundary_BookingDeskCommandLine
---

# Booking desk command line

Expose booking creation, lookup, and cancellation through commands. Origin classification: this channel is an illustrative solution proposal. Its form, command syntax, layout and encoding are outside the L1 conformance claim. The referenced cases define domain inputs and outcomes independently of this channel.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "BND-BOOKING-CLI",
  "name": {
    "text": "Booking desk command line"
  },
  "modality": "cli",
  "purpose": [
    {
      "type": "paragraph",
      "text": "Expose booking creation, lookup, and cancellation through commands."
    },
    {
      "type": "paragraph",
      "text": "Origin classification: this channel is an illustrative solution proposal. Its form, command syntax, layout and encoding are outside the L1 conformance claim. The referenced cases define domain inputs and outcomes independently of this channel."
    }
  ],
  "audience": [
    {
      "type": "paragraph",
      "text": "Desk clerks operating a local terminal."
    }
  ],
  "interactions": [
    {
      "id": "INT-BOOKING-CREATE",
      "name": {
        "text": "Create command"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Accepts a code and title and presents the created booking or a refusal/failure."
        },
        {
          "type": "paragraph",
          "text": "Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here."
        }
      ],
      "use_case": "UC-BOOKING-CREATE",
      "trigger": [
        {
          "type": "paragraph",
          "text": "The clerk invokes booking create."
        }
      ],
      "input_mapping": [
        {
          "source": "argv.code",
          "target": "UC-BOOKING-CREATE.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "argv.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-CREATE",
            "selector": "code",
            "value_type": "text"
          }
        },
        {
          "source": "argv.title",
          "target": "UC-BOOKING-CREATE.input.title",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The title argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "argv.title",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-CREATE",
            "selector": "title",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-BOOKING-CREATE-DONE",
          "target": "stdout.created",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The active booking is created."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-DONE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "stdout.created",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CREATE-INVALID",
          "target": "stderr.invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The code or title is invalid."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "stderr.invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CREATE-CONFLICT",
          "target": "stderr.failure",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store reports a version conflict or unavailability."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-CONFLICT",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "stderr.failure",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CREATE-DENIED",
          "target": "result.out-booking-create-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The trusted caller context does not authorize this case."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "result.out-booking-create-denied",
            "value_type": "outcome"
          }
        }
      ],
      "requirement_refs": [
        "RF-BOOKING-CREATE-01",
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-03",
        "RF-BOOKING-CREATE-04",
        "RF-BOOKING-CREATE-TITLE",
        "RF-BOOKING-CREATE-AUTH"
      ],
      "resources": [],
      "examples": [
        {
          "type": "code",
          "language": "text",
          "text": "booking create BOOK001 \"Annual review\""
        }
      ]
    },
    {
      "id": "INT-BOOKING-CANCEL",
      "name": {
        "text": "Cancel command"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Accepts a code and presents cancellation, already-cancelled, not-found, or failure."
        },
        {
          "type": "paragraph",
          "text": "Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here."
        }
      ],
      "use_case": "UC-BOOKING-CANCEL",
      "trigger": [
        {
          "type": "paragraph",
          "text": "The clerk invokes booking cancel."
        }
      ],
      "input_mapping": [
        {
          "source": "argv.code",
          "target": "UC-BOOKING-CANCEL.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "argv.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-CANCEL",
            "selector": "code",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-BOOKING-CANCEL-DONE",
          "target": "stdout.cancelled",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking is cancelled and retained."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-DONE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stdout.cancelled",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-ALREADY",
          "target": "stderr.already",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking is already cancelled."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-ALREADY",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stderr.already",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-NOTFOUND",
          "target": "stderr.not_found",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The lookup did not find the booking."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-NOTFOUND",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stderr.not_found",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-FAILURE",
          "target": "stderr.failure",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store or lookup failed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-FAILURE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stderr.failure",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-INVALID",
          "target": "result.out-booking-cancel-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Lookup refused an invalid code."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "result.out-booking-cancel-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-DENIED",
          "target": "result.out-booking-cancel-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The trusted caller context does not authorize this case."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "result.out-booking-cancel-denied",
            "value_type": "outcome"
          }
        }
      ],
      "requirement_refs": [
        "RF-BOOKING-CANCEL-01",
        "RF-BOOKING-CANCEL-02",
        "RF-BOOKING-CANCEL-03",
        "RF-BOOKING-CANCEL-04",
        "RF-BOOKING-CANCEL-05",
        "RF-BOOKING-CANCEL-AUTH"
      ],
      "resources": [],
      "examples": [
        {
          "type": "code",
          "language": "text",
          "text": "booking cancel BOOK001"
        }
      ]
    },
    {
      "id": "INT-BOOKING-LOOKUP",
      "name": {
        "text": "Lookup command"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Accepts a code and presents the booking, not found, or failure."
        },
        {
          "type": "paragraph",
          "text": "Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here."
        }
      ],
      "use_case": "UC-BOOKING-LOOKUP",
      "trigger": [
        {
          "type": "paragraph",
          "text": "The clerk invokes booking lookup."
        }
      ],
      "input_mapping": [
        {
          "source": "argv.code",
          "target": "UC-BOOKING-LOOKUP.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "argv.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-LOOKUP",
            "selector": "code",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-BOOKING-LOOKUP-FOUND",
          "target": "stdout.booking",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking is returned."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-FOUND",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "stdout.booking",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-NOTFOUND",
          "target": "stderr.not_found",
          "meaning": [
            {
              "type": "paragraph",
              "text": "No booking has the code."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-NOTFOUND",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "stderr.not_found",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-FAILURE",
          "target": "stderr.failure",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store is unavailable."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-FAILURE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "stderr.failure",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-INVALID",
          "target": "result.out-booking-lookup-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code is invalid."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "result.out-booking-lookup-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-DENIED",
          "target": "result.out-booking-lookup-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The trusted caller context does not authorize this case."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "result.out-booking-lookup-denied",
            "value_type": "outcome"
          }
        }
      ],
      "requirement_refs": [
        "RF-BOOKING-LOOKUP-01",
        "RF-BOOKING-LOOKUP-02",
        "RF-BOOKING-LOOKUP-03",
        "RF-BOOKING-LOOKUP-04",
        "RF-BOOKING-LOOKUP-AUTH"
      ],
      "resources": [],
      "examples": [
        {
          "type": "code",
          "language": "text",
          "text": "booking lookup BOOK001"
        }
      ]
    }
  ],
  "assumptions": [],
  "sources": [
    "SRC-BOOKING-BRIEF"
  ],
  "open_issues": [],
  "classification": "illustration"
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/BookingDesk/boundaries/Boundary_BookingDeskCommandLine.py",
    "symbol": "Boundary_BookingDeskCommandLine"
  },
  "class_kind": "boundary_adapter",
  "boundary_semantics": "Interaction interface only; never a test case or observation point.",
  "classification": "illustration",
  "modality": "cli",
  "methods": [
    {
      "name": "create_command",
      "exposes_use_case": "UC-BOOKING-CREATE",
      "trigger": "The clerk invokes booking create.",
      "input_mapping": [
        {
          "source": "argv.code",
          "target": "UC-BOOKING-CREATE.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "argv.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-CREATE",
            "selector": "code",
            "value_type": "text"
          }
        },
        {
          "source": "argv.title",
          "target": "UC-BOOKING-CREATE.input.title",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The title argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "argv.title",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-CREATE",
            "selector": "title",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-BOOKING-CREATE-DONE",
          "target": "stdout.created",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The active booking is created."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-DONE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "stdout.created",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CREATE-INVALID",
          "target": "stderr.invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The code or title is invalid."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "stderr.invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CREATE-CONFLICT",
          "target": "stderr.failure",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store reports a version conflict or unavailability."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-CONFLICT",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "stderr.failure",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CREATE-DENIED",
          "target": "result.out-booking-create-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The trusted caller context does not authorize this case."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CREATE-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CREATE",
            "selector": "result.out-booking-create-denied",
            "value_type": "outcome"
          }
        }
      ],
      "source_refs": [
        "INT-BOOKING-CREATE",
        "RF-BOOKING-CREATE-01",
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-03",
        "RF-BOOKING-CREATE-04",
        "RF-BOOKING-CREATE-TITLE",
        "RF-BOOKING-CREATE-AUTH"
      ]
    },
    {
      "name": "cancel_command",
      "exposes_use_case": "UC-BOOKING-CANCEL",
      "trigger": "The clerk invokes booking cancel.",
      "input_mapping": [
        {
          "source": "argv.code",
          "target": "UC-BOOKING-CANCEL.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "argv.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-CANCEL",
            "selector": "code",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-BOOKING-CANCEL-DONE",
          "target": "stdout.cancelled",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking is cancelled and retained."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-DONE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stdout.cancelled",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-ALREADY",
          "target": "stderr.already",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking is already cancelled."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-ALREADY",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stderr.already",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-NOTFOUND",
          "target": "stderr.not_found",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The lookup did not find the booking."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-NOTFOUND",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stderr.not_found",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-FAILURE",
          "target": "stderr.failure",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store or lookup failed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-FAILURE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "stderr.failure",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-INVALID",
          "target": "result.out-booking-cancel-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Lookup refused an invalid code."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "result.out-booking-cancel-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-CANCEL-DENIED",
          "target": "result.out-booking-cancel-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The trusted caller context does not authorize this case."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-CANCEL-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-CANCEL",
            "selector": "result.out-booking-cancel-denied",
            "value_type": "outcome"
          }
        }
      ],
      "source_refs": [
        "INT-BOOKING-CANCEL",
        "RF-BOOKING-CANCEL-01",
        "RF-BOOKING-CANCEL-02",
        "RF-BOOKING-CANCEL-03",
        "RF-BOOKING-CANCEL-04",
        "RF-BOOKING-CANCEL-05",
        "RF-BOOKING-CANCEL-AUTH"
      ]
    },
    {
      "name": "lookup_command",
      "exposes_use_case": "UC-BOOKING-LOOKUP",
      "trigger": "The clerk invokes booking lookup.",
      "input_mapping": [
        {
          "source": "argv.code",
          "target": "UC-BOOKING-LOOKUP.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code argument."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "argv.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-BOOKING-LOOKUP",
            "selector": "code",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-BOOKING-LOOKUP-FOUND",
          "target": "stdout.booking",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking is returned."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-FOUND",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "stdout.booking",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-NOTFOUND",
          "target": "stderr.not_found",
          "meaning": [
            {
              "type": "paragraph",
              "text": "No booking has the code."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-NOTFOUND",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "stderr.not_found",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-FAILURE",
          "target": "stderr.failure",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store is unavailable."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-FAILURE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "stderr.failure",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-INVALID",
          "target": "result.out-booking-lookup-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking code is invalid."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "result.out-booking-lookup-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-BOOKING-LOOKUP-DENIED",
          "target": "result.out-booking-lookup-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The trusted caller context does not authorize this case."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-BOOKING-LOOKUP-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-BOOKING-LOOKUP",
            "selector": "result.out-booking-lookup-denied",
            "value_type": "outcome"
          }
        }
      ],
      "source_refs": [
        "INT-BOOKING-LOOKUP",
        "RF-BOOKING-LOOKUP-01",
        "RF-BOOKING-LOOKUP-02",
        "RF-BOOKING-LOOKUP-03",
        "RF-BOOKING-LOOKUP-04",
        "RF-BOOKING-LOOKUP-AUTH"
      ]
    }
  ]
}
```
