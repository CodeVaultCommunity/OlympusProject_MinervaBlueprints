# Minimal request register

This example preserves the cases and contracts of `ATLAS-EX-MINIMAL`, revision `2`, from Atlas Stable-v1.0.0. L2 construction was editorial and AI-assisted. Project-owner acceptance remains pending.

[Atlas JSON](docs/L1_AtlasSpecifications/example.atlas.json) · [Minerva YAML](docs/L2_MinervaBlueprints/blueprint.yaml) · [Provenance](provenance.json) · [Traceability](traceability.md)

| Case | Behavioral test | Criteria |
| --- | --- | --- |
| UC-REQUEST-SUBMIT | BT-REQUEST-SUBMIT | 7 |

All scenarios are planned. The absence of code and executions is intentional: L2 can be authored before L3. Illustrated source channels remain proposals; their drawings and resources are preserved where present.

```bash
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
```

Run from the edition. The result checks Minerva declarations and hashes; it neither interprets Atlas nor executes the scenarios.
