# Atlas → Minerva: mapeamento documental

[English](mapping.md) · [Compatibilidade](compatibility.json) · [Exemplos](../../examples/README.pt-br.md)

Esta pasta documenta a integração. Não contém reader, tradutor executável ou motor de transformação. Os exemplos distribuídos são derivações editoriais assistidas por IA das fontes oficiais Atlas fixadas no commit `b5941830515d9968bb7f313301f1abe25fb6f8aa`.

| Conceito Atlas | Local no Minerva | Obrigação de preservação |
| --- | --- | --- |
| Identidade/revisão do documento | `source_l1`, `provenance.json` do exemplo | Preservar identidade, revisão, commit, arquivo e hash dos bytes |
| Caso | `adpm.cases[].source_case_id` | Exatamente um caso por caso L1 selecionado; preservar objetivo, entradas, resultados e algoritmo |
| Ator e permissão por caso | `source_l1.catalog`, `permission` do caso | Declarar o conjunto permitido específico do caso; preservar contexto confiável e ordem de recusa |
| Entidade, campos e validação | `adpm.entities`, regras e `origin_refs` | Preservar dados exatos, propriedade das regras e construção canônica |
| Ferramenta e operação | `adpm.tools[].operations` | Preservar garantias, falhas distintas, atomicidade e incerteza de escrita separadas do mecanismo |
| RF | Catálogo, comportamento do caso e `traceability` | Preservar obrigação e vínculos de verificação |
| RNF e `reference_to` | Catálogo e uma verificação de apoio canônica | Preservar origem, aplicabilidade, métrica, limite de medição e casos afetados |
| Critério de aceite | Catálogo, teste comportamental e cenários | Preservar identidade e oráculo observável |
| Chamada entre casos | Dependências com `context_forwarding` | Preservar principal, resultado consumido e autorização do caso chamado |
| Grafo | `adpm.graphs` com identidades originais | Preservar nós, transições e significado recuperável; L1 permanece como origem |
| Premissa/pendência | Decisões e limitações do documento | Preservar estado em aberto; não inventar aceitação de stakeholders |
| Ilustração de fronteira | Pacote L1 fixado | Preservar como ilustração; copiar não seleciona implementação de canal |

O catálogo de origem revisado é um índice elaborado dentro do blueprint Minerva. Usa `ref` em vez de `id` para separar os espaços de identidade de origem e L2. `kind` tipa a referência; `case_refs` declara o escopo de critérios/requisitos; `actor_refs` declara o conjunto permitido de um caso de origem. `source_pointer` é um localizador editorial, não uma instrução executada pelo validador. `traceability` identifica os destinos L2 e se o vínculo preserva, refina ou verifica a origem.

O validador lê apenas YAML Minerva e bytes opacos da fonte para calcular o hash. Rejeita origens de entidades não declaradas, origens de regras não resolvidas e atores fora do conjunto do caso declarado no catálogo. Não detecta um catálogo falso porém internamente consistente. A revisão compara catálogo, contratos e cenários com a fonte fixada; a validação externa do Atlas verifica a fonte com suas próprias ferramentas. Não há alegação de motor determinístico de tradução.

## Composição entre casos

O cancelamento de reserva verifica sua permissão e chama a consulta com o mesmo principal/contexto confiável. A consulta verifica sua própria permissão. Permissão apenas de cancelamento não autoriza consulta, e a recusa desta interrompe o fluxo antes da gravação. O exemplo contém cenário específico para essa fronteira.

## Obrigações compartilhadas

Referências de RNF Atlas mantêm seus IDs no catálogo. Criação e cancelamento vinculam-se a `CHK-RNF-BOOKING-CREATE-RESPONSE`, preservando a condição didática canônica de dois segundos e 30 solicitações. Criação/listagem de tarefas compartilham a verificação de retenção. São obrigações planejadas, não medições. As fontes nativas permanecem inalteradas; nenhuma extensão `minerva_shared_criteria` é inserida.

## Grafos e decisões de projeto

Nós de resultado Atlas correspondem a terminais de sucesso Minerva; recusas correspondem a terminais de falha; operações, validações e chamadas de caso correspondem a ações. IDs e rótulos de arestas originais permanecem recuperáveis. Metadados específicos completos dos grafos Atlas ficam na fonte fixada. Regras de transição aplicam-se à transição, não à hidratação de toda entidade existente. O contexto do chamador é uma entidade L2 explícita. Dados de sucesso e resultados nomeados de recusa/falha descrevem o contrato sem escolher mecanismo de exceções/resultados de uma linguagem.

## Revisão de mudanças

Compare revisões da fonte antes de editar L2. Preserve IDs dos casos, identifique critérios/RFs/RNFs alterados, atualize oráculos e vínculos afetados e registre lacunas. A revisão 3 do TaskBoard refina `AC-TASK-LIST-EMPTY`, explicitando vazio consistente autorizado e ausência de mudanças de estado/revisão. Os exemplos pareados preservam a diferença sem inventar um quarto caso.

O RNF de cancelamento referencia um procedimento canônico que ainda menciona 30 solicitações de criação e o estímulo de criação. O exemplo preserva essa redação e registra `DEC-QUALITY-SCOPE`: a medição específica do cancelamento exige esclarecimento do responsável pela fonte. Não se infere uma garantia separada de latência do cancelamento.
