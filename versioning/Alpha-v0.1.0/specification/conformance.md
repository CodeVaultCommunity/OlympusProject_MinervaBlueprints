# Conformance and assessment scope

[Português](conformance.pt-br.md) · [Normative rules](model.md) · [OAL correspondence](oal-correspondence.md)

Minerva establishes the subjects of OAL Stable-v1.0.0 L2: ten ADPM subjects and five ADVS subjects. Model rules, artifact conformity, source preservation and observed realization results are separate claims.

| Assessment | What it establishes | What it does not establish |
| --- | --- | --- |
| Schema | Supported Minerva representation and required fields | Consistent links or sufficient behavior |
| Consistency | Declared identities, typed links, source catalogue, case/test correspondence, criterion coverage and graph topology | Truth/completeness of source declarations or semantic equivalence |
| Source integrity | Supplied artifact matches its declared hash | Its identity/revision or requirements are correctly transcribed |
| Code inspection | Requested source bytes and supported Python lexical names | Execution, authorization enforcement or test results |
| Semantic review | Recorded comparison and design assessment within its stated scope | Stakeholder approval or unobserved runtime properties |

`layer_coverage: declared_adpm_and_advs` means both components were inspected. It is not OAL certification. `reviewed` denotes the declared technical review; the responsible party and open issues retain pending owner acceptance. A draft returns inconclusive in consistency mode. A source record alone is not complete ADMV.

The source catalogue is Minerva content with a separate identity namespace. The validator never parses Atlas or any other L1 model. A wrong declaration added consistently to the catalogue can pass; review must compare it with the pinned source. See [Atlas integration](../integrations/atlas/mapping.md).

Out of scope: automatic translation, executable domain applications, L3 architecture conformance, production authentication, real persistence guarantees, hosted CI results and general algorithm proof. Source contracts may be specified and given planned checks before these implementations exist.
