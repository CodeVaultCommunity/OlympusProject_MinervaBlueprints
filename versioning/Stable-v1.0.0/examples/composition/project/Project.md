---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: MINERVA-BOOKINGDESK
kind: project
source_refs:
- ATLAS-EX-COMPOSITION
generation:
  mode: documentation_only
---

# Booking desk composition

Project-wide semantics and generation context.

## Preserved Atlas semantics

```atlas-source-json
{
  "document_id": "ATLAS-EX-COMPOSITION",
  "title": {
    "text": "Booking desk composition"
  },
  "revision": "2",
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
    "text": "Three use cases sharing an entity, a validation, a tool, and a quality requirement."
  },
  "keywords": [
    {
      "text": "composition"
    },
    {
      "text": "booking"
    },
    {
      "text": "shared validation"
    },
    {
      "text": "case call"
    }
  ],
  "structure": [
    {
      "id": "SEC-BOOK-CONTEXT",
      "level": 1,
      "title": {
        "text": "Context, actors, and scope"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "A booking desk creates, locates, and cancels bookings. The example is a specification, not an application."
        },
        {
          "type": "paragraph",
          "text": "The scope covers these three cases. Payment, customer management, and calendar integration are outside the example."
        },
        {
          "type": "paragraph",
          "text": "This is a synthetic specification example. Source SRC-BOOKING-BRIEF is a teaching baseline, not evidence of stakeholder approval or a claimed Needs-to-L1 derivation."
        }
      ],
      "items": [
        "ACT-BOOKING-CLERK",
        "VOC-BOOKING"
      ]
    },
    {
      "id": "SEC-BOOK-ENTITIES",
      "level": 1,
      "title": {
        "text": "Entity and shared validations"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "The booking entity defines data, states, a transition, and two validations."
        }
      ],
      "items": [
        "TYP-BOOKING-STATUS",
        "ENT-BOOKING"
      ]
    },
    {
      "id": "SEC-BOOK-TOOLS",
      "level": 1,
      "title": {
        "text": "Shared abstract tool"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "One abstract tool serves all three cases through two operations."
        }
      ],
      "items": [
        "TOL-BOOKING-STORE"
      ]
    },
    {
      "id": "SEC-BOOK-CASES",
      "level": 1,
      "title": {
        "text": "Use cases and composition"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "Cancellation calls lookup. The response requirement is defined once and referenced by cancellation."
        }
      ],
      "items": [
        "UC-BOOKING-LOOKUP",
        "UC-BOOKING-CREATE",
        "UC-BOOKING-CANCEL"
      ]
    },
    {
      "id": "SEC-BOOK-BOUNDARIES",
      "level": 1,
      "title": {
        "text": "Interaction boundary"
      },
      "blocks": [
        {
          "type": "paragraph",
          "text": "The command line exposes all three cases and maps their observable outcomes."
        }
      ],
      "items": [
        "BND-BOOKING-CLI"
      ]
    }
  ],
  "presentation": {
    "markdown": {
      "include_toc": false
    },
    "latex": {
      "documentclass": "article",
      "figure_width": "0.62\\linewidth"
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
  "application": "BookingDesk",
  "source_document_id": "ATLAS-EX-COMPOSITION",
  "source_revision": "2",
  "language": "en",
  "rule": "This file is not an Atlas appendix. Atlas concepts live in the code-shaped modules listed by the manifest."
}
```
