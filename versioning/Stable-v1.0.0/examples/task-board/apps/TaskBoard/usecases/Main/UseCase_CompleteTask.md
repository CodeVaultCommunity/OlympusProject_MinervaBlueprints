---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: UC-TASK-COMPLETE
kind: use_case
source_refs:
- UC-TASK-COMPLETE
generation:
  mode: code
  language: python
  path: apps/TaskBoard/usecases/Main/UseCase_CompleteTask.py
  symbol: UseCase_CompleteTask
---

# Complete task

Mark an existing open Task completed without losing a competing change.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "UC-TASK-COMPLETE",
  "name": {
    "text": "Complete task"
  },
  "objective": [
    {
      "type": "paragraph",
      "text": "Mark an existing open Task completed without losing a competing change."
    }
  ],
  "actors": [
    {
      "actor": "ACT-BOARD-MEMBER",
      "permission": {
        "text": "task.complete"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Initiating actor: board member. Require the caller to be resolved to a principal with task.complete for this board; a role name supplied as business input is insufficient."
        }
      ]
    }
  ],
  "trigger": [
    {
      "type": "paragraph",
      "text": "The board member (ACT-BOARD-MEMBER) requests: complete task."
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
          "text": "Exact identifier to complete."
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
        "VLD-TASK-ID",
        "VLD-TASK-COMPLETE"
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
      "operation": "OP-TASK-LOAD",
      "purpose": [
        {
          "type": "paragraph",
          "text": "Use the declared capability and handle every stated observable outcome."
        }
      ]
    },
    {
      "tool": "TOL-TASK-STORE",
      "operation": "OP-TASK-COMPLETE",
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
      "id": "OUT-TASK-COMPLETE-DENIED",
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
      "id": "OUT-TASK-COMPLETE-COMPLETED",
      "kind": "success",
      "description": [
        {
          "type": "paragraph",
          "text": "Return the confirmed completed Task."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "Status changes once; revision increases by one, title/identifier unchanged."
        }
      ]
    },
    {
      "id": "OUT-TASK-COMPLETE-INVALID",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "Identifier is invalid."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No store access."
        }
      ]
    },
    {
      "id": "OUT-TASK-COMPLETE-MISSING",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "Task absence was confirmed at read or write time."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "This invocation makes no write."
        }
      ]
    },
    {
      "id": "OUT-TASK-COMPLETE-ALREADY",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "Task was already completed."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No completion write."
        }
      ]
    },
    {
      "id": "OUT-TASK-COMPLETE-CONFLICT",
      "kind": "refusal",
      "description": [
        {
          "type": "paragraph",
          "text": "The Task changed after the observed read."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "This invocation does not overwrite the competing change."
        }
      ]
    },
    {
      "id": "OUT-TASK-COMPLETE-STORAGE",
      "kind": "failure",
      "description": [
        {
          "type": "paragraph",
          "text": "Storage was unavailable or returned invalid stored state."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "Read failures make no change. For a write, not_applied guarantees no change and unknown leaves the final state unresolved."
        }
      ]
    }
  ],
  "functional_requirements": [
    {
      "id": "RF-TASK-COMPLETE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Resolve the initiating board member and require task.complete for the selected board in trusted caller context. Missing, unresolved, expired, or insufficient context is denied before any entity application or tool call. No anonymous execution is permitted. Origin: SRC-TASK-BRIEF."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-COMPLETE"
      ],
      "flow_refs": [
        "N-TASK-COMPLETE-AUTH",
        "N-TASK-COMPLETE-DENIED",
        "E-TASK-COMPLETE-DENIED",
        "E-TASK-COMPLETE-ALLOWED"
      ]
    },
    {
      "id": "RF-TASK-COMPLETE-ID",
      "statement": [
        {
          "type": "paragraph",
          "text": "After authorization, apply VLD-TASK-ID to the supplied identifier; refuse invalid input before tool access."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-COMPLETE"
      ],
      "flow_refs": [
        "N-TASK-COMPLETE-ID",
        "N-TASK-COMPLETE-VALID",
        "N-TASK-COMPLETE-INVALID",
        "E-TASK-COMPLETE-2"
      ]
    },
    {
      "id": "RF-TASK-COMPLETE-LOAD",
      "statement": [
        {
          "type": "paragraph",
          "text": "Read a ready Task and its observed revision with OP-TASK-LOAD. A confirmed NOT_FOUND is a refusal without write, distinct from unavailable or malformed storage."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-TASK-COMPLETE",
        "OP-TASK-LOAD"
      ],
      "flow_refs": [
        "N-TASK-COMPLETE-LOAD",
        "N-TASK-COMPLETE-MISSING",
        "E-TASK-COMPLETE-3",
        "E-TASK-COMPLETE-4"
      ]
    },
    {
      "id": "RF-TASK-COMPLETE-TRANSITION",
      "statement": [
        {
          "type": "paragraph",
          "text": "Apply VLD-TASK-COMPLETE to the ready Task's current state. If already completed, refuse without writing. Otherwise produce a ready completed Task preserving identifier/title; do not repeat validation of its established invariants."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-COMPLETE"
      ],
      "flow_refs": [
        "N-TASK-COMPLETE-TRANSITION",
        "N-TASK-COMPLETE-ALLOWED",
        "N-TASK-COMPLETE-ALREADY",
        "E-TASK-COMPLETE-6",
        "E-TASK-COMPLETE-8"
      ]
    },
    {
      "id": "RF-TASK-COMPLETE-WRITE",
      "statement": [
        {
          "type": "paragraph",
          "text": "Call OP-TASK-COMPLETE with the completed Task and observed revision. Confirm only its successful result. NOT_FOUND or VERSION_CONFLICT refuses with no write by this operation; never overwrite a competing change."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-TASK-COMPLETE",
        "OP-TASK-COMPLETE"
      ],
      "flow_refs": [
        "N-TASK-COMPLETE-MISSING",
        "N-TASK-COMPLETE-STORE",
        "N-TASK-COMPLETE-CONFLICT",
        "N-TASK-COMPLETE-DONE",
        "E-TASK-COMPLETE-9",
        "E-TASK-COMPLETE-10",
        "E-TASK-COMPLETE-11",
        "E-TASK-COMPLETE-13"
      ]
    },
    {
      "id": "RF-TASK-COMPLETE-FAILURE",
      "statement": [
        {
          "type": "paragraph",
          "text": "Propagate read unavailable/invalid-state failures without a write. On a write's STORE_UNAVAILABLE preserve not_applied versus unknown; do not claim completion or retry automatically."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-TASK-COMPLETE",
        "OP-TASK-LOAD",
        "OP-TASK-COMPLETE"
      ],
      "flow_refs": [
        "N-TASK-COMPLETE-ERROR",
        "E-TASK-COMPLETE-5",
        "E-TASK-COMPLETE-12"
      ]
    }
  ],
  "nonfunctional_requirements": [
    {
      "id": "RNF-TASK-COMPLETE-ATOMICITY",
      "scope": "operation",
      "applies_to": [
        "UC-TASK-COMPLETE",
        "OP-TASK-COMPLETE"
      ],
      "statement": [
        {
          "type": "paragraph",
          "text": "Concurrent completion must not lose an update or report two writes for the same observed revision. Origin: SRC-TASK-BRIEF (synthetic teaching brief)."
        }
      ],
      "criterion": [
        {
          "type": "paragraph",
          "text": "For two conditional writes using the same observed revision, at most one is confirmed; the other returns conflict or an accurately classified failure."
        }
      ],
      "verification": [
        {
          "type": "paragraph",
          "text": "Coordinate concurrent attempts at the conditional-write boundary and inspect confirmed revisions and outcomes."
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
    "main": "GRAPH-TASK-COMPLETE",
    "subflows": []
  },
  "flow_text": [
    {
      "type": "paragraph",
      "text": "Authorize trusted caller context first (RF-TASK-COMPLETE-AUTH). Validate the identifier, then load a ready Task (RF-TASK-COMPLETE-ID, RF-TASK-COMPLETE-LOAD)."
    },
    {
      "type": "paragraph",
      "text": "Refuse a confirmed absence; report a read failure without attempting a write. Apply the entity's transition to the ready Task; refuse already-completed state (RF-TASK-COMPLETE-TRANSITION)."
    },
    {
      "type": "paragraph",
      "text": "Conditionally retain the completed Task with its observed revision. Distinguish success, concurrent conflict, confirmed absence, and unavailable-write outcome (RF-TASK-COMPLETE-WRITE, RF-TASK-COMPLETE-FAILURE)."
    }
  ],
  "acceptance_criteria": [
    {
      "id": "AC-TASK-COMPLETE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-AUTH"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-SUCCESS",
      "statement": [
        {
          "type": "paragraph",
          "text": "For TASK001 open at revision zero, completion returns the same identifier/title, completed status and revision one; later listing reflects that state."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-TRANSITION",
        "RF-TASK-COMPLETE-WRITE"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-MISSING",
      "statement": [
        {
          "type": "paragraph",
          "text": "A confirmed absent identifier produces not-found without calling OP-TASK-COMPLETE."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-LOAD"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-INVALID",
      "statement": [
        {
          "type": "paragraph",
          "text": "An empty or whitespace-only identifier is refused before load or completion tools are invoked."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-ID"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-ALREADY",
      "statement": [
        {
          "type": "paragraph",
          "text": "A ready completed Task produces already-completed refusal and no write; its revision remains unchanged."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-TRANSITION"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-CONFLICT",
      "statement": [
        {
          "type": "paragraph",
          "text": "Change the retained revision between load and completion. Return VERSION_CONFLICT, preserving the competing state."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-WRITE",
        "RNF-TASK-COMPLETE-ATOMICITY"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-UNKNOWN",
      "statement": [
        {
          "type": "paragraph",
          "text": "Lose the completion confirmation after issuing a write. Return unknown without success/no-change claims or automatic retry."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-FAILURE"
      ]
    }
  ],
  "traceability": [
    {
      "id": "TRC-TASK-COMPLETE-ORIGIN",
      "source": "SRC-TASK-BRIEF",
      "targets": [
        "RF-TASK-COMPLETE-AUTH",
        "RF-TASK-COMPLETE-ID",
        "RF-TASK-COMPLETE-LOAD",
        "RF-TASK-COMPLETE-TRANSITION",
        "RF-TASK-COMPLETE-WRITE",
        "RF-TASK-COMPLETE-FAILURE",
        "RNF-TASK-COMPLETE-ATOMICITY"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Synthetic requirements selected for this teaching example; not evidence of stakeholder approval."
        }
      ]
    },
    {
      "id": "TRC-TASK-COMPLETE-AC-1",
      "source": "AC-TASK-COMPLETE-AUTH",
      "targets": [
        "RF-TASK-COMPLETE-AUTH"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-COMPLETE-AC-2",
      "source": "AC-TASK-COMPLETE-SUCCESS",
      "targets": [
        "RF-TASK-COMPLETE-TRANSITION",
        "RF-TASK-COMPLETE-WRITE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-COMPLETE-AC-3",
      "source": "AC-TASK-COMPLETE-MISSING",
      "targets": [
        "RF-TASK-COMPLETE-LOAD"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-COMPLETE-AC-4",
      "source": "AC-TASK-COMPLETE-INVALID",
      "targets": [
        "RF-TASK-COMPLETE-ID"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-COMPLETE-AC-5",
      "source": "AC-TASK-COMPLETE-ALREADY",
      "targets": [
        "RF-TASK-COMPLETE-TRANSITION"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-COMPLETE-AC-6",
      "source": "AC-TASK-COMPLETE-CONFLICT",
      "targets": [
        "RF-TASK-COMPLETE-WRITE",
        "RNF-TASK-COMPLETE-ATOMICITY"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-COMPLETE-AC-7",
      "source": "AC-TASK-COMPLETE-UNKNOWN",
      "targets": [
        "RF-TASK-COMPLETE-FAILURE"
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
    "path": "apps/TaskBoard/usecases/Main/UseCase_CompleteTask.py",
    "symbol": "UseCase_CompleteTask"
  },
  "class_kind": "use_case",
  "consumed_entities": [
    "ENT-TASK"
  ],
  "injected_tools": [
    {
      "abstract_tool_ref": "TOL-TASK-STORE",
      "operation_ref": "OP-TASK-LOAD",
      "injected_concrete_tool_ref": "CTL-TASK-STORE",
      "purpose": "Use the declared capability and handle every stated observable outcome."
    },
    {
      "abstract_tool_ref": "TOL-TASK-STORE",
      "operation_ref": "OP-TASK-COMPLETE",
      "injected_concrete_tool_ref": "CTL-TASK-STORE",
      "purpose": "Use the declared capability and handle every stated observable outcome."
    }
  ],
  "methods": [
    {
      "name": "execute",
      "visibility": "public",
      "trigger": "The board member (ACT-BOARD-MEMBER) requests: complete task.",
      "parameters": [
        {
          "name": "task_identifier",
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
        "Authorize trusted caller context first (RF-TASK-COMPLETE-AUTH). Validate the identifier, then load a ready Task (RF-TASK-COMPLETE-ID, RF-TASK-COMPLETE-LOAD).",
        "Refuse a confirmed absence; report a read failure without attempting a write. Apply the entity's transition to the ready Task; refuse already-completed state (RF-TASK-COMPLETE-TRANSITION).",
        "Conditionally retain the completed Task with its observed revision. Distinguish success, concurrent conflict, confirmed absence, and unavailable-write outcome (RF-TASK-COMPLETE-WRITE, RF-TASK-COMPLETE-FAILURE)."
      ],
      "returns": [
        {
          "outcome_ref": "OUT-TASK-COMPLETE-DENIED",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-COMPLETE-COMPLETED",
          "kind": "success"
        },
        {
          "outcome_ref": "OUT-TASK-COMPLETE-INVALID",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-COMPLETE-MISSING",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-COMPLETE-ALREADY",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-COMPLETE-CONFLICT",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-COMPLETE-STORAGE",
          "kind": "failure"
        }
      ],
      "source_refs": [
        "UC-TASK-COMPLETE",
        "RF-TASK-COMPLETE-AUTH",
        "RF-TASK-COMPLETE-ID",
        "RF-TASK-COMPLETE-LOAD",
        "RF-TASK-COMPLETE-TRANSITION",
        "RF-TASK-COMPLETE-WRITE",
        "RF-TASK-COMPLETE-FAILURE"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-TASK-COMPLETE"
  ]
}
```
