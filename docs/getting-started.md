# Author a Minerva blueprint

[Português](getting-started.pt-br.md) · [Edition](../versioning/Alpha-v0.1.0/README.md)

1. Read the [minimal Atlas source](../versioning/Alpha-v0.1.0/examples/minimal/docs/L1_AtlasSpecifications/example.atlas.json). It specifies request submission, not TaskBoard listing. Note exact code preservation, positive integer quantity, authorization before collaborators, duplicate refusal and unknown-write outcomes.
2. Read the [example overview](../versioning/Alpha-v0.1.0/examples/minimal/README.md), then locate `source_l1`, `adpm.cases` and `advs.behavioral_tests` in its blueprint. There is one source case, one program case and one logical behavioral test, with several scenarios.
3. Copy the [starter](../versioning/Alpha-v0.1.0/implementations/yaml/starter.minerva.yaml). Identify source bytes, revision, scope and author. Declare the source catalogue after reviewing the source; it is not automatically imported.
4. Write entities, canonical rules, tool capability contracts and the case algorithm. Record added design decisions explicitly. Keep concrete database and channel choices separate.
5. Define scenarios with preparation, actor context, action, expected result/effects, boundary and configuration. Link criteria, rules and requirements. Shared quality obligations keep one canonical supporting check.
6. Validate structure, then consistency. Review source fidelity separately. Keep a draft while substantive information is missing; technical review does not imply stakeholder approval.
7. Add planned source bindings when a code design exists. `--verify-code` checks bytes and supported lexical names only. Execute realization tests separately and record actual evidence.

```bash
cd versioning/Alpha-v0.1.0
python validator/minerva_validate.py implementations/yaml/starter.minerva.yaml --structure-only
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
```

No reader or translation engine is included. The [profile](../versioning/Alpha-v0.1.0/implementations/yaml/README.md) defines supported fields and the [assessment guide](../versioning/Alpha-v0.1.0/specification/conformance.md) defines what each result means.
