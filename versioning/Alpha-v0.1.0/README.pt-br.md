# Minerva Blueprints · Alpha-v0.1.0

[English](README.md)

Minerva é o modelo do Olympus Project para **OAL L2 / ADMV: modelagem de programa (ADPM) e especificação de verificação (ADVS)**. Esta Alpha autossuficiente e ainda não publicada contém modelo, perfil YAML, validador de referência e exemplos alinhados ao Atlas. Não inclui reader do Atlas nem motor de tradução; um futuro motor será um projeto separado.

## Leitura e adoção

- [Modelo normativo](specification/model.pt-br.md) — IDs MIN estáveis; inglês é a fonte normativa.
- [Conformidade e limites](specification/conformance.pt-br.md) · [Correspondência OAL](specification/oal-correspondence.pt-br.md).
- [Perfil YAML e starter](implementations/yaml/README.pt-br.md).
- [Mapeamento Atlas](integrations/atlas/mapping.pt-br.md) · [Compatibilidade](integrations/atlas/compatibility.json).
- [Exemplos com fontes oficiais](examples/README.pt-br.md) · [Requisitos](verification/REQUIREMENTS.pt-br.md).
- [Revisão técnica](verification/reviews/contract-review.pt-br.md) · [Verificações observadas](verification/VALIDATION.pt-br.md).

<a id="quick-start"></a>
## Início rápido

Use Python 3.11+. Execute a partir desta edição, com dependências instaladas em ambiente fora da árvore de entrega:

```bash
python -m pip install .
python run_examples.py --all
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
python tests/fixtures/counterexamples/check.py
python run_examples.py --test
```

O comando instalado é `minerva-validate`; `python -m minerva_blueprints` usa a mesma entrada. Outra opção é instalar `requirements.txt` e usar o launcher da edição. Nenhum comando seleciona outra edição, baixa modelos de origem ou executa código da aplicação implicitamente.

O catálogo de origem é conteúdo elaborado no Minerva. A validação verifica suas referências internas e o hash do arquivo L1 opaco. A preservação da fonte é avaliada separadamente na revisão registrada. Cenários dos exemplos continuam planejados; resultados de testes referem-se ao validador salvo identificação explícita em contrário.

<a id="release-notes"></a>
## Revisão antes da publicação

O responsável autorizou editar Alpha-v0.1.0 no próprio diretório antes da publicação. As identidades de modelo/perfil/ferramenta permanecem `Alpha-v0.1.0` / `0.1.0` / `0.1.0a0`. Esta revisão reorganiza o manual, remove o adaptador específico de origem e substitui as instâncias didáticas anteriores pelos exemplos oficiais do Atlas. Rascunhos anteriores não publicados não representam promessa de compatibilidade.

Cada edição contém pacote, schema, starter, exemplos, testes e evidências. `specification/` define regras; `implementations/` descreve a representação; `integrations/` documenta mapeamentos; `verification/` separa requisitos, fontes fixadas, revisões e evidências observadas. A raiz contém apresentação visual e ferramentas de distribuição.
