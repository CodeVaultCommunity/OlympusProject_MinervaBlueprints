# Modelo Minerva Blueprints · Alpha-v0.1.0

[English — normative](model.md) · [Entrada da edição](../README.pt-br.md) · [Conformidade](conformance.pt-br.md)

Este é o texto normativo traduzido da edição. DEVE, NÃO DEVE, DEVERIA e PODE correspondem a MUST, MUST NOT, SHOULD e MAY. Minerva estabelece OAL L2 / ADMV, reunindo ADPM e ADVS. YAML é uma representação; organização de código e execução pertencem à realização L3. Bibliotecas, interfaces e classes abstratas são opcionais.

Esta Alpha ainda não foi publicada e foi revisada no mesmo diretório por autorização expressa do responsável. Edição `Alpha-v0.1.0`, perfil YAML `0.1.0` e ferramenta `0.1.0a0` continuam selecionados explicitamente. Não se promete compatibilidade com rascunhos anteriores não publicados. As fontes externas fixadas preservam seus bytes.

A edição não inclui leitor específico do Atlas nem motor de tradução. Os exemplos foram elaborados com assistência de IA a partir das fontes oficiais identificadas. Um eventual motor será independente. A autorização para editar não substitui aceitação semântica do resultado.

<a id="reference-rules"></a>
## Regras de referência
### MIN-001 — Modelo integrado de programa e verificação

Uma instância Minerva DEVE distinguir seu modelo de programa e sua especificação de verificação e preservar suas relações em um único escopo L2. ADPM isolada, ADVS isolada ou um catálogo de arquivos isolado NÃO DEVEM ser descritos como ADMV completa. Cada declaração de cobertura DEVE identificar componente, casos selecionados e obrigações abrangidas.

### MIN-002 — Semântica anterior à sintaxe

O modelo reúne casos, entidades, capacidades de ferramentas, operações, regras, dependências, decisões, testes comportamentais, cenários e relações de evidência identificáveis. Uma representação DEVE recuperar esses papéis e suas invariantes. YAML, descrições Markdown e imagens carregam significado; não criam camadas OAL. Outra representação exige mapeamento explícito e contrato de preservação; esta edição fornece apenas o perfil YAML.

### MIN-003 — Identidade, revisão e fonte

Um blueprint DEVE identificar identidade, revisão de conteúdo, edição do modelo, edição OAL, escopo, responsável e fonte L1 versionada. A representação também identifica sua versão de perfil. Blueprints YAML revisados DEVEM fixar o arquivo de origem por SHA-256 e declarar um catálogo de origem com identidades, tipos, propriedade por caso e atores permitidos. O catálogo é conteúdo elaborado no Minerva. Sua fidelidade à fonte DEVE ser revisada separadamente; o validador trata o arquivo L1 como bytes opacos.

### MIN-004 — Elementos lógicos e vínculos com arquivos

Identidades lógicas DEVEM permanecer independentes de caminhos, símbolos e agrupamentos físicos. Renomear um arquivo atualiza seu vínculo, não a identidade de uma responsabilidade que permanece a mesma. Uma ficha PODE descrever várias classes, structs, funções ou um módulo; várias fichas PODEM realizar o mesmo elemento lógico. A regra de uma classe por arquivo pertence à organização opcional Vulcan Architecture, não à capacidade do Minerva de documentar aplicações arbitrárias.

### MIN-005 — Casos de programa

Cada caso L1 no escopo DEVE corresponder a exatamente um caso de programa. O caso DEVE preservar objetivo, condições, decisões, resultados, efeitos e falhas pertinentes da especificação e identificar colaboradores e comportamento delegado às entidades. Decisões acrescentadas DEVEM ser distinguíveis dos requisitos herdados. Um procedimento auxiliar sem caso de origem não pode se tornar silenciosamente outro caso de uso modelado.

### MIN-006 — Dados operacionais e colaboradores técnicos

