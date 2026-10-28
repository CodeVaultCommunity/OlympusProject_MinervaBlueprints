<p align="center"><img src="assets/minerva-banner-en.png" alt="Minerva Blueprints · Olympus Project · Alpha-v0.1.0" width="100%"></p>

# Minerva Blueprints

[Português brasileiro](README.pt-br.md)

**An OAL L2 / ADMV model for program modeling and verification specification.** ADPM and ADVS remain connected through contracts, rules, dependencies, scenarios and traceability.

This Alpha is unpublished and was revised in place with owner authorization. It includes a YAML profile and reference validator. **It includes no Atlas reader or translation engine.** Its examples are L2 elaborations of the same official Atlas examples; any future engine is a separate project.

[Start here](docs/getting-started.md) · [Alpha-v0.1.0](versioning/Alpha-v0.1.0/README.md) · [Normative model](versioning/Alpha-v0.1.0/specification/model.md)

## Position in Olympus

![OAL layers](assets/minerva-oal-position-en.png)

Atlas supplies L1 when adopted; Minerva establishes L2; Vulcan may organize the L3 realization. Interaction choices belong to L4. An application can use root `docs/` with adopted materials in `L1_AtlasSpecifications`, `L2_MinervaBlueprints`, `L3_Vulcan` and `Shared`.

![ADPM and ADVS](assets/minerva-model-en.png)

## Examples and integration

- [Minimal request register](versioning/Alpha-v0.1.0/examples/minimal/README.md)
- [TaskBoard](versioning/Alpha-v0.1.0/examples/task-board/README.md), [revisions 2 / 3](versioning/Alpha-v0.1.0/examples/task-board/revisions/README.md)
- [Booking composition](versioning/Alpha-v0.1.0/examples/composition/README.md)
- [Atlas mapping](versioning/Alpha-v0.1.0/integrations/atlas/mapping.md)

Source contracts, IDs and criteria are preserved; application code and domain executions are not supplied. Validation checks Minerva declarations and source integrity. Semantic review is separate.

## Usage and organization

```bash
cd versioning/Alpha-v0.1.0
python -m pip install .
python run_examples.py --all
```

Use Python 3.11+ in an environment outside the delivery tree. `specification/` contains rules; `implementations/`, the profile; `integrations/`, mappings; `minerva_blueprints/`, tooling; `examples/` and `tests/`, demonstrations and checks; `verification/`, sources, review and evidence. Each edition is self-contained.

![Workflow](assets/minerva-workflow-en.png)

[Verification](versioning/Alpha-v0.1.0/verification/VALIDATION.md) · [Release procedure](docs/releasing.md) · [Assets](assets/README.md) · [Acknowledgements](ACKNOWLEDGEMENTS.md)

After extracting a distribution, run `python scripts/check_archive.py .` before creating caches inside it. In a Git checkout, use `python scripts/content_inventory.py --check`.

Douglas de Oliveira Alkimim · Olympus Project · [MIT](LICENSE)
