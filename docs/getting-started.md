# Get started with Minerva Blueprints

[Português brasileiro](getting-started.pt-br.md) · [Home](../README.md) · [Selected edition](../versioning/Stable-v1.0.0/README.md)

Minerva Stable-v1.0.0 transforms an Atlas Stable-v1.1.0 normalized hand-off into a distributed tree of strict Markdown modules shaped like the future codebase. The modules collectively preserve all Atlas semantics and add generation-oriented technical design; they are not an Atlas appendix and they contain no executable implementation.

Use Python 3.11 or later. From the repository root:

```bash
python -m pip install -e "versioning/Stable-v1.0.0"
python versioning/Stable-v1.0.0/run_examples.py
python -m pytest versioning/Stable-v1.0.0/tests
```

To import a normalized Atlas document, provide the application name and, when available, external concrete-tool design data:

```bash
minerva-import-atlas atlas.normalized.json output --app RequestRegister --tool-designs concrete-tools.json
minerva-validate output
```

Read `minerva.project.yaml` only for discovery. The Markdown modules are the semantic authority. Each module combines its controlled Atlas source record with technical classes, methods, collaborators, algorithms, failures, effects, injection points, and generation targets. `Boundary` names only interaction adapters; behavioral tests use scenarios and `observation_points`.
