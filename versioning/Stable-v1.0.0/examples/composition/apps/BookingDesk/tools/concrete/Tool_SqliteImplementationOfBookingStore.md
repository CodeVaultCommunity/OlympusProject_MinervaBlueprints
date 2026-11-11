---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: CTL-BOOKING-STORE
kind: concrete_tool
source_refs:
- TOL-BOOKING-STORE
generation:
  mode: code
  language: python
  path: apps/BookingDesk/tools/concrete/Tool_SqliteBookingStore.py
  symbol: Tool_SqliteBookingStore
---

# SQLite implementation of Booking store

Concrete design implementing Atlas abstract tool TOL-BOOKING-STORE; no executable code is stored in Minerva.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "TOL-BOOKING-STORE",
  "name": {
    "text": "Booking store"
  },
  "purpose": [
    {
      "type": "paragraph",
      "text": "Load and retain bookings. The contract is shared by creation, lookup, and cancellation and does not select a database."
    }
  ],
  "operations": [
    {
      "id": "OP-BOOKING-LOAD",
      "name": {
        "text": "Load booking"
      },
      "purpose": [
        {
          "type": "paragraph",
          "text": "Read one retained booking by code."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Booking code"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The exact code to locate."
            }
          ],
          "required": true
        }
      ],
      "conditions": [
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
            "text": "Booking"
          },
          "type": "BOOKING",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The retained booking with its current status."
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "text": "The result reflects the stored record at read time."
            }
          ]
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "No persisted change."
        }
      ],
      "failures": [
        {
          "code": "NOT_FOUND",
          "meaning": [
            {
              "type": "paragraph",
              "text": "No retained booking has the code."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "Distinct from an invalid code and from an unavailable store."
            }
          ]
        },
        {
          "code": "STORE_UNAVAILABLE",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store could not complete the read."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "Must not be reported as not found."
            }
          ]
        }
      ],
      "guarantees": [
        {
          "type": "paragraph",
          "text": "A successful load returns one current booking."
        }
      ]
    },
    {
      "id": "OP-BOOKING-SAVE",
      "name": {
        "text": "Save booking"
      },
      "purpose": [
        {
          "type": "paragraph",
          "text": "Persist the current data of one booking."
        }
      ],
      "inputs": [
        {
          "name": {
            "text": "Booking"
          },
          "type": "BOOKING",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking to persist, including its status."
            }
          ],
          "required": true
        },
        {
          "name": {
            "text": "Expected version"
          },
          "type": "integer",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The version observed by the caller."
            }
          ],
          "required": true
        }
      ],
      "conditions": [
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
            "text": "Saved booking"
          },
          "type": "BOOKING",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The booking with an incremented version."
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "text": "A successful save confirms the new data."
            }
          ]
        }
      ],
      "effects": [
        {
          "type": "paragraph",
          "text": "The retained booking is replaced with the supplied data."
        }
      ],
      "failures": [
        {
          "code": "VERSION_CONFLICT",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The expected version is no longer current."
            }
          ],
          "consumer_distinction": [
            {
              "type": "paragraph",
              "text": "This operation made no write. The existing or concurrently updated record is not overwritten."
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
              "text": "Distinguish write_outcome=not_applied, when supported by a no-write guarantee, from unknown. Do not report success or automatically retry an unknown write."
            }
          ]
        }
      ],
      "guarantees": [
        {
          "type": "paragraph",
          "text": "A successful save confirms one updated retained booking."
        },
        {
          "type": "paragraph",
          "text": "Expected version zero means insert only if the identifier is absent. A positive expected version means replace only the matching retained version. Comparison and write are atomic; success increments the version by one."
        },
        {
          "type": "paragraph",
          "text": "VERSION_CONFLICT guarantees this operation made no change; another concurrent operation may have changed the stored record."
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
    "path": "apps/BookingDesk/tools/concrete/Tool_SqliteBookingStore.py",
    "symbol": "Tool_SqliteBookingStore"
  },
  "class_kind": "concrete_tool",
  "implements": [
    "TOL-BOOKING-STORE"
  ],
  "technology": "SQLite",
  "design_status": "complete",
  "methods": [
    {
      "name": "load_booking",
      "implements_operation": "OP-BOOKING-LOAD",
      "parameters": [
        {
          "name": "booking_code",
          "type": "text"
        }
      ],
      "returns": [
        "Booking"
      ],
      "algorithm": "Execute parameterized booking reads and state transitions through a repository adapter; hydrate entities through canonical constructors and map concurrency or availability failures to the declared abstract failures.",
      "transaction": "Use one explicit transaction per state-changing operation and optimistic version checks for cancellation; never report success before commit confirmation.",
      "error_mapping": {
        "NOT_FOUND": "NOT_FOUND",
        "STORE_UNAVAILABLE": "STORE_UNAVAILABLE"
      }
    },
    {
      "name": "save_booking",
      "implements_operation": "OP-BOOKING-SAVE",
      "parameters": [
        {
          "name": "booking",
          "type": "BOOKING"
        },
        {
          "name": "expected_version",
          "type": "integer"
        }
      ],
      "returns": [
        "Saved booking"
      ],
      "algorithm": "Execute parameterized booking reads and state transitions through a repository adapter; hydrate entities through canonical constructors and map concurrency or availability failures to the declared abstract failures.",
      "transaction": "Use one explicit transaction per state-changing operation and optimistic version checks for cancellation; never report success before commit confirmation.",
      "error_mapping": {
        "VERSION_CONFLICT": "VERSION_CONFLICT",
        "STORE_UNAVAILABLE": "STORE_UNAVAILABLE"
      }
    }
  ],
  "configuration": [
    "database_path",
    "busy_timeout_ms"
  ],
  "lifecycle": "application_scope_factory_with_operation_scoped_connections",
  "dependencies": [
    "sqlite3"
  ],
  "notes": [
    "Read and write operations share one concrete protocol implementation selected at composition."
  ]
}
```
