---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: BND-REQUEST-WEB
kind: boundary
source_refs:
- BND-REQUEST-WEB
generation:
  mode: code
  language: python
  path: apps/RequestRegister/boundaries/Boundary_RequestRegisterWebForm.py
  symbol: Boundary_RequestRegisterWebForm
---

# Request register web form

Expose the submit-request case through one form. Origin classification: this channel is an illustrative solution proposal. Its form, command syntax, layout and encoding are outside the L1 conformance claim. The referenced cases define domain inputs and outcomes independently of this channel.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "BND-REQUEST-WEB",
  "name": {
    "text": "Request register web form"
  },
  "modality": "web",
  "purpose": [
    {
      "type": "paragraph",
      "text": "Expose the submit-request case through one form."
    },
    {
      "type": "paragraph",
      "text": "Origin classification: this channel is an illustrative solution proposal. Its form, command syntax, layout and encoding are outside the L1 conformance claim. The referenced cases define domain inputs and outcomes independently of this channel."
    }
  ],
  "audience": [
    {
      "type": "paragraph",
      "text": "Requesters using the local register."
    }
  ],
  "interactions": [
    {
      "id": "INT-REQUEST-SUBMIT",
      "name": {
        "text": "Submit request form"
      },
      "description": [
        {
          "type": "paragraph",
          "text": "A form with Request code, Quantity, and Submit request. The result area presents confirmation, invalid data, duplicate code, or store failure."
        },
        {
          "type": "paragraph",
          "text": "Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here."
        }
      ],
      "use_case": "UC-REQUEST-SUBMIT",
      "trigger": [
        {
          "type": "paragraph",
          "text": "The requester activates Submit request."
        }
      ],
      "input_mapping": [
        {
          "source": "form.code",
          "target": "UC-REQUEST-SUBMIT.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Maps the Request code field to the case code input."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "form.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-REQUEST-SUBMIT",
            "selector": "code",
            "value_type": "text"
          }
        },
        {
          "source": "form.quantity",
          "target": "UC-REQUEST-SUBMIT.input.quantity",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Maps the Quantity field to the case quantity input."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "form.quantity",
            "value_type": "integer"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-REQUEST-SUBMIT",
            "selector": "quantity",
            "value_type": "integer"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-REQUEST-CONFIRMED",
          "target": "result.confirmation",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The request is retained and confirmed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-CONFIRMED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.confirmation",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-INVALID",
          "target": "result.invalid_data",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The code or quantity is invalid; the request is refused."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.invalid_data",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-STORE-FAILURE",
          "target": "result.store_unavailable",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store reports that it is unavailable."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-STORE-FAILURE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.store_unavailable",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-DENIED",
          "target": "result.out-request-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The actor is absent or not permitted."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.out-request-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-DUPLICATE",
          "target": "result.out-request-duplicate",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The request code is already retained."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-DUPLICATE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.out-request-duplicate",
            "value_type": "outcome"
          }
        }
      ],
      "requirement_refs": [
        "RF-REQUEST-01",
        "RF-REQUEST-02",
        "RF-REQUEST-03",
        "RF-REQUEST-04",
        "RF-REQUEST-05",
        "RF-REQUEST-06",
        "RF-REQUEST-07"
      ],
      "resources": [
        "RES-REQUEST-WIRE",
        "RES-REQUEST-FLOW"
      ],
      "examples": [
        {
          "type": "figure",
          "resource": "RES-REQUEST-WIRE",
          "caption": {
            "text": "Wireframe with Request code, Quantity, and Submit request."
          },
          "alt": {
            "text": "A form with a Request code field, a Quantity field, and a Submit request button."
          }
        }
      ]
    }
  ],
  "assumptions": [
    "ASM-REQUEST-STORE-UNIQUE"
  ],
  "sources": [
    "SRC-REQUEST-BRIEF"
  ],
  "open_issues": [
    "OI-REQUEST-LATENCY"
  ],
  "classification": "illustration"
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/RequestRegister/boundaries/Boundary_RequestRegisterWebForm.py",
    "symbol": "Boundary_RequestRegisterWebForm"
  },
  "class_kind": "boundary_adapter",
  "boundary_semantics": "Interaction interface only; never a test case or observation point.",
  "classification": "illustration",
  "modality": "web",
  "methods": [
    {
      "name": "submit_request_form",
      "exposes_use_case": "UC-REQUEST-SUBMIT",
      "trigger": "The requester activates Submit request.",
      "input_mapping": [
        {
          "source": "form.code",
          "target": "UC-REQUEST-SUBMIT.input.code",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Maps the Request code field to the case code input."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "form.code",
            "value_type": "text"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-REQUEST-SUBMIT",
            "selector": "code",
            "value_type": "text"
          }
        },
        {
          "source": "form.quantity",
          "target": "UC-REQUEST-SUBMIT.input.quantity",
          "meaning": [
            {
              "type": "paragraph",
              "text": "Maps the Quantity field to the case quantity input."
            }
          ],
          "source_endpoint": {
            "kind": "boundary_input",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "form.quantity",
            "value_type": "integer"
          },
          "target_endpoint": {
            "kind": "use_case_input",
            "owner_ref": "UC-REQUEST-SUBMIT",
            "selector": "quantity",
            "value_type": "integer"
          }
        }
      ],
      "result_mapping": [
        {
          "source": "OUT-REQUEST-CONFIRMED",
          "target": "result.confirmation",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The request is retained and confirmed."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-CONFIRMED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.confirmation",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-INVALID",
          "target": "result.invalid_data",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The code or quantity is invalid; the request is refused."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-INVALID",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.invalid_data",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-STORE-FAILURE",
          "target": "result.store_unavailable",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The store reports that it is unavailable."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-STORE-FAILURE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.store_unavailable",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-DENIED",
          "target": "result.out-request-denied",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The actor is absent or not permitted."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-DENIED",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.out-request-denied",
            "value_type": "outcome"
          }
        },
        {
          "source": "OUT-REQUEST-DUPLICATE",
          "target": "result.out-request-duplicate",
          "meaning": [
            {
              "type": "paragraph",
              "text": "The request code is already retained."
            }
          ],
          "source_endpoint": {
            "kind": "use_case_outcome",
            "owner_ref": "OUT-REQUEST-DUPLICATE",
            "selector": "outcome",
            "value_type": "outcome"
          },
          "target_endpoint": {
            "kind": "boundary_result",
            "owner_ref": "INT-REQUEST-SUBMIT",
            "selector": "result.out-request-duplicate",
            "value_type": "outcome"
          }
        }
      ],
      "source_refs": [
        "INT-REQUEST-SUBMIT",
        "RF-REQUEST-01",
        "RF-REQUEST-02",
        "RF-REQUEST-03",
        "RF-REQUEST-04",
        "RF-REQUEST-05",
        "RF-REQUEST-06",
        "RF-REQUEST-07"
      ]
    }
  ]
}
```
