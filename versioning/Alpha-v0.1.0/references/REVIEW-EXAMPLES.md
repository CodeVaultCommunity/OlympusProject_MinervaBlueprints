# Composition, persistence and change review

English · [Português brasileiro](REVIEW-EXAMPLES.pt-br.md)

These are **illustrative design excerpts**, not extra cases in the TaskBoard source or claims that the excerpted program was executed. They demonstrate review obligations that a structural validator cannot decide by itself.

<a id="case-composition"></a>
## Case composition with two authorization decisions

Assume a separate L1 specification explicitly defines `UC-REPORT-EXPORT` with permission `reports:export`, and `UC-REPORT-READ` with permission `reports:read`. Export needs the read case's data. Model both as ordinary source cases, each with its own directly linked behavioral test. Declare the dependency from export to read and state that the same resolved actor context is forwarded. A composition point injects the read case; the export case does not discover it through a global registry.

```text
exportReport(actor_context, report_id)
  authorize actor_context for reports:export; deny before protected effects
  report = read_case.readReport(actor_context, report_id)
  construct the authorized export from report
  return the export result

readReport(actor_context, report_id)
  authorize actor_context for reports:read; deny before protected effects
  use the declared read tool and return its contract result
```

| Context | Export decision | Read decision | Required observation |
| --- | --- | --- | --- |
| Both permissions | Allow | Allow | Export matches the authorized read result |
| Export only | Allow | Deny | No protected read and no export produced |
| Read only | Deny | Not invoked | Neither called case nor tool is accessed |
| Missing or unresolved | Deny | Not invoked | No domain/storage effect |

If acting on behalf of another participant is required, the L1/L2 contract needs an explicit delegation policy, scope and trust source. Replacing the context with a privileged actor merely because the call is internal violates the composition contract. Separate tests in `tests/test_validation.py` check that a declared case dependency requires forwarded context; those structural tests do not implement this hypothetical report scenario.

## Contextual conditions and ambiguous writes

A ready `Task` is already internally valid. A storage tool must not repeat title-length validation before saving it. A raw row being hydrated still goes through canonical entity construction. Global atomic uniqueness, an expected storage revision or resource existence may be distinct contextual conditions when their own contract states the object, purpose and owner.

| Situation | Correctly limited claim |
| --- | --- |
| Canonical construction rejects raw title before opening storage | No insertion was attempted by that operation |
| Injected connection failure occurs before any database access | No write occurred in that controlled fixture |
| Remote acknowledgement is lost after a write was submitted | Outcome may be unknown; failure alone cannot establish absence of effect |
| Atomic uniqueness is required | A pre-query alone cannot establish the guarantee under concurrency |

The TaskBoard scenarios use local SQLite and an injected **pre-connection** failure. They do not implement the last two contracts or claim recovery of unknown distributed outcomes. A project that needs those guarantees must specify them and add relevant scenarios and evidence.

<a id="change-impact"></a>
## Keep intended meaning when code diverges

The public [observed-drift fixture](../examples/counterexamples/observed-drift.yaml) retains the intended operation “return one” and a hash of its observed baseline. The supplied [current source](../examples/counterexamples/apps/Drift/Example.py) returns two. `--verify-code` reports `CODE_HASH_MISMATCH`. It does not rewrite the blueprint to bless the changed code and it does not pretend a hash comparison established the behavioral difference.

A reviewer follows these steps:

1. Identify which source bytes, symbols and logical IDs changed. Retain both the prior intent and the new observation.
2. Decide whether the change is a defect, an implementation refinement preserving the contract, or a proposed requirement/design change.
3. For a contract change, identify the affected L1 cases/criteria, L2 entity/tool rules and scenarios, L3 realization/tests and any L4 projection. Obtain the appropriate review before changing their authoritative contracts.
4. For an accepted rename without semantic change, preserve logical IDs and update paths, mirror location and observed hash. For an accepted semantic change, revise the document and affected contracts explicitly.
5. Revalidate references and coverage, then execute relevant realization checks. Record actual revision, configuration and result; unresolved effects remain gaps.

For example, raising the title limit from 120 to 200 is a contract proposal affecting the L1 invalid-title criterion, the canonical title rule, construction, length-limit scenarios and source observations. Merely changing `ValueObject_TaskTitle` and updating a hash would hide the outstanding decision. Adding an unrelated internal comment changes the hash but may preserve all semantic contracts; the reviewer can record that narrower conclusion after inspection.

## Review authority

The example's `reviewed` state denotes the declared technical review of this alpha candidate. It does not mean Douglas de Oliveira Alkimim approved the delivery. The responsible-party prose and open issue retain that pending owner review. A consuming project must replace the example's provenance with the real author/reviewer and actual source decisions; copying a teaching example is not approval of its requirements.
