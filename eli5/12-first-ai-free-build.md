# Module 12: first AI-free build — like you're 5

Module 12, taught in `C:\Users\samra\repos\ai-mastery\modules\12-first-ai-free-build\TEACH.md`.

- **One-line reminders:** `GLOSSARY.md` → `## Module 12 — first AI-free build`.
- **Not part of the build:** nothing here is part of `studylog`.
- **The build is yours:** it is AI-free.
- **When to read:** these entries are reading for before or after the build, never during.

---

### Exit code
**Like you're 5:** When a helper finishes a job, they hold up a card: 0 means "all fine", any other number means "something went wrong". Other helpers can read the card without needing to understand the whole messy story of what happened.

**The real words:** The number a program hands back when it ends (0 success, non-zero failure); an interface other programs read, unlike a traceback written for humans. → [12 spec](../modules/12-first-ai-free-build/TEACH.md)

**See it:** in Git Bash, `python -c "import sys; sys.exit(3)"; echo $?` prints `3`; in PowerShell the same number is in `$LASTEXITCODE`.

### Honesty clause
**Like you're 5:** You promised to do your homework with no help. If your big sister helped for five minutes, you write "sister helped, 5 minutes" on the page. Then everyone, you included, knows how well you really did. Hiding it spoils the score for good.

**The real words:** Log every AI-free breach with what and how long; a quantified breach is data, a hidden one corrupts the baseline. → [12 rules](../modules/12-first-ai-free-build/TEACH.md)

**See it:** the model line in `C:\Users\samra\repos\ai-mastery\modules\12-first-ai-free-build\TEACH.md` lines 26–27 — `used Claude for the argparse syntax, 4 minutes` — written the moment it happens.

### Outage score
**Like you're 5:** Imagine your calculator vanished for a week. How much of your maths could you still do: all of it, half, almost none? Write that down as a number, with the date. Next month, ask again. The number should go up.

**The real words:** "% of my productivity surviving a week without Anthropic"; the plan's headline instrument, measured straight after the AI-free build, dated and trended. → [12 baseline](../modules/12-first-ai-free-build/TEACH.md)

**See it:** the question and what to write are in `C:\Users\samra\repos\ai-mastery\modules\12-first-ai-free-build\TEACH.md` lines 93–97: the number, the date, and one sentence on what changed.

### Wall protocol (unassisted)
**Like you're 5:** Stuck on a puzzle with no grown-up to ask? Read the clue from the bottom up. Try the tiniest piece of it. Look at what's really there instead of guessing. Test one idea at a time. If nothing works after a long while, stop and try again tomorrow.

**The real words:** Read the error bottom-up · minimal repro · inspect real values · one hypothesis at a time, written down · 45 min with no progress → log the wall in `journal.md` and return tomorrow. → [12 rules](../modules/12-first-ai-free-build/TEACH.md)

**See it:** practise step 1 on `python -c "print(int('3.5'))"` — read the last line first, `ValueError: invalid literal for int() with base 10: '3.5'`, and it already names the value and what went wrong.
