# How AI-Mastery works — the day, the repo, and everything you needed to learn

## In one minute

- **The floor:** Anki queue plus one green check, every day. Never miss twice.

- **The day is set by** the Notion Uni page → Today. This repo does not plan it.

- **Claude is on call only.** It answers your pasted code or your pasted red line. Nothing before code exists.

- **Where you are, 13/10/2026:** 12 passed, 8 exercises not started. The next file is `ex02_loops`.

- **A 6-hour day** is a shape, not a timetable. It replaces your "no hours" ruling only once you confirm.

Written 13/10/2026 (chain 20261013-a-ai-mastery-eli5, ticket 1) from the files, not from memory.

- **Repo:** `C:\Users\samra\repos\ai-mastery\`
- **Every command below runs from that folder:** `cd C:\Users\samra\repos\ai-mastery`
- **This page is checked by:** `python tools\check_docs.py how-it-works`

---

## How it works

The daily rule, where the day comes from, and what counts as done.

### The floor

The study system is `C:\Users\samra\OneDrive\dev\life\uni\UNI.md` §8.

Its identity line (line 188):

> "Identity: I ship one green check a day."

Its floor bullet (line 190):

> "**Floor:** Anki queue + one checker-green exercise or NeetCode problem every day (the seat's recommendation; Samrath gave no number — he may veto)."

- **Two-minute rule:** the day counts once the file is open and the checker has run.
- **Never miss twice.**

### The Notion Uni page → Today drives the day

- Open it. Do the top item.
- This repo does not plan your day.
- The front door says the same: `C:\Users\samra\repos\ai-mastery\START-HERE.md`.

### What a green check is

- A checker, autograder or Gradescope result that says pass.
- It must come from code you typed.
- **Here, that means** `check.py ex02` printing no `TODO` or `FAIL` line.
- It must end `your files: N passed · 0 failed · 0 exercises not started`.
- A `TODO` or `FAIL` line is not green.

---

## What this repo holds

Seven places, each with its own job.

- **`modules\`** — the 14 built modules.
  - Each has a `TEACH.md` (the notes) and `exercises\`.
  - Most also have a `check.py` (the grader).

- **`modules\03-cs50p-accelerated\exercises\check.py`** — the Python ladder's grader, `ex00` to `ex09`.

- **`anki\`** — your cards and the card law.
  - Card law: `C:\Users\samra\repos\ai-mastery\anki\CARD-RULES.md`

- **`journal.md`** — one line per study session.
  - Path: `C:\Users\samra\repos\ai-mastery\journal.md`

- **`neetcode\`** — your NeetCode solutions.
  - Path: `C:\Users\samra\repos\ai-mastery\neetcode\`

- **`eli5\`** — every taught word explained like you're 5.
  - Written by this chain's tickets 2 and 3.
  - Its index is `eli5\README.md` inside the repo.

- **`GLOSSARY.md`** — the 149 taught terms, one section per module.
  - Path: `C:\Users\samra\repos\ai-mastery\GLOSSARY.md`

---

## The two study windows

Claude opens on call, or on a schedule.

### The on-call window

- `/study-session` is on call only.
- The rule is `C:\Users\samra\repos\ai-mastery\TUTOR-CONTRACT.md` rule 12.

Rule 12, verbatim:

> "**He types first — paste-first, enforced (16/09/2026; hardened 09/10/2026).** ex02 was explained five times (27/08 → 12/09) and never written; the answer was printed in the module's own notes the whole time. The window therefore answers ONLY (a) a pasted attempt — his code, however wrong — or (b) a pasted red checker/autograder line. A question asked before any code exists ("explain dictionaries first", "what are the basics") gets one reply: the exact path, the exact command, and "type line 1 and paste it". No exceptions, no sixth explanation."

In short:

- **It answers:** your pasted code, or your pasted red line.
- **It refuses:** a question asked before code exists.

### The scheduled window

- The `Claude-Study-Launch` scheduled task runs `C:\Users\samra\tools\study-launch.ps1`.
- That opens the on-call window.
- Its brief is `C:\Users\samra\repos\ai-mastery\prompts\study-oncall.md`.
- The six slots come from chain 20261012-a-ai-mastery's plan.

The six slots:

- **Tue:** 13:05
- **Wed:** 13:05
- **Thu:** 09:00
- **Fri:** 13:05
- **Sat:** 10:00
- **Sun:** 18:00

- **No Monday slot.**
- The laptop must be on and logged in for the window to appear.

---

## Sunday, 01/11/2026 and the close

The weekly score, the four-week check, and how a session ends.

### Sunday

- Score the v3 gate on the Notion Uni page.
- **The gate:** 28 days, ≥ 24 with a green check.

### 01/11/2026

UNI.md §8's last bullet:

> "**01/11/2026 check:** 4-week habit check — streak count (gate clears on ≥1 green check on ≥24 of 28 days), decide v3 growth, draft the "skills by January" CV list."

### The close (when a session was used)

- Your own Anki cards, typed by you in the terminal.
- The window only fixes typos, then imports them.
- One line in `journal.md`.
- Commit.

---

## Everything you needed to learn

One block per module.

- Each module's folder is under `C:\Users\samra\repos\ai-mastery\modules\`.
- The "teaches" line is read from the opening of its `TEACH.md`.
- The ELI5 file sits in `eli5\` inside the repo.
- What to learn and do so the target CV comes true, and which slot each piece goes in: `C:\Users\samra\OneDrive\dev\repos\ai-mastery\TARGET-CV-PLAN.md`.

### Module 01

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\`
- **Teaches:** The video canon, taught directly: what LLMs are and how they are made
- **Checker:** `exercises\check.py`
- **Exercises:** ex01–ex03, `.md` files
- **GLOSSARY.md section:** Module 01 — the video canon
- **ELI5 file:** `eli5\01-video-canon.md`

### Module 02

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\02-tutor-setup\`
- **Teaches:** The learning system: toolchain, Anki, the tutor contract, the dojo, the journal, the study-session ritual
- **Checker:** `exercises\check.py`
- **Exercises:** ex01–ex02, `.md` files
- **GLOSSARY.md section:** Module 02 — the tutor setup
- **ELI5 file:** `eli5\02-tutor-setup.md`

### Module 03

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\`
- **Teaches:** Python from zero: ten rungs mirroring CS50P's ten weeks
- **Checker:** `exercises\check.py`
- **Exercises:** ex00–ex09, `.py` files
- **GLOSSARY.md section:** Module 03 — CS50P accelerated
- **ELI5 file:** `eli5\03-cs50p-accelerated.md`

### Module 04

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\04-automate-boring-stuff\`
- **Teaches:** Five Automate the Boring Stuff missions on your own files
- **The five missions:** files, organising, regex, CSV/JSON, scheduling
- **Checker:** `exercises\check.py`
- **Exercises:** ex01–ex05, `.py` files
- **GLOSSARY.md section:** Module 04 — automate the boring stuff
- **ELI5 file:** `eli5\04-automate-boring-stuff.md`

### Module 05

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\05-git-properly\`
- **Teaches:** The git mental model, the undo toolbox, your estate's git doctrine
- **Checker:** `exercises\check.py`
- **Exercises:** ex01 history gym, a `.md` file
- **GLOSSARY.md section:** Module 05 — git properly
- **ELI5 file:** `eli5\05-git-properly.md`

### Module 06

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\06-repo-archaeology\`
- **Teaches:** Reading an unfamiliar codebase like a senior engineer, on psoc-portal and monk-mode, read-only
- **Checker:** no `check.py`
- **Exercises:** ex01 comprehension + `dig-log.md`
- **GLOSSARY.md section:** Module 06 — repo archaeology
- **ELI5 file:** `eli5\06-repo-archaeology.md`

### Module 07

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\07-data-taster-hevy\`
- **Teaches:** First real data analysis: pandas on your Hevy history, inside a venv
- **Checker:** `exercises\check.py`
- **Exercises:** ex01–ex02, `.py` files
- **GLOSSARY.md section:** Module 07 — data taster
- **ELI5 file:** `eli5\07-data-taster-hevy.md`

### Module 08

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\08-how-the-web-works\`
- **Teaches:** One page load of your production site taken apart: DNS → TCP → TLS → HTTP
- **Checker:** `exercises\check.py`
- **Exercises:** ex01 read the wire, a `.md` file
- **GLOSSARY.md section:** Module 08 — how the web works
- **ELI5 file:** `eli5\08-how-the-web-works.md`

### Module 09

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\`
- **Teaches:** A real eval: 10 tasks × 2 models, blind-graded, one results table
- **Checker:** no `check.py`
- **Exercises:** `run_eval.py` + `grade.py` + ex01, a `.md` file
- **GLOSSARY.md section:** Module 09 — eval harness mini
- **ELI5 file:** `eli5\09-eval-harness-mini.md`

### Module 10

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\10-ai-security-taster\`
- **Teaches:** Prompt injection by hand (Gandalf), the OWASP LLM Top 10 (2025), a threat model of your own agent stack
- **Checker:** `exercises\check.py`
- **Exercises:** ex01 classify, a `.md` file
- **GLOSSARY.md section:** Module 10 — AI-security taster
- **ELI5 file:** `eli5\10-ai-security-taster.md`

### Module 11

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\`
- **Teaches:** What is inside the box: a forward pass and an attention head computed by hand
- **Checker:** `exercises\check.py`
- **Exercises:** ex01–ex03, `.md` files
- **GLOSSARY.md section:** Module 11 — neural nets + transformers
- **ELI5 file:** `eli5\11-nn-transformers-intuition.md`

### Module 12

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\12-first-ai-free-build\`
- **Teaches:** One small CLI tool built with zero AI, graded on a rubric, then a cold 30-minute interview simulation
- **Checker:** `exercises\check.py`
- **Exercises:** `interview-sim.md`
- **GLOSSARY.md section:** Module 12 — first AI-free build
- **ELI5 file:** `eli5\12-first-ai-free-build.md`

### Module 13

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\13-cyb-shell-bandit\`
- **Teaches:** Shell fluency + OverTheWire Bandit
- **Track:** secondary track
- **Checker:** `exercises\check.py`
- **Exercises:** `bandit-log.md`
- **GLOSSARY.md section:** Module 13 — shell + Bandit
- **ELI5 file:** `eli5\13-cyb-shell-bandit.md`

### Module 14

- **Folder:** `C:\Users\samra\repos\ai-mastery\modules\14-cyb-crypto-monkmode\`
- **Teaches:** Crypto by example on monk-mode's real tamper-evidence scheme
- **Track:** secondary track
- **Checker:** `exercises\check.py`
- **Exercises:** ex01–ex02, `.py` files
- **GLOSSARY.md section:** Module 14 — crypto by example
- **ELI5 file:** `eli5\14-cyb-crypto-monkmode.md`

---

## The six Sem-1 lanes

The grader decides what counts.

- **Source:** `START-HERE.md` lines 23–30.
- **Decided:** 09/10/2026.

### Python basics

- **Driver:** module 03's ladder now, then MOOC.fi Python Programming 2026.
- **Link:** https://programming-26.mooc.fi/part-1/1-getting-started
- **Grader:** `check.py` here. MOOC.fi's own exercise tests after.
- **This repo's part:** module 03/04 exercises + `check.py` as extra reps.

### Java (COMP5911M)

- **Driver:** MOOC.fi Java Programming I parts 1–7, VS Code + TestMyCode.
- **From ~week 3:** Exercism Java and the Gilded Rose kata in IntelliJ.
- **Grader:** TestMyCode, then Exercism's tests and the kata's tests.
- **This repo's part:** none.

### KRR (COMP5450M)

- **Driver:** the module's Gradescope formatives A/B/C with Prover9.
- **Prolog:** from Learn Prolog Now (https://lpn.swi-prolog.org/).
- **Grader:** Gradescope.
- **This repo's part:** none.

### Data Science (COMP5122M)

- **Driver:** the module's Practical 1 and notebooks.
- **Practical 1:** Titanic CSV, 15 pandas questions.
- **Also:** Kaggle Learn Pandas.
- **Grader:** the practical's questions. Kaggle Learn's graded exercises.
- **This repo's part:** module 07 (your Hevy data), as a later project.

### Coding tests

- **Driver:** HackerRank 3-Month Preparation Kit, week 1 first.
- **Then:** NeetCode 150 once loops are routine.
- **Grader:** HackerRank's test cases. NeetCode's.
- **This repo's part:** `neetcode\`

### Group Project (COMP5530M)

- **Driver:** the Minerva brief.
- **Scoping document due:** 11/12/2026.
- **Written in:** LaTeX via tectonic.
- **Grader:** the marked scoping document.
- **This repo's part:** none.

---

## Skills by 10/01/2027

UNI.md §8's list, verbatim. Each has its lane and the `eli5\` file holding its words.

- **Java with JUnit 5, three GoF patterns and SOLID, refactoring under tests in IntelliJ**
  - Lane: Java
  - ELI5: `eli5\sem1-theory.md`

- **Prolog knowledge base + English→FOL + resolution proof on paper**
  - Lane: KRR
  - ELI5: `eli5\sem1-theory.md`

- **pandas end-to-end (clean → join → chart → findings)**
  - Lane: Data Science
  - ELI5: `eli5\07-data-taster-hevy.md` + `eli5\sem1-theory.md`

- **Python through module 03–04**
  - Lane: Python basics
  - ELI5: `eli5\03-cs50p-accelerated.md` + `eli5\04-automate-boring-stuff.md`

- **one LaTeX report (ACM template via tectonic)**
  - Lane: Group Project
  - ELI5: `eli5\sem1-theory.md`

- **~40 NeetCode problems**
  - Lane: Coding tests
  - ELI5: `eli5\sem1-theory.md`

---

## Where you are

Evidence only. No judgement, no plan.

- **As of:** 13/10/2026.
- **Repo at:** `fae0b33`.

The ladder — `python modules\03-cs50p-accelerated\exercises\check.py`, verbatim:

```
  TODO  ex02_loops: not written yet
  TODO  ex03_exceptions: not written yet
  TODO  ex04_libraries: not written yet
  TODO  ex05_unit_tests: not written yet
  TODO  ex06_files: not written yet
  TODO  ex07_regex: not written yet
  TODO  ex08_oop: not written yet
  TODO  ex09_etcetera: not written yet

