---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: ACT-BOOKING-CLERK
kind: actor
source_refs:
- ACT-BOOKING-CLERK
generation:
  mode: documentation_only
---

# Booking clerk

A person operating the booking desk.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "ACT-BOOKING-CLERK",
  "name": {
    "text": "Booking clerk"
  },
  "kind": "person",
  "description": [
    {
      "type": "paragraph",
      "text": "A person operating the booking desk."
    }
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": null,
  "role": "trusted_actor_role",
  "permissions": [],
  "generation": "referenced_type_or_policy"
}
```
