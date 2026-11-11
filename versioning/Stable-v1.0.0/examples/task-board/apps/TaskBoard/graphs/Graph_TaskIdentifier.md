---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-TASK-ID
kind: graph
source_refs:
- GRAPH-VLD-TASK-ID
generation:
  mode: documentation_only
---

# Task identifier

Preserves Atlas graph GRAPH-VLD-TASK-ID.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-TASK-ID",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-TASK-ID"
  },
  "title": {
    "text": "Task identifier"
  },
  "nodes": [
    {
      "id": "N-VLD-TASK-ID-START",
      "type": "start",
      "label": {
        "text": "Receive candidate"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-ID-CHECK",
      "type": "decision",
      "label": {
        "text": "All conditions hold?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-ID-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-ID-FAIL",
      "type": "refusal",
      "label": {
        "text": "Fail; no mutation"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-TASK-ID-1",
      "from": "N-VLD-TASK-ID-START",
      "to": "N-VLD-TASK-ID-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-TASK-ID-2",
      "from": "N-VLD-TASK-ID-CHECK",
      "to": "N-VLD-TASK-ID-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-TASK-ID-3",
      "from": "N-VLD-TASK-ID-CHECK",
      "to": "N-VLD-TASK-ID-FAIL",
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
    "id": "VLD-TASK-ID"
  },
  "nodes": [
    {
      "id": "N-VLD-TASK-ID-START",
      "type": "start",
      "label": {
        "text": "Receive candidate"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-ID-CHECK",
      "type": "decision",
      "label": {
        "text": "All conditions hold?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-ID-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-ID-FAIL",
      "type": "refusal",
      "label": {
        "text": "Fail; no mutation"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-TASK-ID-1",
      "from": "N-VLD-TASK-ID-START",
      "to": "N-VLD-TASK-ID-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-TASK-ID-2",
      "from": "N-VLD-TASK-ID-CHECK",
      "to": "N-VLD-TASK-ID-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-TASK-ID-3",
      "from": "N-VLD-TASK-ID-CHECK",
      "to": "N-VLD-TASK-ID-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
