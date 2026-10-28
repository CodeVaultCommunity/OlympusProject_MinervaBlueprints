# Minerva Blueprints · Alpha-v0.1.0

[Português brasileiro](README.pt-br.md)

Minerva is the Olympus Project model for **OAL L2 / ADMV: program modeling (ADPM) and verification specification (ADVS)**. This self-contained, unpublished Alpha contains the model, YAML profile, reference validator and Atlas-aligned examples. It includes no Atlas reader or translation engine; a future translation engine is a separate project.

## Read and adopt

- [Normative model](specification/model.md) — stable MIN rule IDs; English is authoritative.
- [Conformance and limits](specification/conformance.md) · [OAL correspondence](specification/oal-correspondence.md).
- [YAML profile and starter](implementations/yaml/README.md).
- [Atlas mapping](integrations/atlas/mapping.md) · [Compatibility](integrations/atlas/compatibility.json).
- [Official-source examples](examples/README.md) · [Requirements](verification/REQUIREMENTS.md).
- [Technical review](verification/reviews/contract-review.md) · [Observed checks](verification/VALIDATION.md).

<a id="quick-start"></a>
## Quick start

Use Python 3.11+. Run from this edition directory, with dependencies installed in an environment outside the delivery tree:

```bash
python -m pip install .
python run_examples.py --all
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
python tests/fixtures/counterexamples/check.py
python run_examples.py --test
```

The installed command is `minerva-validate`; `python -m minerva_blueprints` uses the same entry point. Alternatively, install `requirements.txt` and use the edition-local launcher. No command selects another edition, downloads source models or executes application code implicitly.

The source catalogue is authored Minerva content. Validation checks its internal references and the hash of the opaque L1 artifact. Source preservation is assessed separately in the recorded review. Example scenarios remain planned; test results concern the validator unless explicitly identified otherwise.

<a id="release-notes"></a>
## Unpublished revision

The owner authorized editing Alpha-v0.1.0 in place before publication. Model/profile/tool identities remain `Alpha-v0.1.0` / `0.1.0` / `0.1.0a0`. This revision reorganizes the manual, removes the source-specific adapter and replaces the former teaching instances with the official Atlas examples. Earlier unpublished drafts are not a compatibility promise.

Each edition owns its package, schema, starter, examples, tests and evidence. `specification/` defines rules; `implementations/` describes representation; `integrations/` documents mappings; `verification/` separates requirements, pinned sources, reviews and observed evidence. The root owns presentation artwork and distribution tooling.
