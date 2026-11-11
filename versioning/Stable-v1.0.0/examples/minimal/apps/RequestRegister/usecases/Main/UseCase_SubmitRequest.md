---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: UC-REQUEST-SUBMIT
kind: use_case
source_refs:
- UC-REQUEST-SUBMIT
generation:
  mode: code
  language: python
  path: apps/RequestRegister/usecases/Main/UseCase_SubmitRequest.py
  symbol: UseCase_SubmitRequest
---

# Submit request

Retain one valid request and confirm the stored record.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "UC-REQUEST-SUBMIT",
  "name": {
    "text": "Submit request"
  },
  "objective": [
    {
      "type": "paragraph",
      "text": "Retain one valid request and confirm the stored record."
    }
  ],
  "actors": [
    {
      "actor": "ACT-REQUESTER",
      "permission": {
        "text": "Permitted to submit requests."
      },
      "description": [
        {
          "type": "paragraph",
          "text": "The requester supplies a code and quantity."
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
      "text": "The requester submits the request form."
    }
  ],
  "context": [
    {
      "type": "paragraph",
      "text": "One request is submitted against the single request register."
    },
    {
      "type": "paragraph",
      "text": "Caller context must contain a resolved authenticated principal, the relevant case permissions, and a validity status. Its origin is the application's trusted identity-and-permission authority; request fields and caller-supplied role strings are not trusted authorization evidence. Anonymous execution is not permitted. Missing, unresolved, expired or insufficient context is denied before any validation, tool access or effect."
    },
    {
      "type": "paragraph",
      "text": "The initiating actor is ACT-REQUESTER. The actor is a role; the caller is the concrete principal. The identity/authentication mechanism and channel encoding remain later design decisions."
    }
  ],
  "inputs": [
    {
      "name": {
        "text": "Request code"
      },
      "type": "text",
      "meaning": [
        {
          "type": "paragraph",
          "text": "The code that identifies the request."
        }
      ],
      "required": true
    },
    {
      "name": {
        "text": "Quantity"
      },
      "type": "integer",
      "meaning": [
        {
          "type": "paragraph",
          "text": "The number of units requested."
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
      "entity": "ENT-REQUEST",
      "validations": [
        "VLD-REQUEST-QUANTITY",
        "VLD-REQUEST-CODE"
      ],
      "purpose": [
        {
          "type": "paragraph",
          "text": "Hold the supplied code and quantity and validate the quantity."
        }
      ]
    }
  ],
  "tools": [
    {
      "tool": "TOL-REQUEST-STORE",
      "operation": "OP-REQUEST-STORE",
      "purpose": [
        {
          "type": "paragraph",
          "text": "Retain the request after validation succeeds."
        }
      ]
    }
  ],
  "calls": [],
  "outcomes": [
    {
      "id": "OUT-REQUEST-CONFIRMED",
      "kind": "success",
      "description": [
        {
          "type": "paragraph",
          "text": "The request is retained and confirmed."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "One new request record exists in the store."
        }
      ]
    },
    {
      "id": "OUT-REQUEST-INVALID",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The code or quantity is invalid; the request is refused."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No store call and no retained record."
        }
      ]
    },
    {
      "id": "OUT-REQUEST-DENIED",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The actor is absent or not permitted."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No validation, store call, or retained record."
        }
      ]
    },
    {
      "id": "OUT-REQUEST-STORE-FAILURE",
      "kind": "failure",
      "description": [
        {
          "type": "paragraph",
          "text": "The store reports that it is unavailable."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No confirmed request is reported."
        }
      ]
    },
    {
      "id": "OUT-REQUEST-DUPLICATE",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The request code is already retained."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "This invocation leaves the existing request unchanged."
        }
      ]
    }
  ],
  "functional_requirements": [
    {
      "id": "RF-REQUEST-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case admits only an actor with the requester permission and refuses every other actor before any validation, store call, or effect."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-REQUEST-SUBMIT",
        "INT-REQUEST-SUBMIT"
      ],
      "flow_refs": [
        "N-REQ-PERM",
        "N-REQ-DENY",
        "E-REQ-2"
      ]
    },
    {
      "id": "RF-REQUEST-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "The case applies VLD-REQUEST-QUANTITY to the supplied quantity and, when the validation reports fail, refuses the request with the invalid-data outcome and no store call."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-REQUEST-SUBMIT",
        "INT-REQUEST-SUBMIT"
      ],
      "flow_refs": [
        "N-REQ-VALIDATE",
        "N-REQ-QTYDEC",
        "N-REQ-INVALID",
        "E-REQ-4",
        "E-REQ-5"
      ]
    },
    {
      "id": "RF-REQUEST-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "After a passing validation, the case calls OP-REQUEST-STORE with the code and quantity; a stored result produces the confirmation outcome."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-REQUEST-SUBMIT",
        "OP-REQUEST-STORE"
      ],
      "flow_refs": [
        "N-REQ-STORE",
        "E-REQ-6",
        "E-REQ-7"
      ]
    },
    {
      "id": "RF-REQUEST-04",
      "statement": [
        {
          "type": "paragraph",
          "text": "When OP-REQUEST-STORE reports STORE_UNAVAILABLE, the case reports the store-unavailable failure and does not claim a confirmed request."
        },
        {
          "type": "paragraph",
          "text": "Preserve whether the tool guarantees not_applied or reports unknown. A lost confirmation is not evidence of no write; do not automatically retry."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-REQUEST-SUBMIT",
        "OP-REQUEST-STORE"
      ],
      "flow_refs": [
        "N-REQ-STOREERROR",
        "E-REQ-8"
      ]
    },
    {
      "id": "RF-REQUEST-05",
      "statement": [
        {
          "type": "paragraph",
          "text": "A confirmed request result contains the supplied code and quantity and identifies the new record."
        }
      ],
      "scope": "interaction",
      "applies_to": [
        "UC-REQUEST-SUBMIT",
        "INT-REQUEST-SUBMIT"
      ],
      "flow_refs": [
        "N-REQ-SUCCESS",
        "E-REQ-7"
      ]
    },
    {
      "id": "RF-REQUEST-06",
      "statement": [
        {
          "type": "paragraph",
          "text": "When OP-REQUEST-STORE reports DUPLICATE_CODE, refuse the duplicate and leave the existing request unchanged; do not report confirmation."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-REQUEST-SUBMIT",
        "OP-REQUEST-STORE"
      ],
      "flow_refs": [
        "N-REQ-DUPLICATE",
        "E-REQ-DUPLICATE"
      ]
    },
    {
      "id": "RF-REQUEST-07",
      "statement": [
        {
          "type": "paragraph",
          "text": "After authorization and before quantity validation, apply VLD-REQUEST-CODE. Refuse invalid code without storage; preserve valid code exactly."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-REQUEST-SUBMIT"
      ],
      "flow_refs": [
        "N-REQ-INVALID",
        "N-REQ-CODE",
        "N-REQ-CODE-VALID",
        "E-REQ-CODE-2",
        "E-REQ-CODE-3"
      ]
    }
  ],
  "nonfunctional_requirements": [
    {
      "id": "RNF-REQUEST-01",
      "scope": "interaction",
      "applies_to": [
        "INT-REQUEST-SUBMIT"
      ],
      "statement": [
        {
          "type": "paragraph",
          "text": "For inputs within the declared field limits and an available store, the boundary presents a confirmed or refused result within 2 seconds of the submit stimulus."
        }
      ],
      "criterion": [
        {
          "type": "paragraph",
          "text": "The elapsed time from the submit stimulus to the visible result is at most 2 seconds."
        }
      ],
      "verification": [
        {
          "type": "paragraph",
          "text": "Run 30 sequential submissions with valid and invalid quantities against the declared local configuration and record the result time for each."
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
            "text": "The submit stimulus is accepted by the boundary."
          }
        ],
        "end": [
          {
            "type": "paragraph",
            "text": "The result state is visible to the actor."
          }
        ]
      },
      "references": [
        "SRC-REQUEST-BRIEF"
      ],
      "applicability": [
        {
          "type": "paragraph",
          "text": "Origin: SRC-REQUEST-BRIEF. This is a synthetic teaching obligation; any numeric target and scenario count are illustrative assumptions, not an accepted production SLA or a measurement made by this repository."
        }
      ]
    }
  ],
  "flows": {
    "main": "GRAPH-REQUEST-SUBMIT",
    "subflows": []
  },
  "flow_text": [
    {
      "type": "paragraph",
      "text": "Start: the case receives the request and actor. If the actor is not permitted, refuse with no effects (RF-REQUEST-01)."
    },
    {
      "type": "paragraph",
      "text": "Apply VLD-REQUEST-CODE before the quantity check. An invalid code is refused without storage (RF-REQUEST-07)."
    },
    {
      "type": "paragraph",
      "text": "Apply VLD-REQUEST-QUANTITY (RF-REQUEST-02). A fail result refuses the request as invalid data."
    },
    {
      "type": "paragraph",
      "text": "On pass, call OP-REQUEST-STORE (RF-REQUEST-03). A stored result produces the confirmed outcome (RF-REQUEST-05). STORE_UNAVAILABLE produces the store-unavailable failure (RF-REQUEST-04)."
    },
    {
      "type": "paragraph",
      "text": "DUPLICATE_CODE is the duplicate refusal with no change to the preexisting request (RF-REQUEST-06). A write failure retains its known-not-applied versus unknown distinction (RF-REQUEST-04)."
    }
  ],
  "acceptance_criteria": [
    {
      "id": "AC-REQUEST-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "A requester with a valid code and quantity of 2 receives a confirmed result; a later lookup of the code returns quantity 2."
        }
      ],
      "verifies": [
        "RF-REQUEST-02",
        "RF-REQUEST-03",
        "RF-REQUEST-05"
      ]
    },
    {
      "id": "AC-REQUEST-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "A quantity of 0 is refused as invalid data, and no record is created."
        }
      ],
      "verifies": [
        "RF-REQUEST-02"
      ]
    },
    {
      "id": "AC-REQUEST-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "An actor absent from the permitted set is refused before validation or store access."
        }
      ],
      "verifies": [
        "RF-REQUEST-01"
      ]
    },
    {
      "id": "AC-REQUEST-04",
      "statement": [
        {
          "type": "paragraph",
          "text": "Submit the same code twice. The second attempt reports duplicate-code refusal and preserves the first retained quantity."
        }
      ],
      "verifies": [
        "RF-REQUEST-06"
      ]
    },
    {
      "id": "AC-REQUEST-05",
      "statement": [
        {
          "type": "paragraph",
          "text": "If a store write has an unknown final outcome, return the failure without claiming success or no write and without automatic retry."
        }
      ],
      "verifies": [
        "RF-REQUEST-04"
      ]
    },
    {
      "id": "AC-REQUEST-06",
      "statement": [
        {
          "type": "paragraph",
          "text": "An empty code is refused before quantity validation and store invocation."
        }
      ],
      "verifies": [
        "RF-REQUEST-07"
      ]
    },
    {
      "id": "AC-REQUEST-SUBMIT-QUALITY",
      "statement": [
        {
          "type": "paragraph",
          "text": "In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim."
        }
      ],
      "verifies": [
        "RNF-REQUEST-01"
      ]
    }
  ],
  "traceability": [
    {
      "id": "TRC-REQUEST-01",
      "source": "RF-REQUEST-02",
      "targets": [
        "VLD-REQUEST-QUANTITY",
        "AC-REQUEST-02"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "The case applies the entity validation and states the refusal."
        }
      ]
    },
    {
      "id": "TRC-REQUEST-02",
      "source": "RF-REQUEST-03",
      "targets": [
        "OP-REQUEST-STORE",
        "AC-REQUEST-01"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "The abstract tool contract carries the persistence guarantee."
        }
      ]
    },
    {
      "id": "TRC-REQUEST-SUBMIT-ORIGIN",
      "source": "SRC-REQUEST-BRIEF",
      "targets": [
        "RF-REQUEST-01",
        "RF-REQUEST-02",
        "RF-REQUEST-03",
        "RF-REQUEST-04",
        "RF-REQUEST-05",
        "RF-REQUEST-06",
        "RF-REQUEST-07",
        "RNF-REQUEST-01"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Versioned synthetic origin for these example obligations."
        }
      ]
    }
  ],
  "assumptions": [
    "ASM-REQUEST-STORE-UNIQUE"
  ],
  "sources": [
    "SRC-REQUEST-BRIEF"
  ],
  "open_issues": [
    "OI-REQUEST-LATENCY"
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/RequestRegister/usecases/Main/UseCase_SubmitRequest.py",
    "symbol": "UseCase_SubmitRequest"
  },
  "class_kind": "use_case",
  "consumed_entities": [
    "ENT-REQUEST"
  ],
  "injected_tools": [
    {
      "abstract_tool_ref": "TOL-REQUEST-STORE",
      "operation_ref": "OP-REQUEST-STORE",
      "injected_concrete_tool_ref": "CTL-REQUEST-STORE",
      "purpose": "Retain the request after validation succeeds."
    }
  ],
  "methods": [
    {
      "name": "execute",
      "visibility": "public",
      "trigger": "The requester submits the request form.",
      "parameters": [
        {
          "name": "request_code",
          "type": "text",
          "required": true
        },
        {
          "name": "quantity",
          "type": "integer",
          "required": true
        }
      ],
      "authorization": {
        "actor_refs": [
          "ACT-REQUESTER"
        ],
        "before_effects": true
      },
      "algorithm": [
        "Start: the case receives the request and actor. If the actor is not permitted, refuse with no effects (RF-REQUEST-01).",
        "Apply VLD-REQUEST-CODE before the quantity check. An invalid code is refused without storage (RF-REQUEST-07).",
        "Apply VLD-REQUEST-QUANTITY (RF-REQUEST-02). A fail result refuses the request as invalid data.",
        "On pass, call OP-REQUEST-STORE (RF-REQUEST-03). A stored result produces the confirmed outcome (RF-REQUEST-05). STORE_UNAVAILABLE produces the store-unavailable failure (RF-REQUEST-04).",
        "DUPLICATE_CODE is the duplicate refusal with no change to the preexisting request (RF-REQUEST-06). A write failure retains its known-not-applied versus unknown distinction (RF-REQUEST-04)."
      ],
      "returns": [
        {
          "outcome_ref": "OUT-REQUEST-CONFIRMED",
          "kind": "success"
        },
        {
          "outcome_ref": "OUT-REQUEST-INVALID",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-REQUEST-DENIED",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-REQUEST-STORE-FAILURE",
          "kind": "failure"
        },
        {
          "outcome_ref": "OUT-REQUEST-DUPLICATE",
          "kind": "refusal"
        }
      ],
      "source_refs": [
        "UC-REQUEST-SUBMIT",
        "RF-REQUEST-01",
        "RF-REQUEST-02",
        "RF-REQUEST-03",
        "RF-REQUEST-04",
        "RF-REQUEST-05",
        "RF-REQUEST-06",
        "RF-REQUEST-07"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-REQUEST-SUBMIT"
  ]
}
```
