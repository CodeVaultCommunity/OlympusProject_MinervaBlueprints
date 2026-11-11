---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TST-TASK-CREATE
kind: behavioral_test
source_refs:
- UC-TASK-CREATE
- AC-TASK-CREATE-AUTH
- AC-TASK-CREATE-SUCCESS
- AC-TASK-CREATE-INVALID
- AC-TASK-CREATE-DUPLICATE
- AC-TASK-CREATE-UNKNOWN
generation:
  mode: test
  language: python
  path: apps/TaskBoard/tests/Test_CreateTask.py
  symbol: Test_CreateTask
---

# Behavioral tests for Create task

Executable-test design derived from Atlas acceptance criteria. Scenario observations are observation_points, never Boundaries.

## Preserved Atlas semantics

```atlas-source-json
{
  "use_case": "UC-TASK-CREATE",
  "acceptance_criteria": [
    {
      "id": "AC-TASK-CREATE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-AUTH"
      ]
    },
    {
      "id": "AC-TASK-CREATE-SUCCESS",
      "statement": [
        {
          "type": "paragraph",
          "text": "With trusted create permission and unused TASK001 / Review Atlas, receive the exact open Task at revision zero; a later successful list includes it once."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-DATA",
        "RF-TASK-CREATE-RETAIN",
        "RNF-TASK-CREATE-RETENTION"
      ]
    },
    {
      "id": "AC-TASK-CREATE-INVALID",
      "statement": [
        {
          "type": "paragraph",
          "text": "An empty title or whitespace-only identifier is refused before OP-TASK-CREATE is invoked."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-DATA"
      ]
    },
    {
      "id": "AC-TASK-CREATE-DUPLICATE",
      "statement": [
        {
          "type": "paragraph",
          "text": "Creating TASK001 twice retains the first Task unchanged and returns duplicate-identifier refusal on the second attempt."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-DUPLICATE"
      ]
    },
    {
      "id": "AC-TASK-CREATE-UNKNOWN",
      "statement": [
        {
          "type": "paragraph",
          "text": "Inject a write with lost confirmation. The case reports unknown; it does not claim no write, report success, or initiate a retry."
        }
      ],
      "verifies": [
        "RF-TASK-CREATE-FAILURE"
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
    "path": "apps/TaskBoard/tests/Test_CreateTask.py",
    "symbol": "Test_CreateTask"
  },
  "class_kind": "behavioral_test",
  "tests_use_case": "UC-TASK-CREATE",
  "scenarios": [
    {
      "id": "SCN-AC-TASK-CREATE-AUTH",
      "source_ref": "AC-TASK-CREATE-AUTH",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-CREATE-SUCCESS",
      "source_ref": "AC-TASK-CREATE-SUCCESS",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "With trusted create permission and unused TASK001 / Review Atlas, receive the exact open Task at revision zero; a later successful list includes it once.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-CREATE-INVALID",
      "source_ref": "AC-TASK-CREATE-INVALID",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An empty title or whitespace-only identifier is refused before OP-TASK-CREATE is invoked.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-CREATE-DUPLICATE",
      "source_ref": "AC-TASK-CREATE-DUPLICATE",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Creating TASK001 twice retains the first Task unchanged and returns duplicate-identifier refusal on the second attempt.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-CREATE-UNKNOWN",
      "source_ref": "AC-TASK-CREATE-UNKNOWN",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Inject a write with lost confirmation. The case reports unknown; it does not claim no write, report success, or initiate a retry.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-TASK-CREATE"
  ]
}
```
