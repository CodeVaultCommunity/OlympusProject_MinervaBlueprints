# Counterexamples

Current-tool fixtures; these are not additional Atlas domain examples.

[Expected results](expected-results.json) · [Runner](check.py)

```bash
python tests/fixtures/counterexamples/check.py --json
```

The runner applies declared mutations to temporary copies of the minimal example and compares expected diagnostics. It neither edits examples nor translates L1 sources.
