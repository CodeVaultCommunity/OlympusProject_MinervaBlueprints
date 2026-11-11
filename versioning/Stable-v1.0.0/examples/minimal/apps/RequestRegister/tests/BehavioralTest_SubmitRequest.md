---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TST-REQUEST-SUBMIT
kind: behavioral_test
source_refs:
- UC-REQUEST-SUBMIT
- AC-REQUEST-01
- AC-REQUEST-02
- AC-REQUEST-03
- AC-REQUEST-04
- AC-REQUEST-05
- AC-REQUEST-06
- AC-REQUEST-SUBMIT-QUALITY
generation:
  mode: test
  language: python
  path: apps/RequestRegister/tests/Test_SubmitRequest.py
  symbol: Test_SubmitRequest
---

# Behavioral tests for Submit request

Executable-test design derived from Atlas acceptance criteria. Scenario observations are observation_points, never Boundaries.

## Preserved Atlas semantics

```atlas-source-json
{
  "use_case": "UC-REQUEST-SUBMIT",
  "acceptance_criteria": [
    {
      "id": "AC-REQUEST-01",
      "statement": [
        {
          "type": "paragraph",
          "text": "A requester with a valid code and quantity of 2 receives a confirmed result; a later lookup of the code returns quantity 2."
        }
      ],
      "verifies": [
        "RF-REQUEST-02",
        "RF-REQUEST-03",
        "RF-REQUEST-05"
      ]
    },
    {
      "id": "AC-REQUEST-02",
      "statement": [
        {
          "type": "paragraph",
          "text": "A quantity of 0 is refused as invalid data, and no record is created."
        }
      ],
      "verifies": [
        "RF-REQUEST-02"
      ]
    },
    {
      "id": "AC-REQUEST-03",
      "statement": [
        {
          "type": "paragraph",
          "text": "An actor absent from the permitted set is refused before validation or store access."
        }
      ],
      "verifies": [
        "RF-REQUEST-01"
      ]
    },
    {
      "id": "AC-REQUEST-04",
      "statement": [
        {
          "type": "paragraph",
          "text": "Submit the same code twice. The second attempt reports duplicate-code refusal and preserves the first retained quantity."
        }
      ],
      "verifies": [
        "RF-REQUEST-06"
      ]
    },
    {
      "id": "AC-REQUEST-05",
      "statement": [
        {
          "type": "paragraph",
          "text": "If a store write has an unknown final outcome, return the failure without claiming success or no write and without automatic retry."
        }
      ],
      "verifies": [
        "RF-REQUEST-04"
      ]
    },
    {
      "id": "AC-REQUEST-06",
      "statement": [
        {
          "type": "paragraph",
          "text": "An empty code is refused before quantity validation and store invocation."
        }
      ],
      "verifies": [
        "RF-REQUEST-07"
      ]
    },
    {
      "id": "AC-REQUEST-SUBMIT-QUALITY",
      "statement": [
        {
          "type": "paragraph",
          "text": "In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim."
        }
      ],
      "verifies": [
        "RNF-REQUEST-01"
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
    "path": "apps/RequestRegister/tests/Test_SubmitRequest.py",
    "symbol": "Test_SubmitRequest"
  },
  "class_kind": "behavioral_test",
  "tests_use_case": "UC-REQUEST-SUBMIT",
  "scenarios": [
    {
      "id": "SCN-AC-REQUEST-01",
      "source_ref": "AC-REQUEST-01",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A requester with a valid code and quantity of 2 receives a confirmed result; a later lookup of the code returns quantity 2.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-REQUEST-02",
      "source_ref": "AC-REQUEST-02",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "A quantity of 0 is refused as invalid data, and no record is created.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-REQUEST-03",
      "source_ref": "AC-REQUEST-03",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An actor absent from the permitted set is refused before validation or store access.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-REQUEST-04",
      "source_ref": "AC-REQUEST-04",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "Submit the same code twice. The second attempt reports duplicate-code refusal and preserves the first retained quantity.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-REQUEST-05",
      "source_ref": "AC-REQUEST-05",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "If a store write has an unknown final outcome, return the failure without claiming success or no write and without automatic retry.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-REQUEST-06",
      "source_ref": "AC-REQUEST-06",
      "given": "Arrange inputs, trusted actor context, concrete-tool doubles/resources, and initial state declared by the case.",
      "when": "Invoke execute through the use-case API or a declared Boundary interaction.",
      "then": "An empty code is refused before quantity validation and store invocation.",
      "observation_points": [
        "returned_outcome",
        "declared_effects",
        "concrete_tool_calls"
      ]
    },
    {
      "id": "SCN-AC-REQUEST-SUBMIT-QUALITY",
      "source_ref": "AC-REQUEST-SUBMIT-QUALITY",
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
    "GRAPH-REQUEST-SUBMIT"
  ]
}
```