your files: 12 passed · 0 failed · 8 exercises not started
```

- **Last `journal.md` commit:** `Sat Sep 12 23:34:05 2026 +0100`.
- **Found with:** `git log -1 --format=%cd -- journal.md`
- **Files under `neetcode\`:** 1 (`neetcode\001_contains_duplicate.py`).
- **Last glossary module:** `## Module 14 🔐 — crypto by example *(secondary track)*`.

---

## A 6-hour day

A SHAPE, not a timetable.

- **Your word, 13/10/2026:** "ready to work 6 hours a day".
- The Notion Uni page → Today still decides the items.
- **Your 27/08/2026 ruling was "no hours".**
- This section replaces it only once you confirm.
- The ledger item for chain 20261013-a-ai-mastery-eli5 asks.

### Block 0 — the floor

- Anki queue + one green check.
- **Two-minute rule:** open the file, run the checker.
- A day with only block 0 still counts.
- Never miss twice.

### Block 1 — the day's Today item, ~2 h

UNI.md §8's implementation intention for each weekday:

- **Tue:** after the 13:00 KRR lecture, Prover9/Prolog until 15:00.
- **Wed:** after 13:00, the Java item. DS lab weeks: after 14:00.
- **Thu:** morning, before the 16:30 shift. The Python floor + applications.
- **Fri:** after 11:00, 30 min Group Project. Then after DS at 13:00, the pandas item.
- **Sat:** 10:00, the Java part.
- **Sun:** 18:00, the review.
- **Mon:** no intention in §8. Take the Today page's top item.

