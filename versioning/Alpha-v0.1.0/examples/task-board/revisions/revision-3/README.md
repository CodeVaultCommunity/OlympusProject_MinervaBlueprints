# Task board — create, complete, and list

This example preserves the cases and contracts of `DOC-TASK-BOARD`, revision `3`, from Atlas Stable-v1.0.0. L2 construction was editorial and AI-assisted. Project-owner acceptance remains pending.

[Atlas JSON](docs/L1_AtlasSpecifications/example.atlas.json) · [Minerva YAML](docs/L2_MinervaBlueprints/blueprint.yaml) · [Provenance](provenance.json) · [Traceability](traceability.md)

| Case | Behavioral test | Criteria |
| --- | --- | --- |
| UC-TASK-CREATE | BT-TASK-CREATE | 5 |
| UC-TASK-COMPLETE | BT-TASK-COMPLETE | 7 |
| UC-TASK-LIST | BT-TASK-LIST | 4 |

All scenarios are planned. The absence of code and executions is intentional: L2 can be authored before L3. Illustrated source channels remain proposals; their drawings and resources are preserved where present.

```bash
python validator/minerva_validate.py examples/task-board/revisions/revision-3/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/task-board/revisions/revision-3 --json
```

Run from the edition. The result checks Minerva declarations and hashes; it neither interprets Atlas nor executes the scenarios.
