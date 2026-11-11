# Stable-v1.0.0 release verification

This local edition establishes the first stable Minerva contract. No remote
tag, release, push, or stakeholder approval is asserted.

## Delivered contract

- Atlas input: `atlas-normalized/1.1.0` from Atlas Stable-v1.1.0.
- Semantic authority: distributed code-shaped Markdown modules, never a
  central appendix.
- Controlled module records: exact `atlas-source-json` plus added
  `minerva-design-json`.
- Complete abstract/concrete tool design lineage without executable L2 code.
- Boundary reserved for interaction adapters; tests use `observation_points`.
- Preserved use-case/entity-validation graphs and agent knowledge graph.

## Maintained evidence

| Example | Markdown modules | Atlas concepts | Concrete tools | Generation targets |
| --- | ---: | ---: | ---: | ---: |
| Minimal | 22 | 91 | 1 | 7 |
| Composition | 26 | 199 | 1 | 12 |
| Task board | 28 | 187 | 1 | 12 |

`python -m unittest discover -s tests -v` passes 5 stable-contract tests.
`python run_examples.py` validates all three projects with no errors. The 477
indexed Atlas concepts are covered exactly once by the distributed modules.

The downstream Vulcan edition independently checks the lossless Atlas payload,
the byte identity of each embedded Minerva tree, and all 31 generation targets.

