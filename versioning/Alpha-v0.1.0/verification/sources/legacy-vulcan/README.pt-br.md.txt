# Vulcan Architecture — Alpha-v0.1.0-Alkimim

[English](README.md) · [Guia do repositório](../../README.pt-br.md) · [Formato YAML](references/YAML-FORMAT.pt-br.md) · [Exemplos](examples/README.pt-br.md)

**Edição:** Alpha-v0.1.0-Alkimim. **Data:** 25 de outubro de 2026. **Estado:** especificação experimental para revisão. **Referência OAL:** Alpha-v0.2.0-Alkimim, revisão `5755a4e4a5b31a9614da5d409d03d1db9cf1e20c`.

Esta edição define a Vulcan Architecture como uma organização reutilizável de código de aplicação destinada a satisfazer os requisitos de modelo L3 do OAL. Também define o Vulcan Ecosystem, a organização de projeto na qual aplicações com organizações independentes podem coexistir, ser documentadas, expor boundaries públicas e ser inicializadas conjuntamente ou de forma seletiva. Os exemplos ilustram escolhas concretas; suas linguagens, frameworks, funcionalidades e comandos de execução não se tornam requisitos universais.

## 1. Interpretação e escopo

Os requisitos em inglês identificados por `ECO`, `VA`, `DOC` e `OAL` são o texto de referência desta edição. A edição em português é sua tradução. **DEVE** e **NÃO DEVE** expressam requisitos. **RECOMENDA-SE** expressa uma recomendação cujo afastamento exige explicação quando o escopo pertinente for avaliado. **PODE** expressa uma escolha disponível. Explicações e exemplos esclarecem requisitos sem acrescentar obrigações implícitas.

Os requisitos `ECO` aplicam-se a projetos que adotam Vulcan Ecosystem. Os requisitos `VA` aplicam-se a aplicativos que adotam Vulcan Architecture. Os requisitos `DOC` definem o perfil documental utilizado pelo ecossistema. Os requisitos `OAL` tratam da proveniência, preservação e evidência adicionais necessárias ao declarar uma instanciação ou derivação de L3 do OAL. A declaração identifica seu escopo; adotar um ecossistema não transforma automaticamente cada aplicativo em uma instância de sua arquitetura recomendada.

Um **aplicativo** é um participante identificado com implementação, contratos públicos de interação e modos de execução próprios. Uma **boundary** é a forma publicada de interagir com esse aplicativo: comando, endpoint, interface, canal de eventos, API pública de biblioteca ou outro canal explicitamente descrito. Um **contrato** declara dados e contexto aceitos, resultados, efeitos, condições, falhas e garantias. Ele não exige uma declaração `interface`, classe abstrata ou relação de herança na linguagem de programação.

**Vulcan Architecture** define organização e responsabilidades. **Vulcan Ecosystem** define a cooperação no projeto. **pyVulcan** é o nome de uma biblioteca Python opcional de apoio, fora dos requisitos deste modelo. Este repositório não define classes base `AbsVulcan*` obrigatórias. Bibliotecas para outras linguagens são igualmente possíveis.

Os quatro papéis centrais são value objects, entidades, ferramentas e casos de uso. Composição, configuração, verificação e boundaries apoiam esses papéis. Classificar um código como suporte não permite transferir decisões de aplicação dos casos de uso ou entidades responsáveis.

## 2. Requisitos do Vulcan Ecosystem

### ECO-01 — Raiz e inventário de aplicativos

A raiz do projeto DEVE conter `apps/`, `docs/` e `vulcan.yaml`. Cada aplicativo DEVE ocupar uma pasta identificada sob `apps/` e possuir um manifesto canônico em `docs/<App>/_app.yaml`. O manifesto do ecossistema DEVE identificar os aplicativos e localizar seus manifestos. Os identificadores de aplicativos DEVEM ser únicos no ecossistema.

A raiz também DEVE fornecer o mecanismo de entrada implementado exigido por ECO-08. Arquivos de gerenciamento do repositório, licenciamento, distribuição, automação e suporte geral do ecossistema PODEM existir na raiz. Sua presença não desloca o código das aplicações para fora de `apps/`.

### ECO-02 — Aplicativos heterogêneos

Cada aplicativo DEVE declarar seu perfil arquitetural e as linguagens pertinentes. Um aplicativo PODE utilizar Vulcan Architecture, outra arquitetura, código legado existente ou vários perfis de linguagem. A participação no ecossistema NÃO DEVE exigir a refatoração do aplicativo para as pastas internas da Vulcan nem a adoção de uma biblioteca de apoio.

Um aplicativo com outra arquitetura DEVE ser documentado conforme sua implementação e seus contratos públicos reais. Sua documentação NÃO DEVE inventar classes de casos de uso, renomear símbolos reais ou declarar conformidade Vulcan apenas para se ajustar a um template. Partes cuja implementação não estiver disponível DEVEM ser identificadas como indisponíveis; um contrato externo não demonstra conhecimento de um interior inacessível.

### ECO-03 — Documentação espelhada das fontes

