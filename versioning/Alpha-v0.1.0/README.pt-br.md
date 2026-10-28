# Minerva Blueprints · Alpha-v0.1.0

[English](README.md) · Português brasileiro

**Minerva Blueprints é o modelo do Olympus Project para o L2 do OAL: Analysis-Driven Modeling and Verification (ADMV).** Um blueprint reúne o modelo de programa (ADPM) e a especificação de verificação (ADVS). Ele explica como os casos especificados, entidades e contratos de ferramentas colaboram e como suas obrigações serão verificadas. Pode ser elaborado antes de existir código.

Atlas Specifications fornece a especificação L1 quando esse modelo é escolhido. Vulcan Ecosystem organiza a realização L3 quando esse modelo é escolhido. Minerva é responsável pelos blueprints semânticos e pelo espelho YAML por arquivo. YAML e uma arquitetura de código específica não definem o modelo abstrato. Classes abstratas, interfaces concretas e uma futura biblioteca facilitadora são escolhas opcionais da realização.

Esta edição é autossuficiente. Mantenha a pasta completa para utilizar manuais, schema, validador, starter, exemplos e testes sem outra versão ou a raiz do repositório. A raiz contém a apresentação ilustrada. O inglês é a fonte normativa; este texto é sua tradução de leitura. **DEVE**, **NÃO DEVE**, **RECOMENDA-SE** e **PODE** expressam obrigações, recomendações e opções. Esta é uma **candidata alpha preparada com auxílio de IA e pendente de revisão pelo responsável do projeto**, sem declaração de publicação estável ou certificação.

<a id="release-notes"></a>
## Notas de versão — Alpha-v0.1.0

Esta primeira edição Minerva extrai as responsabilidades L2 do pacote didático Vulcan anterior e explicita as relações ADPM/ADVS. Introduz identidades lógicas próprias, vínculos com fontes e critérios, YAML versionado, validador somente de leitura, fichas de arquivos planejados, ficha legada com múltiplas unidades e contraexemplos públicos. A instância TaskBoard foi reconstruída a partir do demo Vulcan companheiro. Ela **não** afirma realizar o outro TaskBoard publicado pelo Atlas.

A edição do modelo abstrato é `Alpha-v0.1.0`; o perfil YAML é `0.1.0`; a versão do pacote/ferramenta Python é `0.1.0a0`. A referência OAL é `Stable-v1.0.0`. O leitor L1 fornecido suporta JSON de Atlas Specifications `Stable-v1.0.0`. Essas identidades descrevem objetos distintos e não precisam ter a mesma grafia.

As fontes estão fixadas em [source-baselines.json](verification/source-baselines.json). A [cobertura dos requisitos](verification/REQUIREMENTS.pt-br.md) relaciona a entrega ao catálogo acordado. A [evidência de validação](verification/VALIDATION.pt-br.md) diferencia verificações efetivamente realizadas de verificações planejadas. Esta edição não reescreve os pacotes históricos.

## Conteúdo

