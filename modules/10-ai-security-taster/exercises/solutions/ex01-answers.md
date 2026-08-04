# Ex01 — answers, with the controls (open after check.py)

| # | OWASP | Trifecta | Cheapest control that would ACTUALLY help |
|---|-------|----------|-------------------------------------------|
| 1 | LLM01 | P·U·E | Capability narrowing: the session reading issues shouldn't hold push rights or key access. Failing that, a human gate on outward acts (your MANUAL-TASKS pattern). Filtering "SYSTEM:" strings loses to paraphrase. |
| 2 | LLM06 | none | Scope the worker to `machines/context/` — its stated contract. Second-best: disable during build slices. Ledger 108's own recommendation. |
| 3 | LLM03 | none | Review instruction files before install, pin them in git, and re-read diffs on update. Treat a skill like a dependency, because it is one. |
| 4 | LLM10 | none | A hard iteration/budget cap in the runner (MISSION's 16-iteration cap is exactly this control, pre-installed). |
| 5 | LLM09 | U | Never act on a single unverified summary: quote the source line, and gate money on a human reading the original. Provenance beats confidence. |
| 6 | LLM07 | none | Assume leakage: keep NO secrets in CLAUDE.md/skills (paths are fine, credentials never). Your `secrets\` split already does this. |
| 7 | LLM01 | P·U·E | Break a trifecta leg: no send-mail capability in a session that reads untrusted mail AND holds Drive access. This is the canonical Willison case. |
| 8 | LLM03 | none | Install into a venv (module 07's habit), review new deps, prefer stdlib. `--no-deps`/lockfiles for anything long-lived. |

**The pattern across all eight:** the controls that work are *architectural* (narrow the
capability, split the trifecta, cap the budget, gate the irreversible). Every "detect the bad
string" control is a speed bump. Write that sentence in your journal — it's the module's
whole thesis, and it's what makes a security review different from a vibe check.