Cada pasta e subpasta de fontes sob `apps/` DEVE possuir sua localização correspondente sob `docs/`. Cada arquivo de fonte coberto DEVE possuir um documento YAML. O mapeamento padrão substitui o prefixo `apps/` por `docs/` e acrescenta `.yaml` ao nome completo da fonte, incluindo sua extensão. Por exemplo, `apps/Tasks/entities/Entity_Task.py` corresponde a `docs/Tasks/entities/Entity_Task.py.yaml`.

O escopo das fontes DEVE ser explícito. Pastas de dependências instaladas, caches e saídas descartáveis de build PODEM ser excluídas com escopo e justificativa declarados. Testes, fontes legadas, fontes de terceiros incorporadas ao projeto e fontes geradas mantidas como parte dele NÃO DEVEM ser omitidos silenciosamente. Configurações, templates, schemas e entradas de build também PODEM receber fichas que descrevam sua natureza real.

Arquivos adicionais de metadados, incluindo `_app.yaml`, não exigem arquivos de código correspondentes fictícios. Arquivos de documentação não exigem documentação recursiva de si mesmos.

### ECO-04 — Caminhos, colisões e identidade

Os caminhos documentais internos DEVEM ser relativos à raiz do ecossistema e utilizar `/`. Uma colisão de mapeamento, incluindo conflito entre arquivo e pasta ou nomes equivalentes em um sistema de arquivos de destino, DEVE ser resolvida por uma substituição explícita de caminho. A substituição DEVE preservar um documento inequívoco para cada fonte e NÃO DEVE sobrescrever outro documento.

Renomear uma fonte DEVE atualizar seu caminho espelhado e suas referências de entrada. RECOMENDA-SE preservar a identidade lógica quando a responsabilidade não tiver mudado. Referências externas DEVEM declarar a fonte e a versão pertinentes; uma descrição copiada NÃO DEVE se tornar silenciosamente uma segunda definição canônica.

### ECO-05 — Catálogo canônico de boundaries

Cada boundary publicada DEVE possuir uma definição canônica no manifesto de seu aplicativo proprietário. O manifesto do ecossistema DEVE oferecer um catálogo que referencie essas definições. Resolver o catálogo DEVE permitir descobrir as operações públicas do projeto e seus contratos de entrada e saída. Cópias editáveis independentes de um contrato de boundary NÃO DEVEM ser mantidas como autoridades concorrentes.

Uma boundary DEVE identificar proprietário, canal, consumidores esperados, operações, versão pertinente do contrato, mecanismo de descoberta ou invocação e modo de execução necessário. Suas operações DEVEM descrever estímulos, representação de dados, resolução de contexto quando pertinente, destino interno, resultados observáveis e falhas. Resultados imediatos, diferidos, por evento e por fluxo DEVEM ser diferenciados quando utilizados.

### ECO-06 — Mapeamento das interações para implementações

Uma boundary de aplicativo Vulcan DEVE referenciar as operações preparadas de casos de uso que invoca. Um aplicativo de outra arquitetura DEVE referenciar suas operações reais. O mapeamento DEVE admitir vários elementos de interface para um caso e vários casos já especificados para um elemento, com a sequência ou coordenação pertinente explícita. Elementos exclusivamente de interface DEVEM ter sua finalidade identificada.

A coordenação de apresentação NÃO DEVE introduzir uma nova decisão, transação ou objetivo de negócio sem atribuir essa responsabilidade a um caso de uso e revisar as fontes de modelagem pertinentes. Um mapeamento entre botão e caso é um contrato de interação; ele não constitui automaticamente uma API adequada para integração de outros aplicativos.

### ECO-07 — Comunicação entre aplicativos

Os aplicativos DEVEM se comunicar por suas boundaries públicas documentadas. Compartilhar repositório ou processo NÃO DEVE ser utilizado para contornar uma boundary por imports privados, acesso direto ao armazenamento de domínio de outro aplicativo ou chamadas a elementos internos não publicados.

O contrato DEVE descrever a representação pública dos dados. A serialização DEVE ser especificada quando exigida pelo canal. Uma API pública de biblioteca PODE ser utilizada sem serialização por bytes quando seu pacote publicado, superfície, tipos de dados e garantias forem explícitos. Um tipo de entidade local, sua representação pública e o tipo reconstruído pelo consumidor DEVEM permanecer distinguíveis.

A integração DEVE descrever falhas e hipóteses de compatibilidade pertinentes. Prazos, correlação, ordenação, repetição, idempotência, efeitos parciais e resultados incertos DEVEM ser declarados quando afetarem o contrato da operação. Um valor ausente em um template não estabelece uma garantia.

### ECO-08 — Inicialização completa e seletiva

O projeto DEVE fornecer um mecanismo documentado e implementado na raiz para descobrir aplicativos e modos disponíveis, iniciar o perfil completo declarado, iniciar um subconjunto selecionado e informar falhas de inicialização. Linguagem, nome do arquivo, interface e tecnologia de orquestração são escolhas de implementação. Um manifesto que apenas lista comandos não satisfaz, sozinho, a exigência de iniciar o projeto.

