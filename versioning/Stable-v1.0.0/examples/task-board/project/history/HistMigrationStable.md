---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: HIST-MIGRATION-STABLE
kind: history_entry
source_refs:
- HIST-MIGRATION-STABLE
generation:
  mode: documentation_only
---

# HIST-MIGRATION-STABLE

Explicit editorial migration from Atlas Alpha-v0.1.0 revision 1 to Atlas Stable-v1.1.0 revision 2. Model/profile/envelope and producer identities change; existing concept IDs, domain contracts, authored history and resources are retained. This is not format conversion, a Needs-to-L1 derivation, or new stakeholder approval.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "HIST-MIGRATION-STABLE",
  "version": "2",
  "date": "2026-10-25",
  "description": [
    {
      "type": "paragraph",
      "text": "Explicit editorial migration from Atlas Alpha-v0.1.0 revision 1 to Atlas Stable-v1.1.0 revision 2. Model/profile/envelope and producer identities change; existing concept IDs, domain contracts, authored history and resources are retained. This is not format conversion, a Needs-to-L1 derivation, or new stakeholder approval."
    }
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": null,
  "class_kind": "provenance_or_constraint",
  "generation": "documentation_or_code_comment"
}
```
