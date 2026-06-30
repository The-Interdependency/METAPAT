# METAPAT skill-lib / msdmd compliance ledger

## Status

METAPAT now has a structural compliance scaffold for skill-lib / msdmd:

- `AGENTS.md` exists and contains the source `LLMS` declaration.
- `llms.txt` exists as the generated-style repo instruction file.
- `.agents/skills/` exists with local skill entries for the skills that could be written through the GitHub tool.
- `pyproject.toml` exists.
- `src/metapat/` exists as an importable Python package.
- `src/metapat/canon.py` has colocated msdmd metadata for module build, docs, capability, owner, boundary, and contracts.
- `src/metapat/validation.py` has colocated msdmd metadata for module build, docs, capability, owner, boundary, and contracts.
- `src/metapat/flow_plan.py` has colocated msdmd metadata for planned UCNS -> METAPAT -> EDCM flow.
- `tests/test_contracts.py` exists as executable theorem contract tests.
- `metapat_msdmd.ts` exists as the repo-level collection point.

## Planned architecture edge

```text
UCNS -> METAPAT -> EDCM
```

Current state:

```text
UCNS side: hmmm, planned but not implemented.
EDCM side: hmmm, planned but not implemented.
Exact bridge APIs: hmmm.
```

## Remaining hmmm

The GitHub write tool blocked creation of three repo-local skill paths during this pass:

```text
.agents/skills/llms-build/SKILL.md
.agents/skills/test-build/SKILL.md
.agents/skills/the-interdependency/SKILL.md
```

The corresponding upstream skills remain canonical in `The-Interdependency/skill-lib`.

`AGENTS.md`, `llms.txt`, `CONTRACTS` blocks, and executable tests are present despite those local skill-entry gaps.

## Local checks to run after clone

```bash
python -m unittest discover -s tests
```

When skill-lib tooling is available locally, also run:

```bash
python -m llms.build --root . --out llms.txt --check
python -m msdmd.collect --root . --repo metapat --out metapat_msdmd.ts
```

hmmm: exact local runner package path after skill propagation.
