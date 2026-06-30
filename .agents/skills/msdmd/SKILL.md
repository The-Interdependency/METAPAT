---
name: msdmd
description: Module Self-Declared Metadata in Markdown — foundational convention where each source module declares structured metadata in colocated comment blocks. Canonical upstream is The-Interdependency/skill-lib/msdmd. Load this when authoring, checking, or updating METAPAT metadata blocks.
---

# msdmd — local METAPAT skill entry

Canonical upstream: `The-Interdependency/skill-lib/msdmd/SKILL.md`.

METAPAT uses msdmd blocks beside source modules for:

```text
MODULE_BUILD
DOCS
CAPABILITIES
DEPENDENCIES
OWNERS
BOUNDARIES
CONTRACTS
LLMS
```

Unknown fields are `hmmm`, not guessed.

Block form:

```text
# === BLOCK_NAME ===
# id: stable_snake_case_id
#   field: value
# === END BLOCK_NAME ===
```

This local entry exists so agents can load the msdmd trigger inside METAPAT. Use upstream `skill-lib` for the complete parser contract.
