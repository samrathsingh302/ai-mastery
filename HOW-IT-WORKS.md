# How AI-Mastery works — the day, the repo, and everything you needed to learn

Written 13/10/2026 (chain 20261013-a-ai-mastery-eli5, ticket 1) from the files, not from memory.
The repo is `C:\Users\samra\repos\ai-mastery\`. Every command below runs from that folder:
`cd C:\Users\samra\repos\ai-mastery`. `python tools\check_docs.py how-it-works` checks this page.

## How it works

**The floor.** The study system is `C:\Users\samra\OneDrive\dev\life\uni\UNI.md` §8. Its identity
line (line 188): "Identity: I ship one green check a day." Its floor bullet (line 190): "**Floor:**
Anki queue + one checker-green exercise or NeetCode problem every day (the seat's recommendation;
Samrath gave no number — he may veto)." Two-minute rule: the day counts once the file is open and
the checker has run. Never miss twice.

**The Notion Uni page → Today drives the day.** Open it, do the top item. This repo does not plan
your day (`C:\Users\samra\repos\ai-mastery\START-HERE.md`, the front door, says the same).

**What this repo holds.**
- `modules\` — the 14 built modules, each with a `TEACH.md` (the notes), `exercises\` and usually a
  `check.py` (the grader).
- `modules\03-cs50p-accelerated\exercises\check.py` — the Python ladder's grader, `ex00` to `ex09`.
- `anki\` — your cards and the card law, `C:\Users\samra\repos\ai-mastery\anki\CARD-RULES.md`.
- `journal.md` — one line per study session, `C:\Users\samra\repos\ai-mastery\journal.md`.
- `neetcode\` — your NeetCode solutions, `C:\Users\samra\repos\ai-mastery\neetcode\`.
- `eli5\` — every taught word explained like you're 5 (written by this chain's tickets 2 and 3; its
  index is `eli5\README.md` inside the repo).
- `GLOSSARY.md` — the 149 taught terms, one section per module,
  `C:\Users\samra\repos\ai-mastery\GLOSSARY.md`.

**What a green check is.** A checker, autograder or Gradescope result that says pass, produced by
code you typed. Here that means `check.py ex02` printing no `TODO` or `FAIL` line and ending
`your files: N passed · 0 failed · 0 exercises not started`; a `TODO` or `FAIL` line is not green.

**The on-call window.** `/study-session` is on call only. `C:\Users\samra\repos\ai-mastery\TUTOR-CONTRACT.md`
rule 12, verbatim: "**He types first — paste-first, enforced (16/09/2026; hardened 09/10/2026).** ex02
was explained five times (27/08 → 12/09) and never written; the answer was printed in the module's own
notes the whole time. The window therefore answers ONLY (a) a pasted attempt — his code, however wrong —
or (b) a pasted red checker/autograder line. A question asked before any code exists ("explain
dictionaries first", "what are the basics") gets one reply: the exact path, the exact command, and
"type line 1 and paste it". No exceptions, no sixth explanation."
So it answers your pasted code or your pasted red line; it refuses a question asked before code exists.

**The scheduled window.** The `Claude-Study-Launch` scheduled task runs
`C:\Users\samra\tools\study-launch.ps1`, which opens the on-call window with the brief
`C:\Users\samra\repos\ai-mastery\prompts\study-oncall.md` at six slots (chain 20261012-a-ai-mastery's
plan): Tue 13:05 · Wed 13:05 · Thu 09:00 · Fri 13:05 · Sat 10:00 · Sun 18:00. No Monday slot. The
laptop must be on and logged in for the window to appear.

**Sunday and 01/11/2026.** Sunday: score the v3 gate on the Notion Uni page (28 days, ≥ 24 with a
green check). UNI.md §8's last bullet: "**01/11/2026 check:** 4-week habit check — streak count (gate
clears on ≥1 green check on ≥24 of 28 days), decide v3 growth, draft the "skills by January" CV list."

**The close (when a session was used).** Your own Anki cards, typed by you in the terminal (the
window only fixes typos, then imports them); one line in `journal.md`; commit.

## Everything you needed to learn

### (i) The 14 modules

Each module's folder is under `C:\Users\samra\repos\ai-mastery\modules\`. The one-liner is read from
the opening of its `TEACH.md`. The ELI5 file sits in `eli5\` inside the repo.

| Module folder | What it teaches | Exercises / checker | GLOSSARY.md section | ELI5 file |
|---|---|---|---|---|
| `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\` | The video canon, taught directly: what LLMs are and how they are made | `exercises\check.py`, ex01–ex03 (`.md`) | Module 01 — the video canon | `eli5\01-video-canon.md` |
| `C:\Users\samra\repos\ai-mastery\modules\02-tutor-setup\` | The learning system: toolchain, Anki, the tutor contract, the dojo, the journal, the study-session ritual | `exercises\check.py`, ex01–ex02 (`.md`) | Module 02 — the tutor setup | `eli5\02-tutor-setup.md` |
| `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\` | Python from zero: ten rungs mirroring CS50P's ten weeks | `exercises\check.py`, ex00–ex09 (`.py`) | Module 03 — CS50P accelerated | `eli5\03-cs50p-accelerated.md` |
| `C:\Users\samra\repos\ai-mastery\modules\04-automate-boring-stuff\` | Five Automate the Boring Stuff missions (files, organising, regex, CSV/JSON, scheduling) on your own files | `exercises\check.py`, ex01–ex05 (`.py`) | Module 04 — automate the boring stuff | `eli5\04-automate-boring-stuff.md` |
| `C:\Users\samra\repos\ai-mastery\modules\05-git-properly\` | The git mental model, the undo toolbox, your estate's git doctrine | `exercises\check.py`, ex01 history gym (`.md`) | Module 05 — git properly | `eli5\05-git-properly.md` |
| `C:\Users\samra\repos\ai-mastery\modules\06-repo-archaeology\` | Reading an unfamiliar codebase like a senior engineer, on psoc-portal and monk-mode, read-only | no `check.py`: ex01 comprehension + `dig-log.md` | Module 06 — repo archaeology | `eli5\06-repo-archaeology.md` |
| `C:\Users\samra\repos\ai-mastery\modules\07-data-taster-hevy\` | First real data analysis: pandas on your Hevy history, inside a venv | `exercises\check.py`, ex01–ex02 (`.py`) | Module 07 — data taster | `eli5\07-data-taster-hevy.md` |
| `C:\Users\samra\repos\ai-mastery\modules\08-how-the-web-works\` | One page load of your production site taken apart: DNS → TCP → TLS → HTTP | `exercises\check.py`, ex01 read the wire (`.md`) | Module 08 — how the web works | `eli5\08-how-the-web-works.md` |
| `C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\` | A real eval: 10 tasks × 2 models, blind-graded, one results table | no `check.py`: `run_eval.py` + `grade.py` + ex01 (`.md`) | Module 09 — eval harness mini | `eli5\09-eval-harness-mini.md` |
| `C:\Users\samra\repos\ai-mastery\modules\10-ai-security-taster\` | Prompt injection by hand (Gandalf), the OWASP LLM Top 10 (2025), a threat model of your own agent stack | `exercises\check.py`, ex01 classify (`.md`) | Module 10 — AI-security taster | `eli5\10-ai-security-taster.md` |
| `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\` | What is inside the box: a forward pass and an attention head computed by hand | `exercises\check.py`, ex01–ex03 (`.md`) | Module 11 — neural nets + transformers | `eli5\11-nn-transformers-intuition.md` |
| `C:\Users\samra\repos\ai-mastery\modules\12-first-ai-free-build\` | One small CLI tool built with zero AI, graded on a rubric, then a cold 30-minute interview simulation | `exercises\check.py` + `interview-sim.md` | Module 12 — first AI-free build | `eli5\12-first-ai-free-build.md` |
| `C:\Users\samra\repos\ai-mastery\modules\13-cyb-shell-bandit\` | Shell fluency + OverTheWire Bandit (secondary track) | `exercises\check.py` + `bandit-log.md` | Module 13 — shell + Bandit | `eli5\13-cyb-shell-bandit.md` |
| `C:\Users\samra\repos\ai-mastery\modules\14-cyb-crypto-monkmode\` | Crypto by example on monk-mode's real tamper-evidence scheme (secondary track) | `exercises\check.py`, ex01–ex02 (`.py`) | Module 14 — crypto by example | `eli5\14-cyb-crypto-monkmode.md` |

### (ii) The six Sem-1 lanes

From `START-HERE.md` lines 23–30 (decided 09/10/2026). The grader decides what counts.

| Lane | Driver | What the grader is | This repo's part |
|---|---|---|---|
| Python basics | module 03's ladder now, then MOOC.fi Python Programming 2026 (https://programming-26.mooc.fi/part-1/1-getting-started) | `check.py` here; MOOC.fi's own exercise tests after | module 03/04 exercises + `check.py` as extra reps |
| Java (COMP5911M) | MOOC.fi Java Programming I parts 1–7, VS Code + TestMyCode; from ~week 3 Exercism Java and the Gilded Rose kata in IntelliJ | TestMyCode, then Exercism's tests and the kata's tests | none |
| KRR (COMP5450M) | the module's Gradescope formatives A/B/C with Prover9; Prolog from Learn Prolog Now (https://lpn.swi-prolog.org/) | Gradescope | none |
| Data Science (COMP5122M) | the module's Practical 1 (Titanic CSV, 15 pandas questions) and notebooks; Kaggle Learn Pandas | the practical's questions; Kaggle Learn's graded exercises | module 07 (your Hevy data) as a later project |
| Coding tests | HackerRank 3-Month Preparation Kit, week 1 first; NeetCode 150 once loops are routine | HackerRank's test cases; NeetCode's | `neetcode\` |
| Group Project (COMP5530M) | the Minerva brief; scoping document due 11/12/2026, LaTeX via tectonic | the marked scoping document | none |

### (iii) Skills by 10/01/2027

UNI.md §8's list, verbatim, with its lane and the `eli5\` file holding its words.

| Skill (verbatim) | Lane | ELI5 file |
|---|---|---|
| Java with JUnit 5, three GoF patterns and SOLID, refactoring under tests in IntelliJ | Java | `eli5\sem1-theory.md` |
| Prolog knowledge base + English→FOL + resolution proof on paper | KRR | `eli5\sem1-theory.md` |
| pandas end-to-end (clean → join → chart → findings) | Data Science | `eli5\07-data-taster-hevy.md` + `eli5\sem1-theory.md` |
| Python through module 03–04 | Python basics | `eli5\03-cs50p-accelerated.md` + `eli5\04-automate-boring-stuff.md` |
| one LaTeX report (ACM template via tectonic) | Group Project | `eli5\sem1-theory.md` |
| ~40 NeetCode problems | Coding tests | `eli5\sem1-theory.md` |

## Where you are

Evidence as of 13/10/2026, repo at `fae0b33`. No judgement, no plan.

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

- Last `journal.md` commit — `git log -1 --format=%cd -- journal.md`: `Sat Sep 12 23:34:05 2026 +0100`.
- Files under `neetcode\`: 1 (`neetcode\001_contains_duplicate.py`).
- Last glossary module: `## Module 14 🔐 — crypto by example *(secondary track)*`.

