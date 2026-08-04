# Project 07 — Your training, answered (the real 294)

**What:** point your VERIFIED exercise code at the real dataset and answer four questions
you actually care about. ~3h. Tutor rules; the analysis decisions are yours.

## Setup (read-only law)

COPY the data in — never analyse the live file in hevy-brain:
`copy C:\Users\samra\repos\hevy-brain\data\workouts.json .\my-workouts.json`
(This folder's .gitignore excludes it — your training history stays out of the repo.)

## The four questions (one chart + one honest sentence each)

1. **What do I actually train?** Top 10 exercises by total volume, all-time (bar chart).
   Sentence: does the ranking match what you'd have GUESSED? Name one surprise.
2. **Is my bench/squat/deadlift going anywhere?** Pick your top-3 by frequency; per lift,
   best set weight per ISO week (line chart). Sentence per lift: climbing, flat, or noisy —
   and since when?
3. **Where are the plateaus?** 4-week rolling max of est-1RM per top lift; flag any lift
   flat for ≥6 weeks. Sentence: which lift, which weeks — and what was happening in life
   then (term? holiday? the gaps know).
4. **How consistent am I really?** Workouts per ISO week since 2023 (bar). Sentence: your
   real cadence vs the story you tell yourself about it.

Deliverables in this folder: `analysis.py` (or a notebook), 4+ PNGs, and `findings.md`
with the four sentences + one decision your NEXT training block should take because of the
data. That last line is the point of the whole module: data → decision.

## Acceptance checklist

- [ ] Runs top-to-bottom on my-workouts.json without hand-edits (fresh copy = same result)
- [ ] Every chart: title, labelled axes, saved PNG, dd/mm/yyyy dates where shown
- [ ] Set types checked: did you include warm-ups in volume? Say so either way (a tidying
      DECISION, written down)
- [ ] findings.md: four honest sentences + the one training decision
- [ ] Data file gitignored; code + charts + findings committed
