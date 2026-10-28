# Migração para Minerva Blueprints Alpha-v0.1.0

[English](MIGRATION.md) · [Manual](../README.pt-br.md) · [Cobertura](REQUIREMENTS.pt-br.md)

Esta edição extrai e revisa a proposta **Vulcan Architecture Alpha-v0.1.0-Alkimim** em dois modelos do Olympus Project: Minerva Blueprints (L2) e Vulcan Ecosystem (L3). O arquivo original permanece uma origem histórica; a nova edição não altera seus bytes nem apresenta os resultados antigos como novas execuções. Os pins e recortes da origem estão em [source-baselines.json](source-baselines.json).

O [mapeamento legível por máquina](requirements/migration.json) conserva as 40 regras anteriores e seus destinos. O catálogo é a fotografia do levantamento; o status `proposed` nele registra aquele momento. A cobertura desta entrega registra separadamente adoção editorial na Alpha, realização e evidência. A preparação e a revisão técnica foram assistidas por IA; não se afirma aprovação do responsável pelo projeto.

## Responsabilidades que mudaram

| Família anterior | Destino e tratamento |
| --- | --- |
| Ficha YAML por arquivo | L2: `docs/L2_MinervaBlueprints/apps/<App>/<path>/<File.ext>.yaml`; preserva extensão e unidades de arquivos legados. |
| ADPM e ADVS | Blueprint Minerva L2 com identidades, contratos e plano de verificação. |
| Casos e critérios de origem | Instância Atlas própria do exemplo, com reconstrução didática declarada. |
| Manifesto que reunia contratos, organização e canais | Dividido por responsabilidade: contratos L2, realização L3 e interação identificada como L4. |
| Inventário, composição e execução | `docs/L3_Vulcan/`, com referências às definições canônicas L2. |
| Documentação de apoio | `docs/Shared/`, sem criar nova camada OAL. |
| Validador e runner comuns | Recursos locais à edição; validador Minerva e avaliador estrutural Vulcan têm escopos distintos. |

`apps/` e o mecanismo de inicialização na raiz continuam exigidos em um ecossistema Vulcan. `docs/` e suas pastas por camada são recomendadas, com local alternativo admitido quando as informações e referências continuam recuperáveis. A adoção parcial não exige criar pastas vazias.

## Correspondência das 40 regras anteriores

