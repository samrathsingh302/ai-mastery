# SLEEP REPORT — what the overnight factory built (read this over breakfast)

> One entry per iteration, 2–3 lines each, newest at the bottom. Details: PROGRESS.md ticks,
> reports/red-team-findings.md, and each module's TEACH.md.

## Iteration 1 — step 0: red-team → PLAN-MASTER (04/08/2026, ~01:10)
Red-teamed plan v3: **sound, 0 critical** — 4 medium (video canon really ~5.5–6.5h at 1×, Karpathy
Deep Dive verified 3h31m; tier totals double-count fast-track extracts; START-HERE//study-session
didn't exist yet; paid-THM risk inside the "light" cyber interleave). Wrote `PLAN-MASTER.md`:
33-step ladder, cyber as SECONDARY steps 13–16 hooked after core steps 5/6/8/10, free-first, dedupe
law for everything post-12. Three decisions ledgered for you: MANUAL-TASKS 105 (Anki), 106 (THM
£10/mo), 107 (/study-session skill install). Notion page untouched, as ordered.

## Iteration 2 — step 1: the video canon, taught directly (04/08/2026, ~01:40)
Built `modules/01-video-canon/`: TEACH.md distils all five videos (Karpathy's 3h31m Deep Dive is
~83% of the canon and gets the full treatment — pipeline, hallucination mechanics, tokens-to-think,
RL/RLHF + sycophancy's mechanical root). Surprise: research corrected the plan THREE more times —
Fireship #2 is 5:47 not 16m, Ebbelaar is 19:29 not ~1h, and the Tech With Tim title doesn't exist
(real one: "Learning to code has changed", 02/2026); canon totals ≈4h14m, so your ~4h estimate was
accidentally right. Ships: explain-back + rebuild-from-memory + misconception-hunt exercises with a
tested hashed-answer check.py, the barbell-audit-v0 project (your baseline outage score), a
pipeline-explorer + 12-question escalating quiz HTML, 30 Anki cards, 30 glossary terms.

## Iteration 3 — step 2: the tutor setup, operational (04/08/2026, ~02:05)
The machine exists: START-HERE.md (zero-decision daily loop) + journal.md at repo root, contract
card with 8 paste-ready tutor moves, dojo protocol (L0–L4 — L0 needs no Python so the habit starts
TODAY), study-cockpit.html (timed Dojo/Study/AI-free/Weekly modes + streak counter), /study-session
skill drafted (installing it = your call, ledger 107). Surprise: **Anki was already installed** on
this machine — ledger 105 narrowed to "open it + optional sync + first import". Toolchain verified
9/9 green (Python 3.14.5, git 2.54, VS Code 1.129). FSRS numbers pre-decided: 0.90 · 10 new/day.

## Iteration 4 — step 3: CS50P accelerated (04/08/2026, ~02:50)
The big one: a 10-rung Python-from-zero ladder mirroring CS50P weeks 0–9 (structure verified live),
psets-first with my notes as coach + per-rung walls/rescues, and the git-survival sidebar so your
work is versioned from day one. Ships 10 exercise files with a check.py harness that self-verifies
(--solutions mode ran 34/34 green — and en route it caught a bug in MY OWN test data: I'd
miscounted the vowels in "Leeds University"; the harness working as designed, on its author),
the repo-census AI-free project (your first real CLI tool, on your actual repos\), a predict-then-
step code tracer (5 traces incl. the aliasing surprise), 34 Anki cards. Rung 5's exercise is
flipped: implementations given, YOU write the test that catches the planted bug.

## Iteration 5 — step 4: Automate the Boring Stuff, applied (04/08/2026, ~03:20)
Five missions from ATBS 3rd ed (May 2025, free online — chapter mapping verified) aimed straight
at your estate: pathlib on repos\, a dry-run-first organiser, regex on YOUR naming schemes
(handoff filenames, ledger dates, wiki-links), Hevy-CSV→JSON plumbing, and subprocess + Task
Scheduler demystified via your own Claude-CLI-AutoUpdate task. Four safety laws lead the module
(dry-run · quarantine-never-delete · sandbox · idempotent) — the exercises literally cannot touch
real files (check.py builds temp trees; self-verified 5/5). Project: vault-janitor, a read-only
report on OneDrive dev that REUSES his tested exercise functions — composition as the lesson.
Plus a live regex playground that translates patterns into plain words.

## Iteration 6 — step 5: Git properly (04/08/2026, ~04:00)
Git as five sentences (snapshots · graph · sticky-note branches · HEAD · remotes-as-copies),
the undo toolbox with the shared-vs-local rule, and YOUR estate's git doctrine narrated — why
dev/brain have no remotes, why their .git lives outside OneDrive, what session-close pushes and
why. Best material of the iteration: last night's atlas bridge-worker incident (ledger 108, the
auto-`pull --rebase` that flattened a merge commit) is now the module's merge-vs-rebase case
study — your own estate teaching you git. The history-gym exercise grades the GRAPH the learner
builds (I built the reference playground myself: 6/6, then deleted it so it stays yours to do);
the visualiser steps through merge vs rebase vs revert/reset on an SVG DAG.
