---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-VLD-TASK-NEW
kind: graph
source_refs:
- GRAPH-VLD-TASK-NEW
generation:
  mode: documentation_only
---

# New task validity

Preserves Atlas graph GRAPH-VLD-TASK-NEW.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-VLD-TASK-NEW",
  "kind": "flow",
  "owner": {
    "kind": "validation",
    "id": "VLD-TASK-NEW"
  },
  "title": {
    "text": "New task validity"
  },
  "nodes": [
    {
      "id": "N-VLD-TASK-NEW-START",
      "type": "start",
      "label": {
        "text": "Receive candidate"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-NEW-CHECK",
      "type": "decision",
      "label": {
        "text": "All conditions hold?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-NEW-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-NEW-FAIL",
      "type": "refusal",
      "label": {
        "text": "Fail; no mutation"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-TASK-NEW-1",
      "from": "N-VLD-TASK-NEW-START",
      "to": "N-VLD-TASK-NEW-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-TASK-NEW-2",
      "from": "N-VLD-TASK-NEW-CHECK",
      "to": "N-VLD-TASK-NEW-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-TASK-NEW-3",
      "from": "N-VLD-TASK-NEW-CHECK",
      "to": "N-VLD-TASK-NEW-FAIL",
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
    "id": "VLD-TASK-NEW"
  },
  "nodes": [
    {
      "id": "N-VLD-TASK-NEW-START",
      "type": "start",
      "label": {
        "text": "Receive candidate"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-NEW-CHECK",
      "type": "decision",
      "label": {
        "text": "All conditions hold?"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-NEW-PASS",
      "type": "result",
      "label": {
        "text": "Pass unchanged"
      },
      "requirement_refs": []
    },
    {
      "id": "N-VLD-TASK-NEW-FAIL",
      "type": "refusal",
      "label": {
        "text": "Fail; no mutation"
      },
      "requirement_refs": []
    }
  ],
  "edges": [
    {
      "id": "E-VLD-TASK-NEW-1",
      "from": "N-VLD-TASK-NEW-START",
      "to": "N-VLD-TASK-NEW-CHECK",
      "requirement_refs": []
    },
    {
      "id": "E-VLD-TASK-NEW-2",
      "from": "N-VLD-TASK-NEW-CHECK",
      "to": "N-VLD-TASK-NEW-PASS",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-VLD-TASK-NEW-3",
      "from": "N-VLD-TASK-NEW-CHECK",
      "to": "N-VLD-TASK-NEW-FAIL",
      "requirement_refs": [],
      "label": {
        "text": "no"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
