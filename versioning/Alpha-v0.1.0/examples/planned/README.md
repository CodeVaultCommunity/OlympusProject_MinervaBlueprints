# Planned source before implementation

English · [Português brasileiro](README.pt-br.md)

This [blueprint](docs/L2_MinervaBlueprints/blueprint.yaml) selects the same list-case scope as the minimum example and binds it to a [planned source record](docs/L2_MinervaBlueprints/apps/TaskBoard/usecases/TaskManagement/UseCase_ListTasks.py.yaml). `source.state` is `planned`; `sha256` is null. The intended class, operation, context and logical case link exist without an executable application file. No code or execution is claimed.

From the edition directory:

```bash
python validator/minerva_validate.py examples/planned/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/planned --json
```

Expected: exit 0 for model checks. Adding `--verify-code` is intentionally inconclusive (exit 4): a planned source cannot establish correspondence with an absent implementation. When the source is built, review its semantics, record the actual observation/hash and update the content revision. Do not silently turn an intended source into observed evidence because a filename appeared.
