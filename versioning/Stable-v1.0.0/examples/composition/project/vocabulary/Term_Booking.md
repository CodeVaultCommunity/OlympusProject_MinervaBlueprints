---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: VOC-BOOKING
kind: term
source_refs:
- VOC-BOOKING
generation:
  mode: documentation_only
---

# Booking

Preserves Atlas term VOC-BOOKING.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "VOC-BOOKING",
  "term": {
    "text": "Booking"
  },
  "definition": [
    {
      "type": "paragraph",
      "text": "A retained reservation with a code, title, and lifecycle status."
    }
  ],
  "synonyms": []
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": null,
  "role": "ubiquitous_language",
  "generation": "naming_constraint"
}
```