### Block 2 — Python and coding-test reps, ~1.5 h

- The module-03 ladder. Next: `ex02_loops`.
- Then MOOC.fi Python.
- Then HackerRank week 1.

### Block 3 — the week's second lane, ~1.5 h

- Or: one ELI5 entry per word that blocked a line you were typing.
- Then back to typing.

### Close, ~15 min

- Your cards.
- One journal line.
- Commit.

---

## Where Claude fits

What Claude does here, and what it never does.

- **The on-call window** answers only a pasted attempt or a pasted red checker line. Nothing before code.

- **`eli5\`** is reading you open yourself, when a word blocks a line you are typing.
  - The window never recites it.
  - It is never a substitute for typing.

- **`/study-session`** runs the closing ritual on your word:
  - quiz
  - card notes
  - your cards, typed by you
  - one `journal.md` line
  - the tracker tick
  - commit

- **Career work** (postings, applications, CV) lives in `C:\Users\samra\repos\job-engine\`, never here.

---

## Commands

Copy these as is.

```
cd C:\Users\samra\repos\ai-mastery
python modules\03-cs50p-accelerated\exercises\check.py ex02
python modules\03-cs50p-accelerated\exercises\check.py
python tools\check_docs.py all
python tools\anki_import.py <cards.tsv> [--deck "AI Mastery::00 session misses"]
git add -A && git commit -m "…"
```

### What each one does

- **`check.py ex02`** grades one exercise. Swap `ex02` for the one you typed.
- **`check.py` alone** prints the whole ladder.
- **The grader:** `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\exercises\check.py`
- **The next file to type in:** `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\exercises\ex02_loops.py`
- **`check_docs.py all`** checks this page and the `eli5\` folder.

### anki_import.py

Usage is from its own header, `C:\Users\samra\repos\ai-mastery\tools\anki_import.py`.

- One note per line.
- **Format:** `Text<TAB>Extra<TAB>tags` or `Text<TAB>tags`.
- Only `{{c1::…}}` clozes.
- Anki must be open.

### Windows PowerShell 5.1

- It has no `&&`.
- There, run `git add -A` and `git commit -m "…"` as two lines.
