---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: CTL-REQUEST-STORE
kind: concrete_tool
source_refs:
- TOL-REQUEST-STORE
generation:
  mode: code
  language: python
  path: apps/RequestRegister/tools/concrete/Tool_SqliteRequestStore.py
  symbol: Tool_SqliteRequestStore
---

# SQLite implementation of Request store

Concrete design implementing Atlas abstract tool TOL-REQUEST-STORE; no executable code is stored in Minerva.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "TOL-REQUEST-STORE",
  "name": {
    "text": "Request store"
  },
  "purpose": [
    {
      "type": "paragraph",
      "text": "Retain request records durably. The contract does not choose a database, transport, or file layout."
    }
  ],
  "operations": [
    {
      "id": "OP-REQUEST-STORE",
      "name": {
        "text": "Store request"
      },
      "purpose": [
        {
          "type": "paragraph",
          "text": "Create one retained request record when its code is unused."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Request code"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The code to retain."
            }
          ],
          "required": true
        },
        {
          "name": {
            "text": "Quantity"
          },
          "type": "integer",
          "meaning": [
            {
              "type": "paragraph",
              "text": "An already validated positive integer."
            }
          ],
          "required": true
        }
      ],
      "conditions": [
        {
          "type": "paragraph",
          "text": "The code is not allocated to a retained request."
        },
        {
          "type": "paragraph",
          "text": "The store is available."
        },
        {
          "type": "paragraph",
          "text": "Inputs described as ready entities already satisfy canonical entity invariants. Do not duplicate those validations inside this tool. When constructing entities from raw retained records, use the canonical entity hydration rules; operation-specific external conditions remain this tool's responsibility."
        }
      ],
      "results": [
        {
          "name": {
            "text": "Stored request"
          },
          "type": "REQUEST",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The retained request with its code and quantity."
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "text": "After a successful result, the record is readable by code in the same retained store."
            }
          ]
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "One request record is added to the retained store."
        }
      ],
      "failures": [
        {
          "code": "DUPLICATE_CODE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The code is already allocated."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "The consumer must distinguish this from a successful store and from an unavailable store."
            }
          ]
        },
        {
          "code": "STORE_UNAVAILABLE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store did not confirm the write."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "Return write_outcome=not_applied only when the tool can guarantee no write; otherwise return write_outcome=unknown. Neither outcome is confirmation. An unknown outcome must not trigger an automatic retry."
            }
          ]
        }
      ],
      "guarantees": [
        {
          "type": "paragraph",
          "text": "A successful result confirms one retained record."
        },
        {
          "type": "paragraph",
          "text": "A duplicate-code failure leaves the existing record unchanged."
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
    "path": "apps/RequestRegister/tools/concrete/Tool_SqliteRequestStore.py",
    "symbol": "Tool_SqliteRequestStore"
  },
  "class_kind": "concrete_tool",
  "implements": [
    "TOL-REQUEST-STORE"
  ],
  "technology": "SQLite",
  "design_status": "complete",
  "methods": [
    {
      "name": "store_request",
      "implements_operation": "OP-REQUEST-STORE",
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
        "Stored request"
      ],
      "algorithm": "Open a scoped SQLite connection, translate ready domain values to bound parameters, execute the conditional write, and translate the row/result into the abstract operation result without reimplementing entity invariants.",
      "transaction": "Use BEGIN IMMEDIATE for the uniqueness-sensitive write; commit only after the stored result is known and roll back on a known failure. Preserve unknown outcome when commit confirmation is lost.",
      "error_mapping": {
        "DUPLICATE_CODE": "DUPLICATE_CODE",
        "STORE_UNAVAILABLE": "STORE_UNAVAILABLE"
      }
    }
  ],
  "configuration": [
    "database_path"
  ],
  "lifecycle": "application_scope_factory_with_operation_scoped_connections",
  "dependencies": [
    "sqlite3"
  ],
  "notes": [
    "No automatic retry is permitted for unknown write outcomes."
  ]
}
```
