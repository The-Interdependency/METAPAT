# Codex Handoff: Finish full skill-lib compliance locally

## Status

METAPAT now has the main compliance scaffold:

- `AGENTS.md` with source `LLMS` block
- `llms.txt`
- `.agents/skills/README.md`
- local skill entries for most directly used skills
- `pyproject.toml`
- `src/metapat/` package
- colocated msdmd blocks in source modules
- executable tests in `tests/test_contracts.py`
- `metapat_msdmd.ts` collection point
- `COMPLIANCE.md`
- `ROADMAP.md`

## Remaining hmmm

The GitHub write tool blocked direct creation of these local skill paths during initial compliance work:

```text
.agents/skills/llms-build/SKILL.md
.agents/skills/test-build/SKILL.md
.agents/skills/the-interdependency/SKILL.md
```

Resolve by copying these skill directories verbatim from `The-Interdependency/skill-lib` in a local development environment.

## Expected follow-up patch

1. Copy missing skill directories from skill-lib.
2. Regenerate `llms.txt` from `AGENTS.md`.
3. Regenerate `metapat_msdmd.ts` from source blocks.
4. Update `COMPLIANCE.md` to mark local checks pass/fail with exact output.
5. If required, add METAPAT to `skill-lib/ORG_DISTRIBUTION.md` target repos.

## Guardrails

Do not alter Chapter Zero root while doing compliance work.

Do not implement UCNS or EDCM bridges in this compliance patch.

Keep exact bridge APIs as `hmmm` until source repos are inspected.
