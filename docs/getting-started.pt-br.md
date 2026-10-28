# Elaborar um blueprint Minerva

[English](getting-started.md) · [Edição](../versioning/Alpha-v0.1.0/README.pt-br.md)

1. Leia a [fonte Atlas mínima](../versioning/Alpha-v0.1.0/examples/minimal/docs/L1_AtlasSpecifications/example.atlas.json). Ela especifica submissão de solicitações, não listagem de tarefas. Observe código exato, quantidade inteira positiva, autorização antes dos colaboradores, recusa de duplicidade e resultado de escrita desconhecido.
2. Leia a [visão do exemplo](../versioning/Alpha-v0.1.0/examples/minimal/README.pt-br.md) e localize `source_l1`, `adpm.cases` e `advs.behavioral_tests` no blueprint. Há um caso de origem, um caso de programa e um teste comportamental lógico, com vários cenários.
3. Copie o [starter](../versioning/Alpha-v0.1.0/implementations/yaml/starter.minerva.yaml). Identifique bytes da fonte, revisão, escopo e autor. Declare o catálogo após revisar a fonte; ele não é importado automaticamente.
4. Escreva entidades, regras canônicas, contratos de ferramentas e algoritmo do caso. Registre decisões acrescentadas. Mantenha escolhas concretas de banco e canal separadas.
5. Defina cenários com preparação, contexto, ação, resultado/efeitos esperados, fronteira e configuração. Vincule critérios, regras e requisitos. Obrigações compartilhadas de qualidade mantêm uma verificação de apoio canônica.
6. Valide estrutura e depois consistência. Revise fidelidade à fonte separadamente. Preserve o estado de rascunho enquanto faltar conteúdo relevante; revisão técnica não implica aprovação de stakeholders.
7. Acrescente vínculos planejados quando houver projeto de código. `--verify-code` confere apenas bytes e nomes lexicais suportados. Execute os testes da realização separadamente e registre evidência real.

```bash
cd versioning/Alpha-v0.1.0
python validator/minerva_validate.py implementations/yaml/starter.minerva.yaml --structure-only
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
```

Nenhum reader ou motor de tradução é incluído. O [perfil](../versioning/Alpha-v0.1.0/implementations/yaml/README.pt-br.md) define os campos e o [guia de avaliação](../versioning/Alpha-v0.1.0/specification/conformance.pt-br.md) define o significado de cada resultado.
