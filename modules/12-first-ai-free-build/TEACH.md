# Module 12 — The first AI-free build (proof, and your baseline)

> **What this is:** the fast track's finale and its only real exam. You build one small CLI
> tool with **zero AI assistance**, grade it against a rubric written before you start, then
> sit a cold 30-minute interview simulation. **~8h.** Output: proof — to yourself, in
> evidence — plus your first honest outage-test score.
> **Why it exists:** everything up to here can be done while quietly leaning on a tutor. This
> step removes the lean. The plan's north star ("there is no ChatGPT in the interview") is
> not a slogan you agree with; it's a claim you now test.

## The rules (read twice, then commit to them in writing)

**AI-free means:** no Claude, no Copilot/autocomplete (turn it OFF — the plan's Tier-0 rule
about retention is why), no AI search summaries, no "just explain this concept" chats, no
pasting your error into anything. **Allowed:** official docs (docs.python.org), your own
notes and modules 03–11, `help()` and the REPL, Stack Overflow *as a last resort* for
syntax facts (not designs), and paper.

**When you get stuck** — and you will — the drill is the plan's wall protocol, unassisted:
(1) re-read the error bottom-up · (2) reproduce it in the smallest possible snippet ·
(3) print/inspect the actual values, don't theorise · (4) one hypothesis at a time, written
down · (5) if 45 minutes pass with no progress, stop, log the wall in `journal.md`, and
come back tomorrow. **A wall you crossed alone is the single most valuable artefact this
module produces** — more valuable than the tool.

**Honesty clause:** if you break the rule, don't hide it. Write it in the log ("used Claude
for the argparse syntax, 4 minutes"). A quantified breach is data; a hidden one corrupts
your baseline forever, and the baseline is the point.

## What you build: `studylog` — your own study tracker

Small enough to finish, real enough to use daily, and it consumes what you've already built.

```
studylog add --module 03 --mins 90 --note "rung 2 loops, wall on off-by-one"
studylog add --module 03 --mins 20 --dojo --ai-free
studylog today
studylog week
studylog quota
```

**Behaviour spec (this IS the rubric — build to it, nothing more):**

1. `add` appends one entry to a JSON file in the repo (module/mins/note/flags/timestamp).
   Rejects: missing module, non-positive mins, mins > 600 (typo guard) — with a clear
   message and a non-zero exit code, not a traceback.
2. `today` prints today's entries and the total minutes, aligned columns.
3. `week` prints the last 7 days: one line per day, minutes, and a tiny ASCII bar
   (`#### 80m`), plus the week's total and its dojo-day count.
4. `quota` prints AI-free minutes as a percentage of total minutes, and whether you're above
   the plan's 20% line.
5. Data file: created on first use; never silently overwritten; a corrupt/missing file gives
   a clear message, not a crash (module 03 rung 3, applied).
6. `studylog` with no arguments prints usage and exits 0.

**Constraints:** stdlib only (argparse, json, datetime, pathlib) · one file, ≤200 lines ·
functions with returns, not print-everywhere (module 03 rung 5's testability lesson) ·
at least 4 pytest tests you wrote yourself, covering the two rejection cases and the week
aggregation.

## The grading rubric (score yourself BEFORE looking at anything)

| # | Criterion | 0 | 1 | 2 |
|---|-----------|---|---|---|
| 1 | Spec conformance | subcommands missing | all present, some behaviour off | matches the spec exactly |
| 2 | Input rejection | crashes/tracebacks | rejects but messages unclear | clear message + non-zero exit |
| 3 | Data safety | can lose/overwrite data | safe but noisy on corruption | safe, clear, and idempotent-ish |
| 4 | Structure | one long main() | some functions | small functions that return values |
| 5 | Tests | none | tests exist, pass trivially | tests would CATCH a real break |
| 6 | Readability | you'd struggle in a month | fine | a stranger reads it top-to-bottom |
| 7 | AI-free integrity | breaches unlogged | breaches logged | zero breaches |

**Pass = 10/14 with no zeros.** Below that: fix and re-grade — the point isn't the score, it's
that you can now SEE the difference between "it runs" and "it's good".

Only AFTER grading may you open a tutor session — and then only for tutor move #2
(explain-back grading, harsh) on the finished code. Let it name every flaw. You fix them
yourself, then re-grade.

## The exit test: cold 30-minute interview simulation

The fast track's actual exam (the plan's exit criterion). Timer on, no notes, no tabs, spoken
aloud. `exercises/interview-sim.md` is the script — 6 questions across your projects, Python
fundamentals, and "how does an LLM work", each with a model answer and a 0–2 scale. Have
someone read it to you, or read a question, close the sheet, and answer.

**Passing (9+/12) means:** proceed into the full tiers with momentum. **Below 6** doesn't
mean failure — it means the fast track found your gaps, which is its job. Each miss becomes
a drill topic and an Anki card, and you re-sit in a fortnight.

## Your baseline outage score

Immediately after the build (not before — the experience must be fresh), re-answer module
01's project question: *if Anthropic vanished for a week, what % of my productivity
survives?* Write the number, the date, and one sentence on what changed since your
barbell-audit baseline. This is the number that must trend up for the next thousand hours —
and it's the only honest way to measure the thing this whole plan is for.

**Checkpoint — you can now:** ship a small tool unaided, grade your own work against criteria
before seeking praise, survive walls with a written procedure, and state your capability with
a number rather than a feeling.

## Sources

- Rules and exit criterion: plan v3 Part 1 (20% AI-free quota, outage test), Part 3 item 12,
  Part 6c (wall protocol). Rubric and spec: written for this module tonight.
- Everything the build uses was taught in modules 03–06 of this repo; no new material is
  required to finish it.
