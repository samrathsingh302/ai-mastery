# Project 04 — vault-janitor.py (read-only report on your REAL working folders)

**What:** your first automation aimed at real data — a READ-ONLY janitor that surveys
`C:\Users\samra\OneDrive\dev\repos\` and writes `janitor-report.md` here. It changes nothing
(safety laws in force); it tells you what a cleanup WOULD look at. ~2–3h. Tutor rules apply
(contract on; the loops are yours to write).

## Spec

The report, in markdown, per repo folder under `OneDrive\dev\repos\`:

1. **Handoff freshness:** newest file in `handoffs\` (parse the date with your ex03 function —
   import it!) and its age in days; flag `⚠ STALE` if >30 days.
2. **Weight:** total file count + the single biggest file (your ex01 functions — import them).
3. **TODO debt:** count of lines containing `TODO` or `- [ ]` across that repo's `.md` files.
4. Footer: totals + the three stalest repos.

Constraints: pathlib only for walking; compiled regexes; `encoding="utf-8"` everywhere
(errors="ignore" acceptable for stray binaries); the script must run start-to-finish in
under a minute; **zero writes outside this project folder**.

## Why importing your own exercise functions is the real lesson

`from` your exercises folder `import` the functions you already wrote and tested — code you
trust because check.py proved it. That's the whole craft in miniature: build small verified
parts, compose them. (Mechanics: either copy the two files here, or add the exercises folder
to `sys.path` — both are legitimate at this stage; modules and packaging come later.)

## Acceptance checklist

- [ ] Runs on the real OneDrive dev repos folder; nothing modified anywhere
- [ ] Stale flags correct (spot-check two repos by hand against Explorer dates)
- [ ] ex01 + ex03 functions imported and reused, not rewritten
- [ ] Report is honest markdown you'd actually read (columns aligned, dates dd/mm/yyyy)
- [ ] Committed here with the journal line; walls noted
