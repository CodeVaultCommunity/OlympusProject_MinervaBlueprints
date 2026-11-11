---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: UC-TASK-CREATE
kind: use_case
source_refs:
- UC-TASK-CREATE
generation:
  mode: code
  language: python
  path: apps/TaskBoard/usecases/Main/UseCase_CreateTask.py
  symbol: UseCase_CreateTask
---

# Create task

Remember one new unit of work in the board.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "UC-TASK-CREATE",
  "name": {
    "text": "Create task"
  },
  "objective": [
    {
      "type": "paragraph",
      "text": "Remember one new unit of work in the board."
    }
  ],
  "actors": [
    {
      "actor": "ACT-BOARD-MEMBER",
      "permission": {
        "text": "task.create"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Initiating actor: board member. Require the caller to be resolved to a principal with task.create for this board; a role name supplied as business input is insufficient."
        }
      ]
    }
  ],
  "trigger": [
    {
      "type": "paragraph",
      "text": "The board member (ACT-BOARD-MEMBER) requests: create task."
    }
  ],
  "context": [
    {
      "type": "paragraph",
      "text": "Required caller context: resolved principal identifier, selected board identifier, authenticated status, granted case permissions, issuer, and validity status. The context originates from a trusted identity-and-permission authority configured for the application; claims in the task request are untrusted and cannot supply authorization."
    },
    {
      "type": "paragraph",
      "text": "The trust assumption is ASM-TASK-IDENTITY. Authentication is required; its mechanism and token/channel encoding belong to later design. Authorization is reevaluated for this invocation, and composed invocations would preserve the same principal and board context."
    },
    {
      "type": "paragraph",
      "text": "The actor is a role. The caller is the concrete principal for this request. Neither is an accountable human author for a Needs-to-L1 derivation."
    }
  ],
  "inputs": [
    {
      "name": {
        "text": "Task identifier"
      },
      "type": "text",
      "meaning": [
        {
          "type": "paragraph",
          "text": "Requested stable task identifier."
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
          "text": "The work to remember."
        }
      ],
      "required": true
    }
  ],
  "entry_conditions": [
    {
      "type": "paragraph",
      "text": "Requests may arrive with invalid or missing authorization context; the case's denial path remains defined. No downstream effect occurs before authorization succeeds."
    }
  ],
  "entities": [
    {
      "entity": "ENT-TASK",
      "validations": [
        "VLD-TASK-NEW"
      ],
      "purpose": [
        {
          "type": "paragraph",
          "text": "Use the canonical Task meaning and rules. Tools receive ready entities; no repeated validation of ready entity invariants is required."
        }
      ]
    }
  ],
  "tools": [
    {
      "tool": "TOL-TASK-STORE",
      "operation": "OP-TASK-CREATE",
      "purpose": [
        {
          "type": "paragraph",
          "text": "Use the declared capability and handle every stated observable outcome."
        }
      ]
    }
  ],
  "calls": [],
  "outcomes": [
    {
      "id": "OUT-TASK-CREATE-DENIED",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The caller context is absent, unresolved, expired, or lacks this case's permission for this board."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No tool call, no write, and no disclosure of task existence or content."
        }
      ]
    },
    {
      "id": "OUT-TASK-CREATE-CREATED",
      "kind": "success",
      "description": [
        {
          "type": "paragraph",
          "text": "The retained Task is returned."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "Exactly one open Task at revision zero is retained."
        }
      ]
    },
    {
      "id": "OUT-TASK-CREATE-INVALID",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The new-task validity rule failed."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No store invocation or state change."
        }
      ]
    },
    {
      "id": "OUT-TASK-CREATE-DUPLICATE",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The identifier was already retained."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No change to that Task."
        }
      ]
    },
    {
      "id": "OUT-TASK-CREATE-UNAVAILABLE",
      "kind": "failure",
      "description": [
        {
          "type": "paragraph",
          "text": "Storage did not confirm creation; report write_outcome."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "not_applied guarantees no write; unknown leaves final retention state unresolved."
        }
      ]
    }
  ],
  "functional_requirements": [
    {
      "id": "RF-TASK-CREATE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Resolve the initiating board member and require task.create for the selected board in trusted caller context. Missing, unresolved, expired, or insufficient context is denied before any entity application or tool call. No anonymous execution is permitted. Origin: SRC-TASK-BRIEF."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-CREATE"
      ],
      "flow_refs": [
        "N-TASK-CREATE-AUTH",
        "N-TASK-CREATE-DENIED",
        "E-TASK-CREATE-DENIED",
        "E-TASK-CREATE-ALLOWED"
      ]
    },
    {
      "id": "RF-TASK-CREATE-DATA",
      "statement": [
        {
          "type": "paragraph",
          "text": "After authorization, construct a new Task from task_id and title with status open and revision zero, applying VLD-TASK-NEW. An invalid candidate is refused before storage; preserve input text exactly."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-CREATE"
      ],
      "flow_refs": [
        "N-TASK-CREATE-VALIDATE",
        "N-TASK-CREATE-VALID",
        "N-TASK-CREATE-INVALID",
        "E-TASK-CREATE-2"
      ]
    },
    {
      "id": "RF-TASK-CREATE-RETAIN",
      "statement": [
        {
          "type": "paragraph",
          "text": "Pass the ready Task and authorized board to OP-TASK-CREATE once. Only a confirmed result returns the retained identifier, title, open status, and revision zero."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-TASK-CREATE",
        "OP-TASK-CREATE"
      ],
      "flow_refs": [
        "N-TASK-CREATE-STORE",
        "N-TASK-CREATE-CREATED",
        "E-TASK-CREATE-3",
        "E-TASK-CREATE-6"
      ]
    },
    {
      "id": "RF-TASK-CREATE-DUPLICATE",
      "statement": [
        {
          "type": "paragraph",
          "text": "Map DUPLICATE_ID to duplicate-identifier refusal. Preserve the existing Task and do not choose a replacement identifier silently."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-CREATE"
      ],
      "flow_refs": [
        "N-TASK-CREATE-DUPLICATE",
        "E-TASK-CREATE-4"
      ]
    },
    {
      "id": "RF-TASK-CREATE-FAILURE",
      "statement": [
        {
          "type": "paragraph",
          "text": "On STORE_UNAVAILABLE, report write_outcome supplied by the tool. Distinguish not_applied from unknown; never infer no change or success from an absent confirmation and do not retry automatically."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-TASK-CREATE",
        "OP-TASK-CREATE"
      ],
      "flow_refs": [
        "N-TASK-CREATE-UNAVAILABLE",
        "E-TASK-CREATE-5"
      ]
    }
  ],
  "nonfunctional_requirements": [
    {
      "id": "RNF-TASK-CREATE-RETENTION",
      "scope": "system",
      "applies_to": [
        "UC-TASK-CREATE",
        "OP-TASK-CREATE",
        "UC-TASK-LIST"
      ],
      "statement": [
        {
          "type": "paragraph",
          "text": "A confirmed creation remains readable after a normal store restart. Origin: SRC-TASK-BRIEF (synthetic teaching brief)."
        }
      ],
      "criterion": [
        {
          "type": "paragraph",
          "text": "After a confirmed create and normal restart, a successful list returns the Task with unchanged fields exactly once."
        }
      ],
      "verification": [
        {
          "type": "paragraph",
          "text": "Exercise create, restart the chosen persistence implementation normally, then list. This repository supplies the contract, not that implementation."
        }
      ],
      "references": [
        "SRC-TASK-BRIEF"
      ],
      "applicability": [
        {
          "type": "paragraph",
          "text": "Applies under the explicitly stated case and tool conditions. This is an obligation for a future implementation, not a measured claim about this repository."
        }
      ]
    }
  ],
  "flows": {
    "main": "GRAPH-TASK-CREATE",
    "subflows": []
  },
  "flow_text": [
    {
      "type": "paragraph",
      "text": "Resolve trusted context first. Deny missing, unresolved, expired, or insufficient permission before validation and storage (RF-TASK-CREATE-AUTH)."
    },
    {
      "type": "paragraph",
      "text": "Apply VLD-TASK-NEW to input data once. Refuse invalid input without tool access (RF-TASK-CREATE-DATA)."
    },
    {
      "type": "paragraph",
      "text": "Pass the ready Task to OP-TASK-CREATE. Confirm only on its success; map duplicate and unavailable outcomes explicitly (RF-TASK-CREATE-RETAIN, RF-TASK-CREATE-DUPLICATE, RF-TASK-CREATE-FAILURE)."
    }
  ],
  "acceptance_criteria": [
    {
      "id": "AC-TASK-CREATE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-AUTH"
      ]
    },
    {
      "id": "AC-TASK-CREATE-SUCCESS",
      "statement": [
        {
          "type": "paragraph",
          "text": "With trusted create permission and unused TASK001 / Review Atlas, receive the exact open Task at revision zero; a later successful list includes it once."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-DATA",
        "RF-TASK-CREATE-RETAIN",
        "RNF-TASK-CREATE-RETENTION"
      ]
    },
    {
      "id": "AC-TASK-CREATE-INVALID",
      "statement": [
        {
          "type": "paragraph",
          "text": "An empty title or whitespace-only identifier is refused before OP-TASK-CREATE is invoked."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-DATA"
      ]
    },
    {
      "id": "AC-TASK-CREATE-DUPLICATE",
      "statement": [
        {
          "type": "paragraph",
          "text": "Creating TASK001 twice retains the first Task unchanged and returns duplicate-identifier refusal on the second attempt."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-DUPLICATE"
      ]
    },
    {
      "id": "AC-TASK-CREATE-UNKNOWN",
      "statement": [
        {
          "type": "paragraph",
          "text": "Inject a write with lost confirmation. The case reports unknown; it does not claim no write, report success, or initiate a retry."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-FAILURE"
      ]
    }
  ],
  "traceability": [
    {
      "id": "TRC-TASK-CREATE-ORIGIN",
      "source": "SRC-TASK-BRIEF",
      "targets": [
        "RF-TASK-CREATE-AUTH",
        "RF-TASK-CREATE-DATA",
        "RF-TASK-CREATE-RETAIN",
        "RF-TASK-CREATE-DUPLICATE",
        "RF-TASK-CREATE-FAILURE",
        "RNF-TASK-CREATE-RETENTION"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Synthetic requirements selected for this teaching example; not evidence of stakeholder approval."
        }
      ]
    },
    {
      "id": "TRC-TASK-CREATE-AC-1",
      "source": "AC-TASK-CREATE-AUTH",
      "targets": [
        "RF-TASK-CREATE-AUTH"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-CREATE-AC-2",
      "source": "AC-TASK-CREATE-SUCCESS",
      "targets": [
        "RF-TASK-CREATE-DATA",
        "RF-TASK-CREATE-RETAIN",
        "RNF-TASK-CREATE-RETENTION"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-CREATE-AC-3",
      "source": "AC-TASK-CREATE-INVALID",
      "targets": [
        "RF-TASK-CREATE-DATA"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-CREATE-AC-4",
      "source": "AC-TASK-CREATE-DUPLICATE",
      "targets": [
        "RF-TASK-CREATE-DUPLICATE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-CREATE-AC-5",
      "source": "AC-TASK-CREATE-UNKNOWN",
      "targets": [
        "RF-TASK-CREATE-FAILURE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    }
  ],
  "assumptions": [
    "ASM-TASK-SINGLE-BOARD",
    "ASM-TASK-IDENTITY"
  ],
  "sources": [
    "SRC-TASK-BRIEF",
    "SRC-TASK-OAL"
  ],
  "open_issues": []
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/TaskBoard/usecases/Main/UseCase_CreateTask.py",
    "symbol": "UseCase_CreateTask"
  },
  "class_kind": "use_case",
  "consumed_entities": [
    "ENT-TASK"
  ],
  "injected_tools": [
    {
      "abstract_tool_ref": "TOL-TASK-STORE",
      "operation_ref": "OP-TASK-CREATE",
      "injected_concrete_tool_ref": "CTL-TASK-STORE",
      "purpose": "Use the declared capability and handle every stated observable outcome."
    }
  ],
  "methods": [
    {
      "name": "execute",
      "visibility": "public",
      "trigger": "The board member (ACT-BOARD-MEMBER) requests: create task.",
      "parameters": [
        {
          "name": "task_identifier",
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
          "ACT-BOARD-MEMBER"
        ],
        "before_effects": true
      },
      "algorithm": [
        "Resolve trusted context first. Deny missing, unresolved, expired, or insufficient permission before validation and storage (RF-TASK-CREATE-AUTH).",
        "Apply VLD-TASK-NEW to input data once. Refuse invalid input without tool access (RF-TASK-CREATE-DATA).",
        "Pass the ready Task to OP-TASK-CREATE. Confirm only on its success; map duplicate and unavailable outcomes explicitly (RF-TASK-CREATE-RETAIN, RF-TASK-CREATE-DUPLICATE, RF-TASK-CREATE-FAILURE)."
      ],
      "returns": [
        {
          "outcome_ref": "OUT-TASK-CREATE-DENIED",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-CREATE-CREATED",
          "kind": "success"
        },
        {
          "outcome_ref": "OUT-TASK-CREATE-INVALID",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-CREATE-DUPLICATE",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-CREATE-UNAVAILABLE",
          "kind": "failure"
        }
      ],
      "source_refs": [
        "UC-TASK-CREATE",
        "RF-TASK-CREATE-AUTH",
        "RF-TASK-CREATE-DATA",
        "RF-TASK-CREATE-RETAIN",
        "RF-TASK-CREATE-DUPLICATE",
        "RF-TASK-CREATE-FAILURE"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-TASK-CREATE"
  ]
}
```
