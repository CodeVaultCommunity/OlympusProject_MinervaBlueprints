---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TOL-TASK-STORE
kind: abstract_tool
source_refs:
- TOL-TASK-STORE
generation:
  mode: code
  language: python
  path: apps/TaskBoard/tools/abstract/AbstractTool_TaskStore.py
  symbol: AbstractTool_TaskStore
---

# Task store

An abstract retention and retrieval capability. This specification chooses no database, protocol, framework, SQL syntax, route, or concrete adapter.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "TOL-TASK-STORE",
  "name": {
    "text": "Task store"
  },
  "purpose": [
    {
      "type": "paragraph",
      "text": "An abstract retention and retrieval capability. This specification chooses no database, protocol, framework, SQL syntax, route, or concrete adapter."
    }
  ],
  "operations": [
    {
      "id": "OP-TASK-CREATE",
      "name": {
        "text": "Retain a new Task"
      },
      "purpose": [
        {
          "type": "paragraph",
          "text": "Atomically insert one ready open Task if its identifier is absent."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Task"
          },
          "type": "ENT-TASK",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Ready Task after VLD-TASK-NEW; revision zero."
            }
          ],
          "required": true
        },
        {
          "name": {
            "text": "Board"
          },
          "type": "resolved-board",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The board bound to trusted caller context."
            }
          ],
          "required": true
        }
      ],
      "conditions": [
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        },
        {
          "type": "paragraph",
          "text": "All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding."
        }
      ],
      "results": [
        {
          "name": {
            "text": "Created Task"
          },
          "type": "ENT-TASK",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The retained Task, with its exact title and identifier."
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "text": "A successful result confirms retention at revision zero."
            }
          ]
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "One Task is added on success."
        }
      ],
      "failures": [
        {
          "code": "DUPLICATE_ID",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The identifier is already retained in this board."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "This outcome is not applied: the store guarantees that this operation made no change."
            }
          ]
        },
        {
          "code": "STORE_UNAVAILABLE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The capability could not confirm the requested result."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task."
            }
          ]
        }
      ],
      "guarantees": [
        {
          "type": "paragraph",
          "text": "Uniqueness check and insertion are atomic. A duplicate does not overwrite an existing Task."
        },
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        }
      ]
    },
    {
      "id": "OP-TASK-LOAD",
      "name": {
        "text": "Read one Task"
      },
      "purpose": [
        {
          "type": "paragraph",
          "text": "Return a ready Task and its observed revision by exact identifier."
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
              "text": "Identifier already checked against VLD-TASK-ID."
            }
          ],
          "required": true
        },
        {
          "name": {
            "text": "Board"
          },
          "type": "resolved-board",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The authorized board."
            }
          ],
          "required": true
        }
      ],
      "conditions": [
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        },
        {
          "type": "paragraph",
          "text": "All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding."
        }
      ],
      "results": [
        {
          "name": {
            "text": "Task"
          },
          "type": "ENT-TASK",
          "meaning": [
            {
              "type": "paragraph",
              "text": "A ready Task hydrated from one retained record."
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "text": "Its revision describes the same observed record as its fields."
            }
          ]
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No task is changed."
        }
      ],
      "failures": [
        {
          "code": "NOT_FOUND",
          "meaning": [
            {
              "type": "paragraph",
              "text": "No task with this identifier exists in this board at read time."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "Distinct from unavailable or malformed storage."
            }
          ]
        },
        {
          "code": "STORE_UNAVAILABLE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The capability could not confirm the requested result."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task."
            }
          ]
        },
        {
          "code": "STORE_INVALID_STATE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "A stored record could not be hydrated through the canonical Task validity rules."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "Do not return a malformed ready Task, an empty success, or a partial list. Report the integrity failure; no task is changed by the read."
            }
          ]
        }
      ],
      "guarantees": [
        {
          "type": "paragraph",
          "text": "No write occurs. Not-found is a confirmed absence, not a masked read error."
        },
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        }
      ]
    },
    {
      "id": "OP-TASK-COMPLETE",
      "name": {
        "text": "Retain a completion"
      },
      "purpose": [
        {
          "type": "paragraph",
          "text": "Atomically replace the observed Task with a ready completed Task only if its revision still matches."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Task"
          },
          "type": "ENT-TASK",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Ready Task after the entity's open-to-completed transition; identity/title unchanged."
            }
          ],
          "required": true
        },
        {
          "name": {
            "text": "Expected revision"
          },
          "type": "integer",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Revision returned by OP-TASK-LOAD."
            }
          ],
          "required": true
        },
        {
          "name": {
            "text": "Board"
          },
          "type": "resolved-board",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The authorized board."
            }
          ],
          "required": true
        }
      ],
      "conditions": [
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        },
        {
          "type": "paragraph",
          "text": "All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding."
        }
      ],
      "results": [
        {
          "name": {
            "text": "Completed Task"
          },
          "type": "ENT-TASK",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The retained completed Task."
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "text": "Revision is expected_revision+1; identity and title are unchanged."
            }
          ]
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "Status becomes completed and revision increases once on success."
        }
      ],
      "failures": [
        {
          "code": "NOT_FOUND",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The observed Task is no longer present at conditional-write time."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "This outcome is not applied: the store guarantees that this operation made no change."
            }
          ]
        },
        {
          "code": "VERSION_CONFLICT",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The retained revision differs from the expected revision."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "This outcome is not applied: the store guarantees that this operation made no change."
            }
          ]
        },
        {
          "code": "STORE_UNAVAILABLE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The capability could not confirm the requested result."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task."
            }
          ]
        }
      ],
      "guarantees": [
        {
          "type": "paragraph",
          "text": "Existence/revision comparison and replacement are atomic; no lost update is reported as success."
        },
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        }
      ]
    },
    {
      "id": "OP-TASK-LIST",
      "name": {
        "text": "Read the board"
      },
      "purpose": [
        {
          "type": "paragraph",
          "text": "Return one consistent snapshot of all Tasks in the authorized board."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Board"
          },
          "type": "resolved-board",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The authorized board."
            }
          ],
          "required": true
        }
      ],
      "conditions": [
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        },
        {
          "type": "paragraph",
          "text": "All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding."
        }
      ],
      "results": [
        {
          "name": {
            "text": "Tasks"
          },
          "type": "list[ENT-TASK]",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Ready Tasks ordered by exact identifier using Unicode code-point order."
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "text": "Each matching Task appears exactly once; an empty successful list means the board was empty at the snapshot instant."
            }
          ]
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No task is changed."
        }
      ],
      "failures": [
        {
          "code": "STORE_UNAVAILABLE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The capability could not confirm the requested result."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task."
            }
          ]
        },
        {
          "code": "STORE_INVALID_STATE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "A stored record could not be hydrated through the canonical Task validity rules."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "Do not return a malformed ready Task, an empty success, or a partial list. Report the integrity failure; no task is changed by the read."
            }
          ]
        }
      ],
      "guarantees": [
        {
          "type": "paragraph",
          "text": "No partial list is returned as a complete snapshot. Concurrent later changes need not appear in this snapshot."
        },
        {
          "type": "paragraph",
          "text": "A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task."
        }
      ]
    }
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/TaskBoard/tools/abstract/AbstractTool_TaskStore.py",
    "symbol": "AbstractTool_TaskStore"
  },
  "class_kind": "protocol",
  "methods": [
    {
      "name": "retain_a_new_task",
      "parameters": [
        {
          "name": "task",
          "type": "ENT-TASK"
        },
        {
          "name": "board",
          "type": "resolved-board"
        }
      ],
      "returns": [
        "Created Task"
      ],
      "failures": [
        "DUPLICATE_ID",
        "STORE_UNAVAILABLE"
      ],
      "effects": "One Task is added on success.",
      "source_refs": [
        "OP-TASK-CREATE"
      ]
    },
    {
      "name": "read_one_task",
      "parameters": [
        {
          "name": "task_identifier",
          "type": "text"
        },
        {
          "name": "board",
          "type": "resolved-board"
        }
      ],
      "returns": [
        "Task"
      ],
      "failures": [
        "NOT_FOUND",
        "STORE_UNAVAILABLE",
        "STORE_INVALID_STATE"
      ],
      "effects": "No task is changed.",
      "source_refs": [
        "OP-TASK-LOAD"
      ]
    },
    {
      "name": "retain_a_completion",
      "parameters": [
        {
          "name": "task",
          "type": "ENT-TASK"
        },
        {
          "name": "expected_revision",
          "type": "integer"
        },
        {
          "name": "board",
          "type": "resolved-board"
        }
      ],
      "returns": [
        "Completed Task"
      ],
      "failures": [
        "NOT_FOUND",
        "VERSION_CONFLICT",
        "STORE_UNAVAILABLE"
      ],
      "effects": "Status becomes completed and revision increases once on success.",
      "source_refs": [
        "OP-TASK-COMPLETE"
      ]
    },
    {
      "name": "read_the_board",
      "parameters": [
        {
          "name": "board",
          "type": "resolved-board"
        }
      ],
      "returns": [
        "Tasks"
      ],
      "failures": [
        "STORE_UNAVAILABLE",
        "STORE_INVALID_STATE"
      ],
      "effects": "No task is changed.",
      "source_refs": [
        "OP-TASK-LIST"
      ]
    }
  ]
}
```