Contratos de operações DEVEM identificar entradas e saídas por nome, significado, tipo, obrigatoriedade e cardinalidade aplicável. Dados de negócio, contexto de ator da invocação e colaboradores injetados DEVEM permanecer distinguíveis. O perfil YAML utiliza primitivos, entidades e coleções tipadas nos dados operacionais; um tipo escalar nomeado refina um primitivo. Ferramentas, fábricas de conexão e runtimes são colaboradores técnicos, não entradas de negócio serializadas. A assinatura nativa pode registrar detalhes da linguagem separadamente.

### MIN-007 — Regras canônicas das entidades

Entidades DEVEM identificar dados, relações, invariantes, comportamento delegado e dependências. Cada regra DEVE ter responsável e origem recuperáveis. Entidades NÃO DEVEM depender de casos ou ferramentas. Minerva permite entidades orientadas a dados ou com comportamento explicitamente delegado; não prescreve uma distribuição universal de todo comportamento de domínio.

### MIN-008 — Contratos das capacidades das ferramentas

Uma ferramenta DEVE declarar operações, condições, resultados, efeitos, garantias e falhas separadamente do mecanismo selecionado. Casos consomem esses contratos. Satisfazê-los NÃO DEVE exigir uma superclasse, palavra-chave de interface, contêiner de injeção ou biblioteca específica. Um objeto concreto simples com o comportamento documentado é uma realização válida.

### MIN-009 — Entidades prontas e condições contextuais

Uma ferramenta que recebe entidade pronta DEVE confiar em sua validade interna canônica e NÃO DEVE repetir a validação de invariantes, inclusive por condição equivalente renomeada ou gerada automaticamente. A hidratação parte de registros brutos e DEVE utilizar construção canônica. Uma condição contextual distinta, como existência persistida ou unicidade atômica, DEVE identificar objeto, finalidade e responsabilidade. Essas condições não transferem a autorização do caso à ferramenta.

### MIN-010 — Garantias de persistência

Quando houver persistência, o contrato DEVE declarar capacidades de leitura e alteração, responsabilidade pelos dados, garantias transacionais/de concorrência e falhas. Uma consulta prévia não substitui a garantia atômica exigida pelo contrato. Quando uma operação pode ter produzido efeito apesar da falha relatada, o modelo DEVE distinguir resultado desconhecido de ausência de efeito estabelecida. Os exemplos alinhados ao Atlas especificam essas distinções e verificações planejadas; não entregam uma implementação de persistência nem execução de recuperação distribuída.

### MIN-011 — Dependências e composição

O modelo DEVE mostrar o que casos e ferramentas recebem, onde as realizações são selecionadas e como são compostas. Dependências necessárias NÃO DEVEM desaparecer em buscas globais não documentadas. Domínios, tempos de vida e propriedade escolhidos DEVEM ser declarados quando relevantes. Um domínio agrupa responsabilidades; não concede acesso por si só. Minerva não exige organização de pastas nem tempo de vida singleton.

### MIN-012 — Autorização no caso

Cada caso DEVE receber contexto explícito de ator com origem de confiança declarada e decidir permissão antes de efeitos protegidos. Contextos ausentes, não resolvidos, desconhecidos e insuficientes DEVEM ser recusados. Identidade autenticada e participação anônima explícita são decisões contratuais distintas. Um campo JSON fornecido pelo chamador não se torna confiável porque possui a forma de uma entidade. A autorização DEVE funcionar em chamadas diretas ao núcleo.

### MIN-013 — Composição entre casos

Uma chamada a outro caso DEVE declarar dependência, contexto de ator transmitido, contrato consumido e resultado. O caso chamado DEVE aplicar sua própria política. Delegação ou atuação em nome de outro participante exige regra explícita; uma chamada interna não acrescenta permissão. O [exemplo de composição](../examples/composition/README.pt-br.md) preserva o cancelamento chamando a consulta, ambas as decisões de permissão e os resultados de recusa/falha do caso chamado.

### MIN-014 — Comportamento recuperável

Prosa semântica ou pseudocódigo estruturado DEVEM permitir recuperar sequência, decisões, falhas, resultados e efeitos. Um diagrama PODE complementar a descrição. Uma assinatura de método ou caixa genérica “processar” é insuficiente para recuperar o comportamento. RECOMENDA-SE detalhar o contrato sem reproduzir sintaxe incidental da implementação.

