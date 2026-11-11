---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: BND-TASK-ILLUSTRATION
kind: boundary
source_refs:
- BND-TASK-ILLUSTRATION
generation:
  mode: code
  language: python
  path: apps/TaskBoard/boundaries/Boundary_ChannelIndependentInteractionIllustration.py
  symbol: Boundary_ChannelIndependentInteractionIllustration
---

# Channel-independent interaction illustration

Origin: SRC-TASK-BRIEF. This is an illustrative mapping of domain inputs/outcomes. A later solution may select an L4 channel; such a selection must not retroactively become a stakeholder L1 requirement.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "BND-TASK-ILLUSTRATION",
  "name": {
    "text": "Channel-independent interaction illustration"
  },
  "modality": "other",
  "purpose": [
    {
      "type": "paragraph",
      "text": "Origin: SRC-TASK-BRIEF. This is an illustrative mapping of domain inputs/outcomes. A later solution may select an L4 channel; such a selection must not retroactively become a stakeholder L1 requirement."
    }
  ],
  "audience": [
    {
      "type": "paragraph",
      "text": "Authorized board members."
    }
  ],
  "interactions": [
    {
      "id": "INT-TASK-CREATE",
      "name": {
        "text": "Create task"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Illustrative interaction mapping only. No web route, screen, command syntax, or protocol is a normative L1 requirement."
        }
      ],
      "use_case": "UC-TASK-CREATE",
      "trigger": [
        {
          "type": "paragraph",
          "text": "The board member (ACT-BOARD-MEMBER) requests: create task."
        }
      ],
      "input_mapping": [
        {
          "source": "request.task_identifier",
          "target": "UC-TASK-CREATE.input.task_identifier",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Requested stable task identifier."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "request.task_identifier",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-TASK-CREATE",
            "selector": "task_identifier",
            "value_type": "text"
          }
        },
        {
          "source": "request.title",
          "target": "UC-TASK-CREATE.input.title",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The work to remember."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "request.title",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-TASK-CREATE",
            "selector": "title",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-TASK-CREATE-DENIED",
          "target": "result.out-task-create-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The caller context is absent, unresolved, expired, or lacks this case's permission for this board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-CREATED",
          "target": "result.out-task-create-created",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The retained Task is returned."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-CREATED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-created",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-INVALID",
          "target": "result.out-task-create-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The new-task validity rule failed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-DUPLICATE",
          "target": "result.out-task-create-duplicate",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The identifier was already retained."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-DUPLICATE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-duplicate",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-UNAVAILABLE",
          "target": "result.out-task-create-unavailable",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Storage did not confirm creation; report write_outcome."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-UNAVAILABLE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-unavailable",
            "value_type": "outcome"
          }
        }
      ],
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH",
        "RF-TASK-CREATE-DATA",
        "RF-TASK-CREATE-RETAIN",
        "RF-TASK-CREATE-DUPLICATE",
        "RF-TASK-CREATE-FAILURE"
      ],
      "resources": [],
      "examples": []
    },
    {
      "id": "INT-TASK-COMPLETE",
      "name": {
        "text": "Complete task"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Illustrative interaction mapping only. No web route, screen, command syntax, or protocol is a normative L1 requirement."
        }
      ],
      "use_case": "UC-TASK-COMPLETE",
      "trigger": [
        {
          "type": "paragraph",
          "text": "The board member (ACT-BOARD-MEMBER) requests: complete task."
        }
      ],
      "input_mapping": [
        {
          "source": "request.task_identifier",
          "target": "UC-TASK-COMPLETE.input.task_identifier",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Exact identifier to complete."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "request.task_identifier",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-TASK-COMPLETE",
            "selector": "task_identifier",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-TASK-COMPLETE-DENIED",
          "target": "result.out-task-complete-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The caller context is absent, unresolved, expired, or lacks this case's permission for this board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-COMPLETED",
          "target": "result.out-task-complete-completed",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Return the confirmed completed Task."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-COMPLETED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-completed",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-INVALID",
          "target": "result.out-task-complete-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Identifier is invalid."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-MISSING",
          "target": "result.out-task-complete-missing",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Task absence was confirmed at read or write time."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-MISSING",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-missing",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-ALREADY",
          "target": "result.out-task-complete-already",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Task was already completed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-ALREADY",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-already",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-CONFLICT",
          "target": "result.out-task-complete-conflict",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The Task changed after the observed read."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-CONFLICT",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-conflict",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-STORAGE",
          "target": "result.out-task-complete-storage",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Storage was unavailable or returned invalid stored state."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-STORAGE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-storage",
            "value_type": "outcome"
          }
        }
      ],
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH",
        "RF-TASK-COMPLETE-ID",
        "RF-TASK-COMPLETE-LOAD",
        "RF-TASK-COMPLETE-TRANSITION",
        "RF-TASK-COMPLETE-WRITE",
        "RF-TASK-COMPLETE-FAILURE"
      ],
      "resources": [],
      "examples": []
    },
    {
      "id": "INT-TASK-LIST",
      "name": {
        "text": "List tasks"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Illustrative interaction mapping only. No web route, screen, command syntax, or protocol is a normative L1 requirement."
        }
      ],
      "use_case": "UC-TASK-LIST",
      "trigger": [
        {
          "type": "paragraph",
          "text": "The board member (ACT-BOARD-MEMBER) requests: list tasks."
        }
      ],
      "input_mapping": [],
      "result_mapping": [
        {
          "source": "OUT-TASK-LIST-DENIED",
          "target": "result.out-task-list-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The caller context is absent, unresolved, expired, or lacks this case's permission for this board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-LIST-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-LIST",
            "selector": "result.out-task-list-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-LIST-LISTED",
          "target": "result.out-task-list-listed",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Return the complete ordered snapshot, including an empty list for a confirmed empty board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-LIST-LISTED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-LIST",
            "selector": "result.out-task-list-listed",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-LIST-STORAGE",
          "target": "result.out-task-list-storage",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The requested snapshot could not be obtained or contained invalid stored state."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-LIST-STORAGE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-LIST",
            "selector": "result.out-task-list-storage",
            "value_type": "outcome"
          }
        }
      ],
      "requirement_refs": [
        "RF-TASK-LIST-AUTH",
        "RF-TASK-LIST-SNAPSHOT",
        "RF-TASK-LIST-FAILURE"
      ],
      "resources": [],
      "examples": []
    }
  ],
  "assumptions": [],
  "sources": [
    "SRC-TASK-BRIEF"
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
    "path": "apps/TaskBoard/boundaries/Boundary_ChannelIndependentInteractionIllustration.py",
    "symbol": "Boundary_ChannelIndependentInteractionIllustration"
  },
  "class_kind": "boundary_adapter",
  "boundary_semantics": "Interaction interface only; never a test case or observation point.",
  "classification": "illustration",
  "modality": "other",
  "methods": [
    {
      "name": "create_task",
      "exposes_use_case": "UC-TASK-CREATE",
      "trigger": "The board member (ACT-BOARD-MEMBER) requests: create task.",
      "input_mapping": [
        {
          "source": "request.task_identifier",
          "target": "UC-TASK-CREATE.input.task_identifier",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Requested stable task identifier."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "request.task_identifier",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-TASK-CREATE",
            "selector": "task_identifier",
            "value_type": "text"
          }
        },
        {
          "source": "request.title",
          "target": "UC-TASK-CREATE.input.title",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The work to remember."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "request.title",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-TASK-CREATE",
            "selector": "title",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-TASK-CREATE-DENIED",
          "target": "result.out-task-create-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The caller context is absent, unresolved, expired, or lacks this case's permission for this board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-CREATED",
          "target": "result.out-task-create-created",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The retained Task is returned."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-CREATED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-created",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-INVALID",
          "target": "result.out-task-create-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The new-task validity rule failed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-DUPLICATE",
          "target": "result.out-task-create-duplicate",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The identifier was already retained."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-DUPLICATE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-duplicate",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-CREATE-UNAVAILABLE",
          "target": "result.out-task-create-unavailable",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Storage did not confirm creation; report write_outcome."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-CREATE-UNAVAILABLE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-CREATE",
            "selector": "result.out-task-create-unavailable",
            "value_type": "outcome"
          }
        }
      ],
      "source_refs": [
        "INT-TASK-CREATE",
        "RF-TASK-CREATE-AUTH",
        "RF-TASK-CREATE-DATA",
        "RF-TASK-CREATE-RETAIN",
        "RF-TASK-CREATE-DUPLICATE",
        "RF-TASK-CREATE-FAILURE"
      ]
    },
    {
      "name": "complete_task",
      "exposes_use_case": "UC-TASK-COMPLETE",
      "trigger": "The board member (ACT-BOARD-MEMBER) requests: complete task.",
      "input_mapping": [
        {
          "source": "request.task_identifier",
          "target": "UC-TASK-COMPLETE.input.task_identifier",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Exact identifier to complete."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "request.task_identifier",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-TASK-COMPLETE",
            "selector": "task_identifier",
            "value_type": "text"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-TASK-COMPLETE-DENIED",
          "target": "result.out-task-complete-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The caller context is absent, unresolved, expired, or lacks this case's permission for this board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-COMPLETED",
          "target": "result.out-task-complete-completed",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Return the confirmed completed Task."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-COMPLETED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-completed",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-INVALID",
          "target": "result.out-task-complete-invalid",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Identifier is invalid."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-invalid",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-MISSING",
          "target": "result.out-task-complete-missing",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Task absence was confirmed at read or write time."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-MISSING",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-missing",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-ALREADY",
          "target": "result.out-task-complete-already",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Task was already completed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-ALREADY",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-already",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-CONFLICT",
          "target": "result.out-task-complete-conflict",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The Task changed after the observed read."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-CONFLICT",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-conflict",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-COMPLETE-STORAGE",
          "target": "result.out-task-complete-storage",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Storage was unavailable or returned invalid stored state."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-COMPLETE-STORAGE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-COMPLETE",
            "selector": "result.out-task-complete-storage",
            "value_type": "outcome"
          }
        }
      ],
      "source_refs": [
        "INT-TASK-COMPLETE",
        "RF-TASK-COMPLETE-AUTH",
        "RF-TASK-COMPLETE-ID",
        "RF-TASK-COMPLETE-LOAD",
        "RF-TASK-COMPLETE-TRANSITION",
        "RF-TASK-COMPLETE-WRITE",
        "RF-TASK-COMPLETE-FAILURE"
      ]
    },
    {
      "name": "list_tasks",
      "exposes_use_case": "UC-TASK-LIST",
      "trigger": "The board member (ACT-BOARD-MEMBER) requests: list tasks.",
      "input_mapping": [],
      "result_mapping": [
        {
          "source": "OUT-TASK-LIST-DENIED",
          "target": "result.out-task-list-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The caller context is absent, unresolved, expired, or lacks this case's permission for this board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-LIST-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-LIST",
            "selector": "result.out-task-list-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-LIST-LISTED",
          "target": "result.out-task-list-listed",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Return the complete ordered snapshot, including an empty list for a confirmed empty board."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-LIST-LISTED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-LIST",
            "selector": "result.out-task-list-listed",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-TASK-LIST-STORAGE",
          "target": "result.out-task-list-storage",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The requested snapshot could not be obtained or contained invalid stored state."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-TASK-LIST-STORAGE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-TASK-LIST",
            "selector": "result.out-task-list-storage",
            "value_type": "outcome"
          }
        }
      ],
      "source_refs": [
        "INT-TASK-LIST",
        "RF-TASK-LIST-AUTH",
        "RF-TASK-LIST-SNAPSHOT",
        "RF-TASK-LIST-FAILURE"
      ]
    }
  ]
}
```