| Regra anterior | Título original | Tratamento | Requisitos atuais | Justificativa |
| --- | --- | --- | --- | --- |
| ECO-01 | Raiz e inventário de aplicativos | Dividir | VUL-002, VUL-003, VUL-022, VUL-029 | Preservar apps/ e entrada na raiz; recomendar docs/ organizado por camada. Inventário e operação documental ficam em L3. |
| ECO-02 | Aplicativos heterogêneos | Preservar | VUL-003, VUL-004, INT-012 | Manter participação heterogênea com documentação fiel e escopo de conformidade explícito, sem exigir refatoração do legado. |
| ECO-03 | Documentação espelhada das fontes | Revisar | MIN-024, MIN-025, INT-005, VUL-029 | Transferir o espelho por arquivo para Minerva L2, conforme decisão do usuário, preservando cobertura e exclusões declaradas. A localização docs/ é recomendada. |
| ECO-04 | Caminhos, colisões e identidade | Dividir | MIN-004, MIN-024, MIN-025, INT-005 | Identidades lógicas e referências permanecem no modelo e na integração; caminhos, colisões e substituições do espelho são definidos pelo perfil Minerva em L2. |
| ECO-05 | Catálogo canônico de boundaries | Dividir | VUL-003, VUL-021, INT-006, INT-008 | Manter descoberta e propriedade dos contratos públicos no ecossistema, classificando escolhas de canal como L4 e evitando definições autoritativas concorrentes. |
| ECO-06 | Mapeamento das interações para implementações | Dividir | VUL-020, INT-008, INT-002, MIN-023 | O mapeamento de interação conserva responsabilidade L4, enquanto identidades e obrigações verificáveis se vinculam ao núcleo e à ADVS. |
| ECO-07 | Comunicação entre aplicativos | Preservar | VUL-021, VUL-018, INT-003 | Preservar comunicação por contratos públicos e a semântica de dados e falhas, com serialização apenas quando exigida pelo canal. |
| ECO-08 | Inicialização completa e seletiva | Preservar | VUL-022, VUL-023 | Manter inicializador real na raiz e seleção dos modos padrão, sem converter o manifesto de comandos em substituto da execução. |
| ECO-09 | Contratos de execução e dependências | Dividir | VUL-023, VUL-024, VUL-025, VUL-019 | Distribuir o contrato operacional entre modos, dependências de inicialização, prontidão e gestão de recursos, permanecendo responsabilidade Vulcan. |
| ECO-10 | Escopo documental e de execução | Dividir | MIN-024, VUL-003, VUL-004, VUL-027, VUL-029, INT-012 | Distinguir a cobertura do modelo e espelho em L2 da documentação operacional e evidências de execução em L3, com escopo por aplicativo. |
| VA-01 | Quatro áreas centrais e suporte | Preservar | VUL-005, VUL-020 | Manter as quatro áreas do perfil e suportes identificados, distinguindo o código de canal L4 presente nos exemplos. |
| VA-02 | Uma estrutura por arquivo de fonte | Preservar | VUL-007, VUL-009 | Preservar uma estrutura principal por arquivo e exceções técnicas justificadas nos perfis de linguagem. |
| VA-03 | Nomes e perfis de linguagem | Preservar | VUL-008, VUL-009 | Manter prefixos, convenções e correspondência entre arquivo e estrutura, declarando adaptações exigidas pela linguagem. |
| VA-04 | Value objects | Preservar | VUL-010, VUL-014 | Preservar imutabilidade e encapsulamento dos value objects no perfil Vulcan, sem impô-los como dados operacionais públicos. |
| VA-05 | Entidades e invariantes | Dividir | VUL-011, MIN-007, VUL-019 | Separar a modelagem das regras canônicas das entidades de sua realização, mantendo propriedade e vida útil pertinentes explícitas. |
| VA-06 | Ferramentas e garantias técnicas | Dividir | VUL-012, MIN-008, MIN-009, MIN-010 | Extrair contratos e garantias para a modelagem e manter no Vulcan a implementação técnica e o uso da construção canônica das entidades. |
| VA-07 | Casos de uso e núcleo invocável | Dividir | VUL-013, MIN-005, INT-002 | Relacionar o contrato projetado à operação invocável concreta, preservando identidade sem transformar auxiliares em novos casos. |
| VA-08 | Domínios de acesso | Dividir | VUL-006, MIN-011 | Manter a pasta de domínio como escolha do perfil Vulcan e registrar no Minerva os limites e relações de domínio efetivamente modelados. |
| VA-09 | Contexto de ator e autorização | Dividir | VUL-015, MIN-012, MIN-020, INT-003 | Modelar a autorização no Minerva, realizá-la no caso Vulcan e verificar sua preservação inclusive em chamada direta. |
| VA-10 | Composição entre casos e ferramentas | Dividir | VUL-017, MIN-011, MIN-013 | Distinguir a composição lógica dos contratos e as regras concretas de dependência do perfil Vulcan, preservando contexto e autorização. |
| VA-11 | Seleção explícita de colaboradores | Dividir | VUL-016, VUL-019, MIN-011 | Manter seleção concreta e liberação de recursos no Vulcan, com composição e dependências planejadas no Minerva e biblioteca opcional. |
| VA-12 | Dados operacionais e dependências técnicas | Dividir | VUL-014, MIN-006, INT-008 | Separar tipos semânticos modelados, restrição de dados do perfil Vulcan e projeções de representação do canal. |
| VA-13 | Resultados, falhas e efeitos | Dividir | VUL-018, MIN-005, MIN-008, MIN-010 | Modelar resultados e efeitos observáveis e preservar sua realização, incluindo contratos específicos de fluxos, cancelamento e resultados incertos quando usados. |
| VA-14 | Boundaries e responsabilidade do núcleo | Preservar | VUL-020, INT-008 | Manter a separação do núcleo e do código de interação, conservando o contrato técnico de canal e a classificação L4. |
| VA-15 | Documentação do comportamento | Dividir | MIN-014, MIN-015, MIN-028, VUL-029, INT-006 | Manter descrições semânticas e grafos nas fichas e no modelo L2, identificando conteúdo projetado e observado. L3 referencia esse conteúdo e registra decisões de realização. |
| VA-16 | Integração da verificação | Dividir | VUL-026, VUL-027, MIN-017, MIN-022, INT-002 | Separar especificação da verificação, integração executável e resultados observados, preservando os vínculos com cada caso e critério. |
| VA-17 | Evolução e declarações arquiteturais | Dividir | VUL-028, VUL-030, INT-007, INT-012 | Preservar análise de impacto e avaliação do perfil, ampliando a rastreabilidade para as versões Minerva e seu escopo de integração. |
| DOC-01 | Três tipos de documento | Dividir | MIN-024, MIN-025, MIN-026, VUL-003, VUL-023, VUL-029, INT-008 | Reclassificar os envelopes: source acompanha o espelho L2; inventário e operação de app/ecosystem alimentam L3. Contratos de canal mantêm identificação L4. |
| DOC-02 | Identidade e finalidade da fonte | Revisar | MIN-003, MIN-004, MIN-024, INT-005, INT-006 | Identidade, caminho, objetivo e observações por arquivo integram a ficha do espelho Minerva em L2, com IDs lógicos e origem explícita. |
| DOC-03 | Unidades e membros | Dividir | MIN-004, MIN-006, MIN-024, VUL-007, VUL-004, INT-005 | Unidades e membros são descritos nas fichas L2, incluindo múltiplas estruturas legadas. A regra de uma estrutura principal por arquivo continua no perfil de código Vulcan. |
| DOC-04 | Tipos, referências e definições canônicas | Dividir | MIN-006, MIN-007, MIN-025, VUL-014, VUL-021, INT-006 | Definições e referências semânticas ficam em L2; L3 referencia essas definições ao descrever tipos e integrações realizados. |
| DOC-05 | Dependências e evidência de composição | Dividir | MIN-011, VUL-016, VUL-019, VUL-024, INT-005 | Registrar dependências lógicas em L2 e composição, recursos e dependências de inicialização concretos em L3, preservando os vínculos entre eles. |
| DOC-06 | Bindings de boundary | Dividir | INT-008, VUL-020, MIN-006, MIN-023 | Preservar a classificação L4 dos contratos de interação; L2 referencia tipos e cenários, e L3 documenta a realização concreta dos canais e integrações. |
| DOC-07 | Evidência e atualização | Dividir | VUL-027, VUL-028, MIN-022, INT-006, INT-007 | Concentrar evidências de execução em L3; L2 mantém a especificação da verificação e referências à correspondência observada e às revisões avaliadas. |
| DOC-08 | Limites da validação | Dividir | MIN-027, MIN-029, VUL-030, REP-006, INT-012 | Separar validação do modelo e espelho L2 da avaliação da organização e documentação L3, mantendo diagnósticos e limites explícitos. |
| OAL-01 | Objeto declarado e baselines | Revisar | VUL-001, MIN-001, INT-001, REP-001 | Atualizar as declarações para os dois modelos e a baseline OAL selecionada, conservando a distinção entre modelo, artefato e transformador. |
| OAL-02 | Materialização e identidade dos casos | Dividir | VUL-013, VUL-028, MIN-005, MIN-017, INT-002, INT-003 | Preservar a correspondência de casos e contratos, identificando o Minerva como fonte L2 quando adotado e registrando diferenças entre os exemplos existentes. |
| OAL-03 | Preservação de autorização e verificação | Dividir | VUL-015, VUL-026, MIN-012, MIN-020, INT-003 | Distribuir autorização e verificação entre sua especificação e realização, mantendo visíveis recusas, falhas e cenários não executados. |
| OAL-04 | Registros de derivação e alteração | Preservar | INT-004, INT-007, VUL-028, MIN-003, MIN-016 | Conservar proveniência e responsabilidade nominal, distinguindo fontes reconstruídas e decisões acrescentadas de evidência externa e automação demonstrada. |
| OAL-05 | Responsabilidade de boundary e escopo | Dividir | INT-008, VUL-020, MIN-023, INT-012 | Manter contratos e escolhas de canal identificados como L4, com cenários pertinentes referenciados e declarações limitadas ao escopo realmente avaliado. |

## Compatibilidade do exemplo

O exemplo declara `ATLAS-VULCAN-TASKBOARD`, revisão `1`, como sua origem L1. Mantém identificador gerado pela aplicação, título normalizado, conclusão booleana idempotente e listagem na ordem de inserção. Não acrescenta revisão otimista de tarefa nem aceita um identificador de criação escolhido pelo chamador. A instância publicada separadamente no Atlas possui diferenças e não é apresentada como equivalente. O tipo de retorno de uma falha de armazenamento não comprova ausência de efeitos; falhas ambíguas e protocolos distribuídos não foram simulados nesta Alpha.

A edição do modelo (`Alpha-v0.1.0`), a revisão de cada instância (`1`), o perfil YAML Minerva (`0.1.0`) e a versão Python da ferramenta (`0.1.0a0`) são conceitos distintos. Mudar um caminho físico deve atualizar vínculos, sem trocar IDs lógicos cujo significado permaneceu. Alterar o contrato exige analisar impactos L1/L2/L3/L4 e suas verificações, antes de atualizar a evidência.

Não há migrador automático de aplicativos arbitrários. Esta migração entrega os modelos, formatos, procedimentos, exemplos e correspondências para revisão.