Cada aplicativo DEVE declarar um modo padrão de inicialização para participar do perfil completo. Iniciar todos os aplicativos significa selecionar seus modos padrão declarados; tarefas de manutenção são executadas somente quando selecionadas explicitamente, escolhidas como padrão de um aplicativo ou exigidas como dependências declaradas de preparação. Modos mutuamente exclusivos e parâmetros obrigatórios DEVEM ser respeitados.

### ECO-09 — Contratos de execução e dependências

Cada modo de execução DEVE identificar processo, contêiner, mecanismo de hospedagem ou tarefa; localização de trabalho; configuração necessária; dependências de inicialização; condição de prontidão ou conclusão; e comportamento pertinente de encerramento e falha. Nomes de configurações PODEM ser documentados sem incorporar valores secretos. RECOMENDA-SE representar comandos por executável e argumentos; uma string de shell exige um contrato explícito de shell.

O inicializador DEVE declarar se dependências necessárias ampliam uma seleção ou causam falha por dependência ausente. Dependências obrigatórias de prontidão DEVEM admitir uma política válida de execução; esperas circulares NÃO DEVEM ser tratadas como uma ordem válida de início. Dependências de código, dependências de inicialização e relações de dados DEVEM permanecer distinguíveis.

A criação de um processo NÃO DEVE ser informada como prontidão sem a evidência declarada. Uma tarefa concluída com sucesso NÃO DEVE ser informada como serviço em execução. O encerramento DEVE atingir apenas recursos pertencentes àquela execução ou explicitamente colocados sob sua gestão. RECOMENDA-SE oferecer consulta de estado e encerramento de recursos gerenciados quando a gestão de serviços persistentes os exigir.

### ECO-10 — Escopo documental e de execução

O ecossistema DEVE identificar quais fontes, aplicativos, boundaries e modos de execução estão implementados, são ilustrativos, estão indisponíveis ou estão pendentes. Um aplicativo participante com outra arquitetura permanece sujeito aos requisitos de documentação e integração do ecossistema, embora esteja fora do perfil VA.

Alterações de código e da documentação correspondente DEVEM ser entregues conjuntamente. Um projeto em transição PODE registrar cobertura incompleta, mas NÃO DEVE descrever essa cobertura como completa enquanto faltarem fichas de fontes ou contratos públicos obrigatórios.

## 3. Requisitos da Vulcan Architecture

### VA-01 — Quatro áreas centrais e suporte

Um aplicativo Vulcan DEVE tornar `value_objects/`, `entities/`, `tools/` e `usecases/` identificáveis como áreas irmãs da organização de seu núcleo. DEVE colocar as boundaries de canal implementadas em `boundaries/`. Áreas adicionais de composição, configuração, erros, testes e outros suportes necessários PODEM existir com suas responsabilidades identificadas.

Uma área PODE não possuir unidades quando o produto não precisar delas; classes artificiais NÃO DEVEM ser introduzidas apenas para preencher uma pasta. Áreas de suporte NÃO DEVEM esconder casos, decisões de domínio ou acesso à persistência de domínio que pertençam aos papéis centrais.

### VA-02 — Uma estrutura por arquivo de fonte

Cada arquivo de implementação do núcleo DEVE definir uma classe ou struct equivalente principal, com seus atributos, métodos e auxiliares locais associados. Essa regra de uma estrutura também se aplica às classes e structs de boundaries, composição e outros suportes. Uma segunda classe ou struct independente NÃO DEVE ser escondida como auxiliar não principal.

Em C, uma struct, seu typedef correspondente e funções explicitamente associadas PODEM constituir uma unidade. Em Go, uma struct e seus métodos associados PODEM constituir uma unidade. Arquivos de declaração e implementação da mesma unidade, como `.h` e `.c`, PODEM compartilhar o nome-base; ambos precisam de fichas que identifiquem sua relação. Uma interface opcional declarada pelo aplicativo DEVE ocupar arquivo próprio.

Arquivos técnicos exigidos pela linguagem ou pelo sistema de build PODEM utilizar sua estrutura obrigatória quando a finalidade e o escopo da exceção forem explícitos. Essa exceção NÃO DEVE se tornar uma dispensa geral para classes não relacionadas ou operações de aplicação.

### VA-03 — Nomes e perfis de linguagem

O nome-base da fonte DEVE coincidir exatamente com o nome da classe, struct ou interface opcional principal, incluindo maiúsculas, minúsculas e underscores. Os nomes centrais DEVEM utilizar `Entity_<PascalCase>`, `ValueObject_<PascalCase>`, `Tool_<PascalCase>` e `UseCase_<PascalCase>`. A forma prefixo com underscore é deliberadamente híbrida. Nomes de classes de suporte DEVEM utilizar PascalCase ou um prefixo de papel documentado.

Métodos definidos pelo desenvolvedor DEVEM utilizar camelCase, e atributos DEVEM utilizar snake_case. RECOMENDA-SE utilizar snake_case em parâmetros e variáveis locais por consistência. O método de entrada de um caso de uso PODE possuir um nome significativo ou genérico, como `execute`; não há nome fixo obrigatório.

