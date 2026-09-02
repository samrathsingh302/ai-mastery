# career/ — the 2027 graduate-application scaffold

The 25–30-application barbell from `CAREER.md` §6B/§7C, as data plus a CLI.
**Submission is always Samrath's.** This tooling verifies, drafts and tracks; it
never logs in, never submits, never emails.

## The loop

1. Verify the window (opens/closes/eligibility/salary) → record it in `targets.json`
   with its `sources`, then `status <id> verified`.
2. `python career/apply.py draft <id>` → creates `career/drafts/<id>/brief.md`.
3. Paste the live JD and the application questions into that brief, then run its
   `## Drafting prompt` in a Claude session (or use the `/apply-draft` skill).
   Out come `cv-<id>.md`, `answers-<id>.md`, and `cover-<id>.md` if asked for.
4. Samrath opens the employer URL and submits.
5. `python career/apply.py status <id> submitted --note "..."` — and again at each
   later stage (`online-test`, `interview`, `assessment-centre`, `offer`, `rejected`).

## Commands

    python career/apply.py list [--limb london|north|clearance|consulting] [--status S]
    python career/apply.py due [--days 30]
    python career/apply.py draft <id> [--force]
    python career/apply.py status <id> <new-status> [--note TEXT]
    python career/apply.py render [--out PATH]     # rewrites TARGETS.md
    python career/apply.py validate

## Where things live

`targets.json` is the source of truth; `drafts/` is tracked in git on purpose.
The fact base (`FACTS.md`), the master CV (`CV.md`) and the generated `TARGETS.md`
live in `C:\Users\samra\OneDrive\dev\repos\ai-mastery\career\`.

## Tests

    python -m unittest discover -s career/tests -t career
