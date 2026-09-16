# career: moved

Moved 16/09/2026 to `C:\Users\samra\repos\job-engine\career\` by chain `20260916-f-career` (T2 copied, T5 retired the
originals). AI-Mastery is the LEARNING engine only; applications, the tracker and the pipeline live in job-engine, and
the CV engine is `repos\cv-editor`.

| Was here | Is now |
|---|---|
| `career/apply.py` | `C:\Users\samra\repos\job-engine\career\apply.py` |
| `career/build_cv.py` | `C:\Users\samra\repos\job-engine\career\build_cv.py` |
| `career/targets.json` | `C:\Users\samra\repos\job-engine\career\targets.json` |
| `career/tests/` | `C:\Users\samra\repos\job-engine\career\tests\` |
| `career/drafts/` | `C:\Users\samra\repos\job-engine\career\drafts\` (moved, not copied; gitignored there too) |
| `.claude/skills/apply-draft/` | `C:\Users\samra\repos\job-engine\.claude\skills\apply-draft\` |
| `FACTS.md`, `CV.*`, `TARGETS.md`, `research/` (vault) | `C:\Users\samra\OneDrive\dev\life\career\` (T3) |

`career/apply.py` here is a shim: it forwards to job-engine's `apply.py` with `sys.argv` untouched, so
`cd repos\ai-mastery; python career/apply.py validate` still works and operates on job-engine's `targets.json`.
Run the real thing from its home:

    cd C:\Users\samra\repos\job-engine
    python career/apply.py validate

Who Samrath is and what he wants: `C:\Users\samra\OneDrive\dev\life\career\CAREER.md`.
Chain 20260915-a's re-plan evidence stays in the vault at
`C:\Users\samra\OneDrive\dev\repos\ai-mastery\career\replan-2026-09-16\`.
