---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-TASK-CREATE
kind: graph
source_refs:
- GRAPH-TASK-CREATE
generation:
  mode: documentation_only
---

# Create task

Preserves Atlas graph GRAPH-TASK-CREATE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-TASK-CREATE",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-TASK-CREATE"
  },
  "title": {
    "text": "Create task"
  },
  "nodes": [
    {
      "id": "N-TASK-CREATE-START",
      "type": "start",
      "label": {
        "text": "Receive request"
      },
      "requirement_refs": []
    },
    {
      "id": "N-TASK-CREATE-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ]
    },
    {
      "id": "N-TASK-CREATE-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no tool call"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ]
    },
    {
      "id": "N-TASK-CREATE-VALIDATE",
      "type": "validation",
      "label": {
        "text": "Apply new-task validity"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-TASK-NEW"
      }
    },
    {
      "id": "N-TASK-CREATE-VALID",
      "type": "decision",
      "label": {
        "text": "Candidate valid?"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ]
    },
    {
      "id": "N-TASK-CREATE-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid; no write"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ]
    },
    {
      "id": "N-TASK-CREATE-STORE",
      "type": "operation",
      "label": {
        "text": "Retain ready Task"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-CREATE"
      }
    },
    {
      "id": "N-TASK-CREATE-DUPLICATE",
      "type": "refusal",
      "label": {
        "text": "Duplicate; no change"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DUPLICATE"
      ]
    },
    {
      "id": "N-TASK-CREATE-UNAVAILABLE",
      "type": "failure",
      "label": {
        "text": "Report write outcome"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-FAILURE"
      ]
    },
    {
      "id": "N-TASK-CREATE-CREATED",
      "type": "result",
      "label": {
        "text": "Created at revision 0"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-TASK-CREATE-START",
      "from": "N-TASK-CREATE-START",
      "to": "N-TASK-CREATE-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-CREATE-DENIED",
      "from": "N-TASK-CREATE-AUTH",
      "to": "N-TASK-CREATE-DENIED",
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    },
    {
      "id": "E-TASK-CREATE-ALLOWED",
      "from": "N-TASK-CREATE-AUTH",
      "to": "N-TASK-CREATE-VALIDATE",
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-TASK-CREATE-1",
      "from": "N-TASK-CREATE-VALIDATE",
      "to": "N-TASK-CREATE-VALID",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-CREATE-2",
      "from": "N-TASK-CREATE-VALID",
      "to": "N-TASK-CREATE-INVALID",
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-TASK-CREATE-3",
      "from": "N-TASK-CREATE-VALID",
      "to": "N-TASK-CREATE-STORE",
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-TASK-CREATE-4",
      "from": "N-TASK-CREATE-STORE",
      "to": "N-TASK-CREATE-DUPLICATE",
      "requirement_refs": [
        "RF-TASK-CREATE-DUPLICATE"
      ],
      "label": {
        "text": "DUPLICATE_ID"
      }
    },
    {
      "id": "E-TASK-CREATE-5",
      "from": "N-TASK-CREATE-STORE",
      "to": "N-TASK-CREATE-UNAVAILABLE",
      "requirement_refs": [
        "RF-TASK-CREATE-FAILURE"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-TASK-CREATE-6",
      "from": "N-TASK-CREATE-STORE",
      "to": "N-TASK-CREATE-CREATED",
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ],
      "label": {
        "text": "confirmed"
      }
    }
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": null,
  "class_kind": "control_flow_graph",
  "owner": {
    "kind": "use_case",
    "id": "UC-TASK-CREATE"
  },
  "nodes": [
    {
      "id": "N-TASK-CREATE-START",
      "type": "start",
      "label": {
        "text": "Receive request"
      },
      "requirement_refs": []
    },
    {
      "id": "N-TASK-CREATE-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ]
    },
    {
      "id": "N-TASK-CREATE-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no tool call"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ]
    },
    {
      "id": "N-TASK-CREATE-VALIDATE",
      "type": "validation",
      "label": {
        "text": "Apply new-task validity"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-TASK-NEW"
      }
    },
    {
      "id": "N-TASK-CREATE-VALID",
      "type": "decision",
      "label": {
        "text": "Candidate valid?"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ]
    },
    {
      "id": "N-TASK-CREATE-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid; no write"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ]
    },
    {
      "id": "N-TASK-CREATE-STORE",
      "type": "operation",
      "label": {
        "text": "Retain ready Task"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-CREATE"
      }
    },
    {
      "id": "N-TASK-CREATE-DUPLICATE",
      "type": "refusal",
      "label": {
        "text": "Duplicate; no change"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-DUPLICATE"
      ]
    },
    {
      "id": "N-TASK-CREATE-UNAVAILABLE",
      "type": "failure",
      "label": {
        "text": "Report write outcome"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-FAILURE"
      ]
    },
    {
      "id": "N-TASK-CREATE-CREATED",
      "type": "result",
      "label": {
        "text": "Created at revision 0"
      },
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-TASK-CREATE-START",
      "from": "N-TASK-CREATE-START",
      "to": "N-TASK-CREATE-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-CREATE-DENIED",
      "from": "N-TASK-CREATE-AUTH",
      "to": "N-TASK-CREATE-DENIED",
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    },
    {
      "id": "E-TASK-CREATE-ALLOWED",
      "from": "N-TASK-CREATE-AUTH",
      "to": "N-TASK-CREATE-VALIDATE",
      "requirement_refs": [
        "RF-TASK-CREATE-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-TASK-CREATE-1",
      "from": "N-TASK-CREATE-VALIDATE",
      "to": "N-TASK-CREATE-VALID",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-CREATE-2",
      "from": "N-TASK-CREATE-VALID",
      "to": "N-TASK-CREATE-INVALID",
      "requirement_refs": [
        "RF-TASK-CREATE-DATA"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-TASK-CREATE-3",
      "from": "N-TASK-CREATE-VALID",
      "to": "N-TASK-CREATE-STORE",
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-TASK-CREATE-4",
      "from": "N-TASK-CREATE-STORE",
      "to": "N-TASK-CREATE-DUPLICATE",
      "requirement_refs": [
        "RF-TASK-CREATE-DUPLICATE"
      ],
      "label": {
        "text": "DUPLICATE_ID"
      }
    },
    {
      "id": "E-TASK-CREATE-5",
      "from": "N-TASK-CREATE-STORE",
      "to": "N-TASK-CREATE-UNAVAILABLE",
      "requirement_refs": [
        "RF-TASK-CREATE-FAILURE"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-TASK-CREATE-6",
      "from": "N-TASK-CREATE-STORE",
      "to": "N-TASK-CREATE-CREATED",
      "requirement_refs": [
        "RF-TASK-CREATE-RETAIN"
      ],
      "label": {
        "text": "confirmed"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
