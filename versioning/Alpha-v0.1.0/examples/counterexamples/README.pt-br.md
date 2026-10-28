# Contraexemplos públicos e resultados esperados

[English](README.md) · Português brasileiro

Estas fixtures contêm intencionalmente dados inválidos ou alegações limitadas. São **entradas sob teste**, não blueprints aprovados. [expected-results.json](expected-results.json) declara código de saída e diagnóstico esperados. [check.py](check.py) executa o leitor/validador real e compara saídas efetivas; nunca executa código descrito em YAML.

A partir da pasta da edição:

```bash
python examples/counterexamples/check.py --json
```

| Fixture | Resultado esperado |
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
| unsafe-tag.yaml | 1 · YAML_INVALID; a tag com aparência executável não executa |
| draft-is-inconclusive.yaml | 4 · DRAFT_INCOMPLETE |
| legitimate-cycle.yaml | 0 · auto-transição legítima preservada |
| observed-drift.yaml | 1 · CODE_HASH_MISMATCH com inspeção de fonte |

A divergência preserva a intenção “retornar um” e o snapshot original, enquanto o código atual retorna dois. A falha esperada não altera o projeto automaticamente. A fixture de ciclo é válida: rejeitar qualquer ciclo rejeitaria incorretamente transições idempotentes. Algumas entradas inválidas produzem vários diagnósticos; o diagnóstico indicado é exigido e o runner não esconde falhas adicionais.

A saída 0 do runner significa **todas as expectativas corresponderam**, incluindo resultados inválidos/não suportados/inconclusivos esperados. Não significa que todas as fixtures são válidas. Evidência de execução efetiva fica separadamente na pasta verification da edição. A suíte acrescenta testes de propriedade de símbolos Python qualificados, raiz documental alternativa, grafos locais de fichas, critérios compartilhados e inspeção sem execução.