### MIN-015 — Grafos identificados

Um grafo DEVE identificar proprietário, tipo, entrada, nós e transições, incluindo condições e ações. Um fluxo representa passagem de controle; um nó final ou de falha identifica resultado terminal. Uma máquina de estados representa um estado e transições permitidas, incluindo auto-transições legítimas. Um grafo herdado da especificação L1 mantém sua origem L1; armazená-lo em YAML não transforma a decisão em L2.

### MIN-016 — Decisões, observações e pendências

O modelo DEVE distinguir obrigações herdadas, decisões acrescentadas, premissas, pendências e observações do código, preservando origem e estado de revisão. Uma mudança observada NÃO DEVE sobrescrever automaticamente a intenção. A revisão DEVE identificar casos, contratos de ferramentas/entidades, cenários e vínculos afetados antes de aprovar uma revisão. As [revisões do TaskBoard](../examples/task-board/revisions/README.pt-br.md) preservam as identidades dos casos e explicitam o refinamento do critério e seu impacto na verificação.

### MIN-017 — Um teste comportamental diretamente vinculado

Cada caso UCS selecionado DEVE possuir exatamente um teste comportamental lógico diretamente vinculado. Um teste PODE conter muitos cenários e consumir muitas verificações de apoio. Funções, arquivos e fixtures são realizações; sua quantidade não redefine a correspondência lógica entre caso e teste. Uma verificação compartilhada NÃO DEVE criar outro teste diretamente vinculado a um caso já existente.

### MIN-018 — Contratos dos cenários

Cada cenário ou verificação de apoio DEVE declarar preparação e precondições, ação, resultado e efeitos esperados, limite observado e configuração relevante. Cenários de caso DEVEM declarar contexto de ator, inclusive ausência deliberada. Uma condição marcada não aplicável DEVE preservar justificativa e não contribui para cobertura aplicável. O comportamento esperado é um oráculo a revisar, não um resultado observado de execução.

### MIN-019 — Rastreabilidade dos critérios de aceite

Cada critério selecionado DEVE estar ligado ao teste comportamental de seu caso e aos cenários ou apoios aplicáveis. Obrigações compartilhadas DEVEM preservar uma definição canônica e identificar casos afetados e seus testes; não se inventa outro caso. Obrigações de origem e elementos L2 DEVEM ter vínculos explícitos de rastreabilidade. O validador YAML resolve o catálogo e os vínculos declarados. Completude, significado e equivalência de obrigações compartilhadas exigem revisão documentada; nenhuma extensão específica do Atlas ou leitor de origem é exigido.

### MIN-020 — Permissão e ausência de efeitos proibidos

A ADVS DEVE especificar invocações permitidas e negadas para cada caso, incluindo as quatro categorias de recusa e participação anônima explicitamente permitida. O oráculo DEVE observar ausência de efeitos protegidos de domínio ou armazenamento antes da autorização válida, além da mensagem de erro. O validador confere categorias e vínculos declarados; a revisão avalia se os cenários realmente estabelecem a política.

### MIN-021 — Alternativas, falhas e limites pertinentes

O plano DEVE cobrir alternativas, falhas e limites necessários ao contrato alegado, incluindo garantias necessárias de entidades e ferramentas. Condições relevantes ainda não verificadas DEVEM ser visíveis e impedir uma alegação irrestrita de cobertura completa. Vínculos de critérios não provam suficiência dos cenários. Entre os riscos que exigem evidência da realização estão autenticação de produção, recuperação distribuída e comportamento exaustivo de falhas de armazenamento.

### MIN-022 — Plano, realização e evidência observada

A verificação planejada, sua realização executável ou procedimental e uma observação de execução DEVEM permanecer distinguíveis. Um resultado observado DEVE identificar revisão da implementação, ambiente, momento, verificações e relatório de evidência, com limitações. Um arquivo ou símbolo observado não demonstra execução. Os blueprints de exemplo não contêm execuções bem-sucedidas fabricadas; relatórios de validação dizem respeito aos documentos e verificações solicitadas.

### MIN-023 — Obrigações de interação referenciadas

