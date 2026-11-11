---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: GRAPH-REQUEST-SUBMIT
kind: graph
source_refs:
- GRAPH-REQUEST-SUBMIT
generation:
  mode: documentation_only
---

# Submit request

Preserves Atlas graph GRAPH-REQUEST-SUBMIT.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "GRAPH-REQUEST-SUBMIT",
  "kind": "flow",
  "owner": {
    "kind": "use_case",
    "id": "UC-REQUEST-SUBMIT"
  },
  "title": {
    "text": "Submit request"
  },
  "nodes": [
    {
      "id": "N-REQ-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-REQ-PERM",
      "type": "decision",
      "label": {
        "text": "Actor permitted?"
      },
      "requirement_refs": [
        "RF-REQUEST-01"
      ]
    },
    {
      "id": "N-REQ-DENY",
      "type": "refusal",
      "label": {
        "text": "Refuse: actor not permitted"
      },
      "requirement_refs": [
        "RF-REQUEST-01"
      ]
    },
    {
      "id": "N-REQ-VALIDATE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-REQUEST-QUANTITY"
      },
      "requirement_refs": [
        "RF-REQUEST-02"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-REQUEST-QUANTITY"
      }
    },
    {
      "id": "N-REQ-QTYDEC",
      "type": "decision",
      "label": {
        "text": "Quantity valid?"
      },
      "requirement_refs": [
        "RF-REQUEST-02"
      ]
    },
    {
      "id": "N-REQ-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid code or quantity"
      },
      "requirement_refs": [
        "RF-REQUEST-02",
        "RF-REQUEST-07"
      ]
    },
    {
      "id": "N-REQ-STORE",
      "type": "operation",
      "label": {
        "text": "Store request"
      },
      "requirement_refs": [
        "RF-REQUEST-03"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-REQUEST-STORE"
      }
    },
    {
      "id": "N-REQ-STOREERROR",
      "type": "failure",
      "label": {
        "text": "Report STORE_UNAVAILABLE"
      },
      "requirement_refs": [
        "RF-REQUEST-04"
      ]
    },
    {
      "id": "N-REQ-SUCCESS",
      "type": "result",
      "label": {
        "text": "Request confirmed"
      },
      "requirement_refs": [
        "RF-REQUEST-05"
      ]
    },
    {
      "id": "N-REQ-DUPLICATE",
      "type": "refusal",
      "label": {
        "text": "Duplicate code; no change"
      },
      "requirement_refs": [
        "RF-REQUEST-06"
      ]
    },
    {
      "id": "N-REQ-CODE",
      "type": "validation",
      "label": {
        "text": "Apply code validity"
      },
      "requirement_refs": [
        "RF-REQUEST-07"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-REQUEST-CODE"
      }
    },
    {
      "id": "N-REQ-CODE-VALID",
      "type": "decision",
      "label": {
        "text": "Code valid?"
      },
      "requirement_refs": [
        "RF-REQUEST-07"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-REQ-1",
      "from": "N-REQ-START",
      "to": "N-REQ-PERM",
      "requirement_refs": []
    },
    {
      "id": "E-REQ-2",
      "from": "N-REQ-PERM",
      "to": "N-REQ-DENY",
      "requirement_refs": [
        "RF-REQUEST-01"
      ],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-REQ-3",
      "from": "N-REQ-PERM",
      "to": "N-REQ-CODE",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-REQ-4",
      "from": "N-REQ-VALIDATE",
      "to": "N-REQ-QTYDEC",
      "requirement_refs": [
        "RF-REQUEST-02"
      ]
    },
    {
      "id": "E-REQ-5",
      "from": "N-REQ-QTYDEC",
      "to": "N-REQ-INVALID",
      "requirement_refs": [
        "RF-REQUEST-02"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-REQ-6",
      "from": "N-REQ-QTYDEC",
      "to": "N-REQ-STORE",
      "requirement_refs": [
        "RF-REQUEST-03"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-REQ-7",
      "from": "N-REQ-STORE",
      "to": "N-REQ-SUCCESS",
      "requirement_refs": [
        "RF-REQUEST-03",
        "RF-REQUEST-05"
      ],
      "label": {
        "text": "stored"
      }
    },
    {
      "id": "E-REQ-8",
      "from": "N-REQ-STORE",
      "to": "N-REQ-STOREERROR",
      "requirement_refs": [
        "RF-REQUEST-04"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-REQ-DUPLICATE",
      "from": "N-REQ-STORE",
      "to": "N-REQ-DUPLICATE",
      "requirement_refs": [
        "RF-REQUEST-06"
      ],
      "label": {
        "text": "DUPLICATE_CODE"
      }
    },
    {
      "id": "E-REQ-CODE-1",
      "from": "N-REQ-CODE",
      "to": "N-REQ-CODE-VALID",
      "requirement_refs": []
    },
    {
      "id": "E-REQ-CODE-2",
      "from": "N-REQ-CODE-VALID",
      "to": "N-REQ-VALIDATE",
      "requirement_refs": [
        "RF-REQUEST-07"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-REQ-CODE-3",
      "from": "N-REQ-CODE-VALID",
      "to": "N-REQ-INVALID",
      "requirement_refs": [
        "RF-REQUEST-07"
      ],
      "label": {
        "text": "fail"
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
    "id": "UC-REQUEST-SUBMIT"
  },
  "nodes": [
    {
      "id": "N-REQ-START",
      "type": "start",
      "label": {
        "text": "Start"
      },
      "requirement_refs": []
    },
    {
      "id": "N-REQ-PERM",
      "type": "decision",
      "label": {
        "text": "Actor permitted?"
      },
      "requirement_refs": [
        "RF-REQUEST-01"
      ]
    },
    {
      "id": "N-REQ-DENY",
      "type": "refusal",
      "label": {
        "text": "Refuse: actor not permitted"
      },
      "requirement_refs": [
        "RF-REQUEST-01"
      ]
    },
    {
      "id": "N-REQ-VALIDATE",
      "type": "validation",
      "label": {
        "text": "Apply VLD-REQUEST-QUANTITY"
      },
      "requirement_refs": [
        "RF-REQUEST-02"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-REQUEST-QUANTITY"
      }
    },
    {
      "id": "N-REQ-QTYDEC",
      "type": "decision",
      "label": {
        "text": "Quantity valid?"
      },
      "requirement_refs": [
        "RF-REQUEST-02"
      ]
    },
    {
      "id": "N-REQ-INVALID",
      "type": "refusal",
      "label": {
        "text": "Invalid code or quantity"
      },
      "requirement_refs": [
        "RF-REQUEST-02",
        "RF-REQUEST-07"
      ]
    },
    {
      "id": "N-REQ-STORE",
      "type": "operation",
      "label": {
        "text": "Store request"
      },
      "requirement_refs": [
        "RF-REQUEST-03"
      ],
      "call": {
        "kind": "operation",
        "id": "OP-REQUEST-STORE"
      }
    },
    {
      "id": "N-REQ-STOREERROR",
      "type": "failure",
      "label": {
        "text": "Report STORE_UNAVAILABLE"
      },
      "requirement_refs": [
        "RF-REQUEST-04"
      ]
    },
    {
      "id": "N-REQ-SUCCESS",
      "type": "result",
      "label": {
        "text": "Request confirmed"
      },
      "requirement_refs": [
        "RF-REQUEST-05"
      ]
    },
    {
      "id": "N-REQ-DUPLICATE",
      "type": "refusal",
      "label": {
        "text": "Duplicate code; no change"
      },
      "requirement_refs": [
        "RF-REQUEST-06"
      ]
    },
    {
      "id": "N-REQ-CODE",
      "type": "validation",
      "label": {
        "text": "Apply code validity"
      },
      "requirement_refs": [
        "RF-REQUEST-07"
      ],
      "call": {
        "kind": "validation",
        "id": "VLD-REQUEST-CODE"
      }
    },
    {
      "id": "N-REQ-CODE-VALID",
      "type": "decision",
      "label": {
        "text": "Code valid?"
      },
      "requirement_refs": [
        "RF-REQUEST-07"
      ]
    }
  ],
  "edges": [
    {
      "id": "E-REQ-1",
      "from": "N-REQ-START",
      "to": "N-REQ-PERM",
      "requirement_refs": []
    },
    {
      "id": "E-REQ-2",
      "from": "N-REQ-PERM",
      "to": "N-REQ-DENY",
      "requirement_refs": [
        "RF-REQUEST-01"
      ],
      "label": {
        "text": "no"
      }
    },
    {
      "id": "E-REQ-3",
      "from": "N-REQ-PERM",
      "to": "N-REQ-CODE",
      "requirement_refs": [],
      "label": {
        "text": "yes"
      }
    },
    {
      "id": "E-REQ-4",
      "from": "N-REQ-VALIDATE",
      "to": "N-REQ-QTYDEC",
      "requirement_refs": [
        "RF-REQUEST-02"
      ]
    },
    {
      "id": "E-REQ-5",
      "from": "N-REQ-QTYDEC",
      "to": "N-REQ-INVALID",
      "requirement_refs": [
        "RF-REQUEST-02"
      ],
      "label": {
        "text": "fail"
      }
    },
    {
      "id": "E-REQ-6",
      "from": "N-REQ-QTYDEC",
      "to": "N-REQ-STORE",
      "requirement_refs": [
        "RF-REQUEST-03"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-REQ-7",
      "from": "N-REQ-STORE",
      "to": "N-REQ-SUCCESS",
      "requirement_refs": [
        "RF-REQUEST-03",
        "RF-REQUEST-05"
      ],
      "label": {
        "text": "stored"
      }
    },
    {
      "id": "E-REQ-8",
      "from": "N-REQ-STORE",
      "to": "N-REQ-STOREERROR",
      "requirement_refs": [
        "RF-REQUEST-04"
      ],
      "label": {
        "text": "STORE_UNAVAILABLE"
      }
    },
    {
      "id": "E-REQ-DUPLICATE",
      "from": "N-REQ-STORE",
      "to": "N-REQ-DUPLICATE",
      "requirement_refs": [
        "RF-REQUEST-06"
      ],
      "label": {
        "text": "DUPLICATE_CODE"
      }
    },
    {
      "id": "E-REQ-CODE-1",
      "from": "N-REQ-CODE",
      "to": "N-REQ-CODE-VALID",
      "requirement_refs": []
    },
    {
      "id": "E-REQ-CODE-2",
      "from": "N-REQ-CODE-VALID",
      "to": "N-REQ-VALIDATE",
      "requirement_refs": [
        "RF-REQUEST-07"
      ],
      "label": {
        "text": "pass"
      }
    },
    {
      "id": "E-REQ-CODE-3",
      "from": "N-REQ-CODE-VALID",
      "to": "N-REQ-INVALID",
      "requirement_refs": [
        "RF-REQUEST-07"
      ],
      "label": {
        "text": "fail"
      }
    }
  ],
  "generation": "method_control_flow"
}
```