- [Início rápido](#quick-start) · [Versões](#versions) · [Modelo abstrato e regras](#reference-rules)
- [Representação YAML](implementations/yaml/README.pt-br.md) · [Exemplos](examples/README.pt-br.md)
- [Conformidade](#conformance) · [Verificação](#verification) · [Versionamento](#versioning)
- [Correspondência OAL](references/OAL-ALIGNMENT.pt-br.md) · [Composição e revisão de mudanças](references/REVIEW-EXAMPLES.pt-br.md)

<a id="versions"></a>
## Versões

| Edição | Estado | Regras | Verificação | Conformidade |
| --- | --- | --- | --- | --- |
| Alpha-v0.1.0 | Primeira candidata; revisão do responsável pendente | [Referência](#reference-rules) | [Guia](#verification) | [Escopo](#conformance) |

<a id="quick-start"></a>
## Iniciar um blueprint

Utilize **Python 3.11+**. Execute os comandos nesta pasta de edição. Nenhum outro checkout é necessário.

```bash
python -m venv .venv
# POSIX: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install .
python run_examples.py --all
python examples/counterexamples/check.py
python run_examples.py --test
```

A instalação disponibiliza `minerva-validate`; `python -m minerva_blueprints` e o launcher local da edição oferecem a mesma interface. Como alternativa, instale `requirements.txt` e utilize o launcher diretamente. Nenhum launcher escolhe outra edição ou instala dependências automaticamente.

```bash
python validator/minerva_validate.py \
  examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml \
  --root examples/minimal --json
```

Copie [o starter](implementations/yaml/starter.minerva.yaml) para a pasta L2 escolhida no ecossistema. Defina identidade, escopo, especificação de origem e responsável. Selecione os casos de origem, modele contratos e colaboradores e defina um teste comportamental lógico por caso com os cenários necessários. Acrescente fichas por arquivo conforme a realização for projetada ou observada. Altere `document.status` de `draft` para `reviewed` somente após a revisão técnica declarada, registrando pendências e quem revisou. O rótulo não concede aprovação das partes interessadas.

O starter é um rascunho intencionalmente incompleto. A conferência apenas estrutural retorna sucesso; a verificação completa de consistência retorna **4 (inconclusiva)**. Essa distinção impede apresentar uma estrutura vazia como L2 completo.

```bash
python validator/minerva_validate.py implementations/yaml/starter.minerva.yaml --structure-only
```

A organização recomendada do ecossistema contém `apps/`, `docs/L1_AtlasSpecifications/`, `docs/L2_MinervaBlueprints/`, `docs/L3_Vulcan/` e `docs/Shared/`. `docs/` na raiz é recomendação. Outra localização documental é válida quando sua raiz e seu mapeamento são declarados e as referências continuam resolvíveis. Minerva não impõe a localização dos aplicativos executáveis para todos os modelos L3.

<a id="reference-rules"></a>
<a id="abstract-model"></a>
## Modelo abstrato e regras de referência

As regras abaixo definem obrigações semânticas independentemente da grafia das chaves YAML. Seus identificadores também correspondem ao catálogo de requisitos acordado. O guia YAML apresenta o mapeamento da representação; o guia de correspondência explica as obrigações OAL. Uma alegação completa vale para um escopo declarado, não automaticamente para todos os aplicativos de um repositório.

### MIN-001 — Modelo integrado de programa e verificação

Uma instância Minerva DEVE distinguir seu modelo de programa e sua especificação de verificação e preservar suas relações em um único escopo L2. ADPM isolada, ADVS isolada ou um catálogo de arquivos isolado NÃO DEVEM ser descritos como ADMV completa. Cada declaração de cobertura DEVE identificar componente, casos selecionados e obrigações abrangidas.

### MIN-002 — Semântica anterior à sintaxe

O modelo reúne casos, entidades, capacidades de ferramentas, operações, regras, dependências, decisões, testes comportamentais, cenários e relações de evidência identificáveis. Uma representação DEVE recuperar esses papéis e suas invariantes. YAML, descrições Markdown e imagens carregam significado; não criam camadas OAL. Outra representação exige mapeamento explícito e contrato de preservação; esta edição fornece apenas o perfil YAML.

### MIN-003 — Identidade, revisão e fonte

Um blueprint DEVE identificar a si próprio, revisão de conteúdo, edição do modelo, edição OAL escolhida, escopo, responsável e fonte L1 versionada. A representação também identifica seu perfil. Revisões de conteúdo mudam o significado elaborado; versões de modelo/perfil mudam contratos reutilizáveis. Identidades e revisões de origem DEVEM ser resolvíveis. O perfil fornecido permite hash para reforçar a fixação do conteúdo de origem.

### MIN-004 — Elementos lógicos e vínculos com arquivos

Identidades lógicas DEVEM permanecer independentes de caminhos, símbolos e agrupamentos físicos. Renomear um arquivo atualiza seu vínculo, não a identidade de uma responsabilidade que permanece a mesma. Uma ficha PODE descrever várias classes, structs, funções ou um módulo; várias fichas PODEM realizar o mesmo elemento lógico. A regra de uma classe por arquivo pertence à organização opcional Vulcan Architecture, não à capacidade do Minerva de documentar aplicações arbitrárias.

### MIN-005 — Casos de programa

Cada caso L1 no escopo DEVE corresponder a exatamente um caso de programa. O caso DEVE preservar objetivo, condições, decisões, resultados, efeitos e falhas pertinentes da especificação e identificar colaboradores e comportamento delegado às entidades. Decisões acrescentadas DEVEM ser distinguíveis dos requisitos herdados. Um procedimento auxiliar sem caso de origem não pode se tornar silenciosamente outro caso de uso modelado.

### MIN-006 — Dados operacionais e colaboradores técnicos

Contratos de operações DEVEM identificar entradas e saídas por nome, significado, tipo, obrigatoriedade e cardinalidade aplicável. Dados de negócio, contexto de ator da invocação e colaboradores injetados DEVEM permanecer distinguíveis. A integração Vulcan utiliza primitivos, entidades e coleções tipadas nos dados operacionais; um tipo escalar nomeado refina um primitivo. Ferramentas, fábricas de conexão e runtimes são colaboradores técnicos, não entradas de negócio serializadas. A assinatura nativa pode registrar detalhes da linguagem separadamente.

### MIN-007 — Regras canônicas das entidades

Entidades DEVEM identificar dados, relações, invariantes, comportamento delegado e dependências. Cada regra DEVE ter responsável e origem recuperáveis. Entidades NÃO DEVEM depender de casos ou ferramentas. Minerva permite entidades orientadas a dados ou com comportamento explicitamente delegado; não prescreve uma distribuição universal de todo comportamento de domínio.

### MIN-008 — Contratos das capacidades das ferramentas

Uma ferramenta DEVE declarar operações, condições, resultados, efeitos, garantias e falhas separadamente do mecanismo selecionado. Casos consomem esses contratos. Satisfazê-los NÃO DEVE exigir uma superclasse, palavra-chave de interface, contêiner de injeção ou biblioteca específica. Um objeto concreto simples com o comportamento documentado é uma realização válida.

### MIN-009 — Entidades prontas e condições contextuais

Uma ferramenta que recebe entidade pronta DEVE confiar em sua validade interna canônica e NÃO DEVE repetir a validação de invariantes, inclusive por condição equivalente renomeada ou gerada automaticamente. A hidratação parte de registros brutos e DEVE utilizar construção canônica. Uma condição contextual distinta, como existência persistida ou unicidade atômica, DEVE identificar objeto, finalidade e responsabilidade. Essas condições não transferem a autorização do caso à ferramenta.

### MIN-010 — Garantias de persistência

Quando há persistência, o contrato DEVE declarar capacidades de leitura e alteração, responsabilidade pelos dados, garantias transacionais e de concorrência pertinentes e falhas. Uma consulta prévia não substitui garantia atômica exigida. Quando uma operação pode ter produzido efeito apesar da falha relatada, o modelo DEVE distinguir resultado desconhecido de ausência de efeito estabelecida. O demo promete sucesso local durável e propagação de falhas; não promete recuperação distribuída nem classificação de todo resultado possível durante commit.

### MIN-011 — Dependências e composição

O modelo DEVE mostrar o que casos e ferramentas recebem, onde as realizações são selecionadas e como são compostas. Dependências necessárias NÃO DEVEM desaparecer em buscas globais não documentadas. Domínios, tempos de vida e propriedade escolhidos DEVEM ser declarados quando relevantes. Um domínio agrupa responsabilidades; não concede acesso por si só. Minerva não exige organização de pastas nem tempo de vida singleton.

### MIN-012 — Autorização no caso

Cada caso DEVE receber contexto explícito de ator com origem de confiança declarada e decidir permissão antes de efeitos protegidos. Contextos ausentes, não resolvidos, desconhecidos e insuficientes DEVEM ser recusados. Identidade autenticada e participação anônima explícita são decisões contratuais distintas. Um campo JSON fornecido pelo chamador não se torna confiável porque possui a forma de uma entidade. A autorização DEVE funcionar em chamadas diretas ao núcleo.

### MIN-013 — Composição entre casos

Uma chamada a outro caso DEVE declarar dependência, contexto de ator transmitido, contrato consumido e resultado. O caso chamado DEVE aplicar sua própria política. Delegação ou atuação em nome de outro participante exige regra explícita; uma chamada interna não acrescenta permissão. O [exemplo de composição](references/REVIEW-EXAMPLES.pt-br.md#case-composition) demonstra duas políticas sem modificar o escopo de origem do TaskBoard ou inventar um quarto caso de negócio.

### MIN-014 — Comportamento recuperável

Prosa semântica ou pseudocódigo estruturado DEVEM permitir recuperar sequência, decisões, falhas, resultados e efeitos. Um diagrama PODE complementar a descrição. Uma assinatura de método ou caixa genérica “processar” é insuficiente para recuperar o comportamento. RECOMENDA-SE detalhar o contrato sem reproduzir sintaxe incidental da implementação.

### MIN-015 — Grafos identificados

Um grafo DEVE identificar proprietário, tipo, entrada, nós e transições, incluindo condições e ações. Um fluxo representa passagem de controle; um nó final ou de falha identifica resultado terminal. Uma máquina de estados representa um estado e transições permitidas, incluindo auto-transições legítimas. Um grafo herdado da especificação L1 mantém sua origem L1; armazená-lo em YAML não transforma a decisão em L2.

### MIN-016 — Decisões, observações e pendências

O modelo DEVE distinguir obrigações herdadas, decisões, premissas, pendências e observações do código, preservando origem e estado de revisão. Uma alteração observada NÃO DEVE sobrescrever automaticamente a semântica pretendida. A revisão DEVE identificar casos, contratos de ferramentas/entidades, cenários e vínculos afetados antes de aprovar uma revisão. A [revisão de mudanças](references/REVIEW-EXAMPLES.pt-br.md#change-impact) e o contraexemplo de divergência preservam intenção e observação simultaneamente.

### MIN-017 — Um teste comportamental diretamente vinculado

Cada caso UCS selecionado DEVE possuir exatamente um teste comportamental lógico diretamente vinculado. Um teste PODE conter muitos cenários e consumir muitas verificações de apoio. Funções, arquivos e fixtures são realizações; sua quantidade não redefine a correspondência lógica entre caso e teste. Uma verificação compartilhada NÃO DEVE criar outro teste diretamente vinculado a um caso já existente.

### MIN-018 — Contratos dos cenários

Cada cenário ou verificação de apoio DEVE declarar preparação e precondições, ação, resultado e efeitos esperados, limite observado e configuração relevante. Cenários de caso DEVEM declarar contexto de ator, inclusive ausência deliberada. Uma condição marcada não aplicável DEVE preservar justificativa e não contribui para cobertura aplicável. O comportamento esperado é um oráculo a revisar, não um resultado observado de execução.

### MIN-019 — Rastreabilidade dos critérios de aceite

Cada critério selecionado DEVE estar ligado ao teste comportamental de seu caso e aos cenários ou verificações de apoio aplicáveis que o cobrem. Um critério compartilhado de integração DEVE preservar uma definição canônica e identificar todos os casos afetados e seus testes. Não se inventa outro caso para o critério. O leitor Atlas fornecido suporta uma extensão explícita documentada para critérios compartilhados; não infere significado compartilhado por semelhança de texto.

### MIN-020 — Permissão e ausência de efeitos proibidos

A ADVS DEVE especificar invocações permitidas e negadas para cada caso, incluindo as quatro categorias de recusa e participação anônima explicitamente permitida. O oráculo DEVE observar ausência de efeitos protegidos de domínio ou armazenamento antes da autorização válida, além da mensagem de erro. O validador confere categorias e vínculos declarados; a revisão avalia se os cenários realmente estabelecem a política.

### MIN-021 — Alternativas, falhas e limites pertinentes

O plano DEVE cobrir alternativas, falhas e limites necessários ao contrato alegado, incluindo garantias necessárias de entidades e ferramentas. Condições relevantes ainda não verificadas DEVEM ser visíveis e impedir uma alegação irrestrita de cobertura completa. Vínculos de critérios não provam suficiência dos cenários. Entre os riscos além do demo estão autenticação de produção, recuperação distribuída e comportamento exaustivo de falhas de armazenamento.

### MIN-022 — Plano, realização e evidência observada

A verificação planejada, sua realização executável ou procedimental e uma observação de execução DEVEM permanecer distinguíveis. Um resultado observado DEVE identificar revisão da implementação, ambiente, momento, verificações e relatório de evidência, com limitações. Um arquivo ou símbolo observado não demonstra execução. Os blueprints de exemplo não contêm execuções bem-sucedidas fabricadas; relatórios de validação dizem respeito aos documentos e verificações solicitadas.

### MIN-023 — Obrigações de interação referenciadas

Quando a interação L4 selecionada introduzir obrigações observáveis, a ADVS DEVE referenciar sua origem e especificar cenários pertinentes. Escolha de canal, sintaxe de rota/CLI e representação continuam responsabilidades L4; restrições externas exigidas preservam origem L1. O exemplo completo vincula obrigações HTTP e CLI de `docs/Shared/interaction.md` sem tornar esses canais obrigatórios para Minerva.

### MIN-024 — Espelho YAML versionado em L2

O perfil YAML DEVE fornecer uma ficha por fonte no escopo declarado do espelho, preservando subdiretórios e a extensão original antes de `.yaml`. Na organização recomendada, `apps/TaskBoard/entities/Entity_Task.py` corresponde a `docs/L2_MinervaBlueprints/apps/TaskBoard/entities/Entity_Task.py.yaml`. `Task.py` e `Task.go` permanecem distintos. Cada ficha contém objetivo, unidades e membros, descrição semântica, entradas/saídas e dependências diretamente ou por referências lógicas. Intenção, bytes observados e pendências DEVEM permanecer distinguíveis.

### MIN-025 — Raízes, referências e empacotamento

Um pacote DEVE declarar raiz documental, lista de fichas, cobertura selecionada e exclusões. Caminhos relativos são resolvidos pela raiz do ecossistema explicitamente fornecida, não por um diretório de trabalho variável. Mover o pacote completo DEVE preservar as relações. Fichas planejadas PODEM existir antes do código, sem hash observado. Alegar correspondência atual com fontes realizadas exige inspeção atual do escopo; uma verificação apenas do modelo não estabelece essa correspondência.

### MIN-026 — Leitura previsível apenas como dados

O leitor DEVE tratar YAML como dados. Rejeita chaves duplicadas ou não textuais, âncoras, aliases e tags explícitas, inclusive executáveis. Fixa a interpretação de escalares, rejeita números não finitos e limita documentos a 8 MiB. Texto parecido com comando permanece texto. O leitor NÃO DEVE importar módulos do aplicativo nem executar fontes, campos YAML ou testes enquanto valida um blueprint.

### MIN-027 — Validação estrutural e de consistência

O validador DEVE conferir schema suportado, IDs declarados, referências tipadas, relações permitidas, cardinalidade selecionada de casos/testes e vínculos de critérios. Diagnósticos DEVEM distinguir essa verificação finita da revisão semântica. Uma ficha válida isolada não estabelece ADMV. Um modelo vazio marcado como revisado não pode alegar cobertura. Suficiência completa, equivalência de algoritmos e correção comportamental permanecem fora da prova automática desta edição.

### MIN-028 — Validação de grafos

Para grafos suportados, o validador DEVE conferir proprietários, referências de nós/arestas, entrada e alcançabilidade, além de declaração terminal para fluxos finitos. DEVE permitir ciclos legítimos, como conclusão idempotente. Aprovação não prova terminação nem correção das condições. RECOMENDA-SE que um diagrama derivado identifique grafo autoritativo e edição; uma visão ilustrativa não substitui o contrato do grafo.

### MIN-029 — Diagnósticos revisáveis

Diagnósticos DEVEM conter código, severidade, documento, elemento e motivo. Texto e JSON expõem o mesmo problema. Sucesso, documento inválido, perfil não suportado, erro operacional e avaliação inconclusiva DEVEM ter resultados de processo distintos. A automação DEVE avaliar nível e escopo solicitados além do código de saída.

### MIN-030 — Exemplos e contraexemplos

Esta edição DEVE incluir instância ADPM/ADVS preenchida, escopo mínimo selecionado, vínculo legado com múltiplas unidades, exemplo de fonte planejada e contraexemplos reproduzíveis. Resultados esperados DEVEM ser separados das evidências efetivas. Exemplos são artefatos didáticos com procedência declarada; validação bem-sucedida não aprova o modelo em nome do responsável do projeto.

<a id="conformance"></a>
## Conformidade e escopo

O modelo declara estabelecer os **assuntos de ADPM e ADVS do L2 do OAL**. A [correspondência OAL](references/OAL-ALIGNMENT.pt-br.md) mapeia os dez assuntos ADPM e os cinco ADVS. Não afirma implementar as demais camadas nem um mecanismo geral de derivação. Atlas e Vulcan são companheiros selecionados compatíveis quando seus contratos reais de origem e realização concordam; compartilhar o nome Olympus não prova compatibilidade.

Uma alegação de representação identifica as edições de modelo/perfil e preserva o conteúdo obrigatório no escopo. Uma alegação de instância também identifica fonte, casos, decisões, lacunas e evidências de revisão. Uma ficha isolada é recorte de vinculação. `draft` é incompleto. `reviewed` significa que ocorreu a revisão técnica declarada; responsável e limitações devem dizer por quem e se a aprovação das partes interessadas continua pendente.

O validador retorna `layer_coverage: declared_adpm_and_advs` para um blueprint revisado cujos componentes foram inspecionados. Isso significa que ambos foram fornecidos, **não** que o plano é suficiente ou a realização é conforme. Um cenário ligado a critério pode ter oráculo errado. Um hash correspondente pode descrever programa defeituoso. Alegações mais amplas exigem revisão semântica humana e evidência da implementação.

<a id="verification"></a>
## Verificação

```bash
python run_examples.py --all
python examples/counterexamples/check.py --json
python run_examples.py --test
python validator/minerva_validate.py examples/planned/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/planned --json
```

`--structure-only` lê um documento e valida sua representação, sem resolver L1 ou fichas companheiras. O modo normal resolve fichas declaradas e verifica consistência suportada. `--verify-code` também confere presença/hashes das fontes, unidades e métodos Python de primeiro nível, símbolos dos testes de apoio e cobertura declarada dos arquivos. Nunca executa aplicativo ou testes.

O exemplo Minerva completo contém fichas observadas das fontes Vulcan companheiras **sem distribuir essas fontes de aplicação aqui**. Sua validação de modelo é autossuficiente. Solicitar `--verify-code` nesse diretório Minerva retorna disponibilidade de código inconclusiva. Execute a conferência no ecossistema companheiro após copiar as mesmas fichas L2, ou coloque a realização explicitamente correspondente nos caminhos declarados. Não remova a opção e depois descreva o resultado como correspondência do código.

| Saída | Significado | Exemplo |
| --- | --- | --- |
| `0` | Verificações solicitadas aprovadas | Modelo válido; ou somente schema de rascunho válido |
| `1` | Documento suportado inválido | Teste ausente, ID duplicado, grafo inválido, divergência de fonte |
| `2` | Modelo/perfil/adaptador não suportado | Perfil YAML `2.0.0`; também erro de uso da CLI |
| `3` | Falha operacional | Arquivo ilegível ou dependência ausente |
| `4` | Avaliação solicitada inconclusiva | Consistência de rascunho; fonte indisponível para inspeção |

O validador não confere toda a semântica Atlas; use a ferramenta Atlas fixada para validação L1 completa. Não analisa linguagens arbitrárias, prova transações, compara algoritmos, valida autenticação de produção ou executa oráculos. Inspeções suportam nomes Python e hashes; outras linguagens recebem hashes com limitação explícita de inspeção de símbolos. Consulte [evidência e limitações registradas](verification/VALIDATION.pt-br.md).

<a id="versioning"></a>
## Versionamento e controle de mudanças

Esta edição é selecionada explicitamente por caminho. O pacote não resolve um perfil mutável “mais recente”. Identidades de modelo/perfil não suportadas são recusadas. Mudança de conteúdo incrementa a revisão; o elemento lógico conserva identidade enquanto sua responsabilidade mantém continuidade. Mudança de modelo ou representação exige edição/perfil e declaração de migração próprios. Renomear um arquivo atualiza caminho espelhado e snapshot observado, preservando identidades.

Mantenha intenção proposta, divergência observada e decisões de revisão juntas até resolver a alteração. Uma observação nova não revisa requisitos L1 silenciosamente. Mudar uma garantia de falha de ferramenta pode afetar casos, interpretação de aceite, cenários, representações de boundary e testes L3. Os [exemplos de revisão](references/REVIEW-EXAMPLES.pt-br.md) apresentam procedimento concreto de impacto. Fontes congeladas e registros de entrega permitem inspecionar a base desta alpha.

## Autoria e licença

Minerva Blueprints integra o Olympus Project, de autoria de Douglas de Oliveira Alkimim. Esta candidata e seus exemplos foram preparados com auxílio de IA; verificações técnicas não implicam aprovação do autor ou publicação pública. A edição é distribuída sob [MIT](LICENSE); procedência e licenças retidas das fontes estão em `verification/sources/`.
