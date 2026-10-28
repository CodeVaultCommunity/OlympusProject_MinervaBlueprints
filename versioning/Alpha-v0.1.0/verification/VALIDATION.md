# Observed validation and limits

[Português](VALIDATION.pt-br.md) · [Commands, environment and input hashes](evidence/checks.json) · [Source review](reviews/contract-review.md)

The revised unpublished Alpha-v0.1.0 was checked on **Windows / CPython 3.12.14**. These results concern tools, source documents and packaging. They are not domain-scenario executions or owner acceptance.

| Check | Observed result | Evidence |
| --- | --- | --- |
| Edition regression suite | 50 tests passed | [Output](evidence/validator-tests.stderr.txt) |
| Repository maintenance | 33 tests passed | [Output](evidence/repository-tests.stdout.txt) |
| Minerva examples | Three main examples and two revision snapshots passed; starter passed structure only | [Reports](evidence/model-examples.stdout.txt) |
| Counterexamples | 12 expected outcomes matched | [Reports](evidence/counterexamples.stdout.txt) |
| Original Atlas inputs | Five source snapshots accepted by the pinned official Atlas tooling, with resource checking | [Commands and individual outputs](evidence/checks.json) |
| Isolated edition | Examples and counterexamples passed from a copy of only the edition and an external working directory | [Examples](evidence/isolated-examples.stdout.txt) · [Fixtures](evidence/isolated-counterexamples.stdout.txt) |
| Python wheel | Built without build isolation, installed with no dependencies into a fresh target; packaged schema and minimal validation passed | [Build](evidence/wheel-build.stdout.txt) · [Smoke check](evidence/wheel-smoke.stdout.txt) |
| Artwork | Eight PNG/SVG pairs checked; two changed model diagrams visually reviewed | [Record](evidence/artwork.json) |

Runtime dependencies were PyYAML 6.0.3 and jsonschema 4.25.1. Repository tests used pytest 9.2.0. Build used build 1.6.1, setuptools 84.2.1 and wheel 0.48.0. Complete versions, commands, timestamps, exit codes and raw stdout/stderr are retained together. Dependencies were already present for the wheel check; this does not prove a fresh network install. The isolated copy intentionally had no parent repository resources.

Regressions exercise restricted YAML, portable roots, opaque source bytes, source hashes, catalogue namespaces and typed origins, case-specific permitted actors, invariant ownership/kind, case/test cardinality, canonical shared obligations, composition authorization, graph integrity/cycles, draft/unsupported states and optional Python symbol inspection without imports. A binary source artifact with a non-Atlas model exercises the absence of an Atlas reader.

## Reproduce

From the edition, with dependencies installed externally:

```bash
python run_examples.py --test
python run_examples.py --all --json
python tests/fixtures/counterexamples/check.py --json
```

From the repository root:

```bash
python scripts/check_repository.py
python -m pytest scripts/tests
python scripts/content_inventory.py --check
```

Declared Python support is 3.11+, but only 3.12.14 on Windows was observed here. The configured Linux/Windows CI matrix is not reported as executed. Model checks establish supported declarations and selected consistency, not faithful catalogue transcription or semantic equivalence. Source review is separately documented. `--verify-code` checks selected bytes/symbols; it neither imports code nor runs the application. All example domain scenarios remain planned and their execution lists are empty. The shared cancellation timing ambiguity remains visible in the contract review.
