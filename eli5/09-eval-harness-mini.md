# 09-eval-harness-mini — like you're 5

Taught in `C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\TEACH.md` (the output contract is in its `drills.md`); the one-line reminders are `GLOSSARY.md` → `## Module 09 — eval harness mini`. The harness lives in `C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\exercises\`; `--dry-run` runs it offline on the fixtures, with no model calls. None of these is an exercise answer: ex01's four tasks are yours to write.

### Blind grading
**Like you're 5:** Two friends bake cakes for a contest. You put on a blindfold, taste both, and write your scores down before anyone tells you who baked which. If you knew, you'd give your best friend extra points without even meaning to.
**The real words:** Scoring anonymised, shuffled outputs against written criteria BEFORE identities are revealed; the integrity of rubric evals. → [09 idea 3](../modules/09-eval-harness-mini/TEACH.md)
**See it:** `start C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\interactive\blind-grader.html`, or `cd C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\exercises` then `python grade.py --dry-run` — the answers show only as A/B until your scores are locked.

### Contamination
**Like you're 5:** A spelling test where you saw the answer sheet yesterday. You get every word right, but that only shows you remember the sheet, not that you can spell. A model that read a puzzle's answer on the internet is the same.
**The real words:** A task whose answer exists as memorised text; it measures recall, not capability. → [09 idea 4](../modules/09-eval-harness-mini/TEACH.md)
**See it:** compare two tasks: "write a function that reverses a string" (thousands of copies online, so a perfect reply proves little) and "summarise the last line of `C:\Users\samra\repos\ai-mastery\journal.md`" (no model can have memorised it).

### Output contract
**Like you're 5:** The teacher says "answer with just one word: yes or no". Now she can mark fifty papers in a minute by looking for one word. If she let everyone write a story instead, she'd have to read every single one.
**The real words:** "Reply with ONLY…": the instruction that makes programmatic checking possible; prompt design and eval design are one skill. → [09 drills](../modules/09-eval-harness-mini/drills.md)
**See it:** open `C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\exercises\tasks.json` and read task `01-dates-extract`'s prompt — "reply with ONLY the dates, comma-separated, no spaces" is the contract.

### pass@k / repeats
**Like you're 5:** Flip a coin once and get heads, and you might think it always lands heads. Flip it twenty times and you see the truth. A model is like a coin that can answer differently each time, so you ask it the same thing many times.
**The real words:** Models are stochastic, so one run is an anecdote and repeated runs make signal; pass@k is the chance that at least one of k attempts passes. → [09 idea 5](../modules/09-eval-harness-mini/TEACH.md)
**See it:** run `claude -p "Name one fruit. Reply with ONLY the word." --model haiku` three times in a row and compare the three words.

### Programmatic vs rubric scoring
**Like you're 5:** Some homework a machine can mark: 2 + 2 is 4 or it isn't. Some homework needs a person, like "is this story kind?" For that kind, the teacher writes down what "good" means first, then marks against that list.
**The real words:** A checker decides (exact match, tests pass, a regex validates) vs a blinded human grades against written criteria; his harness mixes both, 6 programmatic + 4 rubric. → [09 idea 2](../modules/09-eval-harness-mini/TEACH.md)
**See it:** `cd C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\exercises` then `python grade.py --dry-run` — the programmatic scores print first, then the rubric round asks you for 0–2 per answer.
