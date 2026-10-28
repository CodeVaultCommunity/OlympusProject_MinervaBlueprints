# Revisão da fonte e dos contratos

[English](contract-review.md) · [Comparação detalhada](contract-review.json) · [Mapeamento](../../integrations/atlas/mapping.pt-br.md)

Esta é uma revisão técnica assistida por IA dos exemplos oficiais fixados do Atlas e dos modelos Minerva elaborados a partir deles. O aceite do responsável permanece pendente. A comparação pontual usada na revisão fica fora do produto entregue; nenhum reader de origem ou motor de tradução é incluído.

| Exemplo | Casos / testes comportamentais lógicos | Critérios | Cenários planejados |
| --- | --- | --- | --- |
| Cadastro mínimo de solicitações | 1 / 1 | 7 | 12 |
| Quadro de tarefas | 3 / 3 | 16 | 31 |
| Composição de reservas | 3 / 3 | 18 | 33 |
| TaskBoard revisão 2 | 3 / 3 | 16 | 31 |
| TaskBoard revisão 3 | 3 / 3 | 16 | 31 |

Os três exemplos principais têm sete casos e 41 critérios. As revisões são snapshots separados, não novos casos da aplicação. Cada JSON de origem corresponde byte a byte ao checkout oficial fixado; recursos e licenças originais acompanham o exemplo mínimo. A comparação conferiu cada localizador e enunciado do catálogo, identidades/objetivos/fluxos/atores dos casos, vínculos entre critérios e testes, mapeamentos de requisitos e IDs/extremidades dos grafos. O JSON registra hashes e a correspondência exata dos critérios. A validação externa com Atlas está nas [verificações](../evidence/checks.json).

## Revisão semântica

O exemplo mínimo preserva o código exato e sensível a maiúsculas, quantidade inteira de pelo menos um, validação do código antes da quantidade, recusa de duplicidade, autorização antes do trabalho protegido e resultado desconhecido da escrita. A obrigação de tempo continua uma condição didática sintética e não executada.

TaskBoard preserva identificadores fornecidos pelo chamador, títulos exatos com o limite da fonte, estados open/completed, revisão zero na criação, conclusão condicional, recusa da conclusão repetida, escopo do quadro, proteção atômica contra conflitos e ordenação determinística da fonte. Falha de armazenamento não equivale a lista vazia bem-sucedida. A revisão 3 refina `AC-TASK-LIST-EMPTY` para explicitar vazio consistente autorizado e ausência de alterações de estado/revisão; a revisão 2 conserva a redação original.

A composição preserva códigos alfanuméricos maiúsculos (1–12 caracteres), títulos exatos com conteúdo significativo, inserção com versão esperada zero, substituição condicional com versão positiva e incremento de versão. Cancelamento chama consulta com o mesmo contexto confiável; a consulta ainda decide sua própria permissão. Consulta malsucedida não chega ao save. Escrita desconhecida não prova ausência de efeito nem justifica repetição automática.

Regras de transição ficam separadas das referências de invariantes usadas na construção/hidratação. As verificações planejadas distinguem chamadas permitidas e contextos ausentes, não resolvidos, desconhecidos, insuficientes, expirados e explicitamente anônimos. RNFs compartilhados mantêm uma verificação de apoio canônica e vínculos recíprocos com casos/testes.

## Questões abertas e limites

O RNF canônico de tempo referenciado pelo cancelamento ainda menciona 30 solicitações de criação e o estímulo de criação. O exemplo preserva esse procedimento exato e registra `DEC-QUALITY-SCOPE`. A medição específica de cancelamento exige esclarecimento na fonte; não é uma garantia inferida. Medir tempo de interação exige um canal selecionado; medir somente o núcleo não estabelece tempo de resposta visível.

A representação do contexto do chamador é decisão L2 explícita; nenhum provedor de identidade, mecanismo de armazenamento ou canal é selecionado. A projeção dos grafos preserva identidades, topologia e rótulos; demais metadados específicos do Atlas permanecem na fonte fixada. Premissas e questões abertas de origem mantêm seu estado não resolvido.

Todos os cenários ADVS são planos e `executions` permanece vazio. A revisão não demonstra autorização em produção, persistência/concorrência, tempos de resposta, suficiência exaustiva dos cenários, conformidade universal com OAL ou aceite do responsável. Isso exige avaliação da realização selecionada e revisão responsável.
