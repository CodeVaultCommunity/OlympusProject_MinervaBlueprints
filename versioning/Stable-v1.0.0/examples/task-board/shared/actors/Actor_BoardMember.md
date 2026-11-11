---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: ACT-BOARD-MEMBER
kind: actor
source_refs:
- ACT-BOARD-MEMBER
generation:
  mode: documentation_only
---

# Board member

An external person acting as a member of the selected board; concrete caller identity and permissions are resolved separately.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "ACT-BOARD-MEMBER",
  "name": {
    "text": "Board member"
  },
  "kind": "role",
  "description": [
    {
      "type": "paragraph",
      "text": "An external person acting as a member of the selected board; concrete caller identity and permissions are resolved separately."
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
