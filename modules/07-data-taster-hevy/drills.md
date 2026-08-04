# Drills — module 07

## Anki-importable block (tab-separated: Front ⇥ Back)

A virtual environment is…	A private Python + packages inside the project folder — projects can't break each other; delete the folder, it's gone.
The three venv commands?	py -m venv .venv · .venv\Scripts\activate · pip install <things>
A DataFrame is… a Series is…	A table · one typed, labelled column of it.
The pandas reflex after every load?	df.head() · df.shape · df.dtypes · df.describe() — inspect before trusting.
Tidy data means…	One row per observation (one row per SET here) — every question becomes filter/group over rows.
Why almost never loop in pandas?	You operate column-at-a-time: df["volume"] = df["weight_kg"] * df["reps"] multiplies whole columns.
Convert ISO date strings to real datetimes?	df["date"] = pd.to_datetime(df["date"])
Split-apply-combine is…	Split rows into groups → apply a function per group → combine results: df.groupby("exercise")["volume"].sum()
Filter rows for one exercise?	A boolean mask: df[df["exercise"] == "Bench Press (Barbell)"]
Sort a groupby result descending?	.sort_values(ascending=False)
ISO week key from a date column?	df["date"].dt.isocalendar() → year + "-W" + zero-padded week
The Epley est-1RM formula?	weight × (1 + reps/30) — computed per set, take the max.
Detect a plateau with pandas?	Rolling window: series.rolling(4).max() flat for weeks = plateau.
Minimum viable matplotlib?	series.plot(kind="bar", title=...) · plt.tight_layout() · plt.savefig("name.png")
Why copy the data file before analysing?	Read-only law on live repos — and a fresh copy re-run proving same results is your reproducibility check.
"Warm-ups in volume?" is what kind of question?	A tidying DECISION — either answer is fine, but it must be written down.
The point of the whole module in 4 words?	Data → honest sentence → decision.

## Quick-fire (aloud, 30 seconds)

1. One row per what? 2. groupby's three beats? 3. First four commands after load? 4. venv undo?
*(set · split-apply-combine · head/shape/dtypes/describe · delete the folder)*
