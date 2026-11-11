---
format: minerva-markdown/1.0.0
model_version: Stable-v1.0.0
id: TYP-BOOKING-STATUS
kind: type
source_refs:
- TYP-BOOKING-STATUS
generation:
  mode: code
  language: python
  path: apps/BookingDesk/types/Type_BookingStatus.py
  symbol: Type_BookingStatus
---

# Booking status

Preserves Atlas type TYP-BOOKING-STATUS.

## Preserved Atlas semantics

```atlas-source-json
{
  "id": "TYP-BOOKING-STATUS",
  "name": {
    "text": "Booking status"
  },
  "definition": [
    {
      "type": "paragraph",
      "text": "The lifecycle state of a booking."
    }
  ],
  "constraints": [
    {
      "type": "paragraph",
      "text": "Known values are active and cancelled."
    }
  ],
  "examples": [
    {
      "text": "active"
    },
    {
      "text": "cancelled"
    }
  ]
}
```

## Generation-oriented design

```minerva-design-json
{
  "target": {
    "language": "python",
    "path": "apps/BookingDesk/types/Type_BookingStatus.py",
    "symbol": "Type_BookingStatus"
  },
  "class_kind": "value_type",
  "base": null,
  "constraints": [
    {
      "type": "paragraph",
      "text": "Known values are active and cancelled."
    }
  ]
}
```
