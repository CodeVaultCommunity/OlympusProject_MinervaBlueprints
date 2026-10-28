# Preparing a Minerva Blueprints release

[Português](releasing.pt-br.md) · [Home](../README.md) · [Agent guide](../AGENTS.md)

This procedure concerns the repository distribution. It adds no model requirement and does not turn local validation into stakeholder approval or remote publication. Select the intended edition and use its manual, dependencies, examples and tools together.

## 1. Finalize sources and evidence

Preserve user changes and published historical editions. Keep the English normative manual and its Portuguese translation aligned. Confirm model, profile and tool versions independently from instance revisions. Preserve source provenance, licenses and the hashes of frozen upstream snapshots.

Keep virtual environments, generated databases and temporary outputs outside the delivery tree. Use a clean checkout and respect `.gitattributes`. Hash the actual bytes without normalizing line endings while hashing. Do not regenerate an inventory to conceal unintended checkout changes.

From the repository root, install the declared development dependencies and run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/check_repository.py
python -m pytest scripts/tests
```

From `versioning/Alpha-v0.1.0/`, install `requirements.txt` and execute the edition-local checks:

```bash
python -m pip install -r requirements.txt
python run_examples.py --all
python tests/fixtures/counterexamples/check.py
python run_examples.py --test
```

After artwork changes, follow `assets/README.md`, regenerate the derived files and inspect them. Runtime commands do not depend on the root artwork. Record only checks actually executed, including commands, environments, counts and limits. A configured workflow is not evidence that hosted CI ran.

## 2. Generate the single content inventory

Root `CONTENT-SHA256.json` is the only active distribution inventory. Its metadata contains `algorithm`, `minerva_edition`, scope and exclusions. Each file entry identifies a relative POSIX path, exact byte size and SHA-256. It covers every indexed delivery file, including edition content, assets, tooling, reports and workflows. Only the inventory itself is excluded.

Finish the evidence first. Stage the intended additions, changes and deletions explicitly, then run from the root:

```bash
python scripts/content_inventory.py --write
git add -- CONTENT-SHA256.json
python scripts/content_inventory.py --check
git diff --cached --stat
```

Generation reads paths from the Git index and bytes from the working tree. Untracked additions are not discovered automatically. Confirm that staged blobs and working bytes agree, then commit the complete tree locally. Do not place the final commit ID or the ZIP's own digest inside the commit or ZIP that it identifies.

## 3. Build and audit the committed distribution

With a clean committed tree, run:

```bash
python scripts/build_distribution.py --output /absolute/path/OlympusProject_MinervaBlueprints_Alpha-v0.1.0.zip
python scripts/check_archive.py /absolute/path/OlympusProject_MinervaBlueprints_Alpha-v0.1.0.zip
```

The builder refuses dirty tracked content, stale inventories, tracked caches/intermediates and an existing output file. It archives committed files into one `OlympusProject_MinervaBlueprints/` directory, without `.git`, then checks complete inventory coverage and exact bytes.

Extract the actual ZIP into a fresh empty directory and audit it **before** installing dependencies, generating caches or editing files:

```bash
python /absolute/extraction/OlympusProject_MinervaBlueprints/scripts/check_archive.py /absolute/extraction/OlympusProject_MinervaBlueprints
```

The archive/directory checker needs only Python's standard library. It does not need Git and rejects missing, additional, duplicate or changed files, invalid paths and unsupported links. `content_inventory.py`, in contrast, is intended for a Git checkout. Once environments or caches have been created inside the extracted tree, a strict audit correctly reports them as extra content.

Verify the extracted edition using an environment outside its directory. For edition-isolation evidence, copy only `versioning/Alpha-v0.1.0/` into a separate directory and repeat its documented commands. This tests portability independently of root assets and packaging helpers.

## 4. Keep the external receipt

Record the local commit ID, final ZIP filename, byte size, SHA-256, inventory/file counts, audit results and relevant limits in an external receipt. The receipt must stay outside the commit and ZIP it identifies. The inventory protects distributed file bytes; the external ZIP digest protects the package including the inventory.

This unpublished Alpha revision is local and reviewable. It does not imply a GitHub repository, pushed branch, tag, release, hosted CI result or independent approval. A later authorized publication should use the same checked commit and archive and verify its hosted checks before announcing a remote release.
