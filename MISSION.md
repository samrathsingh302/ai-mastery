# MISSION — the overnight AI-tutor factory (written 04/08/2026 by the estate session, Samrath asleep)

You are a fresh Fable 5 session at MAX effort (Samrath's explicit one-night exception to the
effort law, granted 04/08/2026 via pop-up). Your job: turn the AI Mastery Plan into
**tutor-grade, self-contained learning material Samrath learns from directly** — he should be
able to learn from YOUR material alone, with the plan's external courses as optional extras.
He is asleep; run fully autonomously; he will kill the loop when his quota resets.

## The order (stepwise law — one step per loop iteration, numbered, NO skipping)
- **Step 0**: RED-TEAM the plan (`PLAN-v3-notion-export.md`) — adversarially review ordering,
  gaps, redundancy, hour-estimates, and where cybersecurity slots in as a LIGHT INTERLEAVE
  (clearly-marked secondary modules after related core AI steps; AI order untouched — his
  04/08 decision). Output: `PLAN-MASTER.md` = the corrected, fully NUMBERED master order the
  rest of the loop follows (fast-track first), plus `reports/red-team-findings.md`. Do NOT
  edit the Notion page — he decides on plan edits in the morning.
- **Steps 1–12**: the Fast Track items, in order, one per iteration.
- **After 12**: continue down `PLAN-MASTER.md` (breadth layer / tiers in Part-6 order,
  cyber interleave modules where step 0 placed them) until stopped.
- An iteration that can't finish its step cleanly finishes it NEXT iteration — never half-ship
  and move on, never reorder.

## What "tutor-grade" means — per step, create `modules/NN-<slug>/` containing
1. **TEACH.md** — the lesson itself, written for intense deep-work study:
   - **Baby rule (absolute)**: NO term, concept, or notation is used before it has been
     explained in plain words + one analogy + one concrete example. Maintain a cumulative
     `GLOSSARY.md` at repo root; link back instead of re-explaining.
   - Structured for speed: the 80/20 map first, then depth; explicit "you can now…" checkpoints.
   - For video/course steps (e.g. step 1's video canon): write the full companion notes —
     what each video teaches, distilled, so watching becomes optional review, not the source.
2. **exercises/** — numbered, hands-on, self-checking: starter code + `check.py` (or
   equivalent) the learner runs to verify, solutions in `solutions/` (separate, spoiler-safe).
   Follow the plan's own tutor moves: bug-hunts, close-window-retype prompts, explain-back
   questions with model answers.
3. **project/** — one mini-project per step applying it to HIS real estate (Hevy data,
   psoc-portal, monk-mode, the vault, this machine) with an acceptance checklist. His repos
   are at `C:\Users\samra\repos\` — read them for authentic project framing, do not modify them.
4. **interactive/** — at least one self-contained HTML interactive (quiz that gets harder,
   code-tracer, visualiser — inline CSS/JS, opens offline in a browser).
5. **drills.md** — quick-fire spaced-repetition fodder: Q&A pairs, Anki-importable
   (tab-separated block included).
6. **Research first**: before writing each module, WebSearch for current best practice on
   teaching that skill + verify any resource facts you assert (fact-discipline: no invented
   URLs, no unverified claims; cite what you used at the bottom of TEACH.md).

## Cadence per iteration (mechanical)
1. Read `PROGRESS.md` → identify the next unfinished step. 2. Build its module completely.
3. Update `PROGRESS.md` (tick, one evidence line). 4. Append 2–3 lines to
`reports/SLEEP-REPORT.md` (what was built, anything surprising) — this is what he reads on
waking. 5. `git add -A; git commit; git push` (remote: private GitHub `ai-mastery`).
6. Re-fire the loop (ScheduleWakeup per /loop dynamic mode — continuous work, minimal delay).

## Budget guard (hard)
He granted **40 percentage points** of the 20x Fable window (50% → stop by ~10% remaining).
You cannot read the quota meter — so: generate ONE module per iteration, no gold-plating
loops, and **hard-cap at 16 iterations** (step 0 + fast-track 1–12 + at most 3 more), then
stop, /session-close per the skill, and leave `carry-on` pointing at the next step. If
anything smells like runaway spend (retries, errors, huge rework), stop early and close clean.
Delegation: you MAY spawn researcher subagents for search fan-out; the TEACHING material is
written by you (Fable) directly — that's what he paid max for tonight.

## Standing laws that still apply overnight
British English · dd/mm/yyyy · no invented facts · no third-party personal data in materials ·
commit+push every iteration (two-laptop law) · MANUAL-TASKS gets anything human-required ·
if genuinely blocked, write the handoff and stop rather than guessing (gated-scope).
