<p align="center"><img src="assets/minerva-banner-pt-br.png" alt="Minerva Blueprints · Olympus Project" width="100%"></p>

# Minerva Blueprints

[English](README.md) · [Stable-v1.0.0](versioning/Stable-v1.0.0/README.pt-br.md) · [Verificação](versioning/Stable-v1.0.0/verification/RELEASE.pt-br.md)

O Minerva é a camada OAL L2 entre o Atlas Specifications e o código Vulcan. A
Stable-v1.0.0 substitui o antigo blueprint YAML central por uma árvore
distribuída de módulos Markdown estritos com a forma da futura base de código.

Cada módulo preserva sua semântica Atlas em `atlas-source-json` e acrescenta o
projeto técnico em `minerva-design-json`: alvos, símbolos, métodos,
colaboradores, algoritmos, falhas, efeitos, testes e grafos. O manifesto serve
somente para descoberta.

Ferramentas concretas são projetos técnicos em Markdown, sem implementação L2.
`Boundary` significa apenas adaptador de interação; cenários usam
`observation_points`. Os três exemplos preservam 477 conceitos Atlas em 76
módulos e declaram 31 alvos para o Vulcan.

```powershell
cd versioning/Stable-v1.0.0
python -m pip install -e .
python run_examples.py
python -m unittest discover -s tests -v
```

A edição histórica [Alpha-v0.1.0](versioning/Alpha-v0.1.0/README.pt-br.md)
permanece disponível. Concepção e autoria: Douglas de Oliveira Alkimim.
[Licença MIT](LICENSE).
