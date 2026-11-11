---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TST-BOOKING-CREATE
kind: behavioral_test
source_refs:
- UC-BOOKING-CREATE
- AC-BOOKING-CREATE-01
- AC-BOOKING-CREATE-02
- AC-BOOKING-CREATE-03
- AC-BOOKING-CREATE-TITLE
- AC-BOOKING-CREATE-AUTH
- AC-BOOKING-CREATE-QUALITY
generation:
  mode: test
  language: python
  path: apps/BookingDesk/tests/Test_CreateBooking.py
  symbol: Test_CreateBooking
---

# Behavioral tests for Create booking

Executable-test design derived from Atlas acceptance criteria. Scenario observations are observation_points, never Boundaries.

## Preserved Atlas semantics

```atlas-source-json
{
  "use_case": "UC-BOOKING-CREATE",
  "acceptance_criteria": [
    {
      "id": "AC-BOOKING-CREATE-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "A valid code creates an active booking and a later lookup returns it."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-02",
        "RF-BOOKING-CREATE-04"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "An invalid code is refused with no retained booking."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-01"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "A version conflict is never presented as a created booking."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-03"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-TITLE",
      "statement": [
        {
          "type": "paragraph",
          "text": "A whitespace-only title is refused and OP-BOOKING-SAVE is not invoked."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-TITLE"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure."
        }
      ],
      "verifies": [
        "RF-BOOKING-CREATE-AUTH"
      ]
    },
    {
      "id": "AC-BOOKING-CREATE-QUALITY",
      "statement": [
        {
          "type": "paragraph",
          "text": "In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim."
        }
      ],
      "verifies": [
        "RNF-BOOKING-CREATE-RESPONSE"
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
    "path": "apps/BookingDesk/tests/Test_CreateBooking.py",
    "symbol": "Test_CreateBooking"
  },
  "class_kind": "behavioral_test",
  "tests_use_case": "UC-BOOKING-CREATE",
  "scenarios": [
    {
      "id": "SCN-AC-BOOKING-CREATE-01",
      "source_ref": "AC-BOOKING-CREATE-01",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A valid code creates an active booking and a later lookup returns it.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CREATE-02",
      "source_ref": "AC-BOOKING-CREATE-02",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An invalid code is refused with no retained booking.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CREATE-03",
      "source_ref": "AC-BOOKING-CREATE-03",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A version conflict is never presented as a created booking.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CREATE-TITLE",
      "source_ref": "AC-BOOKING-CREATE-TITLE",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A whitespace-only title is refused and OP-BOOKING-SAVE is not invoked.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-BOOKING-CREATE-AUTH",
      "source_ref": "AC-BOOKING-CREATE-AUTH",
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
      "id": "SCN-AC-BOOKING-CREATE-QUALITY",
      "source_ref": "AC-BOOKING-CREATE-QUALITY",
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
    "GRAPH-BOOKING-CREATE"
  ]
}
```
