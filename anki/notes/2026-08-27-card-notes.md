# Card notes — 27/08/2026 session (NeetCode #1 Contains Duplicate + module 03 rung 2 opener)

> Samrath authors his cards (scribe workflow, 26/08): these are the facts worth carding.
> Style reference: anki/CARD-RULES.md. Recommended: 6–8 cards.

1. **The accumulator pattern, four steps:** set up an empty thing BEFORE the loop → visit
   each item → fold it in → return AFTER the loop. Half of all beginner code is this shape;
   your contains_duplicate was one.
2. **for vs while:** `for` = for each thing in a known collection; `while` = keep going
   until the condition stops being true (unknown number of rounds — retry-until-valid, games).
3. **The infinite-while wall:** the loop never ends because nothing inside changes what
   the condition checks. Fix = change the ingredient (e.g. `n = n - 1` inside the body).
4. **Unpacking pairs in a loop:** `for weight, reps in sets:` — two names before `in`,
   each pair pours into them every round.
5. **List positions:** index from 0 (`items[0]` = first); `len(items)` counts;
   `range(n)` gives 0…n-1.
6. **Membership test:** `x in some_list` → True/False, "is x anywhere in there". Works on
   strings too (`ch in "aeiou"`).
7. **`.append(x)`** sticks x on the END of a list.
8. **Contains Duplicate (the idea, not the code):** you don't need counts — remember only
   the numbers already seen; return True the instant the current number is already there;
   an empty list runs the loop zero times → False.
9. **Terminology:** `[]` is an empty LIST, not a set — sets are a different type (and the
   optimal version of this problem uses one; later).

## Image-occlusion candidates
- none today (all textual)
