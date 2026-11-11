---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: MINERVA-TASKBOARD
kind: project
source_refs:
- DOC-TASK-BOARD
generation:
  mode: documentation_only
---

# Task board — create, complete, and list

Project-wide semantics and generation context.

## Preserved Atlas semantics

```atlas-source-json
{
  "document_id": "DOC-TASK-BOARD",
  "title": {
    "text": "Task board — create, complete, and list"
  },
  "revision": "3",
  "spec_version": "Stable-v1.1.0",
  "profile_version": "Stable-v1.1.0",
  "translator_version": "1.1.0",
  "language": "en",
  "status": "draft",
  "authors": [
    {
      "name": {
        "text": "Douglas de Oliveira Alkimim"
      },
      "role": {
        "text": "Specification author"
      }
    }
  ],
  "created": "2026-10-25",
  "updated": "2026-10-28",
  "subtitle": {
    "text": "Synthetic L1 reference for Atlas Specifications"
  },
  "keywords": [
    {
      "text": "Atlas"
    },
    {
      "text": "OAL L1"
    },
    {
      "text": "task board"
    },
    {
      "text": "synthetic example"
    }
  ],
  "structure": [
    {
      "id": "SEC-TASK-CONTEXT",
      "level": 1,
      "title": {
        "text": "Context, scope, and evidence"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "This synthetic board demonstrates the Atlas L1 contract for creating, completing, and listing Tasks. It does not implement a business application or assert independent stakeholder validation.",
          "nature": "note"
        },
        {
          "type": "paragraph",
          "text": "Origin: SRC-TASK-BRIEF is the versioned teaching baseline. The three goals, rules, authorization policy and quality obligations are didactic design choices. No Needs-to-L1 derivation, interview, or named human approval is claimed.",
          "nature": "note"
        },
        {
          "type": "paragraph",
          "text": "Out of scope: editing titles, deleting Tasks, multiple boards, anonymous access, storage technology, authentication mechanisms, transport protocols, screens, and quantitative response-time targets.",
          "nature": "note"
        }
      ],
      "items": [
        "ACT-BOARD-MEMBER",
        "TYP-TASK-STATUS"
      ]
    },
    {
      "id": "SEC-TASK-ENTITIES",
      "level": 1,
      "title": {
        "text": "Entities and canonical rules"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "Entities own meaning and validity; they have no collaborators."
        }
      ],
      "items": [
        "ENT-TASK"
      ]
    },
    {
      "id": "SEC-TASK-TOOLS",
      "level": 1,
      "title": {
        "text": "Abstract tool contracts"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "Tools consume ready entities and define atomicity, failure distinctions and persistence uncertainty without selecting implementations."
        }
      ],
      "items": [
        "TOL-TASK-STORE"
      ]
    },
    {
      "id": "SEC-TASK-CASES",
      "level": 1,
      "title": {
        "text": "Use cases and acceptance"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "Each case declares actor context, functional behavior, flow links, quality obligations, and acceptance criteria."
        }
      ],
      "items": [
        "UC-TASK-CREATE",
        "UC-TASK-COMPLETE",
        "UC-TASK-LIST"
      ]
    },
    {
      "id": "SEC-TASK-INTERACTIONS",
      "level": 1,
      "title": {
        "text": "Illustrative interaction mapping"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "The mappings below show which inputs/results cross the interaction boundary. They are explanatory examples, not a choice of an L4 channel."
        }
      ],
      "items": [
        "BND-TASK-ILLUSTRATION"
      ]
    }
  ],
  "presentation": {
    "markdown": {
      "include_toc": false
    },
    "latex": {
      "documentclass": "article",
      "figure_width": "0.78\\linewidth"
    }
  },
  "extensions": {}
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": null,
  "semantic_role": "distributed_project_metadata",
  "application": "TaskBoard",
  "source_document_id": "DOC-TASK-BOARD",
  "source_revision": "3",
  "language": "en",
  "rule": "This file is not an Atlas appendix. Atlas concepts live in the code-shaped modules listed by the manifest."
}
```