Quando uma interação L4 selecionada introduzir obrigações observáveis, a ADVS DEVE referenciar sua origem e especificar cenários pertinentes. Canal, sintaxe de rota/CLI e representação continuam responsabilidades L4; restrições externas exigidas preservam a origem L1. Ilustrações da fonte não selecionam uma implementação L4. Os exemplos preservam obrigações de qualidade com escopo de interação como verificações planejadas e deixam os canais concretos em aberto.

### MIN-024 — Espelho YAML versionado em L2

O perfil YAML DEVE fornecer uma ficha por fonte no escopo declarado do espelho, preservando subdiretórios e a extensão original antes de `.yaml`. Na organização recomendada, `apps/TaskBoard/entities/Entity_Task.py` corresponde a `docs/L2_MinervaBlueprints/apps/TaskBoard/entities/Entity_Task.py.yaml`. `Task.py` e `Task.go` permanecem distintos. Cada ficha contém objetivo, unidades e membros, descrição semântica, entradas/saídas e dependências diretamente ou por referências lógicas. Intenção, bytes observados e pendências DEVEM permanecer distinguíveis.

### MIN-025 — Raízes, referências e empacotamento

Um pacote DEVE declarar raiz documental, lista de fichas, cobertura selecionada e exclusões. Caminhos relativos são resolvidos pela raiz do ecossistema explicitamente fornecida, não por um diretório de trabalho variável. Mover o pacote completo DEVE preservar as relações. Fichas planejadas PODEM existir antes do código, sem hash observado. Alegar correspondência atual com fontes realizadas exige inspeção atual do escopo; uma verificação apenas do modelo não estabelece essa correspondência.

### MIN-026 — Leitura previsível apenas como dados

O leitor DEVE tratar YAML como dados. Rejeita chaves duplicadas ou não textuais, âncoras, aliases e tags explícitas, inclusive executáveis. Fixa a interpretação de escalares, rejeita números não finitos e limita documentos a 8 MiB. Texto parecido com comando permanece texto. O leitor NÃO DEVE importar módulos do aplicativo nem executar fontes, campos YAML ou testes enquanto valida um blueprint.

### MIN-027 — Validação estrutural e de consistência

O validador de referência DEVE verificar schema Minerva suportado, IDs, referências tipadas, relações permitidas, cardinalidade caso/teste, origens declaradas e vínculos de critérios. DEVE rejeitar entidade vinculada a entidade de origem não declarada, origem de regra não resolvida e ator fora do conjunto permitido pelo caso de origem declarado no catálogo. Isso verifica a consistência do Minerva, não a verdade do catálogo perante L1. Diagnósticos DEVEM distinguir essas verificações da revisão semântica. Um modelo revisado vazio não pode alegar cobertura; validade estrutural não prova preservação comportamental.

### MIN-028 — Validação de grafos

Para grafos suportados, o validador DEVE conferir proprietários, referências de nós/arestas, entrada e alcançabilidade, além de declaração terminal para fluxos finitos. DEVE permitir ciclos legítimos, incluindo autotransições em máquinas de estados. Aprovação não prova terminação nem correção das condições. RECOMENDA-SE que um diagrama derivado identifique grafo autoritativo e edição; uma visão ilustrativa não substitui o contrato do grafo.

### MIN-029 — Diagnósticos revisáveis

Diagnósticos DEVEM conter código, severidade, documento, elemento e motivo. Texto e JSON expõem o mesmo problema. Sucesso, documento inválido, perfil não suportado, erro operacional e avaliação inconclusiva DEVEM ter resultados de processo distintos. A automação DEVE avaliar nível e escopo solicitados além do código de saída.

### MIN-030 — Exemplos e contraexemplos

Esta edição DEVE incluir versões L2 dos exemplos mínimo, task-board e composição do Atlas fixado, incluindo as revisões identificadas do TaskBoard. Fixtures de fontes planejadas e contraexemplos reproduzíveis exercitam a ferramenta atual. Resultados esperados DEVEM permanecer separados de evidências efetivas de execução. A preparação e revisão técnica dos exemplos não afirmam aceitação pelo responsável do projeto.
