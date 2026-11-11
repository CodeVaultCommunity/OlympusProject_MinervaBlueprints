# Primeiros passos com Minerva Blueprints

[English](getting-started.md) · [Início](../README.pt-br.md) · [Edição selecionada](../versioning/Stable-v1.0.0/README.pt-br.md)

Minerva Stable-v1.0.0 transforma uma passagem normalizada do Atlas Stable-v1.1.0 em uma árvore distribuída de módulos Markdown estritos, com formato semelhante ao futuro código. Em conjunto, os módulos preservam toda a semântica do Atlas e acrescentam projeto técnico orientado à geração; eles não formam um apêndice do Atlas e não contêm implementação executável.

Use Python 3.11 ou superior. Na raiz do repositório:

```bash
python -m pip install -e "versioning/Stable-v1.0.0"
python versioning/Stable-v1.0.0/run_examples.py
python -m pytest versioning/Stable-v1.0.0/tests
```

Para importar um documento Atlas normalizado, informe o nome da aplicação e, quando disponíveis, dados externos de projeto das ferramentas concretas:

```bash
minerva-import-atlas atlas.normalized.json output --app RequestRegister --tool-designs concrete-tools.json
minerva-validate output
```

Use `minerva.project.yaml` apenas para descoberta. Os módulos Markdown são a autoridade semântica. Cada módulo combina seu registro controlado da origem Atlas com classes, métodos, colaboradores, algoritmos, falhas, efeitos, pontos de injeção e destinos de geração. `Boundary` nomeia somente adaptadores de interação; testes comportamentais usam cenários e `observation_points`.
