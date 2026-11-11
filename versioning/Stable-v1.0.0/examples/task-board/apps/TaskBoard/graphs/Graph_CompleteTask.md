---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-TASK-COMPLETE
kind: graph
source_refs:
- GRAPH-TASK-COMPLETE
generation:
  mode: documentation_only
---

# Complete task

Preserves Atlas graph GRAPH-TASK-COMPLETE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-TASK-COMPLETE",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-TASK-COMPLETE"
  },
  "title": {
    "text": "Complete task"
  },
  "nodes": [
    {
      "id": "N-TASK-COMPLETE-START",
      "type": "start",
      "label": {
        "text": "Receive request"
      },
      "requirement_refs": []
    },
    {
      "id": "N-TASK-COMPLETE-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no tool call"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-ID",
      "type": "validation",
      "label": {
        "text": "Apply identifier validity"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-TASK-ID"
      }
    },
    {
      "id": "N-TASK-COMPLETE-VALID",
      "type": "decision",
      "label": {
        "text": "Identifier valid?"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid identifier"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-LOAD",
      "type": "operation",
      "label": {
        "text": "Load ready Task"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-LOAD"
      }
    },
    {
      "id": "N-TASK-COMPLETE-MISSING",
      "type": "refusal",
      "label": {
        "text": "Task not found"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD",
        "RF-TASK-COMPLETE-WRITE"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-TRANSITION",
      "type": "validation",
      "label": {
        "text": "Apply completion rule"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-TASK-COMPLETE"
      }
    },
    {
      "id": "N-TASK-COMPLETE-ALLOWED",
      "type": "decision",
      "label": {
        "text": "Transition allowed?"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-ALREADY",
      "type": "refusal",
      "label": {
        "text": "Already completed"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-STORE",
      "type": "operation",
      "label": {
        "text": "Conditional completion"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-COMPLETE"
      }
    },
    {
      "id": "N-TASK-COMPLETE-CONFLICT",
      "type": "refusal",
      "label": {
        "text": "Version conflict"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-ERROR",
      "type": "failure",
      "label": {
        "text": "Report storage outcome"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-FAILURE"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-DONE",
      "type": "result",
      "label": {
        "text": "Completion confirmed"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-TASK-COMPLETE-START",
      "from": "N-TASK-COMPLETE-START",
      "to": "N-TASK-COMPLETE-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-COMPLETE-DENIED",
      "from": "N-TASK-COMPLETE-AUTH",
      "to": "N-TASK-COMPLETE-DENIED",
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    },
    {
      "id": "E-TASK-COMPLETE-ALLOWED",
      "from": "N-TASK-COMPLETE-AUTH",
      "to": "N-TASK-COMPLETE-ID",
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-TASK-COMPLETE-1",
      "from": "N-TASK-COMPLETE-ID",
      "to": "N-TASK-COMPLETE-VALID",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-COMPLETE-2",
      "from": "N-TASK-COMPLETE-VALID",
      "to": "N-TASK-COMPLETE-INVALID",
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-TASK-COMPLETE-3",
      "from": "N-TASK-COMPLETE-VALID",
      "to": "N-TASK-COMPLETE-LOAD",
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-TASK-COMPLETE-4",
      "from": "N-TASK-COMPLETE-LOAD",
      "to": "N-TASK-COMPLETE-MISSING",
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD"
      ],
      "label": {
        "text": "NOT_FOUND"
      }
    },
    {
      "id": "E-TASK-COMPLETE-5",
      "from": "N-TASK-COMPLETE-LOAD",
      "to": "N-TASK-COMPLETE-ERROR",
      "requirement_refs": [
        "RF-TASK-COMPLETE-FAILURE"
      ],
      "label": {
        "text": "unavailable / invalid state"
      }
    },
    {
      "id": "E-TASK-COMPLETE-6",
      "from": "N-TASK-COMPLETE-LOAD",
      "to": "N-TASK-COMPLETE-TRANSITION",
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ],
      "label": {
        "text": "ready Task"
      }
    },
    {
      "id": "E-TASK-COMPLETE-7",
      "from": "N-TASK-COMPLETE-TRANSITION",
      "to": "N-TASK-COMPLETE-ALLOWED",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-COMPLETE-8",
      "from": "N-TASK-COMPLETE-ALLOWED",
      "to": "N-TASK-COMPLETE-ALREADY",
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-TASK-COMPLETE-9",
      "from": "N-TASK-COMPLETE-ALLOWED",
      "to": "N-TASK-COMPLETE-STORE",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-TASK-COMPLETE-10",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-CONFLICT",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "label": {
        "text": "VERSION_CONFLICT"
      }
    },
    {
      "id": "E-TASK-COMPLETE-11",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-MISSING",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "label": {
        "text": "NOT_FOUND"
      }
    },
    {
      "id": "E-TASK-COMPLETE-12",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-ERROR",
      "requirement_refs": [
        "RF-TASK-COMPLETE-FAILURE"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-TASK-COMPLETE-13",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-DONE",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
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
    "id": "UC-TASK-COMPLETE"
  },
  "nodes": [
    {
      "id": "N-TASK-COMPLETE-START",
      "type": "start",
      "label": {
        "text": "Receive request"
      },
      "requirement_refs": []
    },
    {
      "id": "N-TASK-COMPLETE-AUTH",
      "type": "decision",
      "label": {
        "text": "Trusted permission?"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-DENIED",
      "type": "refusal",
      "label": {
        "text": "Denied; no tool call"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-ID",
      "type": "validation",
      "label": {
        "text": "Apply identifier validity"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-TASK-ID"
      }
    },
    {
      "id": "N-TASK-COMPLETE-VALID",
      "type": "decision",
      "label": {
        "text": "Identifier valid?"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid identifier"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-LOAD",
      "type": "operation",
      "label": {
        "text": "Load ready Task"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-LOAD"
      }
    },
    {
      "id": "N-TASK-COMPLETE-MISSING",
      "type": "refusal",
      "label": {
        "text": "Task not found"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD",
        "RF-TASK-COMPLETE-WRITE"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-TRANSITION",
      "type": "validation",
      "label": {
        "text": "Apply completion rule"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-TASK-COMPLETE"
      }
    },
    {
      "id": "N-TASK-COMPLETE-ALLOWED",
      "type": "decision",
      "label": {
        "text": "Transition allowed?"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-ALREADY",
      "type": "refusal",
      "label": {
        "text": "Already completed"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-STORE",
      "type": "operation",
      "label": {
        "text": "Conditional completion"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-TASK-COMPLETE"
      }
    },
    {
      "id": "N-TASK-COMPLETE-CONFLICT",
      "type": "refusal",
      "label": {
        "text": "Version conflict"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-ERROR",
      "type": "failure",
      "label": {
        "text": "Report storage outcome"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-FAILURE"
      ]
    },
    {
      "id": "N-TASK-COMPLETE-DONE",
      "type": "result",
      "label": {
        "text": "Completion confirmed"
      },
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-TASK-COMPLETE-START",
      "from": "N-TASK-COMPLETE-START",
      "to": "N-TASK-COMPLETE-AUTH",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-COMPLETE-DENIED",
      "from": "N-TASK-COMPLETE-AUTH",
      "to": "N-TASK-COMPLETE-DENIED",
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ],
      "label": {
        "text": "missing / unresolved / insufficient"
      }
    },
    {
      "id": "E-TASK-COMPLETE-ALLOWED",
      "from": "N-TASK-COMPLETE-AUTH",
      "to": "N-TASK-COMPLETE-ID",
      "requirement_refs": [
        "RF-TASK-COMPLETE-AUTH"
      ],
      "label": {
        "text": "authorized"
      }
    },
    {
      "id": "E-TASK-COMPLETE-1",
      "from": "N-TASK-COMPLETE-ID",
      "to": "N-TASK-COMPLETE-VALID",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-COMPLETE-2",
      "from": "N-TASK-COMPLETE-VALID",
      "to": "N-TASK-COMPLETE-INVALID",
      "requirement_refs": [
        "RF-TASK-COMPLETE-ID"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-TASK-COMPLETE-3",
      "from": "N-TASK-COMPLETE-VALID",
      "to": "N-TASK-COMPLETE-LOAD",
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-TASK-COMPLETE-4",
      "from": "N-TASK-COMPLETE-LOAD",
      "to": "N-TASK-COMPLETE-MISSING",
      "requirement_refs": [
        "RF-TASK-COMPLETE-LOAD"
      ],
      "label": {
        "text": "NOT_FOUND"
      }
    },
    {
      "id": "E-TASK-COMPLETE-5",
      "from": "N-TASK-COMPLETE-LOAD",
      "to": "N-TASK-COMPLETE-ERROR",
      "requirement_refs": [
        "RF-TASK-COMPLETE-FAILURE"
      ],
      "label": {
        "text": "unavailable / invalid state"
      }
    },
    {
      "id": "E-TASK-COMPLETE-6",
      "from": "N-TASK-COMPLETE-LOAD",
      "to": "N-TASK-COMPLETE-TRANSITION",
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ],
      "label": {
        "text": "ready Task"
      }
    },
    {
      "id": "E-TASK-COMPLETE-7",
      "from": "N-TASK-COMPLETE-TRANSITION",
      "to": "N-TASK-COMPLETE-ALLOWED",
      "requirement_refs": []
    },
    {
      "id": "E-TASK-COMPLETE-8",
      "from": "N-TASK-COMPLETE-ALLOWED",
      "to": "N-TASK-COMPLETE-ALREADY",
      "requirement_refs": [
        "RF-TASK-COMPLETE-TRANSITION"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-TASK-COMPLETE-9",
      "from": "N-TASK-COMPLETE-ALLOWED",
      "to": "N-TASK-COMPLETE-STORE",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-TASK-COMPLETE-10",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-CONFLICT",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "label": {
        "text": "VERSION_CONFLICT"
      }
    },
    {
      "id": "E-TASK-COMPLETE-11",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-MISSING",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "label": {
        "text": "NOT_FOUND"
      }
    },
    {
      "id": "E-TASK-COMPLETE-12",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-ERROR",
      "requirement_refs": [
        "RF-TASK-COMPLETE-FAILURE"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-TASK-COMPLETE-13",
      "from": "N-TASK-COMPLETE-STORE",
      "to": "N-TASK-COMPLETE-DONE",
      "requirement_refs": [
        "RF-TASK-COMPLETE-WRITE"
      ],
      "label": {
        "text": "confirmed"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
