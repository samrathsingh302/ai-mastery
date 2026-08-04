# Module 02 — The Tutor Setup (the machine that runs everything else)

> **What this is:** the operational build-out of your learning system: toolchain, Anki, the
> tutor contract, the dojo, the journal, and the study-session ritual. After this module,
> "studying" is a button you press, not a plan you renegotiate daily. **Time: ~3h once,
> then it runs at ~30 min/day.**
> **Why it's step 2, before any Python:** the sweep's core research note (plan, Part 2):
> learners using AI as a *tutor* outperformed peers; learners using it as an *answer machine*
> underperformed even the no-AI group. Same tool, opposite outcomes — the difference is the
> contract and the ritual. You install both today, so CS50P (step 3) lands on rails.

## Setup checklist (pre-verified on YOUR machine, 04/08/2026)

| Check | Status tonight | Re-verify command |
|-------|---------------|-------------------|
| Python | **✓ 3.14.5** (py launcher also has 3.12, 3.13) | `python --version` |
| Git | **✓ 2.54.0.windows.1** | `git --version` |
| VS Code | **✓ 1.129.0** | `code --version` |
| Anki desktop | **✓ ALREADY INSTALLED** (`%LOCALAPPDATA%\Programs\Anki\anki.exe`) | `check.py` in exercises/ |
| Anki first-open + sync | ☐ YOURS: open Anki once; optional AnkiWeb account for phone sync (ledger item 105) | — |
| First deck imported | ☐ YOURS: module 01's drills block (exercise 02 walks it) | — |

Run `python modules/02-tutor-setup/exercises/check.py` any time — it re-verifies all of this
and tells you exactly what's missing.

## Piece 1 — The Tutor Contract (why it works, how to use it)

**The failure it prevents** *(plain words)*: the **illusion of knowing** — AI's trick of making
you feel you could do what you only watched it do. *(Analogy: watching a gym video vs lifting;
the video feels like progress and moves no iron.)* *(Example: "vibe learning" module 01 warned
about — working projects, empty skills.)*

**The mechanism:** the contract forces every session through **active recall** *(plain words:
answering from memory rather than re-reading — the single best-evidenced study technique;
analogy: closed-book beats open-book practice for the same reason match-fitness beats watching
matches)*: Socratic questions, explain-backs, end-of-session quizzes, cards from your misses.

**How to use it:** paste `tutor-contract.md`'s block at the start of every study session — or
type `/study-session` once you've installed the draft skill (your call — ledger item 107; the
draft ships in this module at `study-session-skill/`).

**The eight tutor moves** (paste-ready phrasings live in the contract file): teach-me-the-map ·
explain-back grading · close-window-retype · interactive artifacts on demand · weakness-
calibrated drills · the bug hunt · mock interviews · the Anki pipeline.

**When NOT to use Claude** (the contract's flip side): during struggle reps, during the 20%
AI-free quota, during the first 30 minutes of any wall. Walls are the curriculum.

## Piece 2 — Anki, properly (10 min/day, forever)

- **Spaced repetition** *(plain words)*: reviewing a fact just before you'd forget it, at
  stretching intervals — each successful recall pushes the next review further out. *(Analogy:
  watering plants on the day the soil dries, not daily.)* *(Example: a card seen today returns
  in 3 days, then 10, then a month.)*
- **FSRS** *(plain words)*: Anki's modern built-in scheduler that learns YOUR forgetting curve
  and picks those intervals for you — turn it on and stop hand-tuning.

**Your settings (decided — zero decisions left):**
1. Anki → deck options → enable **FSRS** · desired retention **0.90**.
2. **New cards: 10/day** (your budget is 10 min/day; at this cap the mature queue settles
   around a manageable size — beginners who take Anki's old default of 20 end up buried).
3. Maximum reviews/day: leave high (let FSRS decide) — EXCEPT the plan's backlog emergency
   rule: reviews consistently painful → cap at 20, **bulk-suspend the rest guilt-free**, prune
   bad cards. A small live deck beats a dead perfect one (plan, edge-case 4).
4. **The pipeline law: AI drafts, YOU curate.** Claude proposes 3–8 cards from your misses;
   you delete any you wouldn't defend; only then import. Unreviewed AI decks are how Anki dies
   (community consensus, plan Part 2).
5. Import mechanics: each module's `drills.md` has a tab-separated block → save as `.txt` →
   Anki: File → Import → separator Tab. First deck: module 01's 30 cards (exercise 02).

## Piece 3 — The Dojo (20 min/day)

The daily code-review rep. Full protocol: `dojo.md` (levels, timing, scoring, the AI-free
alternates from the audit-stocked issue lists). Until you can read Python (module 03), the dojo
runs on *process* bug-hunts — the method is the muscle; the language plugs in later.

## Piece 4 — The Journal (1 line/day, 1 block/week)

`journal.md` at repo root — baseline block, daily line, weekly outage-test block. Objective
instruments only: sims, scores, tallies. Feelings don't grade; the numbers do (plan,
edge-case 9).

## Piece 5 — The ritual, assembled

`START-HERE.md` at repo root is now the whole system on one page: day-one script, the daily
loop (Anki → dojo → module block → close ritual), lanes, weekly review. The cockpit
(`interactive/study-cockpit.html`) runs the timers so no session needs a decision.

**Checkpoint — you can now:** state the illusion-of-knowing failure and the contract rule that
blocks it; say what FSRS does for you and your three fixed Anki numbers (0.90 · 10 new/day ·
emergency cap 20); and run tomorrow morning entirely from START-HERE.md without deciding
anything.

## Sources (verified 04/08/2026)

- Plan v3 Parts 2 + 6c (the contract, the eight moves, the research note, edge-cases 4/9) —
  `PLAN-v3-notion-export.md` (provenance: 06/07/2026 sweeps).
- FSRS current-practice check: iatrox.com/academy/study/anki-fsrs-settings-2026 ·
  studycardsai.com/blog/anki-settings-guide ·
  slidetoanki.com/blog/how-to-use-fsrs-anki-guide (consensus: FSRS on, retention ~0.85–0.90,
  low new-card caps for non-medics, generous review ceiling).
- Toolchain + Anki presence: verified live on this machine tonight (see checklist).
