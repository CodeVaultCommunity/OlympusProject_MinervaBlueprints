---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: ENT-REQUEST
kind: entity
source_refs:
- ENT-REQUEST
generation:
  mode: code
  language: python
  path: apps/RequestRegister/entities/Entity_Request.py
  symbol: Entity_Request
---

# Request

Preserves Atlas entity ENT-REQUEST.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "ENT-REQUEST",
  "name": {
    "text": "Request"
  },
  "meaning": [
    {
      "type": "paragraph",
      "text": "A request asks the register to retain a quantity of a catalog code. The request is identified by its code."
    }
  ],
  "identity": {
    "description": [
      {
        "type": "paragraph",
        "text": "Two requests are the same when their codes are equal."
      }
    ],
    "fields": [
      "FLD-REQUEST-CODE"
    ]
  },
  "fields": [
    {
      "id": "FLD-REQUEST-CODE",
      "name": {
        "text": "Request code"
      },
      "type": "text",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "A non-empty code chosen by the requester."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "The code is preserved exactly; case is significant."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "REQ-001"
          },
          {
            "text": "req-001"
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
      "id": "FLD-REQUEST-QUANTITY",
      "name": {
        "text": "Quantity"
      },
      "type": "integer",
      "cardinality": "1",
      "required": true,
      "description": [
        {
          "type": "paragraph",
          "text": "The number of units requested."
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "text": "The value must be an integer greater than or equal to 1."
        }
      ],
      "examples": {
        "valid": [
          {
            "text": "1"
          },
          {
            "text": "2"
          }
        ],
        "invalid": [
          {
            "text": "0"
          },
          {
            "text": "1.5"
          }
        ]
      }
    }
  ],
  "relationships": [],
  "states": [],
  "transitions": [],
  "validations": [
    {
      "id": "VLD-REQUEST-QUANTITY",
      "name": {
        "text": "Quantity is a positive integer"
      },
      "scope": "field",
      "statement": [
        {
          "type": "paragraph",
          "text": "The quantity field is valid when its value is an integer greater than or equal to 1."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Quantity"
          },
          "source": "field",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The value supplied for FLD-REQUEST-QUANTITY."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-VLD-REQ-INT",
          "condition": {
            "text": "The value is an integer."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "A fractional or textual value fails this condition."
            }
          ]
        },
        {
          "id": "C-VLD-REQ-MIN",
          "condition": {
            "text": "The value is at least 1."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "Zero and negative values fail this condition."
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
              "text": "Both conditions hold; the field accepts the value."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "At least one condition fails; the field rejects the value."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-REQUEST-QUANTITY"
    },
    {
      "id": "VLD-REQUEST-CODE",
      "name": {
        "text": "Request code is non-empty text"
      },
      "scope": "field",
      "statement": [
        {
          "type": "paragraph",
          "text": "The code must be text containing at least one character. Preserve the code exactly; case is significant."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Code"
          },
          "source": "field",
          "meaning": [
            {
              "type": "paragraph",
              "text": "FLD-REQUEST-CODE candidate."
            }
          ]
        }
      ],
      "conditions": [
        {
          "id": "C-VLD-REQ-CODE-NONEMPTY",
          "condition": {
            "text": "The code is text with at least one character."
          },
          "meaning": [
            {
              "type": "paragraph",
              "text": "An empty or non-text code fails."
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
              "text": "Accept unchanged."
            }
          ]
        },
        {
          "outcome": "fail",
          "description": [
            {
              "type": "paragraph",
              "text": "Refuse before persistence."
            }
          ]
        }
      ],
      "flow": "GRAPH-VLD-REQUEST-CODE"
    }
  ],
  "examples": [
    {
      "id": "EX-REQUEST-VALID",
      "kind": "valid",
      "description": [
        {
          "type": "paragraph",
          "text": "A request with a non-empty code and a positive quantity."
        }
      ],
      "data": {
        "code": "REQ-001",
        "quantity": 2
      }
    },
    {
      "id": "EX-REQUEST-INVALID",
      "kind": "invalid",
      "description": [
        {
          "type": "paragraph",
          "text": "A request whose quantity is zero."
        }
      ],
      "data": {
        "code": "REQ-001",
        "quantity": 0
      }
    }
  ],
  "assumptions": [
    "ASM-REQUEST-STORE-UNIQUE"
  ],
  "open_issues": [
    "OI-REQUEST-LATENCY"
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/RequestRegister/entities/Entity_Request.py",
    "symbol": "Entity_Request"
  },
  "class_kind": "entity",
  "fields": [
    {
      "name": "request_code",
      "type": "text",
      "required": true,
      "source_ref": "FLD-REQUEST-CODE"
    },
    {
      "name": "quantity",
      "type": "integer",
      "required": true,
      "source_ref": "FLD-REQUEST-QUANTITY"
    }
  ],
  "methods": [
    {
      "name": "create",
      "visibility": "public",
      "trigger": "when raw values enter the domain",
      "parameters": [
        {
          "name": "request_code",
          "type": "text"
        },
        {
          "name": "quantity",
          "type": "integer"
        }
      ],
      "returns": [
        "Request"
      ],
      "algorithm": "Construct only after all Atlas entity validations pass; never leave a partially valid entity.",
      "source_refs": [
        "ENT-REQUEST",
        "VLD-REQUEST-QUANTITY",
        "VLD-REQUEST-CODE"
      ]
    },
    {
      "name": "validate_quantity_is_a_positive_integer",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "quantity",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "The quantity field is valid when its value is an integer greater than or equal to 1.",
      "source_refs": [
        "VLD-REQUEST-QUANTITY"
      ]
    },
    {
      "name": "validate_request_code_is_non_empty_text",
      "visibility": "private",
      "trigger": "during canonical construction and state transition",
      "parameters": [
        {
          "name": "code",
          "type": "unknown"
        }
      ],
      "returns": [
        "pass",
        "fail"
      ],
      "algorithm": "The code must be text containing at least one character. Preserve the code exactly; case is significant.",
      "source_refs": [
        "VLD-REQUEST-CODE"
      ]
    }
  ],
  "dependencies": []
}
```
