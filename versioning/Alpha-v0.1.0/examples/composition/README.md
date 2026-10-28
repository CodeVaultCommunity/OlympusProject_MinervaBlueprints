# Booking desk composition

This example preserves the cases and contracts of `ATLAS-EX-COMPOSITION`, revision `2`, from Atlas Stable-v1.0.0. L2 construction was editorial and AI-assisted. Project-owner acceptance remains pending.

[Atlas JSON](docs/L1_AtlasSpecifications/example.atlas.json) · [Minerva YAML](docs/L2_MinervaBlueprints/blueprint.yaml) · [Provenance](provenance.json) · [Traceability](traceability.md)

| Case | Behavioral test | Criteria |
| --- | --- | --- |
| UC-BOOKING-LOOKUP | BT-BOOKING-LOOKUP | 5 |
| UC-BOOKING-CREATE | BT-BOOKING-CREATE | 6 |
| UC-BOOKING-CANCEL | BT-BOOKING-CANCEL | 7 |

All scenarios are planned. The absence of code and executions is intentional: L2 can be authored before L3. Illustrated source channels remain proposals; their drawings and resources are preserved where present.

```bash
python validator/minerva_validate.py examples/composition/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/composition --json
```

Run from the edition. The result checks Minerva declarations and hashes; it neither interprets Atlas nor executes the scenarios.
