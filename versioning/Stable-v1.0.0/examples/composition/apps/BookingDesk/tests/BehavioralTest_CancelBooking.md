---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TST-BOOKING-CANCEL
kind: behavioral_test
source_refs:
- UC-BOOKING-CANCEL
- AC-BOOKING-CANCEL-01
- AC-BOOKING-CANCEL-02
- AC-BOOKING-CANCEL-03
- AC-BOOKING-CANCEL-FAILURE
- AC-BOOKING-CANCEL-CONTEXT
- AC-BOOKING-CANCEL-AUTH
- AC-BOOKING-CANCEL-QUALITY
generation:
  mode: test
  language: python
  path: apps/BookingDesk/tests/Test_CancelBooking.py
  symbol: Test_CancelBooking
---

# Behavioral tests for Cancel booking

Executable-test design derived from Atlas acceptance criteria. Scenario observations are observation_points, never Boundaries.

## Preserved Atlas semantics

```atlas-source-json
{
  "use_case": "UC-BOOKING-CANCEL",
  "acceptance_criteria": [
    {
      "id": "AC-BOOKING-CANCEL-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "Cancelling an active booking returns cancelled and retains the code."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-02",
        "RF-BOOKING-CANCEL-04"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "Cancelling an already-cancelled booking is refused with no data change."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "A lookup not-found is distinguishable from an already-cancelled refusal."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-01",
        "RF-BOOKING-CANCEL-03"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-FAILURE",
      "statement": [
        {
          "type": "paragraph",
          "text": "An unavailable lookup or save remains a failure; an unknown write is not reported as no change, success, or retried automatically."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-05"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-CONTEXT",
      "statement": [
        {
          "type": "paragraph",
          "text": "A caller allowed to cancel but not to locate is denied by the composed lookup, with the same principal preserved and no save."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-01"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure."
        }
      ],
      "verifies": [
        "RF-BOOKING-CANCEL-AUTH"
      ]
    },
    {
      "id": "AC-BOOKING-CANCEL-QUALITY",
      "statement": [
        {
          "type": "paragraph",
          "text": "In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim."
        }
      ],
      "verifies": [
        "RNF-BOOKING-CANCEL-RESPONSE"
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
    "path": "apps/BookingDesk/tests/Test_CancelBooking.py",
    "symbol": "Test_CancelBooking"
  },
  "class_kind": "behavioral_test",
  "tests_use_case": "UC-BOOKING-CANCEL",
  "scenarios": [
    {
      "id": "SCN-AC-BOOKING-CANCEL-01",
      "source_ref": "AC-BOOKING-CANCEL-01",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Cancelling an active booking returns cancelled and retains the code.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CANCEL-02",
      "source_ref": "AC-BOOKING-CANCEL-02",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Cancelling an already-cancelled booking is refused with no data change.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CANCEL-03",
      "source_ref": "AC-BOOKING-CANCEL-03",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A lookup not-found is distinguishable from an already-cancelled refusal.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CANCEL-FAILURE",
      "source_ref": "AC-BOOKING-CANCEL-FAILURE",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An unavailable lookup or save remains a failure; an unknown write is not reported as no change, success, or retried automatically.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CANCEL-CONTEXT",
      "source_ref": "AC-BOOKING-CANCEL-CONTEXT",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A caller allowed to cancel but not to locate is denied by the composed lookup, with the same principal preserved and no save.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CANCEL-AUTH",
      "source_ref": "AC-BOOKING-CANCEL-AUTH",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CANCEL-QUALITY",
      "source_ref": "AC-BOOKING-CANCEL-QUALITY",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-BOOKING-CANCEL",
    "GRAPH-BOOKING-CANCEL-REFUSAL"
  ]
}
```
