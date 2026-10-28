# Legacy multi-unit source record

English · [Português brasileiro](README.pt-br.md)

The [reports.py source record](docs/L2_MinervaBlueprints/apps/LegacyReports/reports.py.yaml) describes the companion procedural LegacyReports application. One file has several independently identified functions plus any module-level description needed; all are represented in one YAML record. The source extension is preserved as `reports.py.yaml`.

This is explicitly a **binding excerpt**. It is not a reconstructed complete L2 instance: no unsubstantiated UCS cases or behavioral-test identities are invented for an existing legacy program. It demonstrates Minerva's ability to document another architecture. The one-class-per-file convention is not imposed on this procedural source. The actual executable source belongs to the companion Vulcan ecosystem; this example supplies its observed record only.

From the edition directory:

```bash
python validator/minerva_validate.py examples/legacy/docs/L2_MinervaBlueprints/apps/LegacyReports/reports.py.yaml --root examples/legacy --json
```

Expected: exit 0 and `layer_coverage: source_record_only`. A model-level conformance claim would additionally require the declared source specification, program model, verification plan and links for the chosen legacy scope.
