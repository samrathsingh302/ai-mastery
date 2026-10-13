# eli5 — every taught word, explained like you're 5

## What this folder is

Your words, 13/10/2026: "i want theory learning as well explained like i'm 5 and concepts explained like i'm 5
easily". This folder is that. It holds every term in `C:\Users\samra\repos\ai-mastery\GLOSSARY.md` (the 14
modules) plus the Semester 1 theory words, each one as a picture a five-year-old could hold, then the grown-up
words, then one thing you can see or run.

It is reading, not a lesson. Nothing here is an exercise answer.

## How to use it

- You are typing a line and one WORD stops you (what is a "parameter" again?). Open that module's file, read the
  one entry, close it, and carry on typing.
- Never open it before typing. `C:\Users\samra\repos\ai-mastery\TUTOR-CONTRACT.md` rule 12 still stands: you type
  first, and the on-call window answers only a pasted attempt or a pasted red checker line. It never reads these
  entries out to you, and this folder is not a sixth explanation of an exercise.
- To find a word fast: `cd C:\Users\samra\repos\ai-mastery`, then `git grep -n "### Token" -- eli5` (swap in your
  word).

## The format every entry follows

```
### <the term, exactly as GLOSSARY.md writes it>
**Like you're 5:** <60 words at most: one everyday picture>
**The real words:** <one sentence in the grown-up vocabulary, ending with the link to where it was taught>
**See it:** <one concrete thing: a 1–3 line example, a command with its folder, or a place in your own repos>
```

## The fifteen files

- [01-video-canon.md](01-video-canon.md) — what an LLM is and how it is made: tokens, training, SFT, RL,
  hallucination, context window, agents, RAG, evals, vibe coding (29 terms).
- [02-tutor-setup.md](02-tutor-setup.md) — how you study: active recall, spaced repetition, FSRS, the dojo, the
  tutor contract (6 terms).
- [03-cs50p-accelerated.md](03-cs50p-accelerated.md) — Python itself: variables, types, functions, loops, lists,
  dicts, exceptions, tests, files, regex, classes (20 terms).
- [04-automate-boring-stuff.md](04-automate-boring-stuff.md) — scripts that touch real files safely: dry-run,
  idempotent, quarantine, pathlib, shutil, JSON, subprocess, Task Scheduler (8 terms).
- [05-git-properly.md](05-git-properly.md) — git as snapshots and sticky notes: commit, branch, HEAD, merge,
  rebase, revert, reflog, remotes (11 terms).
- [06-repo-archaeology.md](06-repo-archaeology.md) — reading a real codebase (psoc-portal, monk-mode): entry
  points, vertical slices, middleware, migrations, atomic writes, fail-closed, HMAC, PBKDF2 (11 terms).
- [07-data-taster-hevy.md](07-data-taster-hevy.md) — pandas on your Hevy data: DataFrame, tidy data, groupby,
  rolling windows, the venv (5 terms).
- [08-how-the-web-works.md](08-how-the-web-works.md) — what happens between a browser and a server (10 terms).
- [09-eval-harness-mini.md](09-eval-harness-mini.md) — measuring an AI system with a small eval harness
  (5 terms).
- [10-ai-security-taster.md](10-ai-security-taster.md) — how AI systems get attacked and defended (6 terms).
- [11-nn-transformers-intuition.md](11-nn-transformers-intuition.md) — neural nets and transformers, by
  intuition (14 terms).
- [12-first-ai-free-build.md](12-first-ai-free-build.md) — the words from your first build with no AI help
  (4 terms).
- [13-cyb-shell-bandit.md](13-cyb-shell-bandit.md) — the shell, through the Bandit wargame (7 terms).
- [14-cyb-crypto-monkmode.md](14-cyb-crypto-monkmode.md) — cryptography by example, on monk-mode (13 terms).
- [sem1-theory.md](sem1-theory.md) — Semester 1 theory by lane: Java (COMP5911M), KRR (COMP5450M), Data Science
  (COMP5122M), coding tests, writing (COMP5530M) (32 terms).

## Adding a new term

1. `C:\Users\samra\repos\ai-mastery\GLOSSARY.md` first: add the `- **term** — …` bullet under its module.
2. Then here: add the `### term` entry to that module's file, in the glossary's order, in the format above.
3. Then check: `cd C:\Users\samra\repos\ai-mastery` and `python tools\check_docs.py all` — it must end
   `0 failed`.

A Semester 1 word has no glossary section: its heading goes in the `SEM1_TERMS` list in
`C:\Users\samra\repos\ai-mastery\tools\check_docs.py` and in `sem1-theory.md` under its lane, then the same check.
