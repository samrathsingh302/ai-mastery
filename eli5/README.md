# eli5 — every taught word, explained like you're 5

## In one minute

- **What it is:** every term from the 14 modules, plus the Semester 1 theory words, explained like you're 5.

- **It is reading, not a lesson.** Nothing here is an exercise answer.

- **When to open it:** only when one word stops you while typing. Never before typing.

- **The fifteen files:** one per module, plus Semester 1 theory. The list is in §4.

- **Adding a term:** the glossary first, then here, then the check. Steps in §5.

---

## 1. What this folder is

Where it came from, and what it holds.

Your words, 13/10/2026:

> i want theory learning as well explained like i'm 5 and concepts explained like i'm 5 easily

- This folder is that.
- It holds every term in `C:\Users\samra\repos\ai-mastery\GLOSSARY.md` (the 14 modules).
- It also holds the Semester 1 theory words.
- Each one is a picture a five-year-old could hold.
- Then come the grown-up words.
- Then one thing you can see or run.
- It is reading, not a lesson.
- Nothing here is an exercise answer.

---

## 2. How to use it

When to open it, when not to, and how to find a word.

### Open it when a word stops you

- You are typing a line and one WORD stops you (what is a "parameter" again?).
- Open that module's file and read the one entry.
- Close it, and carry on typing.

### Never open it before typing

- `C:\Users\samra\repos\ai-mastery\TUTOR-CONTRACT.md` rule 12 still stands: you type first.
- The on-call window answers only a pasted attempt or a pasted red checker line.
- It never reads these entries out to you.
- This folder is not a sixth explanation of an exercise.

### Find a word fast

- First: `cd C:\Users\samra\repos\ai-mastery`
- Then: `git grep -n "### Token" -- eli5`
- Swap in your word for Token.

---

## 3. The format every entry follows

Every entry has the same four lines.

```
### <the term, exactly as GLOSSARY.md writes it>
**Like you're 5:** <60 words at most: one everyday picture>
**The real words:** <one sentence in the grown-up vocabulary, ending with the link to where it was taught>
**See it:** <one concrete thing: a 1–3 line example, a command with its folder, or a place in your own repos>
```

---

## 4. The fifteen files

One file per module, then one for Semester 1 theory.

- **[01-video-canon.md](01-video-canon.md)** — what an LLM is and how it is made. 29 terms.
  - Covers: tokens, training, SFT, RL, hallucination, context window, agents, RAG, evals, vibe coding.

- **[02-tutor-setup.md](02-tutor-setup.md)** — how you study. 6 terms.
  - Covers: active recall, spaced repetition, FSRS, the dojo, the tutor contract.

- **[03-cs50p-accelerated.md](03-cs50p-accelerated.md)** — Python itself. 20 terms.
  - Covers: variables, types, functions, loops, lists, dicts, exceptions, tests, files, regex, classes.

- **[04-automate-boring-stuff.md](04-automate-boring-stuff.md)** — scripts that touch real files safely. 8 terms.
  - Covers: dry-run, idempotent, quarantine, pathlib, shutil, JSON, subprocess, Task Scheduler.

- **[05-git-properly.md](05-git-properly.md)** — git as snapshots and sticky notes. 11 terms.
  - Covers: commit, branch, HEAD, merge, rebase, revert, reflog, remotes.

- **[06-repo-archaeology.md](06-repo-archaeology.md)** — reading a real codebase (psoc-portal, monk-mode). 11 terms.
  - Covers: entry points, vertical slices, middleware, migrations, atomic writes, fail-closed, HMAC, PBKDF2.

- **[07-data-taster-hevy.md](07-data-taster-hevy.md)** — pandas on your Hevy data. 5 terms.
  - Covers: DataFrame, tidy data, groupby, rolling windows, the venv.

- **[08-how-the-web-works.md](08-how-the-web-works.md)** — what happens between a browser and a server. 10 terms.

- **[09-eval-harness-mini.md](09-eval-harness-mini.md)** — measuring an AI system with a small eval harness. 5 terms.

- **[10-ai-security-taster.md](10-ai-security-taster.md)** — how AI systems get attacked and defended. 6 terms.

- **[11-nn-transformers-intuition.md](11-nn-transformers-intuition.md)** — neural nets and transformers, by intuition. 14 terms.

- **[12-first-ai-free-build.md](12-first-ai-free-build.md)** — the words from your first build with no AI help. 4 terms.

- **[13-cyb-shell-bandit.md](13-cyb-shell-bandit.md)** — the shell, through the Bandit wargame. 7 terms.

- **[14-cyb-crypto-monkmode.md](14-cyb-crypto-monkmode.md)** — cryptography by example, on monk-mode. 13 terms.

- **[sem1-theory.md](sem1-theory.md)** — Semester 1 theory, by lane. 32 terms.
  - Java (COMP5911M)
  - KRR (COMP5450M)
  - Data Science (COMP5122M)
  - coding tests
  - writing (COMP5530M)

---

## 5. Adding a new term

Three steps, in this order.

1. **The glossary first.** In `C:\Users\samra\repos\ai-mastery\GLOSSARY.md`, add the `- **term** — …` bullet under its module.

2. **Then here.** Add the `### term` entry to that module's file. Keep the glossary's order and the format in §3.

3. **Then check.** Run `cd C:\Users\samra\repos\ai-mastery` and `python tools\check_docs.py all`. It must end `0 failed`.

### A Semester 1 word

- It has no glossary section.
- Its heading goes in the `SEM1_TERMS` list in `C:\Users\samra\repos\ai-mastery\tools\check_docs.py`.
- It also goes in `sem1-theory.md`, under its lane.
- Then run the same check.