Construtores reservados, operadores, métodos especiais e overrides exigidos externamente preservam a grafia obrigatória. Um perfil de linguagem DEVE identificar adaptações necessárias e seu escopo exato. Por exemplo, Go exige inicial maiúscula em identificadores exportados; assim, um método público entre packages pode realizar a operação semântica `createTask` como `CreateTask`. Um perfil adaptado NÃO DEVE declarar cumprimento literal da regra estrita de grafia que altera. As regras de responsabilidade arquitetural permanecem em vigor.

### VA-04 — Value objects

Um value object DEVE representar um valor significativo com invariantes explícitas e igualdade de acordo com seu conteúdo pertinente. DEVE ser imutável e independente de infraestrutura. Suas operações DEVEM ser puras em relação a recursos externos.

Somente entidades do mesmo aplicativo PODEM consumir value objects diretamente no código de produção. Testes de apoio PODEM exercitá-los diretamente. Um value object NÃO DEVE aparecer como entrada ou saída operacional pública de um caso de uso, ferramenta ou boundary. A entidade que o contém expõe dados primitivos, entidades ou operações apropriadas, preservando o encapsulamento. Várias entidades locais PODEM reutilizar um tipo de value object.

### VA-05 — Entidades e invariantes

Uma entidade DEVE descrever seus dados, estado, relações, invariantes e garantias pertinentes de propriedade ou mutação. PODE representar dados de domínio, uma entrada, um resultado ou um contexto de invocação. Identidade persistente, armazenamento em banco e uma estratégia universal de igualdade não são propriedades obrigatórias de toda entidade neste modelo.

Entidades PODEM depender de entidades locais, value objects locais, tipos neutros e operações puras. NÃO DEVEM depender de ferramentas, casos de uso, implementações de canal ou recursos de infraestrutura. A construção canônica e as alterações permitidas DEVEM preservar a validade interna da entidade.

O comportamento alocado a uma entidade DEVE ser identificável regra por regra. Decisões de aplicação alocadas a um caso de uso DEVEM permanecer nesse caso. Compartilhar um tipo de entidade entre domínios não exige compartilhar instâncias mutáveis; propriedade e vida útil pertinentes das instâncias DEVEM ser declaradas.

### VA-06 — Ferramentas e garantias técnicas

Uma ferramenta DEVE realizar uma capacidade técnica sob contrato explícito de entradas, saídas, efeitos, falhas e garantias. PODE utilizar bibliotecas e recursos técnicos e PODE receber, construir ou devolver entidades locais. NÃO DEVE inventar regras de domínio nem assumir a decisão de autorização de um caso de uso.

Uma ferramenta que recebe uma entidade pronta DEVE confiar nas invariantes internas já estabelecidas dessa entidade e NÃO DEVE repetir sua validação canônica ou uma cópia equivalente. A hidratação de registros brutos DEVE utilizar a construção canônica da entidade. Condições técnicas distintas, como versão esperada, unicidade atômica, conflito de persistência ou disponibilidade de recurso, PODEM ser avaliadas quando seu objeto e sua responsabilidade forem explícitos.

Verificações de representação e conversão técnica de registros DEVEM permanecer distinguíveis da validade de domínio. Garantias de persistência que exigem atomicidade NÃO DEVEM ser substituídas por verificações prévias não atômicas apresentadas como garantias equivalentes.

### VA-07 — Casos de uso e núcleo invocável

Um caso de uso DEVE implementar uma operação identificável da aplicação e suas decisões, regras, alternativas e falhas alocadas. PODE consumir entidades locais, ferramentas e outros casos de uso locais. Seu contrato invocável DEVE permanecer utilizável sem exigir um canal externo específico, como Web ou CLI.

A extração de um auxiliar NÃO DEVE criar uma nova identidade de caso apenas porque a implementação precisa de outro arquivo ou função. Quando a decomposição revelar um novo objetivo de domínio, as fontes de modelagem e identidades de casos correspondentes DEVEM ser revisadas explicitamente. A organização do código DEVE preservar o significado da operação que materializa.

### VA-08 — Domínios de acesso

Cada caso de uso DEVE pertencer a um domínio identificado em `usecases/<Domain>/`. O manifesto do aplicativo DEVE declarar finalidade do domínio, casos integrantes, políticas de acesso aplicáveis e responsabilidade pertinente sobre os dados. Um domínio PODE agrupar casos por responsabilidade e contexto de acesso; não precisa coincidir com um papel de usuário, banco, tabela ou aplicativo separado.

Políticas compartilhadas PODEM ser referenciadas, mas a política efetiva de cada caso DEVE permanecer recuperável. Pertencer a uma pasta NÃO DEVE conceder permissão por si só. A organização por domínios é exigida por esta edição Vulcan; o termo “domínio de acesso” e essa convenção de pastas são escolhas da Vulcan, sem afirmar que o OAL as exige universalmente.

RECOMENDA-SE escolher e documentar o isolamento de dados de acordo com as obrigações do domínio. Separação física, separação lógica e compartilhamento justificado são possibilidades; nenhuma autoriza acesso aos dados privados de outro aplicativo fora de ECO-07.

### VA-09 — Contexto de ator e autorização

Cada caso de uso DEVE receber contexto de ator por um caminho explícito de invocação com origem e hipóteses de confiança declaradas. O contexto PODE ser representado por uma entidade local ou dados primitivos sob o contrato documentado; não há classe base universal de contexto nem conjunto fixo de campos obrigatório.

