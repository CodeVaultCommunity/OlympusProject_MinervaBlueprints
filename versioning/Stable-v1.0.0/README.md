# Minerva Blueprints · Stable-v1.0.0

Minerva is the generation-oriented L2 layer between Atlas Specifications and
Vulcan code. Its semantic source is a **distributed tree of strict Markdown
modules shaped like the future codebase**. It is not a human-oriented manual,
not a central YAML blueprint, and not an Atlas appendix.

## Ecosystem contract

- Atlas Stable-v1.1.0 supplies the complete L1 meaning through
  `atlas-normalized/1.1.0`.
- Every Atlas concept is preserved byte-for-value inside the controlled
  `atlas-source-json` block of the code-shaped module that owns it.
- `minerva-design-json` adds technical information: target file/symbol,
  classes, methods, parameters, call order, collaborators, algorithms,
  failures, effects, dependency injection, and tests.
- Abstract tools remain visible as protocols. Every abstract tool has at least
  one concrete-tool **design** with technology, lifecycle, configuration,
  method behavior, transactions, and error mapping. Minerva contains no
  executable implementation.
- Boundary means only an interaction adapter that exposes use cases. Test
  scenarios use `observation_points`; they never overload Boundary.
- Atlas use-case and entity-validation graphs are preserved as graph modules
  and connected into the knowledge graph.

## Project shape

```text
minerva.project.yaml                 discovery only
project/                            project semantics, vocabulary, decisions
shared/actors/                      actor roles
shared/types/                       shared generation types
apps/<App>/entities/                Entity_*.md
apps/<App>/usecases/<Domain>/       UseCase_*.md
apps/<App>/tools/abstract/          AbstractTool_*.md
apps/<App>/tools/concrete/          Tool_*.md (design, not code)
apps/<App>/boundaries/              Boundary_*.md
apps/<App>/graphs/                  Graph_*.md
apps/<App>/tests/                   BehavioralTest_*.md
apps/<App>/composition/             AppComposition.md
provenance/coverage.json            total Atlas-to-module ledger
knowledge/graph.json                agent navigation graph
```

`minerva.project.yaml` is an index. The Markdown modules are the semantic
authority. Reading all listed modules reconstructs all Atlas semantics plus L2
technical design.

## Controlled module format

Each module has YAML frontmatter with `id`, `kind`, `source_refs`, and a
generation target/mode. It then contains exactly two machine-readable fences:

1. `atlas-source-json`: exact Atlas source semantics owned by the module;
2. `minerva-design-json`: added technical design consumed by a future
   Minerva-to-Vulcan engine.

Prose outside these fences is explanatory and never overrides the controlled
records.

## Import and validation

```powershell
minerva-import-atlas atlas.normalized.json output --app RequestRegister `
  --tool-designs concrete-tools.json
minerva-validate output
```

The importer accepts external concrete-tool design data. If it is absent, the
module is explicitly marked `requires_external_design`; Stable maintained
examples require `complete`. The validator checks source hashes, exact concept
coverage, safe paths, unique generation targets, tool lineage, Boundary
semantics, observation-point terminology, and knowledge-graph coverage.

## Maintained examples

- `examples/minimal`: Request Register.
- `examples/composition`: Booking Desk.
- `examples/task-board`: Task Board.

Each example is generated from the matching Atlas 1.1 normalized hand-off and
then validated independently.

## License

Distributed under the [MIT license](LICENSE).
