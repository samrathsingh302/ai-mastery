# The daily sheets — how they work

From 16/09/2026 the week runs from a sheet per day, not from a session. The law is ten lines:

1. **Open today's file** in this folder — `sheets\<yyyy-mm-dd>-<ddd>.md`. That file is the day.
2. **Do it top to bottom.** The order on the sheet is the order; applications come before study.
3. **Every item names its file or URL, its explanation, its check command and its done-when.**
   You never have to work out where something lives or whether it is finished.
4. **The check command decides, not you and not Claude.** Green is green; nothing else counts.
5. **Ask the on-call tutor only when stuck** — 30 minutes of genuine struggle first, then paste
   the line, question or error into `/study-session`. It does not teach unprompted.
6. **Close with the ritual**: Anki queue + your own cards, one journal line, `apply.py status`
   for any submission, carry-forward named.
7. **A missed item is carried**, named, to the top of its lane on tomorrow's sheet — never
   dropped silently.
8. **If a day overflows, drop from the bottom** of the rank (applications > Gate 1 + NeetCode >
   Prolog/KRR > case study > Java > Cantrill), never the top.
9. **Anki reviews are the floor every day**, including zero-days, and are not re-listed per item.
10. **The week is scored Tuesday 22/09** on this list (CAREER.md §7K); §7I-R's W3' onward is
    unchanged.

## The week — Wed 16/09 → Tue 22/09

| Day | Sheet | Headline |
|---|---|---|
| Wed 16/09 | `C:\Users\samra\repos\ai-mastery\sheets\2026-09-16-wed.md` | ex02 typed and green · NeetCode #2 · SWI-Prolog installed |
| Thu 17/09 | `C:\Users\samra\repos\ai-mastery\sheets\2026-09-17-thu.md` | Lloyds submitted · Gate-0 pastes · ex03 + ex04 · NeetCode #3–5 · LPN ch 1 · mooc.fi account · Cantrill 1 |
| Fri 18/09 | `C:\Users\samra\repos\ai-mastery\sheets\2026-09-18-fri.md` | Palantir FDE + Barclays · ex05 · NeetCode #6–9 · Java Part 1 · LPN ch 2 + 5 KRR cards · Cantrill 2 · case-study outline |
| Sat 19/09 | `C:\Users\samra\repos\ai-mastery\sheets\2026-09-19-sat.md` (creates) | ticket 3 — Goldman + Optiver · ex06 + ex07 · NeetCode #10–13 · LPN ch 3 · Java Part 2 |
| Sun 20/09 | `C:\Users\samra\repos\ai-mastery\sheets\2026-09-20-sun.md` (creates) | ticket 3 — Palantir SWE + Jane Street · ex08 + ex09 + module 04 · NeetCode #14–17 · Sunday review |
| Mon 21/09 | `C:\Users\samra\repos\ai-mastery\sheets\2026-09-21-mon.md` (creates) | ticket 3 — ledger 298 + 302 · module 04 ex04–05 → Gate 1 · NeetCode #18–21 · case study DRAFTED |
| Tue 22/09 | `C:\Users\samra\repos\ai-mastery\sheets\2026-09-22-tue.md` (creates) | ticket 3 — week close, every submission recorded, the week scored |

Shifts (unavailable): Thu 16:30–23 · Sat 06:30–14:30 · Sun 07–12 · Tue 16–21.

## The checker

From `C:\Users\samra\repos\ai-mastery`:

```
python sheets/check_sheets.py
```

It proves every sheet carries the four headings (`## Today`, `## Do`, `## If stuck`, `## Close`)
and that every path a sheet sends you to actually exists — a path marked `(creates)` is one the
item makes itself, or an untracked one (`career\drafts\` is gitignored). It prints
`N sheets checked, M paths verified` and exits 1 on any miss.

Source of the week: `C:\Users\samra\OneDrive\dev\repos\ai-mastery\CAREER.md` §7K (the pace record)
and the signed plan `C:\Users\samra\OneDrive\dev\_global\plans\2026-09-15-ai-mastery-replan.md`.
The tutor's side of the contract lives in `C:\Users\samra\repos\ai-mastery\TUTOR-CONTRACT.md`.
