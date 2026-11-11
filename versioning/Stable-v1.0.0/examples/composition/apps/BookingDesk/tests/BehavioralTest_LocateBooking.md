---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TST-BOOKING-LOOKUP
kind: behavioral_test
source_refs:
- UC-BOOKING-LOOKUP
- AC-BOOKING-LOOKUP-01
- AC-BOOKING-LOOKUP-02
- AC-BOOKING-LOOKUP-03
- AC-BOOKING-LOOKUP-INVALID
- AC-BOOKING-LOOKUP-AUTH
generation:
  mode: test
  language: python
  path: apps/BookingDesk/tests/Test_LocateBooking.py
  symbol: Test_LocateBooking
---

# Behavioral tests for Locate booking

Executable-test design derived from Atlas acceptance criteria. Scenario observations are observation_points, never Boundaries.

## Preserved Atlas semantics

```atlas-source-json
{
  "use_case": "UC-BOOKING-LOOKUP",
  "acceptance_criteria": [
    {
      "id": "AC-BOOKING-LOOKUP-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "A retained code returns the booking and its current status."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-02"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "An unknown code returns not found, not an empty booking."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-03"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "An unavailable store is distinguished from not found."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-04"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-INVALID",
      "statement": [
        {
          "type": "paragraph",
          "text": "A lowercase or punctuated code fails the canonical code rule and no load is invoked."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-01"
      ]
    },
    {
      "id": "AC-BOOKING-LOOKUP-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure."
        }
      ],
      "verifies": [
        "RF-BOOKING-LOOKUP-AUTH"
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
    "path": "apps/BookingDesk/tests/Test_LocateBooking.py",
    "symbol": "Test_LocateBooking"
  },
  "class_kind": "behavioral_test",
  "tests_use_case": "UC-BOOKING-LOOKUP",
  "scenarios": [
    {
      "id": "SCN-AC-BOOKING-LOOKUP-01",
      "source_ref": "AC-BOOKING-LOOKUP-01",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A retained code returns the booking and its current status.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-LOOKUP-02",
      "source_ref": "AC-BOOKING-LOOKUP-02",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An unknown code returns not found, not an empty booking.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-LOOKUP-03",
      "source_ref": "AC-BOOKING-LOOKUP-03",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An unavailable store is distinguished from not found.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-LOOKUP-INVALID",
      "source_ref": "AC-BOOKING-LOOKUP-INVALID",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A lowercase or punctuated code fails the canonical code rule and no load is invoked.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-LOOKUP-AUTH",
      "source_ref": "AC-BOOKING-LOOKUP-AUTH",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-BOOKING-LOOKUP"
  ]
}
```
