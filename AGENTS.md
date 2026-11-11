# Agent guide for Minerva Blueprints

## Select the edition

Respect an explicitly requested edition. Otherwise select the highest numeric
Stable edition under `versioning/`. Stable-v1.0.0 is the current edition;
Alpha-v0.1.0 is historical and must not be silently used as a generator or
contract for Stable work.

## Preserve the distributed source of truth

For Stable-v1.0.0, `minerva.project.yaml` is discovery only. The listed strict
Markdown modules are the semantic authority. Never move Atlas content into a
central appendix or replace the modules with a summary blueprint.

Every module contains one exact `atlas-source-json` record and one added
`minerva-design-json` record. Together the modules must preserve the complete
Atlas normalized hand-off and add generation-ready technical detail. Keep
paths, IDs, source references, methods, collaborators, algorithms, failures,
effects, and generation targets explicit.

Abstract tools remain protocols. Concrete tools are technical Markdown designs
with technology, lifecycle, configuration, transaction behavior, and error
mapping; Minerva must not contain their executable implementation.

`Boundary` means only an interaction interface that exposes use cases. Test
scenarios and instrumentation use `observation_points`. Preserve use-case and
entity-validation graphs and keep the knowledge graph complete.

## Maintain and verify

Edit the Atlas importer or external concrete-tool design inputs before
regenerating importer-owned example trees. Run `python run_examples.py` and
`python -m unittest discover -s tests -v` from the selected edition. A valid
project proves structural/traceability consistency, not stakeholder approval.

Keep English and Portuguese aligned. Preserve upstream editions and the exact
normalized Atlas payload. Do not publish, tag, push, or replace historical
edition bytes without explicit authorization.
