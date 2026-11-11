---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-TASK-LIST
kind: graph
source_refs:
- GRAPH-TASK-LIST
generation:
  mode: documentation_only
---

# List tasks

Preserves Atlas graph GRAPH-TASK-LIST.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-TASK-LIST",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-TASK-LIST"
  },
  "title": {
    "text": "List tasks"
  },
  "nodes": [
    {
      "id": "N-TASK-LIST-START",
      "type": "start",
      "label": {
        "text": "Receive request"
      },
      "requirement_refs": []
    },
    {
      "id": "N-TASK-LIST-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ]
    },
    {
      "id": "N-TASK-LIST-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no tool call"
      },
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ]
    },
    {
      "id": "N-TASK-LIST-READ",
      "type": "operation",
      "label": {
        "text": "Read board snapshot"
      },
      "requirement_refs": [
        "RF-TASK-LIST-SNAPSHOT"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-LIST"
      }
    },
    {
      "id": "N-TASK-LIST-FAIL",
      "type": "failure",
      "label": {
        "text": "Read failure; no list"
      },
      "requirement_refs": [
        "RF-TASK-LIST-FAILURE"
      ]
    },
    {
      "id": "N-TASK-LIST-RETURN",
      "type": "result",
      "label": {
        "text": "Return exact snapshot"
      },
      "requirement_refs": [
        "RF-TASK-LIST-SNAPSHOT"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-TASK-LIST-START",
      "from": "N-TASK-LIST-START",
      "to": "N-TASK-LIST-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-LIST-DENIED",
      "from": "N-TASK-LIST-AUTH",
      "to": "N-TASK-LIST-DENIED",
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    },
    {
      "id": "E-TASK-LIST-ALLOWED",
      "from": "N-TASK-LIST-AUTH",
      "to": "N-TASK-LIST-READ",
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-TASK-LIST-1",
      "from": "N-TASK-LIST-READ",
      "to": "N-TASK-LIST-FAIL",
      "requirement_refs": [
        "RF-TASK-LIST-FAILURE"
      ],
      "label": {
        "text": "unavailable / invalid state"
      }
    },
    {
      "id": "E-TASK-LIST-2",
      "from": "N-TASK-LIST-READ",
      "to": "N-TASK-LIST-RETURN",
      "requirement_refs": [
        "RF-TASK-LIST-SNAPSHOT"
      ],
      "label": {
        "text": "complete snapshot"
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
    "id": "UC-TASK-LIST"
  },
  "nodes": [
    {
      "id": "N-TASK-LIST-START",
      "type": "start",
      "label": {
        "text": "Receive request"
      },
      "requirement_refs": []
    },
    {
      "id": "N-TASK-LIST-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ]
    },
    {
      "id": "N-TASK-LIST-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no tool call"
      },
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ]
    },
    {
      "id": "N-TASK-LIST-READ",
      "type": "operation",
      "label": {
        "text": "Read board snapshot"
      },
      "requirement_refs": [
        "RF-TASK-LIST-SNAPSHOT"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-LIST"
      }
    },
    {
      "id": "N-TASK-LIST-FAIL",
      "type": "failure",
      "label": {
        "text": "Read failure; no list"
      },
      "requirement_refs": [
        "RF-TASK-LIST-FAILURE"
      ]
    },
    {
      "id": "N-TASK-LIST-RETURN",
      "type": "result",
      "label": {
        "text": "Return exact snapshot"
      },
      "requirement_refs": [
        "RF-TASK-LIST-SNAPSHOT"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-TASK-LIST-START",
      "from": "N-TASK-LIST-START",
      "to": "N-TASK-LIST-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-LIST-DENIED",
      "from": "N-TASK-LIST-AUTH",
      "to": "N-TASK-LIST-DENIED",
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    },
    {
      "id": "E-TASK-LIST-ALLOWED",
      "from": "N-TASK-LIST-AUTH",
      "to": "N-TASK-LIST-READ",
      "requirement_refs": [
        "RF-TASK-LIST-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-TASK-LIST-1",
      "from": "N-TASK-LIST-READ",
      "to": "N-TASK-LIST-FAIL",
      "requirement_refs": [
        "RF-TASK-LIST-FAILURE"
      ],
      "label": {
        "text": "unavailable / invalid state"
      }
    },
    {
      "id": "E-TASK-LIST-2",
      "from": "N-TASK-LIST-READ",
      "to": "N-TASK-LIST-RETURN",
      "requirement_refs": [
        "RF-TASK-LIST-SNAPSHOT"
      ],
      "label": {
        "text": "complete snapshot"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
