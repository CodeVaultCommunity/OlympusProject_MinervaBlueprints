---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: UC-TASK-LIST
kind: use_case
source_refs:
- UC-TASK-LIST
generation:
  mode: code
  language: python
  path: apps/TaskBoard/usecases/Main/UseCase_ListTasks.py
  symbol: UseCase_ListTasks
---

# List tasks

Observe all current Tasks in the authorized board without changing them.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "UC-TASK-LIST",
  "name": {
    "text": "List tasks"
  },
  "objective": [
    {
      "type": "paragraph",
      "text": "Observe all current Tasks in the authorized board without changing them."
    }
  ],
  "actors": [
    {
      "actor": "ACT-BOARD-MEMBER",
      "permission": {
        "text": "task.list"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Initiating actor: board member. Require the caller to be resolved to a principal with task.list for this board; a role name supplied as business input is insufficient."
        }
      ]
    }
  ],
  "trigger": [
    {
      "type": "paragraph",
      "text": "The board member (ACT-BOARD-MEMBER) requests: list tasks."
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
  "inputs": [],
  "entry_conditions": [
    {
      "type": "paragraph",
      "text": "Requests may arrive with invalid or missing authorization context; the case's denial path remains defined. No downstream effect occurs before authorization succeeds."
    }
  ],
  "entities": [
    {
      "entity": "ENT-TASK",
      "validations": [],
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
      "operation": "OP-TASK-LIST",
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
      "id": "OUT-TASK-LIST-DENIED",
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
      "id": "OUT-TASK-LIST-LISTED",
      "kind": "success",
      "description": [
        {
          "type": "paragraph",
          "text": "Return the complete ordered snapshot, including an empty list for a confirmed empty board."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No task changes."
        }
      ]
    },
    {
      "id": "OUT-TASK-LIST-STORAGE",
      "kind": "failure",
      "description": [
        {
          "type": "paragraph",
          "text": "The requested snapshot could not be obtained or contained invalid stored state."
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No task changes; no usable complete list is claimed."
        }
      ]
    }
  ],
  "functional_requirements": [
    {
      "id": "RF-TASK-LIST-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Resolve the initiating board member and require task.list for the selected board in trusted caller context. Missing, unresolved, expired, or insufficient context is denied before any entity application or tool call. No anonymous execution is permitted. Origin: SRC-TASK-BRIEF."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-LIST"
      ],
      "flow_refs": [
        "N-TASK-LIST-AUTH",
        "N-TASK-LIST-DENIED",
        "E-TASK-LIST-DENIED",
        "E-TASK-LIST-ALLOWED"
      ]
    },
    {
      "id": "RF-TASK-LIST-SNAPSHOT",
      "statement": [
        {
          "type": "paragraph",
          "text": "After authorization, call OP-TASK-LIST for the trusted board. Return every ready Task exactly once in the declared identifier order, preserving title, state, and revision. A confirmed empty snapshot is a successful empty list. Do not revalidate ready entities."
        }
      ],
      "scope": "case",
      "applies_to": [
        "UC-TASK-LIST",
        "OP-TASK-LIST"
      ],
      "flow_refs": [
        "N-TASK-LIST-READ",
        "N-TASK-LIST-RETURN",
        "E-TASK-LIST-2"
      ]
    },
    {
      "id": "RF-TASK-LIST-FAILURE",
      "statement": [
        {
          "type": "paragraph",
          "text": "Report unavailable or invalid-state retrieval as a failure, preserving its distinction. Do not return an empty or partial success and make no task changes."
        }
      ],
      "scope": "operation",
      "applies_to": [
        "UC-TASK-LIST",
        "OP-TASK-LIST"
      ],
      "flow_refs": [
        "N-TASK-LIST-FAIL",
        "E-TASK-LIST-1"
      ]
    }
  ],
  "nonfunctional_requirements": [
    {
      "id": "RNF-TASK-LIST-CONSISTENCY",
      "scope": "operation",
      "applies_to": [
        "UC-TASK-LIST",
        "OP-TASK-LIST"
      ],
      "statement": [
        {
          "type": "paragraph",
          "text": "The list represents one consistent snapshot of the authorized board. Origin: SRC-TASK-BRIEF (synthetic teaching brief)."
        }
      ],
      "criterion": [
        {
          "type": "paragraph",
          "text": "Every returned Task belongs to the same board snapshot, appears exactly once, and has mutually consistent fields/revision; no read changes a Task."
        }
      ],
      "verification": [
        {
          "type": "paragraph",
          "text": "Exercise listing alongside concurrent changes, verify against the chosen store's snapshot guarantee, and inspect before/after write counters."
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
    },
    {
      "id": "RNF-TASK-LIST-RETENTION",
      "reference_to": "RNF-TASK-CREATE-RETENTION",
      "scope": "system",
      "applies_to": [
        "UC-TASK-LIST",
        "OP-TASK-LIST"
      ],
      "references": [
        "SRC-TASK-BRIEF"
      ],
      "applicability": [
        {
          "type": "paragraph",
          "text": "The canonical confirmed-retention obligation defined in creation also applies when listing after a normal store restart."
        }
      ]
    }
  ],
  "flows": {
    "main": "GRAPH-TASK-LIST",
    "subflows": []
  },
  "flow_text": [
    {
      "type": "paragraph",
      "text": "Resolve and authorize caller context before retrieving any Task (RF-TASK-LIST-AUTH)."
    },
    {
      "type": "paragraph",
      "text": "Read one complete snapshot with OP-TASK-LIST and return the ready Tasks unchanged. An empty successful snapshot means confirmed emptiness (RF-TASK-LIST-SNAPSHOT)."
    },
    {
      "type": "paragraph",
      "text": "Report retrieval failure as failure, never as an empty or partial successful list (RF-TASK-LIST-FAILURE)."
    }
  ],
  "acceptance_criteria": [
    {
      "id": "AC-TASK-LIST-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed."
        }
      ],
      "verifies": [
        "RF-TASK-LIST-AUTH"
      ]
    },
    {
      "id": "AC-TASK-LIST-CONTENT",
      "statement": [
        {
          "type": "paragraph",
          "text": "Given open TASK002 and completed TASK001, return TASK001 then TASK002 with exact fields, once each, with no state or revision changed."
        }
      ],
      "verifies": [
        "RF-TASK-LIST-SNAPSHOT",
        "RNF-TASK-LIST-CONSISTENCY"
      ]
    },
    {
      "id": "AC-TASK-LIST-EMPTY",
      "statement": [
        {
          "type": "paragraph",
          "text": "A successful consistent read of an empty authorized board returns an empty list and changes no task state or revision; an unavailable store instead returns failure, never a falsely empty success."
        }
      ],
      "verifies": [
        "RF-TASK-LIST-SNAPSHOT",
        "RF-TASK-LIST-FAILURE",
        "RNF-TASK-LIST-CONSISTENCY"
      ]
    },
    {
      "id": "AC-TASK-LIST-INTEGRITY",
      "statement": [
        {
          "type": "paragraph",
          "text": "If hydration finds an invalid stored Task, report STORE_INVALID_STATE without publishing a partial successful list."
        }
      ],
      "verifies": [
        "RF-TASK-LIST-FAILURE"
      ]
    }
  ],
  "traceability": [
    {
      "id": "TRC-TASK-LIST-ORIGIN",
      "source": "SRC-TASK-BRIEF",
      "targets": [
        "RF-TASK-LIST-AUTH",
        "RF-TASK-LIST-SNAPSHOT",
        "RF-TASK-LIST-FAILURE",
        "RNF-TASK-LIST-CONSISTENCY",
        "RNF-TASK-LIST-RETENTION"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Synthetic requirements selected for this teaching example; not evidence of stakeholder approval."
        }
      ]
    },
    {
      "id": "TRC-TASK-LIST-AC-1",
      "source": "AC-TASK-LIST-AUTH",
      "targets": [
        "RF-TASK-LIST-AUTH"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-LIST-AC-2",
      "source": "AC-TASK-LIST-CONTENT",
      "targets": [
        "RF-TASK-LIST-SNAPSHOT",
        "RNF-TASK-LIST-CONSISTENCY"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-LIST-AC-3",
      "source": "AC-TASK-LIST-EMPTY",
      "targets": [
        "RF-TASK-LIST-SNAPSHOT",
        "RF-TASK-LIST-FAILURE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-LIST-AC-4",
      "source": "AC-TASK-LIST-INTEGRITY",
      "targets": [
        "RF-TASK-LIST-FAILURE"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "Acceptance criterion states an observable obligation, not a claim that a task application has been tested."
        }
      ]
    },
    {
      "id": "TRC-TASK-LIST-RETENTION",
      "source": "RNF-TASK-LIST-RETENTION",
      "targets": [
        "RNF-TASK-CREATE-RETENTION",
        "AC-TASK-CREATE-SUCCESS"
      ],
      "note": [
        {
          "type": "paragraph",
          "text": "One canonical integration criterion covers confirmed creation and subsequent listing after a normal restart; no duplicate full requirement is authored."
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
    "path": "apps/TaskBoard/usecases/Main/UseCase_ListTasks.py",
    "symbol": "UseCase_ListTasks"
  },
  "class_kind": "use_case",
  "consumed_entities": [
    "ENT-TASK"
  ],
  "injected_tools": [
    {
      "abstract_tool_ref": "TOL-TASK-STORE",
      "operation_ref": "OP-TASK-LIST",
      "injected_concrete_tool_ref": "CTL-TASK-STORE",
      "purpose": "Use the declared capability and handle every stated observable outcome."
    }
  ],
  "methods": [
    {
      "name": "execute",
      "visibility": "public",
      "trigger": "The board member (ACT-BOARD-MEMBER) requests: list tasks.",
      "parameters": [],
      "authorization": {
        "actor_refs": [
          "ACT-BOARD-MEMBER"
        ],
        "before_effects": true
      },
      "algorithm": [
        "Resolve and authorize caller context before retrieving any Task (RF-TASK-LIST-AUTH).",
        "Read one complete snapshot with OP-TASK-LIST and return the ready Tasks unchanged. An empty successful snapshot means confirmed emptiness (RF-TASK-LIST-SNAPSHOT).",
        "Report retrieval failure as failure, never as an empty or partial successful list (RF-TASK-LIST-FAILURE)."
      ],
      "returns": [
        {
          "outcome_ref": "OUT-TASK-LIST-DENIED",
          "kind": "refusal"
        },
        {
          "outcome_ref": "OUT-TASK-LIST-LISTED",
          "kind": "success"
        },
        {
          "outcome_ref": "OUT-TASK-LIST-STORAGE",
          "kind": "failure"
        }
      ],
      "source_refs": [
        "UC-TASK-LIST",
        "RF-TASK-LIST-AUTH",
        "RF-TASK-LIST-SNAPSHOT",
        "RF-TASK-LIST-FAILURE"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-TASK-LIST"
  ]
}
```