O caso DEVE avaliar sua política de autorização antes de efeitos de domínio. Contexto ausente, não resolvido, desconhecido, não permitido ou insuficiente por outro motivo DEVE ser recusado. Participação anônima DEVE ser explicitamente permitida e representada; falha de resolução NÃO DEVE se tornar silenciosamente acesso anônimo. A política DEVE permanecer efetiva nas chamadas diretas ao núcleo e nas chamadas por boundary.

Uma boundary ou mecanismo declarado de chamada direta fornece o contexto e realiza a autenticação exigida. Uma string de papel fornecida pelo chamador NÃO DEVE, sozinha, ser tratada como resolução confiável. Um ator sistema, uma chamada interna ou um controle oculto de interface não cria permissão.

### VA-10 — Composição entre casos e ferramentas

Dependências de casos de uso em outros casos locais DEVEM ser explícitas e acíclicas. O chamador DEVE fornecer o contexto de ator pertinente, e o caso chamado DEVE aplicar sua própria política. Delegação ou atuação em nome de outro participante exige contrato explícito.

A composição técnica entre ferramentas locais PODE ser utilizada com dependências explícitas e um grafo acíclico de dependências entre ferramentas. Essa permissão e a restrição de ausência de ciclos são escolhas deste modelo. Ferramentas NÃO DEVEM consumir casos de uso nem chamar uma boundary local para alcançar indiretamente o núcleo. Laços de algoritmos e transições de estado não são ciclos do grafo de dependências dos componentes.

Entidades e value objects preservam as restrições de dependência de VA-04 e VA-05. Casos de uso NÃO DEVEM consumir diretamente value objects, requests de framework, referências nativas de infraestrutura ou o mecanismo global de composição. Bibliotecas neutras e puras PODEM ser utilizadas sem introduzir dependências ocultas de rede ou estado.

### VA-11 — Seleção explícita de colaboradores

Um aplicativo DEVE possuir um local identificável de composição que selecione implementações e forneça colaboradores. PODE ser uma função, módulo, classe, pacote ou configuração de framework. Dependências necessárias NÃO DEVEM ficar ocultas em busca global nem ser obtidas fornecendo o container inteiro ao núcleo.

Uma classe concreta, interface da linguagem, contrato estrutural ou classe base abstrata PODE expressar o contrato de um colaborador. Não se exige herança de `AbsVulcan*`, padrão de interface por ferramenta, classe `Container` ou framework de injeção. A implementação escolhida DEVE atender às garantias documentadas na configuração selecionada.

Vida útil e liberação de recursos DEVEM ser declaradas quando pertinentes: escopos de aplicativo, sessão, requisição ou operação são possibilidades. Uma única instância por aplicativo é opcional. Construir entidades de dados durante uma operação não autoriza selecionar provedores de infraestrutura dentro do caso.

### VA-12 — Dados operacionais e dependências técnicas

Entradas e saídas operacionais de dados DEVEM consistir em primitivos, entidades locais ou representações públicas de entidades explicitamente declaradas. Coleções PODEM compor esses tipos; elementos de listas e valores de mapas DEVEM ser tipados, e chaves de mapas DEVEM ser primitivas. Valores ausentes e retornos sem resultado DEVEM ser representados explicitamente. Restrições de formato e precisão DEVEM ser declaradas quando afetarem o significado.

Colaboradores, conexões nativas, clientes de SDK, callbacks e objetos de framework DEVEM ser documentados como parâmetros técnicos, recursos ou dependências de injeção, em vez de disfarçados como entidades públicas de dados. Uma assinatura nativa registrada não substitui o contrato semântico de dados. Referências técnicas opacas, quando operacionalmente necessárias, exigem representação neutra com propriedade, validade e operações permitidas declaradas.

Restrições de transporte público, como chaves textuais de mapas, DEVEM possuir projeção declarada que preserve as distinções pertinentes. Um dicionário genérico ou tipo nativo sem restrições NÃO DEVE esconder um contrato de entidade ou primitivo que seria exigido.

### VA-13 — Resultados, falhas e efeitos

Operações DEVEM diferenciar resultados bem-sucedidos, ausência, falha, resultados parciais e efeitos incertos quando aplicável. Uma linguagem PODE expressar falhas por exceções, variantes de resultado ou códigos de retorno; o significado documentado DEVE permanecer recuperável independentemente desse mecanismo. Dados de falha DEVEM seguir VA-12.

Para fluxos de itens ou trabalho diferido, o contrato DEVE descrever tipo de item, ordenação quando garantida, conclusão, falha e cancelamento. Cancelamento NÃO DEVE ser representado como rollback, salvo quando houver garantia real de rollback. Efeitos pertinentes de mutação e propriedade DEVEM ser registrados junto às saídas.

### VA-14 — Boundaries e responsabilidade do núcleo

Boundaries do aplicativo DEVEM invocar casos de uso preparados e traduzir dados de canal, contexto, resultados e falhas conforme seus contratos. PODEM utilizar entidades locais e mecanismos específicos do canal. NÃO DEVEM chamar diretamente ferramentas do núcleo, expor value objects ou absorver decisões de domínio do núcleo.