## A 6-hour day

Your word, 13/10/2026: "ready to work 6 hours a day". This is a SHAPE, not a timetable. The Notion
Uni page → Today still decides the items. Your 27/08/2026 ruling was "no hours"; this section
replaces it only once you confirm (the ledger item for chain 20261013-a-ai-mastery-eli5 asks).

- **Block 0 — the floor.** Anki queue + one green check. Two-minute rule: open the file, run the
  checker. A day with only block 0 still counts. Never miss twice.
- **Block 1 — the day's Today item, ~2 h.** UNI.md §8's implementation intention for the weekday:
  Tue after the 13:00 KRR lecture, Prover9/Prolog until 15:00 · Wed after 13:00 (DS lab weeks:
  after 14:00), the Java item · Thu morning before the 16:30 shift, the Python floor + applications ·
  Fri after 11:00, 30 min Group Project, then after DS at 13:00 the pandas item · Sat 10:00, the Java
  part · Sun 18:00, the review. Monday has no intention in §8: take the Today page's top item.
- **Block 2 — Python and coding-test reps, ~1.5 h.** The module-03 ladder (next: `ex02_loops`) →
  MOOC.fi Python → HackerRank week 1.
- **Block 3 — the week's second lane, ~1.5 h.** Or: one ELI5 entry per word that blocked a line you
  were typing, then back to typing.
