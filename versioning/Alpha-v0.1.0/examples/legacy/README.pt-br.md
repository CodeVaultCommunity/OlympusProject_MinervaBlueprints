# Ficha legada com múltiplas unidades

[English](README.md) · Português brasileiro

A [ficha de reports.py](docs/L2_MinervaBlueprints/apps/LegacyReports/reports.py.yaml) descreve a aplicação procedural LegacyReports companheira. Um arquivo possui várias funções identificadas independentemente, mais descrição de módulo quando necessária; tudo fica em uma ficha YAML. A extensão é preservada em `reports.py.yaml`.

É explicitamente um **recorte de vinculação**, não instância L2 reconstruída completa. Nenhum caso UCS ou teste comportamental sem origem é inventado para o legado. Demonstra a capacidade Minerva de documentar outra arquitetura, sem impor uma classe por arquivo ao código procedural. A fonte executável está no ecossistema Vulcan companheiro; aqui se fornece apenas sua ficha observada.

A partir da pasta da edição:

```bash
python validator/minerva_validate.py examples/legacy/docs/L2_MinervaBlueprints/apps/LegacyReports/reports.py.yaml --root examples/legacy --json
```

Esperado: saída 0 e `layer_coverage: source_record_only`. Alegar conformidade do modelo exigiria também especificação de origem declarada, modelo de programa, plano de verificação e vínculos do escopo legado escolhido.
