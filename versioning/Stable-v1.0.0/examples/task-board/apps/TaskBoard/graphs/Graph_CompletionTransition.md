---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-TASK-COMPLETE
kind: graph
source_refs:
- GRAPH-VLD-TASK-COMPLETE
generation:
  mode: documentation_only
---

# Completion transition

Preserves Atlas graph GRAPH-VLD-TASK-COMPLETE.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-TASK-COMPLETE",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-TASK-COMPLETE"
  },
  "title": {
    "text": "Completion transition"
  },
  "nodes": [
    {
      "id": "N-VLD-TASK-COMPLETE-START",
      "type": "start",
      "label": {
        "text": "Receive candidate"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-COMPLETE-CHECK",
      "type": "decision",
      "label": {
        "text": "All conditions hold?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-COMPLETE-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-COMPLETE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Fail; no mutation"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-TASK-COMPLETE-1",
      "from": "N-VLD-TASK-COMPLETE-START",
      "to": "N-VLD-TASK-COMPLETE-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-TASK-COMPLETE-2",
      "from": "N-VLD-TASK-COMPLETE-CHECK",
      "to": "N-VLD-TASK-COMPLETE-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-TASK-COMPLETE-3",
      "from": "N-VLD-TASK-COMPLETE-CHECK",
      "to": "N-VLD-TASK-COMPLETE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    }
  ],
  "notes": [
    {
      "type": "paragraph",
      "text": "The entity owns these conditions. Applying them needs no collaborator."
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
    "kind": "validation",
    "id": "VLD-TASK-COMPLETE"
  },
  "nodes": [
    {
      "id": "N-VLD-TASK-COMPLETE-START",
      "type": "start",
      "label": {
        "text": "Receive candidate"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-COMPLETE-CHECK",
      "type": "decision",
      "label": {
        "text": "All conditions hold?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-COMPLETE-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-COMPLETE-FAIL",
      "type": "refusal",
      "label": {
        "text": "Fail; no mutation"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-TASK-COMPLETE-1",
      "from": "N-VLD-TASK-COMPLETE-START",
      "to": "N-VLD-TASK-COMPLETE-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-TASK-COMPLETE-2",
      "from": "N-VLD-TASK-COMPLETE-CHECK",
      "to": "N-VLD-TASK-COMPLETE-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-TASK-COMPLETE-3",
      "from": "N-VLD-TASK-COMPLETE-CHECK",
      "to": "N-VLD-TASK-COMPLETE-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
