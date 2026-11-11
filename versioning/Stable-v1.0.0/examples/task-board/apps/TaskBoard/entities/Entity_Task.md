---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: ENT-TASK
kind: entity
source_refs:
- ENT-TASK
generation:
  mode: code
  language: python
  path: apps/TaskBoard/entities/Entity_Task.py
  symbol: Entity_Task
---

# Task

Preserves Atlas entity ENT-TASK.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "ENT-TASK",
  "name": {
    "text": "Task"
  },
  "meaning": [
    {
      "type": "paragraph",
      "text": "A unit of work retained in one board. Its identity and title survive completion. The entity owns data validity and state-transition rules; it has no tool or use-case dependency."
    }
  ],
  "identity": {
    "description": [
      {
        "type": "paragraph",
        "text": "Tasks with exactly equal task identifiers in the same board are the same task."
      }
    ],
    "fields": [
      "FLD-TASK-ID"
    ]
  },
  "fields": [
    {
      "id": "FLD-TASK-ID",
      "name": {
        "text": "Task identifier"
      },
      "type": "text",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "Identity within this board."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "Non-empty, non-whitespace text; equality is exact and case-sensitive."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "TASK001"
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
      "id": "FLD-TASK-TITLE",
      "name": {
        "text": "Title"
      },
      "type": "text",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "The work to be remembered."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "At least one non-whitespace character; retain the original text."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "Review Atlas"
          }
        ],
        "invalid": [
          {
            "text": ""
          }
        ]
      }
    },
    {
      "id": "FLD-TASK-STATUS",
      "name": {
        "text": "Status"
      },
      "type": "task-status",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "Lifecycle state."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "One of open or completed."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "open"
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
      "id": "FLD-TASK-REVISION",
      "name": {
        "text": "Revision"
      },
      "type": "integer",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "Concurrency token for a retained Task."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "A non-negative integer, increased by one for each successful completion."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "0"
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
      "id": "ST-TASK-OPEN",
      "name": {
        "text": "Open"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Work is still pending."
        }
      ]
    },
    {
      "id": "ST-TASK-COMPLETED",
      "name": {
        "text": "Completed"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "Work has been completed; the task remains retained."
        }
      ]
    }
  ],
  "transitions": [
    {
      "id": "TRN-TASK-COMPLETE",
      "name": {
        "text": "Complete"
      },
      "from": "ST-TASK-OPEN",
      "to": "ST-TASK-COMPLETED",
      "description": [
        {
          "type": "paragraph",
          "text": "Preserve identity and title; change status to completed. The store increments revision after the conditional write succeeds."
        }
      ]
    }
  ],
  "validations": [
    {
      "id": "VLD-TASK-ID",
      "name": {
        "text": "Task identifier"
      },
      "scope": "field",
      "statement": [
        {
          "type": "paragraph",
          "text": "A task identifier is non-empty text, preserved exactly."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Candidate"
          },
          "source": "input",
          "meaning": [
            {
              "type": "paragraph",
              "text": "A task identifier is non-empty text, preserved exactly."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-TASK-ID-1",
          "condition": {
            "text": "The candidate is text containing at least one non-whitespace character."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "The candidate is text containing at least one non-whitespace character."
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
              "text": "All stated conditions hold. No normalization or persistence occurs."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "At least one stated condition fails. Preserve prior state."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-TASK-ID"
    },
    {
      "id": "VLD-TASK-NEW",
      "name": {
        "text": "New task validity"
      },
      "scope": "entity",
      "statement": [
        {
          "type": "paragraph",
          "text": "A new Task has a valid identifier, a meaningful title, open status, and revision zero."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Candidate"
          },
          "source": "input",
          "meaning": [
            {
              "type": "paragraph",
              "text": "A new Task has a valid identifier, a meaningful title, open status, and revision zero."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-TASK-NEW-1",
          "condition": {
            "text": "The task identifier satisfies VLD-TASK-ID."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "The task identifier satisfies VLD-TASK-ID."
            }
          ]
        },
        {
          "id": "C-TASK-NEW-2",
          "condition": {
            "text": "The title is text with at least one non-whitespace character."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "The title is text with at least one non-whitespace character."
            }
          ]
        },
        {
          "id": "C-TASK-NEW-3",
          "condition": {
            "text": "The status is open."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "The status is open."
            }
          ]
        },
        {
          "id": "C-TASK-NEW-4",
          "condition": {
            "text": "The revision is the integer zero."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "The revision is the integer zero."
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
              "text": "All stated conditions hold. No normalization or persistence occurs."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "At least one stated condition fails. Preserve prior state."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-TASK-NEW"
    },
    {
      "id": "VLD-TASK-COMPLETE",
      "name": {
        "text": "Completion transition"
      },
      "scope": "transition",
      "statement": [
        {
          "type": "paragraph",
          "text": "A ready Task may transition from open to completed; a completed Task cannot be completed again."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Candidate"
          },
          "source": "state",
          "meaning": [
            {
              "type": "paragraph",
              "text": "A ready Task may transition from open to completed; a completed Task cannot be completed again."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-TASK-COMPLETE-1",
          "condition": {
            "text": "The current state is ST-TASK-OPEN."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "The current state is ST-TASK-OPEN."
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
              "text": "All stated conditions hold. No normalization or persistence occurs."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "At least one stated condition fails. Preserve prior state."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-TASK-COMPLETE"
    }
  ],
  "examples": [
    {
      "id": "EX-TASK-OPEN",
      "kind": "valid",
      "description": [
        {
          "type": "paragraph",
          "text": "A valid new Task."
        }
      ],
      "data": {
        "task_id": "TASK001",
        "title": "Review Atlas",
        "status": "open",
        "revision": 0
      }
    },
    {
      "id": "EX-TASK-COMPLETED",
      "kind": "valid",
      "description": [
        {
          "type": "paragraph",
          "text": "A retained Task after one completion."
        }
      ],
      "data": {
        "task_id": "TASK001",
        "title": "Review Atlas",
        "status": "completed",
        "revision": 1
      }
    },
    {
      "id": "EX-TASK-INVALID",
      "kind": "invalid",
      "description": [
        {
          "type": "paragraph",
          "text": "An empty title violates entity validity."
        }
      ],
      "data": {
        "task_id": "TASK001",
        "title": "",
        "status": "open",
        "revision": 0
      }
    }
  ],
  "assumptions": [
    "ASM-TASK-SINGLE-BOARD"
  ],
  "open_issues": []
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/TaskBoard/entities/Entity_Task.py",
    "symbol": "Entity_Task"
  },
  "class_kind": "entity",
  "fields": [
    {
      "name": "task_identifier",
      "type": "text",
      "required": true,
      "source_ref": "FLD-TASK-ID"
    },
    {
      "name": "title",
      "type": "text",
      "required": true,
      "source_ref": "FLD-TASK-TITLE"
    },
    {
      "name": "status",
      "type": "task-status",
      "required": true,
      "source_ref": "FLD-TASK-STATUS"
    },
    {
      "name": "revision",
      "type": "integer",
      "required": true,
      "source_ref": "FLD-TASK-REVISION"
    }
  ],
  "methods": [
    {
      "name": "create",
      "visibility": "public",
      "trigger": "when raw values enter the domain",
      "parameters": [
        {
          "name": "task_identifier",
          "type": "text"
        },
        {
          "name": "title",
          "type": "text"
        },
        {
          "name": "status",
          "type": "task-status"
        },
        {
          "name": "revision",
          "type": "integer"
        }
      ],
      "returns": [
        "Task"
      ],
      "algorithm": "Construct only after all Atlas entity validations pass; never leave a partially valid entity.",
      "source_refs": [
        "ENT-TASK",
        "VLD-TASK-ID",
        "VLD-TASK-NEW",
        "VLD-TASK-COMPLETE"
      ]
    },
    {
      "name": "validate_task_identifier",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "candidate",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "A task identifier is non-empty text, preserved exactly.",
      "source_refs": [
        "VLD-TASK-ID"
      ]
    },
    {
      "name": "validate_new_task_validity",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "candidate",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "A new Task has a valid identifier, a meaningful title, open status, and revision zero.",
      "source_refs": [
        "VLD-TASK-NEW"
      ]
    },
    {
      "name": "validate_completion_transition",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "candidate",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "A ready Task may transition from open to completed; a completed Task cannot be completed again.",
      "source_refs": [
        "VLD-TASK-COMPLETE"
      ]
    }
  ],
  "dependencies": []
}
```