- **Close, ~15 min.** Your cards, one journal line, commit.

## Where Claude fits

- The on-call window answers only a pasted attempt or a pasted red checker line. Nothing before code.
- `eli5\` is reading you open yourself, when a word blocks a line you are typing. The window never
  recites it, and it is never a substitute for typing.
- `/study-session` runs the closing ritual on your word: quiz, card notes, your cards typed by you,
  one `journal.md` line, the tracker tick, commit.
- Career work (postings, applications, CV) lives in `C:\Users\samra\repos\job-engine\`, never here.

## Commands

```
cd C:\Users\samra\repos\ai-mastery
python modules\03-cs50p-accelerated\exercises\check.py ex02
python modules\03-cs50p-accelerated\exercises\check.py
python tools\check_docs.py all
python tools\anki_import.py <cards.tsv> [--deck "AI Mastery::00 session misses"]
git add -A && git commit -m "…"
```

- `check.py ex02` grades one exercise (swap `ex02` for the one you typed); `check.py` alone prints
  the whole ladder. The grader is `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\exercises\check.py`;
  the next file to type in is `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\exercises\ex02_loops.py`.
- `check_docs.py all` checks this page and the `eli5\` folder.
- `anki_import.py` usage is from its own header, `C:\Users\samra\repos\ai-mastery\tools\anki_import.py`:
  one note per line, `Text<TAB>Extra<TAB>tags` or `Text<TAB>tags`, only `{{c1::…}}` clozes, Anki
  must be open.
- Windows PowerShell 5.1 has no `&&`: there, run `git add -A` and `git commit -m "…"` as two lines.
