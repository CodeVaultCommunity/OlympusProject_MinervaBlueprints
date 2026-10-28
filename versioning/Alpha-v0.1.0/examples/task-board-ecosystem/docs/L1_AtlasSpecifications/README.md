# TaskBoard L1 source

This folder contains an Atlas Specifications Stable-v1.0.0 instance with document ID `ATLAS-VULCAN-TASKBOARD`, revision `1`. It is the didactic source for this example, manually reconstructed from the earlier Vulcan demo and the requirements discussion. It has not been independently approved by stakeholders.

The contract preserves application-assigned IDs, trimmed titles of 1–120 characters, a boolean completion flag, default-deny authorization and idempotent repeated completion. The published Atlas Task Board has a different contract (caller-supplied IDs, revisions and conflict outcomes); no equivalence with that example is claimed.

Read [the structured source](task-board.atlas.json). The Minerva blueprint references its three cases and eleven acceptance criteria. Operational choices, routes and commands belong to the realization and interaction documents; this L1 source does not require a particular database or framework.

The document is checked with the pinned Atlas reference validator during preparation. The edition verification report records its structural and consistency checks, command and result; preservation of the selected behavior also requires review. Reproducing an Atlas validation uses the referenced Atlas edition; the Minerva checker verifies its declared correspondence, not the entire Atlas language.
