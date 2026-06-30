# Full compliance checklist

## Done

- Canon docs seeded.
- Agent entry point added.
- Source LLMS block added.
- `llms.txt` added.
- Python package scaffold added.
- msdmd source blocks added to package modules.
- Executable contract tests added.
- Repo-level msdmd collection point added.
- Compliance ledger added.
- UCNS -> METAPAT -> EDCM roadmap added.

## hmmm

- Local write tool blocked three repo-local skill entries.
- Local execution of test and msdmd runners was not possible from this environment because GitHub could not be cloned from the container.
- Verbatim skill-lib propagation still needs a local pass.

## Next local pass

- Copy missing skill directories from skill-lib.
- Run tests.
- Regenerate `llms.txt`.
- Regenerate `metapat_msdmd.ts`.
- Record exact command output in `COMPLIANCE.md`.
