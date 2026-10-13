# 07-data-taster-hevy — like you're 5

Taught in `C:\Users\samra\repos\ai-mastery\modules\07-data-taster-hevy\TEACH.md`; the one-line reminders are `GLOSSARY.md` → `## Module 07 — data taster`. The pandas lines need the module's venv (TEACH.md's first block makes it): `cd C:\Users\samra\repos\ai-mastery\modules\07-data-taster-hevy\exercises`, `.venv\Scripts\activate`, then `python` and `import pandas as pd`. None of them is an exercise answer.

### DataFrame / Series
**Like you're 5:** A DataFrame is a whole times-table grid with names along the top. A Series is one column of it, cut out on its own, still keeping its name and its row numbers.
**The real words:** A table / one typed, labelled column of it; you work column-at-a-time, not with loops. → [07 mental model](../modules/07-data-taster-hevy/TEACH.md)
**See it:** `df = pd.DataFrame({"fruit": ["apple", "pear"], "count": [3, 5]})` then `df["count"]` — that column is a Series.

### groupby (split-apply-combine)
**Like you're 5:** Tip a bag of sweets on the table, sort them into piles by colour, count each pile, then write one line per colour on a little chart. Sort, count, write down.
**The real words:** Split rows into groups → apply a function per group → combine into a new table; the idea under all analytics. → [07 step 2](../modules/07-data-taster-hevy/TEACH.md)
**See it:** `pd.DataFrame({"colour": ["red", "blue", "red"], "n": [1, 1, 1]}).groupby("colour")["n"].sum()` → blue 1, red 2. Animated: `start C:\Users\samra\repos\ai-mastery\modules\07-data-taster-hevy\interactive\groupby-visualiser.html`.

### Rolling window
**Like you're 5:** A little frame that only shows the last four days of your sticker chart. Each day it slides along by one. If the best sticker in the frame stays the same for weeks, you've stopped getting better.
**The real words:** A statistic over the last N points (`rolling(4).max()`); a flat rolling max means a plateau. → [07 step 4](../modules/07-data-taster-hevy/TEACH.md)
**See it:** `pd.Series([60, 62, 62, 62, 62, 62]).rolling(4).max()` — three blanks (NaN), then 62, 62, 62: flat, so a plateau.

### Tidy data
**Like you're 5:** One sticker per line in the notebook: every single set you did gets its own line. Then any question, "how many squats?", is just counting lines that match.
**The real words:** One row per observation (here: per set); questions become filters and groups. → [07 step 1](../modules/07-data-taster-hevy/TEACH.md)
**See it:** `C:\Users\samra\repos\hevy-brain\data\workouts.json` is NOT tidy (workouts hold exercises hold sets); open it and see the nesting the flatten step removes.

### Venv (virtual environment)
**Like you're 5:** Each project gets its own toolbox instead of everyone sharing one messy drawer. Put tools in this box and no other project can break them. Throw the box away and nothing else is touched.
**The real words:** A private Python plus packages per project; delete the folder to undo. → [07 the venv](../modules/07-data-taster-hevy/TEACH.md)
**See it:** After `.venv\Scripts\activate` your prompt starts with `(.venv)`; `python -c "import sys; print(sys.prefix)"` then prints a path inside `.venv`.