Armazenamento exclusivo de estado técnico do canal, como sessões e correlação, PODE ser utilizado sob contrato explícito com dados, vida útil, condições e falhas declarados. NÃO DEVE oferecer um atalho para ler ou alterar dados de domínio nem substituir a autorização do caso. Mecanismos de boundary permanecem responsabilidades L4 em um escopo OAL.

### VA-15 — Documentação do comportamento

Cada operação relevante DEVE possuir uma descrição semântica suficiente para recuperar decisões, efeitos, resultados e falhas. RECOMENDA-SE utilizar grafos de fluxo para ramificações ou sequências significativas e máquinas de estados quando transições de estado forem relevantes ao contrato.

Um grafo DEVE identificar início, nós, arestas, condições e operações invocadas pertinentes. Uma máquina de estados DEVE identificar de quem é o estado modelado, seus estados, estado inicial quando aplicável, eventos, guardas, efeitos e transições. O progresso de uma invocação NÃO DEVE ser confundido com o ciclo de vida persistido de uma entidade ou o estado de um recurso técnico.

YAML estruturado é a representação canônica de um grafo documentado neste perfil. Diagramas renderizados PODEM ser derivados dele. Definições concorrentes e independentes de um grafo NÃO DEVEM ser mantidas como se ambas fossem autoritativas. Uma unidade simples PODE declarar a inaplicabilidade de um grafo com explicação suficiente.

### VA-16 — Integração da verificação

O aplicativo DEVE identificar como suas verificações comportamentais e verificações de apoio são executadas contra o núcleo invocável e os canais pertinentes. Vínculos entre caso, critério, cenário e verificação de apoio DEVEM permanecer identificáveis. A verificação de chamada direta DEVE incluir o comportamento de autorização quando ele integrar o contrato.

Código de verificação, cenários planejados e execuções observadas DEVEM ser registrados como objetos distintos. Verificações falhas, ignoradas, não executadas ou inconclusivas DEVEM ser informadas no escopo declarado. Uma verificação bem-sucedida do núcleo NÃO DEVE ser apresentada como evidência de um canal não testado.

### VA-17 — Evolução e declarações arquiteturais

Alterações em contratos de fontes, permissões, representações, dependências ou responsabilidades de componentes DEVEM provocar análise de impacto no código, documentação, consumidores e verificação. O aplicativo DEVE preservar versões pertinentes das fontes e manter identidades quando as responsabilidades permanecerem as mesmas.

Uma declaração de perfil estrito DEVE identificar a edição Vulcan e o escopo do aplicativo. Uma declaração de perfil adaptado DEVE identificar cada adaptação de linguagem e a propriedade preservada. Uso de biblioteca, nomes de pastas, verificações estruturais aprovadas e hashes de fontes NÃO DEVEM ser apresentados isoladamente como prova de conformidade arquitetural ou comportamental completa.

## 4. Perfil documental

### DOC-01 — Três tipos de documento

O perfil documental DEVE distinguir documentos `ecosystem`, `app` e `source` e identificar sua versão de formato. O `vulcan.yaml` da raiz inventaria aplicativos, referências de boundaries, escopo documental e política de execução. Cada `_app.yaml` contém os domínios, boundaries canônicas, informações de tipos públicos e modos de execução de seu aplicativo. Cada ficha de fonte explica seu arquivo correspondente.

Os documentos DEVEM seguir as definições de campos e o schema publicados para a versão de formato selecionada. Mapeamentos YAML DEVEM possuir chaves únicas. A documentação DEVE ser interpretada como dados; strings, tags, comandos e condições de grafos NÃO DEVEM ser executados apenas porque um leitor está abrindo um documento. O guia [YAML-FORMAT](references/YAML-FORMAT.pt-br.md) explica os campos e aponta para [o schema](schemas/vulcan.schema.json).

### DOC-02 — Identidade e finalidade da fonte

Uma ficha de fonte DEVE identificar aplicativo proprietário, caminho exato da fonte, linguagem, natureza do arquivo, perfil arquitetural, finalidade e unidades presentes. Fontes geradas DEVEM identificar seu gerador e entradas pertinentes quando conhecidos. Uma observação indisponível DEVE permanecer indisponível, em vez de ser preenchida com hash, execução ou versão inventados.

Declarações, implementações, configurações, marcadores vazios de pacote e testes DEVEM ser descritos segundo seu papel real. Um arquivo sem operação chamável NÃO DEVE receber uma assinatura artificial de entrada e saída apenas para satisfazer um template.

### DOC-03 — Unidades e membros

A coleção de unidades DEVE identificar classes, structs, interfaces, funções ou outras estruturas realmente presentes. Operações e atributos DEVEM declarar as informações necessárias para recuperar seu significado e contrato. Auxiliares associados DEVEM identificar a unidade que apoiam.

O perfil Vulcan DEVE aplicar VA-02, em vez de tratar a coleção como permissão para várias estruturas não relacionadas. Outros perfis PODEM descrever fielmente várias unidades independentes em uma ficha de fonte. Essa documentação não constitui solicitação de refatoração do arquivo.

### DOC-04 — Tipos, referências e definições canônicas

