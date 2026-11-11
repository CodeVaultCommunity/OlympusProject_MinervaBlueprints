---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TST-TASK-COMPLETE
kind: behavioral_test
source_refs:
- UC-TASK-COMPLETE
- AC-TASK-COMPLETE-AUTH
- AC-TASK-COMPLETE-SUCCESS
- AC-TASK-COMPLETE-MISSING
- AC-TASK-COMPLETE-INVALID
- AC-TASK-COMPLETE-ALREADY
- AC-TASK-COMPLETE-CONFLICT
- AC-TASK-COMPLETE-UNKNOWN
generation:
  mode: test
  language: python
  path: apps/TaskBoard/tests/Test_CompleteTask.py
  symbol: Test_CompleteTask
---

# Behavioral tests for Complete task

Executable-test design derived from Atlas acceptance criteria. Scenario observations are observation_points, never Boundaries.

## Preserved Atlas semantics

```atlas-source-json
{
  "use_case": "UC-TASK-COMPLETE",
  "acceptance_criteria": [
    {
      "id": "AC-TASK-COMPLETE-AUTH",
      "statement": [
        {
          "type": "paragraph",
          "text": "Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-AUTH"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-SUCCESS",
      "statement": [
        {
          "type": "paragraph",
          "text": "For TASK001 open at revision zero, completion returns the same identifier/title, completed status and revision one; later listing reflects that state."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-TRANSITION",
        "RF-TASK-COMPLETE-WRITE"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-MISSING",
      "statement": [
        {
          "type": "paragraph",
          "text": "A confirmed absent identifier produces not-found without calling OP-TASK-COMPLETE."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-LOAD"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-INVALID",
      "statement": [
        {
          "type": "paragraph",
          "text": "An empty or whitespace-only identifier is refused before load or completion tools are invoked."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-ID"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-ALREADY",
      "statement": [
        {
          "type": "paragraph",
          "text": "A ready completed Task produces already-completed refusal and no write; its revision remains unchanged."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-TRANSITION"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-CONFLICT",
      "statement": [
        {
          "type": "paragraph",
          "text": "Change the retained revision between load and completion. Return VERSION_CONFLICT, preserving the competing state."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-WRITE",
        "RNF-TASK-COMPLETE-ATOMICITY"
      ]
    },
    {
      "id": "AC-TASK-COMPLETE-UNKNOWN",
      "statement": [
        {
          "type": "paragraph",
          "text": "Lose the completion confirmation after issuing a write. Return unknown without success/no-change claims or automatic retry."
        }
      ],
      "verifies": [
        "RF-TASK-COMPLETE-FAILURE"
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
    "path": "apps/TaskBoard/tests/Test_CompleteTask.py",
    "symbol": "Test_CompleteTask"
  },
  "class_kind": "behavioral_test",
  "tests_use_case": "UC-TASK-COMPLETE",
  "scenarios": [
    {
      "id": "SCN-AC-TASK-COMPLETE-AUTH",
      "source_ref": "AC-TASK-COMPLETE-AUTH",
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
      "id": "SCN-AC-TASK-COMPLETE-SUCCESS",
      "source_ref": "AC-TASK-COMPLETE-SUCCESS",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "For TASK001 open at revision zero, completion returns the same identifier/title, completed status and revision one; later listing reflects that state.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-COMPLETE-MISSING",
      "source_ref": "AC-TASK-COMPLETE-MISSING",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A confirmed absent identifier produces not-found without calling OP-TASK-COMPLETE.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-COMPLETE-INVALID",
      "source_ref": "AC-TASK-COMPLETE-INVALID",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An empty or whitespace-only identifier is refused before load or completion tools are invoked.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-COMPLETE-ALREADY",
      "source_ref": "AC-TASK-COMPLETE-ALREADY",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A ready completed Task produces already-completed refusal and no write; its revision remains unchanged.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-COMPLETE-CONFLICT",
      "source_ref": "AC-TASK-COMPLETE-CONFLICT",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Change the retained revision between load and completion. Return VERSION_CONFLICT, preserving the competing state.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-TASK-COMPLETE-UNKNOWN",
      "source_ref": "AC-TASK-COMPLETE-UNKNOWN",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Lose the completion confirmation after issuing a write. Return unknown without success/no-change claims or automatic retry.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    }
  ],
  "graph_refs": [
    "GRAPH-TASK-COMPLETE"
  ]
}
```
