# The Dojo — 20 minutes, every day, even zero-days

**What it is:** a daily code-review rep: hunt planted bugs using the debugging method, by hand.
The method IS the interview skill (and it's the same loop your `debugging-to-root-cause` skill
runs — you're practising your own agents' procedure, manually).

## The protocol (cockpit runs these timers)

| Min | Step |
|-----|------|
| 0–2 | Get material: paste tutor move #6 into a Claude session ("~30-line function, 3 subtle bugs, level N") — or pick an AI-free alternate (below) |
| 2–15 | **Hunt.** The loop, by hand: (a) predict what the code SHOULD do; (b) trace what it ACTUALLY does — line by line, on paper; (c) one hypothesis at a time — name the suspect line, say WHY, check it; never shotgun |
| 15–18 | Commit to your answers, THEN ask for the reveal. For each bug: found/missed + can you state the root cause in one sentence? |
| 18–20 | Score the journal line (`found/total · level · mins`) · every MISS becomes a drafted Anki card (move #8) |

## Levels (tell the tutor your level; it plants accordingly)

- **L0 — process** (pre-Python, this week): English procedures — recipes, checklists, game
  rules — with 3 planted logic bugs (wrong order, missing case, off-by-one). Method without
  syntax.
- **L1 — reading**: syntax-visible bugs (wrong operator, wrong variable, bad initialisation).
- **L2 — logic**: off-by-one, boundary conditions, wrong loop exit, state mutation surprises.
- **L3 — semantics**: shadowing, mutability aliasing, wrong API assumption, silent type issues.
- **L4 — design**: the code "works" but a requirement is quietly violated; race-ish ordering
  bugs; error paths that swallow.
- **Rule:** 3 clean days (all bugs found in time) → level up. A brutal day → stay, don't drop.

## AI-free alternates (count toward the 20% quota; zero setup)

Real open issues from the 07/07 audits, per the plan (Part 1, added 08/07/2026): hevy-brain
#13/#14 · cv-editor #1 · loop-runner #1–#3 (GitHub) · VAULT-1/2 in `dev\_global\tasks.md`.
Pick ONE, fix it fully AI-free, journal it. (Re-check the issue still exists before starting —
lists age.)

## Why 20 minutes daily beats 2 hours weekly

Spacing (module 02, piece 2) applies to skills, not just cards: daily short reps under mild
time pressure build the pattern-recognition that interview panels and production incidents
actually test. The dojo is also the plan's designated streak-restart ritual: worst day, do ONE
dojo, streak lives.
