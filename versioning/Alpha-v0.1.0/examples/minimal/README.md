# Minimal selected-scope blueprint

English · [Português brasileiro](README.pt-br.md)

This example selects only **UC-TASK-002**, the list operation, from the pinned [didactic Atlas source](docs/L1_AtlasSpecifications/task-board.atlas.json). The source still contains its original three cases; `source_l1.case_ids` makes the one-case L2 scope explicit. The [blueprint](docs/L2_MinervaBlueprints/blueprint.yaml) contains program contracts, entity/tool rules, context authorization, a directly linked behavioral test, criteria coverage, positive/denied/empty scenarios and a storage-failure scenario. It is a small selected scope, not a complete realization of every source case.

No code files are supplied or claimed by its declared mirror. Source records are not a prerequisite to reason about the program before implementation. Supporting checks identify intended realizations separately from results; no execution is claimed here.

From the edition directory:

```bash
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
```

Expected result: exit 0, one program case, one directly linked behavioral test and three criteria. Review the actor trust premise, insertion-order guarantee, distinction between confirmed empty storage and failure, and the absence of writes during listing. Structural success does not prove those claims against code.
