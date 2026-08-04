# Module 07 — Data taster: pandas on YOUR Hevy data

> **What this is:** your first real data analysis, on the dataset you care most about — your
> own training history. Surveyed tonight: **294 real workouts** in
> `repos\hevy-brain\data\workouts.json` (the Hevy API shape — richer than the app's CSV
> export), back to 2023. The exercises run on a bundled sample in the EXACT same schema, so
> everything is testable; the project points your verified code at the real 294. **~10h.**
> **Optional companion:** Kaggle Learn's Python and pandas micro-courses (free, browser
> notebooks) — good extra reps, not required; these notes teach what you need directly.

## The venv (do this first — it IS an exercise)

Your machine's Python has no pandas (verified tonight), and that's correct: real projects
isolate their dependencies in a **virtual environment** *(plain words: a private copy of
Python + packages inside the project folder, so projects can't break each other; analogy:
each project gets its own toolbox instead of everyone sharing one drawer)*:

```
cd modules\07-data-taster-hevy\exercises
py -m venv .venv                # create the private toolbox (a .venv folder)
.venv\Scripts\activate          # step into it (prompt gains "(.venv)")
pip install pandas matplotlib   # tools go into THIS toolbox only
python check.py                 # everything below is now testable
```

`deactivate` steps back out. Delete the folder, the toolbox is gone — nothing global was
touched. (This is why module 04's safety instincts and this pattern are the same idea:
contain your blast radius.)

## The pandas mental model (three sentences)

A **DataFrame** is a table; each column is a **Series** (a typed array with labels).
You almost never loop — you say what you want *column-at-a-time* (`df["volume"] =
df["weight_kg"] * df["reps"]` multiplies whole columns at once). Analysis is the **golden
path**: load → inspect → tidy/derive → group → plot.

## Step 1 — Load + flatten (nested JSON → tidy table)

Your workouts.json is a dict keyed by workout id; each workout holds a list of exercises;
each exercise a list of sets (`weight_kg`, `reps`, `type`, `rpe`, …). Analysis wants **tidy
data** *(plain words: one row per observation — here, one row per SET; every question
becomes a filter/group over rows)*. So: three nested loops building row-dicts, then
`pd.DataFrame(rows)` — exactly your module-04 skills plus one new call:

```python
df["date"] = pd.to_datetime(df["date"])     # ISO strings -> real datetimes
```

`ex01_flatten.py` is this, spec'd precisely. **Inspect before trusting:** `df.head()`,
`df.shape`, `df.dtypes`, `df.describe()` — the four-command reflex after every load.
(Real-data honesty: your file includes a workout titled "forgot to track lol" — real
datasets are messy because real life is; `or 0` on missing weights is a *decision*, and
tidying decisions get written down.)

## Step 2 — Groupby: split-apply-combine

The idea under ALL analytics: **split** rows into groups (by exercise, by week), **apply**
a function to each group (sum, max, count), **combine** into a new table.

```python
df.groupby("exercise")["volume"].sum().sort_values(ascending=False)   # your top lifts
iso = df["date"].dt.isocalendar()
weeks = iso["year"].astype(str) + "-W" + iso["week"].astype(str).str.zfill(2)
df.groupby(weeks)["volume"].sum()                                      # volume per week
```

Filtering is a boolean mask: `df[df["exercise"] == "Bench Press (Barbell)"]`. Derived
metrics are column maths: Epley estimated 1RM = `weight * (1 + reps/30)`. That's the whole
grammar — `ex02_analyse.py` makes you speak it four ways (top-volume table, weekly series,
PR set with tie-breaking, best est-1RM). The interactive animates split-apply-combine if it
won't click.

## Step 3 — Plot (matplotlib minimum viable)

```python
import matplotlib.pyplot as plt
weekly = ex02.weekly_volume(df)
ax = weekly.plot(kind="bar", title="Weekly volume (kg)")
plt.tight_layout(); plt.savefig("weekly-volume.png")
```

`.plot()` on any Series/DataFrame; `kind=` bar/line/hist; always title + savefig. Chart
grammar beyond this lives in Tier D — the taster needs only: *can you SEE your training*.

## Step 4 — Ask real questions (the project)

Progression = best set per week per lift (line chart, does it climb?). Plateau = a lift
whose 4-week rolling best hasn't moved (`series.rolling(4).max()`). Consistency = workouts
per week (bar chart; the gaps tell your training story — term crunches will be visible).
The project runs all four on the real 294 and makes you write one honest sentence per chart.

**Checkpoint — you can now:** stand up a venv; flatten nested JSON to tidy rows; run the
four-command inspect reflex; answer "top lifts / weekly volume / PR / est-1RM" in groupby
grammar; save a chart; and explain split-apply-combine with your own analogy.

## Sources (verified 04/08/2026)

- Your real data: `repos\hevy-brain\data\workouts.json` — 294 workouts, schema inspected
  live tonight (dict-by-id → exercises[] → sets[] with weight_kg/reps/type/rpe).
- Exercise sample: `exercises/workouts-sample.json` — synthetic values, EXACT real schema;
  expected answers machine-verified (9/9) in a clean pandas venv tonight.
- pandas/matplotlib behaviour: exercised by that verification run (pandas current stable,
  installed fresh).
- Optional: Kaggle Learn Python + pandas micro-courses (free) — kaggle.com/learn.
