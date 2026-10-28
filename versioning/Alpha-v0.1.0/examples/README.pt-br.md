# Exemplos

[English](README.md) · Português brasileiro · [Guia da edição](../README.pt-br.md)

Execute os comandos a partir da **pasta da edição**, não da raiz do repositório. São exemplos elaborados com escopo e procedência explícitos; não inventam evidência de execução nem aprovação do responsável.

| Exemplo | Escopo | Resultado normal |
| --- | --- | --- |
| [Mínimo](minimal/README.pt-br.md) | Caso L1 de listar, ADPM e um teste comportamental; sem vínculo de fonte necessário ainda | Saída 0 nas verificações declaradas do modelo |
| [Ecossistema TaskBoard](task-board-ecosystem/README.pt-br.md) | Três casos, onze critérios, ADPM/ADVS e quinze fichas observadas | Saída 0 no modelo; código no Vulcan companheiro |
| [Planejado](planned/README.pt-br.md) | Blueprint de listar e uma ficha planejada anterior ao código | Saída 0; inspeção explícita de código inconclusiva |
| [Legado](legacy/README.pt-br.md) | Várias unidades procedurais na ficha de um arquivo | Saída 0, apenas ficha; sem alegação ADMV completa |
| [Contraexemplos](counterexamples/README.pt-br.md) | Treze resultados esperados inspecionáveis, incluindo ciclo válido e divergência | Runner retorna 0 somente se todas as expectativas corresponderem |

```bash
python run_examples.py --list
python run_examples.py --all
python run_examples.py minimal --json
python examples/counterexamples/check.py --json
python run_examples.py --test
```

O [starter](../implementations/yaml/starter.minerva.yaml) é rascunho estruturalmente válido. `--all` confere somente sua estrutura; a consistência normal retorna 4. Uma ficha isolada não fornece componentes ausentes de programa/verificação. Preserve a distinção entre observação de fonte e execução de testes.
