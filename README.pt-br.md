<p align="center"><img src="assets/minerva-banner-pt-br.png" alt="Minerva Blueprints · Olympus Project · Alpha-v0.1.0" width="100%"></p>

<p align="center"><strong>Minerva Blueprints Alpha-v0.1.0 · OAL L2 / ADMV</strong></p>

Português brasileiro · [English](README.md)

# Minerva Blueprints

**Minerva Blueprints é um modelo de L2 do OAL para descrever o programa e especificar sua verificação.** Reúne ADPM e ADVS, contratos de casos, entidades e ferramentas, dependências, comportamento, cenários e um espelho YAML por arquivo em L2.

Integra o **Olympus Project**, junto do Atlas Specifications (L1) e do Vulcan Ecosystem (L3).

Este README é a apresentação ilustrada. O [manual da edição](versioning/Alpha-v0.1.0/README.pt-br.md) contém as regras textuais. Inglês é normativo; português é sua tradução. A Alpha está pronta para experimentação e revisão; o [relatório de verificação](versioning/Alpha-v0.1.0/verification/RELEASE.md) delimita os resultados observados.

## Conteúdo

- [Posicionamento no Olympus](#position)
- [Programa e verificação](#content)
- [Fluxo de trabalho](#workflow)
- [Início rápido](#quick-start)
- [Documentação por camada](#documentation)
- [Exemplos](#examples)
- [Versões](#versions)
- [Organização do repositório](#repository-organization)
- [Verificação e integridade](#verification)
- [Autoria e licença](#authorship)

<a id="position"></a>
## Posicionamento no Olympus

<p align="center"><img src="assets/minerva-oal-position-pt-br.png" alt="Minerva Blueprints and the OAL layers" width="900"></p>

A referência é [OAL Stable-v1.0.0](https://github.com/CodeVaultCommunity/OAL_OpenAnalysisLayers). O Atlas fornece especificações L1; Minerva reúne ADPM e ADVS em L2; Vulcan organiza a realização em L3. As fontes estão fixadas por revisão e bytes em [source-baselines.json](versioning/Alpha-v0.1.0/verification/source-baselines.json).

<a id="content"></a>
## Programa e verificação

<p align="center"><img src="assets/minerva-model-pt-br.png" alt="Minerva Blueprints: responsibilities and artifacts" width="900"></p>

O modelo define identidades, contratos e relações. O perfil YAML representa esse conteúdo e organiza as fichas por arquivo. O validador verifica estrutura, referências, cobertura declarada e condições do perfil; a revisão de preservação do comportamento permanece explícita.

Consulte as [regras identificadas](versioning/Alpha-v0.1.0/README.pt-br.md#reference-rules) e o [mapeamento dos requisitos](versioning/Alpha-v0.1.0/verification/REQUIREMENTS.pt-br.md). Identidade do modelo, versão do perfil e revisão de um documento permanecem distinguíveis.

<a id="workflow"></a>
## Fluxo de trabalho

<p align="center"><img src="assets/minerva-workflow-pt-br.png" alt="Minerva Blueprints: authoring, verification and feedback" width="900"></p>

Selecione a fonte L1, modele o programa e os cenários, registre decisões e valide o pacote. Fichas podem descrever arquivos planejados. Ao relacionar código existente, preserve a diferença entre projetado e observado e registre as divergências.

<a id="quick-start"></a>
## Início rápido

Use Python 3.11 ou superior. Na raiz extraída, execute:

```bash
cd versioning/Alpha-v0.1.0
python -m venv .venv
# POSIX: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python run_examples.py --all
python validator/minerva_validate.py examples/task-board-ecosystem/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/task-board-ecosystem --json
```

A edição contém suas ferramentas e recursos. Consulte os comandos e pré-requisitos completos no [manual](versioning/Alpha-v0.1.0/README.pt-br.md#quick-start). O projeto distribui um modelo e ferramentas de referência; a biblioteca de conveniência permanece opcional.

<a id="documentation"></a>
## Documentação por camada

| Local recomendado | Conteúdo |
| --- | --- |
| `docs/L1_AtlasSpecifications/` | Casos e contratos de origem. |
| `docs/L2_MinervaBlueprints/` | ADPM, ADVS e espelho YAML por arquivo. |
| `docs/L3_Vulcan/` | Organização, composição, operação, integrações e evidências. |
| `docs/Shared/` | Apoio e assuntos transversais, com referências canônicas. |

Docs/ na raiz é recomendado. Uma alternativa declarada pode preservar as informações e os vínculos exigidos. As fichas por arquivo pertencem ao Minerva: apps/TaskBoard/entities/Entity_Task.py corresponde a docs/L2_MinervaBlueprints/apps/TaskBoard/entities/Entity_Task.py.yaml. O repositório de especificação mantém sua própria organização editorial.

<a id="examples"></a>
## Exemplos

| Exemplo | O que demonstra |
| --- | --- |
| [TaskBoard](versioning/Alpha-v0.1.0/examples/task-board-ecosystem/README.pt-br.md) | Fonte Atlas própria, ADPM, ADVS e fichas L2. |
| [Minimal](versioning/Alpha-v0.1.0/examples/minimal/README.pt-br.md) | Um contrato pequeno para começar. |
| [Legacy](versioning/Alpha-v0.1.0/examples/legacy/README.pt-br.md) | Várias unidades em um arquivo legado. |
| [Planned](versioning/Alpha-v0.1.0/examples/planned/README.pt-br.md) | Modelagem anterior à implementação. |

O TaskBoard usa uma instância Atlas própria, reconstruída e didática. Seu contrato difere do Task Board publicado pelo Atlas. Origem, diferenças e limites estão identificados nos documentos do exemplo; não se afirma geração automática nem aprovação independente de stakeholders.

<a id="versions"></a>
## Versões

| Edição | Status | Manual e notas | Verificação |
| --- | --- | --- | --- |
| Alpha-v0.1.0 | Alpha | [English](versioning/Alpha-v0.1.0/README.md#release-notes) · [Português](versioning/Alpha-v0.1.0/README.pt-br.md#release-notes) | [Report](versioning/Alpha-v0.1.0/verification/RELEASE.md) |

Cada edição contém suas dependências, ferramentas, exemplos e testes. Esta distribuição inclui somente Alpha-v0.1.0; revisões futuras deverão preservar os snapshots publicados e declarar migrações.

<a id="repository-organization"></a>
## Organização do repositório

| Local | Finalidade |
| --- | --- |
| `README.md`, `README.pt-br.md` | Apresentação ilustrada e navegação. |
| [`assets/`](assets/README.pt-br.md) | Ícones fornecidos, headers, diagramas e fontes editáveis. |
| [`versioning/Alpha-v0.1.0/`](versioning/Alpha-v0.1.0/README.pt-br.md) | Manual textual e edição autossuficiente. |
| [`CONTENT-SHA256.json`](CONTENT-SHA256.json) | Inventário único de bytes e hashes de distribuição. |
| [`scripts/`](scripts/) | Verificação de links, inventário e empacotamento. |
| [`docs/releasing.pt-br.md`](docs/releasing.pt-br.md) | Procedimento reproduzível de distribuição. |
| [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md) | Navegação e manutenção assistida. |

<a id="verification"></a>
## Verificação e integridade

```bash
python scripts/check_archive.py .
python scripts/check_repository.py
```

Execute a auditoria do diretório logo após extrair, antes de criar ambientes ou caches dentro dele. O inventário cobre todos os arquivos distribuídos, exceto ele próprio. Detecta ausências, acréscimos e alterações. O [guia de release](docs/releasing.pt-br.md) distingue verificações locais, CI configurada e publicação remota.

<a id="authorship"></a>
## Autoria e licença

Conceito e autoria do projeto: **Douglas de Oliveira Alkimim**. Preparação desta Alpha com assistência de IA, para revisão. Distribuído sob a [licença MIT](LICENSE). Créditos das fontes e dos recursos em [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md); metadados em [CITATION.cff](CITATION.cff).

<p><img src="https://avatars.githubusercontent.com/u/65194413?v=4" alt="Douglas de Oliveira Alkimim" width="88" height="88" align="left" hspace="12"><strong>Douglas de Oliveira Alkimim</strong><br><a href="https://github.com/douglas-alkimim">GitHub</a> · <a href="https://www.linkedin.com/in/douglas-alkimim/">LinkedIn</a></p>
<br clear="all">