Descrições de tipos operacionais DEVEM seguir VA-12. Definições de entidades e value objects DEVEM ser referenciadas por suas unidades canônicas de fonte, em vez de copiadas como definições concorrentes. Referências DEVEM resolver para o papel, unidade e operação pretendidos, não apenas para um nome de arquivo existente.

Um aplicativo pode descrever localmente um contrato público externo de dados sem importar a classe interna de entidade do produtor. Esse registro DEVE identificar a boundary de origem e a representação pública. Um valor estruturado legado PODE ser documentado como entidade de dados sem exigir que uma classe `Entity_` exista no código legado.

### DOC-05 — Dependências e evidência de composição

Registros de dependências DEVEM identificar colaborador, finalidade, contrato, mecanismo de obtenção ou injeção e escopo da relação. Registros de recursos técnicos DEVEM identificar bibliotecas, SDKs, recursos nativos e nomes de configuração pertinentes sem transformá-los em entidades de domínio ou ferramentas fictícias.

Dependências de código, relações por boundary entre aplicativos e dependências de inicialização DEVEM permanecer separadas. Uma dependência legada problemática documentada PODE ser registrada como fato existente a revisar; NÃO DEVE redefinir silenciosamente uma permissão Vulcan.

### DOC-06 — Bindings de boundary

A documentação de boundary DEVE relacionar os dados recebidos e o contexto resolvido às entradas da operação interna, e relacionar seus resultados e falhas às saídas do canal. Os bindings DEVEM utilizar identidades de operações e campos que possam ser resolvidas. Várias invocações DEVEM identificar cada chamada e sua coordenação, de modo que saídas e dependências sejam inequívocas.

O contrato operacional interno e a representação do canal DEVEM ser distinguíveis. Um corpo JSON, argumento CLI ou envelope de transporte não substitui, por si só, o contrato de dados do núcleo. Obrigações de representação PODEM ser declaradas em um schema de conteúdo com a interpretação necessária identificada.

### DOC-07 — Evidência e atualização

Revisões ou digests de fontes DEVEM identificar os bytes efetivamente observados quando registrados. Um digest coincidente estabelece que os bytes observados correspondem à referência registrada; não demonstra a correção semântica da documentação ou implementação. Dependências e alterações contratuais DEVEM ser consideradas mesmo quando o digest da própria fonte de um consumidor não tiver mudado.

Evidências de execução DEVEM declarar versão pertinente da implementação, ambiente, comando ou mecanismo, cenários, resultados e limites. Registros planejados, implementados, não executados, falhos e observados como aprovados NÃO DEVEM ser condensados em um único estado genérico de aprovação. A localização das evidências DEVE ser descobrível a partir dos registros pertinentes de aplicativo ou caso.

### DOC-08 — Limites da validação

A aceitação estrutural pelo schema DEVE ser diferenciada da resolução de referências, revisão semântica, inspeção da fonte e verificação de execução. Um verificador DEVE declarar quais dessas atividades realiza. Cobertura incompleta e verificações de linguagem não suportadas DEVEM ser informadas, em vez de contadas silenciosamente como aprovadas.

Uma avaliação DEVE identificar versão do modelo, aplicativos, perfis de linguagem, fontes e verificações selecionadas. A aprovação dos exemplos fornecidos demonstra somente as observações registradas para esses exemplos e configurações. Não certifica aplicativos futuros nem estabelece comportamento universal.

## 5. Instanciação de L3 do OAL e proveniência

### OAL-01 — Objeto declarado e baselines

Uma declaração OAL DEVE distinguir o modelo L3, um artefato concreto organizado por esse modelo e qualquer derivação ou transformador declarado. DEVE identificar edição OAL, edição Vulcan, objeto declarado, escopo, baselines das fontes, adaptações e evidências. Os requisitos da edição OAL referenciada permanecem autoritativos para essa declaração.

O Vulcan Ecosystem PODE reunir artefatos de várias camadas. Sua coexistência NÃO DEVE ser apresentada como prova de cobertura completa das camadas OAL, de um transformador construído ou de uma transformação executada. Definir um modelo L3 não exige executar todos os testes de projetos futuros que possam instanciá-lo.

### OAL-02 — Materialização e identidade dos casos

Um aplicativo que declara uma derivação para L3 DEVE identificar suas fontes L2 versionadas, incluindo ADPM e ADVS, e mapear seus papéis, dependências, algoritmos, falhas e identidades de casos para o código. Desvios pertinentes e fontes afetadas DEVEM ser registrados. UCS consultada como fonte adicional DEVE ter sua baseline e finalidade identificadas.

No escopo OAL declarado, cada identidade de caso UCS DEVE corresponder a exatamente uma identidade de caso ADPM, um teste comportamental ADVS diretamente vinculado e uma identidade de caso ADI. Identidades extras de casos ADPM ou ADI e testes comportamentais ADVS diretamente vinculados adicionais NÃO DEVEM ser introduzidos fora dessa correspondência. Auxiliares e subtestes de apoio não criam identidades de casos adicionais. Um teste comportamental PODE conter vários cenários e verificações de apoio; a regra de identidade não exige uma única função ou arquivo físico de teste.

### OAL-03 — Preservação de autorização e verificação

