# Card notes — 26/08/2026 session (module 03, rungs 0–1)

> Samrath makes the cards himself (his ruling 26/08/2026); this file is the session's
> notes: what's worth carding, explained, with a recommended count.
> Style reference when making them: anki/CARD-RULES.md.

**Recommended: ~7 cards** (the 8 facts below; facts 2 and 3 overlap — one card or two, your call).

1. **The str+int TypeError rule** (your #1 recurring miss). `"2" + 2` → TypeError.
   `+` adds (both numbers) or glues (both strings); it NEVER mixes number and text.
   Contrast that with fact 7 — numbers mix with numbers freely.

2. **A function where no `return` runs gives back `None`.** Every call hands something
   back; if no return statement is hit, that something is None. The classic cause:
   you wrote `print` where you meant `return`.

3. **return vs print.** `return` hands a value to the caller — usable, storable,
   testable. `print` only paints pixels for a human; the print version returns None.

4. **"Contains at least one digit" needs a wrapper** (your other recurring miss —
   dropping `any()`). `any(ch.isdigit() for ch in pw)`. The trap: `pw.isdigit()` asks
   "is the WHOLE string digits?" — the wrong question.

5. **What `any()` does.** Takes a stream of booleans, gives back ONE: True if at least
   one is True. Without it you have many answers and no verdict.

6. **if/elif runs the FIRST true branch only** — the rest are skipped even if also
   true. Consequence: the narrowest/highest test goes first.

7. **`2 + 2.5` → `4.5`, a float.** Numbers mix freely (the int gets promoted); only
   number-meets-TEXT errors (fact 1's rule).

8. **Fix is right but the checker still fails → is the file SAVED?** The checker runs
   what's on disk. VS Code tell: ● on the tab = unsaved.

## The backlog (for future sessions' notes, not now)

The 14 files in `anki/cards/*.tsv` hold all 288 module drill facts in question¶answer
form — raw material to mine module-by-module as you study each one. Next in study
order: module 03's remaining rungs, then per the CAREER.md priority order.

## Image-occlusion candidates (manual, whenever you want)

- The transformer stack diagram (m11) — occlude layers
- Git graph shapes: merge vs rebase vs revert (m05)
- The 9-hop page-load journey (m08)
- Your monk-mode tick-loop / psoc request-trace maps (m06)
