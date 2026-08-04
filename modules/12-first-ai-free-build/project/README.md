# Project 12 — studylog (the build itself)

Build to the spec in `../TEACH.md`. This folder is where `studylog.py`, `test_studylog.py`,
`build-log.md` and `grading.md` live. **AI-free from the first keystroke.**

## Before you start (5 min, do not skip)

1. Turn Copilot/autocomplete **off**. Close every AI tab. Note the time.
2. Copy the rubric table from TEACH.md into `grading.md` — before writing code, so you're
   building to criteria rather than rationalising afterwards.
3. Start `build-log.md` with the honesty clause pasted at the top and the date.

## While building — the log is half the deliverable

Append to `build-log.md` as you go (short lines, timestamps):

```
10:40 started, sketched the JSON shape on paper
11:05 WALL: argparse subcommands — 25 min. Cause: I put add_argument on the parent parser,
      not the subparser. Found by reading the argparse docs' subcommand example line by line.
11:30 tests for the rejection cases pass
12:10 BREACH: none
```

Every wall gets: what broke · how long · what actually fixed it · what you'd check first next
time. That last field is how walls compound into skill.

## After the build

1. **Grade yourself** in `grading.md` against the rubric — score, then one sentence of
   evidence per criterion. Be harsher than you want to be.
2. **Then** (only then) a tutor session, move #2 only: paste the code, ask for harsh
   explain-back grading. It may name flaws; **you** fix them. Re-grade and note both scores.
3. **Use it for a week.** A tool you don't use taught you syntax; a tool you use teaches you
   design. Note in `build-log.md` what you wanted to change after 3 days of real use.

## Acceptance checklist

- [ ] All six spec behaviours work; `studylog` with no args prints usage, exit 0
- [ ] Both rejection cases give a clear message and a non-zero exit code (test them by hand)
- [ ] Corrupt data file → clear message, no traceback (simulate: write junk into the JSON)
- [ ] ≥4 pytest tests you wrote, and at least one you can prove would catch a real break
      (break the code on purpose, watch it fail, restore)
- [ ] ≤200 lines, stdlib only, functions that return values
- [ ] `grading.md` scored before any AI contact; both scores recorded
- [ ] `build-log.md` complete, walls logged with causes, breaches (if any) logged honestly
- [ ] Baseline outage score written in `journal.md` with today's date
