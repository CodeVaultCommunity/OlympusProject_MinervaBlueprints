---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: ACT-REQUESTER
kind: actor
source_refs:
- ACT-REQUESTER
generation:
  mode: documentation_only
---

# Requester

A person who submits a request to the register.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "ACT-REQUESTER",
  "name": {
    "text": "Requester"
  },
  "kind": "person",
  "description": [
    {
      "type": "paragraph",
      "text": "A person who submits a request to the register."
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
