# Atlas Stable-v1.1.0 → Minerva Stable-v1.0.0

The normative transfer is `atlas-normalized/1.1.0`. `/atlas` is lossless;
`/concepts` and `/relations` are indexes. Minerva imports the transfer and
distributes semantics as follows:

| Atlas concept | Minerva owner |
| --- | --- |
| document metadata/structure | `project/Project.md` |
| actor/type/term | `shared/` or `project/vocabulary/` |
| entity + fields + validations | `apps/<App>/entities/Entity_*.md` |
| abstract tool + operations | `apps/<App>/tools/abstract/AbstractTool_*.md` |
| use case + outcomes + RF/RNF + acceptance | `apps/<App>/usecases/**/UseCase_*.md` |
| Boundary + interactions + typed mappings | `apps/<App>/boundaries/Boundary_*.md` |
| graph nodes/edges | `apps/<App>/graphs/Graph_*.md` |
| sources/assumptions/decisions/history/resources | `project/**` |

Concrete-tool modules are an L2 addition and must reference the abstract tool
they implement. The coverage ledger proves that no Atlas concept was omitted;
it is evidence, not the semantic source.
