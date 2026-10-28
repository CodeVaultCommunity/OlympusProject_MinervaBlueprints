# Public counterexamples and expected outcomes

English · [Português brasileiro](README.pt-br.md)

These fixtures deliberately contain invalid data or limited claims. They are **inputs under test**, not approved application blueprints. [expected-results.json](expected-results.json) declares the expected exit code and diagnostic. [check.py](check.py) runs the real reader/validator and compares actual outputs; it never executes the code described in YAML.

From the edition directory:

```bash
python examples/counterexamples/check.py --json
```

| Fixture | Expected result |
| --- | --- |
| missing-behavioral-test.yaml | 1 · TEST_BIJECTION |
| duplicate-behavioral-test.yaml | 1 · TEST_BIJECTION |
| duplicate-id.yaml | 1 · ID_DUPLICATE |
| wrong-reference-kind.yaml | 1 · REF_WRONG_TYPE |
| uncovered-criterion.yaml | 1 · CRITERION_UNCOVERED |
| entity-revalidation.yaml | 1 · ENTITY_REVALIDATION |
| broken-graph.yaml | 1 · GRAPH_EDGE |
| unsupported-profile.yaml | 2 · PROFILE_UNSUPPORTED |
| duplicate-yaml-key.yaml | 1 · YAML_INVALID |
| unsafe-tag.yaml | 1 · YAML_INVALID; executable-looking tag is not executed |
| draft-is-inconclusive.yaml | 4 · DRAFT_INCOMPLETE |
| legitimate-cycle.yaml | 0 · legitimate state-machine self-loop retained |
| observed-drift.yaml | 1 · CODE_HASH_MISMATCH with code inspection |

The drift fixture retains its intended “return one” semantics and original snapshot while current code returns two. Its expected failure does not automatically change the design. The cycle fixture is deliberately valid: rejecting every cycle would incorrectly reject idempotent state transitions. Some invalid fixtures produce more than one diagnostic; the named diagnostic is required and the runner does not hide additional failures.

The runner's own exit 0 means **all expectations matched**, including expected invalid/unsupported/inconclusive outcomes. It does not mean every fixture was valid. Actual execution evidence is recorded separately under the edition's verification folder. The unit suite adds tests for qualified Python symbol ownership, alternate documentary roots, source-local graph references, shared criteria and read-only inspection.
