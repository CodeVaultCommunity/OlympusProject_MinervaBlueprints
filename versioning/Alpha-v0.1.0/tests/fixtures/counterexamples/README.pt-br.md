# Contraexemplos

Fixtures da ferramenta atual; não são exemplos adicionais de domínio Atlas.

[Expected results](expected-results.json) · [Runner](check.py)

```bash
python tests/fixtures/counterexamples/check.py --json
```

O runner aplica mutações declaradas em cópias temporárias do exemplo mínimo e compara os diagnósticos esperados. Não altera os exemplos e não traduz fontes L1.
