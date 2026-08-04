# Project 09 — Run the eval for real, publish the findings

**What:** the live run — your 10 shipped tasks + your 4 from ex01, two models you actually
care about, blind-graded, findings written. ~2h including grading.

## Steps

1. Dry-run first if you haven't (`run_eval.py --dry-run` → `grade.py --dry-run`) — learn
   the grading flow where mistakes are free.
2. Merge your ex01 tasks into a `tasks-mine.json` (14 tasks total) and point the scripts at
   it (both take the filename from tasks.json — copy it over or edit the constant; your
   call, note which you did).
3. Pick the two models. Recommendation: your daily default vs the small/fast one — that gap
   is the one you PAY for daily, so it's the one worth measuring.
4. `python run_eval.py --model-a <one> --model-b <two>` (28 calls; a few minutes).
5. `python grade.py` — programmatic, then blind rubric. Lock scores before the reveal.
   No reading outputs/ first.
6. `findings.md` here: the table + per-family subtotals + three sentences —
   **biggest gap** (which family, how big) · **biggest surprise** (which task flipped your
   prior) · **what n=1 does NOT prove** (write the humility down; it's part of the method).

## Acceptance checklist

- [ ] 14 tasks ran against both models; outputs + results.csv exist locally (gitignored)
- [ ] Rubric tasks graded BLIND (honesty check: could you have identified the models from
      style anyway? Say so in findings — that's a real blind-grading limitation)
- [ ] findings.md has the table, per-family subtotals, and the three sentences
- [ ] One deliberate follow-up named: the ONE task you'd add next time and what it would
      discriminate
- [ ] findings.md committed (it's the artefact; the raw outputs stay local)
