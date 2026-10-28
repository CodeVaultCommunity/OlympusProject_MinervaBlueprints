# Validation evidence and limits

English · [Português brasileiro](VALIDATION.pt-br.md) · [Verification guide](../README.md#verification)

This record describes **observed checks of the candidate edition**, not a claim that every modeled scenario was executed or that the project owner approved the design. Complete commands, times, environment and source hashes are retained in [observed/checks.json](observed/checks.json), with stdout/stderr beside it. The separate [contract review](CONTRACT-REVIEW.md) examines the teaching contracts and evidence links.

## Observed results

| Check | Observed result | Evidence |
| --- | --- | --- |
| Validator regression suite | **44 tests passed** on CPython 3.12.14 / Linux | [Test output](observed/validator-tests.stderr.txt) · [commands/environment](observed/checks.json) |
| Ordinary examples | Minimal, full TaskBoard, planned and legacy passed their declared scopes | [Example reports](observed/model-examples.stdout.txt) |
| Draft starter | Passed structure-only inspection; normal-mode inconclusive behavior tested separately | [Reports](observed/model-examples.stdout.txt) · regression suite |
| Public fixtures | **13 expected outcomes matched**, including invalid, unsupported, inconclusive and valid-cycle inputs | [Output](observed/counterexamples.stdout.txt) |
| Isolated edition | Copy of only this edition executed examples and fixtures from an external working directory | [Isolation record](observed/isolation.json) |
| Python wheel | Local offline build, temporary-target install and minimal validation through the installed package passed; schema included | [Packaging record](packaging.json) |

Declared Python support is 3.11+; this evidence exercises **3.12.14 only**. PyYAML 6.0.3 and jsonschema 4.25.1 were used. The unittest suite does not require pytest; repository distribution checks use their own recorded environment. A configured CI workflow is not evidence that GitHub Actions ran.

## What the regressions establish

Tests exercise duplicate keys and prohibited tags/aliases, deterministic scalar types, source-version/hash pins, missing and duplicate case/test links, criterion ownership/coverage, typed references, canonical-entity validation boundaries, actor categories, composition declarations, graph edges/reachability and legitimate loops, source-local graphs, alternative roots, shared criteria, source drift, draft/operational/unsupported results and JSON CLI output.

A specific regression rejects `Expected.testRun` when `testRun` belongs only to `Other`; symbol inspection follows qualified lexical ownership. Another supplies a Python file whose top-level code would raise on import and demonstrates inspection without importing or executing it. These checks address the **validator**. They are not application-domain behavioral tests; their count does not alter TaskBoard's three directly linked test identities.

## Packaging observation

The default isolated wheel-build attempt could not download setuptools because the environment blocked its network/proxy connection. The successful build used already available setuptools 84.1.0 and wheel 0.48.0 with `--no-build-isolation`; the wheel was installed into a fresh temporary target without downloading runtime packages. Validation then loaded `minerva_blueprints` from that installed target and found its packaged schema.

This supports local packaging/installability with available dependencies. It does not claim a successful fresh network installation, another operating system or all supported Python versions. Build products, caches and temporary installed packages are excluded from the source distribution.

## Reproduce

From this edition with the declared dependencies installed:

```bash
python run_examples.py --all --json
python examples/counterexamples/check.py --json
python run_examples.py --test
```

For offline wheel reproduction, the environment must already provide a compatible setuptools backend and wheel tooling:

```bash
python -m pip wheel . --no-deps --no-build-isolation --wheel-dir /tmp/minerva-wheel
```

A default `python -m pip install .` may need network access for build/runtime dependencies. The direct launcher can instead use an environment where `requirements.txt` is already satisfied.

## Limits and interpretation

- A successful model check establishes supported structure, declared links and selected consistency only. Oracle correctness, complete scenario sufficiency, algorithm equivalence and semantic conformance require review.
- The full Minerva example stores observed companion source records without application code. A current realization claim requires `--verify-code` in the matching companion ecosystem. Absence returns inconclusive when inspection is requested.
- Code inspection checks hashes, Python lexical symbols and declared file coverage. It does not execute applications/tests, prove transaction semantics, validate production authentication or inspect every language.
- Test realization references are not results. `advs.executions` is empty in the teaching blueprints. Actual application execution reports belong to the evaluated realization and configuration.
- The L1 reader is the selected Atlas Stable JSON adapter, not a general derivation engine or the complete Atlas validator.
- Sources, documentary corrections, review authority and unresolved limitations remain visible. This evidence is neither blanket OAL certification nor project-owner approval.
