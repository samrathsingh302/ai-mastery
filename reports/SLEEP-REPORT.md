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

## Iteration 7 — step 6: repo archaeology ×2 (04/08/2026, ~04:40)
A researcher surveyed both flagships read-only (file:line evidence), and the module turns that
into guided digs: the 6-pass method, psoc-portal's add-task slice (proxy.ts gate → server action
re-checking auth → supabase insert → migration 0001 → revalidate; 45 migrations, ~170 test files,
zero TODOs), and monk-mode's block slice (verb dispatch → AtomicHosts → HMAC-sealed config →
10-second fail-closed enforcement tick → watchdog). The ConfigIntegrity walkthrough (HMAC-SHA256
+ PBKDF2 600k, DPAPI key, tamper-evidence-over-confidentiality) doubles as module 14's crypto
hook. Interactive: both REAL slices as predict-then-step hop traces. Repos untouched.

## Iteration 8 — step 7: pandas on YOUR Hevy data (04/08/2026, ~10:15)
Found the real thing: 294 workouts in repos\hevy-brain\data\workouts.json (API JSON, richer than
the CSV the plan assumed) — the module teaches against that exact schema, with a synthetic sample
in the same shape so exercises self-check. pandas wasn't installed globally, so the venv IS the
opening lesson. Honesty note for breakfast: my first check.py expectations were hand-mathed wrong
(24 rows not 25; Bench top on 3140, not Deadlift); caught by my own recompute, then machine-
verified 9/9 in a clean venv — the red-team habit earning its keep on its author, twice in one
night. Project: four questions on the real 294 (top lifts, progression, plateaus via rolling max,
consistency), each ending in one honest sentence + one training decision. Also: the /study-session
skill draft has appeared in the session skill list (project-local discovery) — ledger 107 (global
install) still yours.

## Iteration 9 — step 8: how the web works, on YOUR wire (04/08/2026, ~10:45)
Built from live captures against the real site — and the wire had news: psoc-portal.vercel.app
now 308-redirects to **www.leedspunjabisociety.com**, which is served by **Cloudflare in front of
Vercel** (Age: 6282 = an edge-cache hit; cf-nel telemetry header). The module-06 arc completes on
the wire: /dashboard logged out answers 307→/login in 0.17s — proxy.ts observed from outside.
Heads-up: `guides/PUBLIC-SITE-UPDATES.md:7` still names the old vercel.app URL — stale doc, the
project asks you to fix-or-flag it (your repo, your call). Ships: the dated fixture, a 12-question
hashed checker (tested 12/12), a narrated full-trace project, and a 9-hop page-load journey
interactive carrying the real captured values.

## Iteration 10 — step 9: the eval harness mini (04/08/2026, ~11:15)
A WORKING harness, not a description: 10 tasks (6 programmatic — exact/code-tests/regex-cases/
contains-all — + 4 rubric), run_eval.py drives your claude CLI in print mode (subscription, no
API key; models are flags, nothing pinned), grade.py does per-task blind shuffling and only
reveals after scores lock. Verified end-to-end offline tonight; the dry-run fixtures are designed
to teach: a 9–9 DEAD HEAT with opposite profiles — model A followed output contracts exactly,
model B explained beautifully but ignored "reply with ONLY…" four times. Which one you want
depends on the job — that's per-family reading, the module's whole point. Your live run (project)
adds 4 self-designed tasks and ends in findings.md with the n=1 humility written down.

## Iteration 11 — step 10: AI-security taster + cyber hook (04/08/2026, ~11:50)
Built on YOUR live configuration, not generic advice: bypassPermissions confirmed, 4 hooks, 7
agents, 27 skills, and **4 unattended Claude scheduled tasks all Ready** (AutoUpdate, Doctrine-
Mirror, Vault-Daily-Backup, BridgeWorker). Verified the OWASP LLM Top 10 (2025) and Willison's
lethal trifecta (16/06/2025) fresh, then mapped both onto your estate — with ledger item 108's
bridge worker as the worked LLM06 excessive-agency case (capability beyond contract, unattended,
no attacker required). The trifecta lab lets you toggle legs and loads your five REAL session
shapes; the estate session + Gmail is the one that lights up red — that's the finding worth
sleeping on. Project = a proper threat model of your own stack (read-only), which is the
CV-worthy artefact the plan's C2 tier wants. Cyber interleave modules 13–16 hook here, free-first.

## Iteration 12 — step 11: neural nets + transformers intuition (04/08/2026, ~12:25)
The mechanism under module 01, taught so you can COMPUTE it: three by-hand exercises (a forward
pass, one attention head — masked and unmasked, and the temperature dial), every expected answer
computed numerically before writing, checker tested 12/12. Plan correction: the 3Blue1Brown
series **ends at chapter 7, not 8** — ch.5–7 are the transformer ones (Apr–Aug 2024); I've put
verified runtimes in the module and flagged the two I could only single-source. Two extra verified
free interactives: bbycroft.net/llm (fly through a 3D GPT) and Transformer Explainer (runs a real
GPT-2 in-browser). My own attention lab lets you drag token 3's key until it wins the query, and
toggle masking/scaling to see why √d exists. Module 01's laws are now mechanical, not folklore.