O caminho explícito do contexto de ator, as hipóteses de confiança e a autorização do caso exigidos por VA-09 DEVEM preservar os contratos de modelagem pertinentes. A verificação derivada de ADVS DEVE permanecer vinculada a seu caso, critérios e cenários e ser executável contra a configuração declarada do núcleo.

O registro DEVE distinguir execução permitida de recusas por contexto ausente, não resolvido, desconhecido, não permitido ou insuficiente, conforme aplicável, incluindo chamadas diretas. Participação anônima explicitamente permitida DEVE ser tratada conforme seu contrato especificado. Obrigações falhas e não executadas DEVEM permanecer visíveis.

### OAL-04 — Registros de derivação e alteração

Uma derivação declarada DEVE registrar baselines versionadas de origem e destino, uma pessoa responsável identificada pelo nome, escopo, obrigações de preservação e decisões acrescentadas. Organizar código manualmente segundo este modelo NÃO DEVE ser descrito como construir ou executar um transformador automatizado, salvo quando essa declaração separada for sustentada.

Alterações DEVEM preservar a rastreabilidade às fontes L2 pertinentes e identificar artefatos e verificações afetados. Requisitos reconstruídos DEVEM ser identificados como reconstruídos, em vez de apresentados como evidência independente de stakeholders.

### OAL-05 — Responsabilidade de boundary e escopo

Contratos do núcleo invocável pertencem à organização L3. Decisões sobre botões, telas, rotas, comandos, tópicos, representações de payload e resultados apresentados pertencem a L4. Um formato YAML ou uma pasta física compartilhada NÃO DEVE ser utilizado para apagar essa distinção.

Quando um projeto também declara um escopo L4, DEVE identificar o modelo L4 aplicável e as obrigações de canal, preservar os mapeamentos de casos e registrar verificação específica do canal. Um núcleo funcionando não estabelece o comportamento de uma boundary não testada. O mapeamento muitos para muitos de interface não cria novas identidades de casos.

## 6. Uso desta edição

O [ecossistema de quadro de tarefas](examples/task-board-ecosystem/README.pt-br.md) oferece uma superfície concreta de revisão da organização de código, interação pública, aplicativos heterogêneos, documentação e inicialização. Os guias e registros de verificação dos próprios exemplos definem o que está implementado e o que foi observado. O comportamento de produto dos exemplos é ilustrativo e não acrescenta funcionalidades obrigatórias à Vulcan.

O [alinhamento com OAL](references/OAL-ALIGNMENT.pt-br.md) relaciona estes requisitos aos cinco assuntos de ADI. O [guia de migração](references/MIGRATION.pt-br.md) explica quais premissas da arquitetura anterior foram preservadas ou substituídas. O [guia YAML](references/YAML-FORMAT.pt-br.md) descreve a representação documental. As ilustrações do repositório ficam no guia da raiz e nos assets; este texto versionado é a especificação para revisão.

O estado Alpha indica que a edição está aberta a revisão. Uma alteração que afete significado precisa receber versão ou registro de revisão explícito. RECOMENDA-SE que os consumidores fixem a edição e a revisão exatas do repositório que avaliam, em vez de depender de uma declaração genérica de “mais recente”. Políticas de publicação e distribuição são registradas pelo repositório; não modificam os requisitos acima.

## 7. Referências primárias

A referência OAL está fixada na revisão `5755a4e4a5b31a9614da5d409d03d1db9cf1e20c` da edição **Alpha-v0.2.0-Alkimim**. As seções pertinentes são [regras entre camadas](https://github.com/CodeVaultCommunity/OAL-Open-Analysis-Layers/blob/5755a4e4a5b31a9614da5d409d03d1db9cf1e20c/versioning/Alpha-v0.2.0-Alkimim/README.md#oal-layers), [ADPM](https://github.com/CodeVaultCommunity/OAL-Open-Analysis-Layers/blob/5755a4e4a5b31a9614da5d409d03d1db9cf1e20c/versioning/Alpha-v0.2.0-Alkimim/README.md#adpm), [ADVS](https://github.com/CodeVaultCommunity/OAL-Open-Analysis-Layers/blob/5755a4e4a5b31a9614da5d409d03d1db9cf1e20c/versioning/Alpha-v0.2.0-Alkimim/README.md#advs), [ADI](https://github.com/CodeVaultCommunity/OAL-Open-Analysis-Layers/blob/5755a4e4a5b31a9614da5d409d03d1db9cf1e20c/versioning/Alpha-v0.2.0-Alkimim/README.md#adi) e [ADIB](https://github.com/CodeVaultCommunity/OAL-Open-Analysis-Layers/blob/5755a4e4a5b31a9614da5d409d03d1db9cf1e20c/versioning/Alpha-v0.2.0-Alkimim/README.md#adib).

A adaptação de nomes Go segue a [regra de identificadores exportados](https://go.dev/ref/spec#Exported_identifiers) da especificação da linguagem. A serialização documental utiliza [YAML 1.2.2](https://yaml.org/spec/1.2.2/) e um JSON Schema versionado aplicado após interpretar o YAML. Essas ferramentas de serialização não substituem os requisitos semânticos desta edição.
