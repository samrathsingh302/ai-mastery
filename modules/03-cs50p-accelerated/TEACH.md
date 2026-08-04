# Module 03 — CS50P, accelerated (real Python, unaided)

> **What this is:** your Python-from-zero ladder, built to run CS50P (Harvard's Introduction to
> Programming with Python — cs50.harvard.edu/python, free) the *accelerated* way: **problem
> sets first, these notes as the teaching, lectures only as rescue**. Ten rungs mirror the
> course's ten weeks. **Budget: ~40h over 2–3 weeks at your pace.**
> **Method (from the plan):** for each rung — read the rung's notes here (20–40 min) → attempt
> the pset COLD (`cs50.harvard.edu/python/psets/N`) → wall >30 min? struggle first, then the
> rescue pointers → pset passes `check50` → do my matching exercise (`exercises/exNN_*.py`,
> `python check.py` to verify) → tick the checkpoint → next rung. The pset is the workout;
> these notes are the coach.
> **Where to write code:** CS50 gives you a browser VS Code at cs50.dev (zero setup, their
> checker built in). For MY exercises and the project, work locally (your machine verified
> green in module 02) — that's deliberate: both worlds, early.

## ⚡ The git survival minimum (before rung 0 — 15 minutes, once)

Module 05 teaches git properly; until then you version your work with four commands, by rote,
in `repos\ai-mastery\`:

```
git add -A                                   # stage everything you changed
git commit -m "rung 2: loops exercises"      # snapshot with a message
git push                                     # copy the snapshot to GitHub
git log --oneline -5                         # see your last five snapshots
```

Run them at the end of every study session (the cockpit's closing step reminds you). If any
command errors: STOP, screenshot, ask your tutor session to explain — do not improvise git
commands you don't know yet.

## The mental model that carries all ten rungs

A Python program is **a list of instructions executed top to bottom, one at a time**. Three
things exist while it runs: **values** (the data), **names** (labels you stick on values), and
**control flow** (the rules for which instruction runs next: normally "the next line", unless
an `if`, a loop, or a function call redirects). Every rung below adds one power to that model —
nothing ever replaces it. *(Analogy: a recipe — ingredients (values), labelled jars (names),
and "now do step 4 / repeat until golden" (control flow).)*

---

## Rung 0 — Functions & variables *(pset 0)*

- **Variable** *(plain words)*: a name stuck on a value so you can use it later. `spend = 12.50`
  sticks the label `spend` on the value `12.50`. *(Analogy: a labelled jar — the label isn't
  the contents.)* Reassigning (`spend = 14`) moves the label to a new jar; the old value isn't
  changed, it's abandoned.
- **Type**: what KIND of value something is. The starters: `str` (text, in quotes: `"leeds"`),
  `int` (whole number: `42`), `float` (decimal: `12.5`). Types matter because operations mean
  different things per type: `2 + 2` is `4`; `"2" + "2"` is `"22"` (gluing text). Convert with
  `int("2")`, `str(42)`, `float("12.5")`.
- **Function** *(plain words)*: a named, reusable block of instructions that takes inputs and
  hands back an output. *(Analogy: a kettle — water in, button, boiling water out; you don't
  re-explain boiling each time.)* You've been USING them already: `print("hi")` (shows text),
  `input("Name? ")` (asks the user, gives back a `str` — always a str, even if they type 7).
- **Defining your own:**

  ```python
  def price_with_vat(price):        # def = "I'm defining a function"; price = parameter
      return price * 1.20           # return = the value handed back to the caller

  total = price_with_vat(10.0)      # calling it; 10.0 = argument; total is now 12.0
  ```

  **Parameter** = the placeholder name in the definition; **argument** = the actual value you
  pass. `return` ≠ `print`: return hands a value back (usable, testable); print only shows
  pixels to a human. *This distinction is the #1 beginner wall — my ex00 drills it.*
- **f-strings** (build text from values): `f"hello, {name}"` drops the value of `name` into
  the text. Method calls on strings: `name.strip()` (trim spaces), `name.title()`,
  `name.upper()` — a **method** is just a function that lives on a value, called with a dot.
- **Pset-0 walls + rescue:** everything is `input()` + string methods + f-strings + arithmetic.
  Wall: "my maths is wrong" → you did arithmetic on strings; convert first. Wall: "nothing
  prints" → you returned but never printed, or defined a function and never called it.

**Checkpoint — you can now:** explain variable/type/function/parameter-vs-argument/return-vs-
print with your own analogies, and pset 0 passes check50.

## Rung 1 — Conditionals *(pset 1)*

- **Boolean**: a value that is only ever `True` or `False`. Comparisons make them: `==` (equal
  — TWO signs; one `=` is assignment), `!=`, `<`, `>=`…
- **`if` / `elif` / `else`**: the fork in the road. Python finds the FIRST true branch, runs
  it, skips the rest — order matters:

  ```python
  def quota_lane(hours):
      if hours >= 25:  return "holiday template"
      elif hours >= 15: return "normal template"
      elif hours >= 7:  return "crunch template"
      else:             return "maintenance mode"
  ```

- Combine with `and` / `or` / `not`; membership with `in` (`if "r" in word:`). **Indentation
  IS the syntax** in Python: the indented block is what the `if` owns. Four spaces, always.
- **Pset-1 walls:** overlapping ranges (put the narrowest/highest test first, like above);
  comparing a number to `input()`'s string (`int()` first); `=` vs `==` (Python will error on
  the first — read the error, it's teaching rung 3 early).

**Checkpoint:** you can hand-trace any if/elif chain and say which branch fires and why;
pset 1 passes.

## Rung 2 — Loops *(pset 2)*

- **Loop** *(plain words)*: "repeat this block". Two kinds, two jobs:
  - `for x in collection:` — *for each thing, do this* (known collection).
  - `while condition:` — *keep going until this stops being true* (unknown count: retry until
    valid input, game loops).
- **The accumulator pattern** (half of all beginner code is this shape):

  ```python
  def total_volume(sets):           # sets like [(100, 5), (110, 3)]  (weight, reps)
      total = 0                     # 1. start an accumulator
      for weight, reps in sets:     # 2. visit each item (unpacking the pair)
          total += weight * reps    # 3. fold it in
      return total                  # 4. hand back the result
  ```

- **Lists** arrive here properly: `["a", "b", "c"]` — ordered, indexed from **0** (`items[0]`
  is the first; `len(items)` counts). `range(n)` gives 0…n-1 for counted loops. Strings loop
  too (`for ch in word:`).
- **Pset-2 walls:** infinite `while` (you never changed the condition's ingredients); off-by-
  one (`range(len(s))` vs `range(len(s)-1)` — trace on paper with a 3-item list, always);
  building a new string vs printing as you go (accumulate, then return).

**Checkpoint:** you can write the accumulator pattern from a blank file without notes (do it —
close-window-rebuild), and pset 2 passes.

## Rung 3 — Exceptions *(pset 3)*

- **Exception** *(plain words)*: Python's "I cannot continue this instruction" signal — the
  program stops and prints a **traceback** unless you catch it. *(Analogy: a fire alarm — it
  interrupts everything; catching it is having a plan instead of evacuating.)*
- **Read the traceback BOTTOM-UP**: last line = what went wrong (`ValueError: invalid literal
  for int() with base 10: 'cat'`); the lines above = where. This single habit is half of
  debugging. The dojo has been training exactly this muscle.
- **Catching:**

  ```python
  def robust_int(text, default=0):
      try:                       # attempt the risky thing
          return int(text)
      except ValueError:         # the plan if THAT specific alarm rings
          return default
  ```

  Catch the SPECIFIC exception (`except ValueError:`), never bare `except:` — a bare except
  swallows every alarm including ones you needed to hear (ex01's backup bug, in code form).
- The retry idiom: `while True:` + `try` + `return`/`break` on success — pset 3 is this idiom
  three ways.
- **Pset-3 walls:** catching too much (bare except hides YOUR typo); catching too early (let
  the error happen where you can actually respond); forgetting `else`/second `input()` inside
  the retry loop.

**Checkpoint:** you can read any traceback aloud (what + where), and pset 3 passes.

## Rung 4 — Libraries *(pset 4)*

- **Module/library** *(plain words)*: someone else's tested functions, shipped with Python or
  installed, that you pull in with `import`. *(Analogy: power tools you borrow instead of
  forging your own.)* `import random` → `random.choice(options)`; `from statistics import
  mean` → `mean(numbers)`.
- The ones pset 4 plays with: `random`, `statistics`, `sys` (`sys.argv` = the words typed
  after your script's name on the command line; `sys.exit("message")` to quit deliberately),
  and installing with `pip install` (e.g. `cowsay`, API clients).
- **Reading documentation is the actual skill of this rung**: the pattern is *find the
  function → what does it take → what does it return → tiny experiment in the REPL*
  (`python` alone opens the interactive prompt — the fastest laboratory you own; `exit()`
  leaves).
- **Pset-4 walls:** `sys.argv[0]` is the script name (your argument is `[1]`); crashes when
  arguments are missing (check `len(sys.argv)` first — conditionals paying rent).

**Checkpoint:** given a stdlib function you've never seen, you can learn it from `help()` /
the docs and use it in under 10 minutes; pset 4 passes.

## Rung 5 — Unit tests *(pset 5)*

- **Unit test** *(plain words)*: a small program whose only job is to check one behaviour of
  another program, automatically, forever. *(Analogy: a smoke detector you install once; it
  guards while you sleep.)* You met evals in module 01 — unit tests are evals for ordinary
  code.
- **`assert`**: `assert square(3) == 9` — silence if true, alarm (AssertionError) if false.
- **pytest**: put functions named `test_*` in `test_something.py`; run `pytest`; it hunts and
  runs them all. Structure your code so it's testable: logic in functions that RETURN (rung
  0's lesson compounding — you can't assert on print).
- **What makes a test GOOD** (the plan's Tier-1 question, seeded now): it fails when the
  behaviour breaks (catches the bug), it tests the boundary (0, empty, negative, huge), and
  its name says what it guards. A test that can't fail is decoration — my ex05 makes you
  prove yours can catch a planted bug.
- **Pset-5 walls:** testing print instead of return (restructure); forgetting edge cases
  (check50 will find them for you, humblingly).

**Checkpoint:** you can write a test that FAILS on a planted bug and passes on the fix —
ex05 is exactly this; pset 5 passes.

## Rung 6 — File I/O *(pset 6)*

- **File I/O** = reading/writing files so data outlives the program. The safe idiom:

  ```python
  with open("log.txt") as f:        # "with" closes the file for you, even on errors
      for line in f:                # files loop line by line
          process(line.strip())     # strip the invisible newline FIRST
  ```

  Writing: `with open("out.txt", "w") as f: f.write(text)` — `"w"` REPLACES the file, `"a"`
  appends. (You know this failure class: it's Set-Content vs Add-Content.)
- **CSV** (comma-separated values — spreadsheets as text): `import csv`, `csv.DictReader(f)`
  gives you each row as a dict. Your Hevy export is exactly this — module 07 feasts on it.
- **Dictionaries** earn their keep here: `{"name": "squat", "reps": 5}` — labelled values,
  looked up by key (`row["name"]`), built with `counts[word] = counts.get(word, 0) + 1`.
- **Pset-6 walls:** the phantom `\n` (strip it); `"w"` nuking a file you meant to append to;
  paths (relative paths are relative to where you RUN python, not where the file lives).

**Checkpoint:** you can round-trip data (write → read back → same values) and count things in
a real file; pset 6 passes.

## Rung 7 — Regular expressions *(pset 7)*

- **Regex** *(plain words)*: a mini-language for describing text PATTERNS instead of exact
  text. *(Analogy: a police description — "medium height, red coat" matches many people;
  `\d{2}/\d{2}/\d{4}` matches every dd/mm/yyyy date.)*
- The survival kit (this is 80% of real use): `\d` digit · `\w` word-char · `.` anything ·
  `+` one-or-more · `*` zero-or-more · `?` optional · `[abc]` one of these · `^` start ·
  `$` end · `()` capture group. `import re`; `re.search(pattern, text)` finds; `.group(1)`
  extracts the capture; `re.findall` collects all matches.
- **Law: always use raw strings for patterns** — `r"\d+"` — so Python doesn't eat the
  backslashes before regex sees them.
- **Pset-7 walls:** greedy `.*` swallowing too much (prefer specific classes like `[^@]+`);
  forgetting `^…$` so partial junk matches; testing regex in your head (don't — build it
  piece by piece in the REPL).

**Checkpoint:** you can write, from memory, a regex that pulls every dd/mm/yyyy date out of a
paragraph (my ex07); pset 7 passes.

## Rung 8 — Object-oriented programming *(pset 8)*

- **Class** *(plain words)*: a blueprint for values that carry BOTH data and the functions
  that belong with that data. *(Analogy: a cookie cutter (class) and cookies (objects /
  instances).)* You've been using objects all along — `"hi".upper()` is a method on a str
  object; rung 8 is you finally making your own cutters.

  ```python
  class Workout:
      def __init__(self, exercise, weight, reps):   # runs at creation; self = THIS cookie
          self.exercise = exercise                  # attributes: data stuck on the object
          self.weight = weight
          self.reps = reps

      @property
      def volume(self):                             # computed attribute: w.volume, no ()
          return self.weight * self.reps

      def __str__(self):                            # what print(w) shows
          return f"{self.exercise}: {self.weight}kg x {self.reps}"
  ```

- `__init__` (the constructor), `self` (the object being operated on — Python passes it for
  you), `@property` (computed-on-read attribute), `__str__` (human display). That quartet is
  pset 8's whole vocabulary; inheritance exists but is a later-tier concern.
- **Pset-8 walls:** forgetting `self.` (assigning to a local that evaporates); calling a
  property with `()`; doing everything in `__init__` instead of methods.

**Checkpoint:** you can explain class-vs-object with your own analogy and write the quartet
cold — ex08 is a Hevy-flavoured rep of exactly it; pset 8 passes.

## Rung 9 — Et cetera *(pset 9 + the graduation)*

The finishing moves, each one line of leverage: **list comprehensions** (`[s.upper() for s in
names if s]` — a loop that builds a list, in one readable line; if it needs two thoughts, use
a normal loop), **unpacking** (`a, b = pair`, `*rest`), `sorted(items, key=...)` for "top N
by…", sets (`set(names)` — instant de-duplication), `enumerate` (index + item together), and
type hints (`def f(x: int) -> str:` — labels for humans and tools; Python doesn't enforce
them, but every serious codebase — including the ones you'll archaeology in module 06 —
speaks them).

**Graduation (before calling this module done):** CS50P's final project — but per the house
rules it's your module-12 AI-free build that really graduates you. Minimum here: psets 0–8
green + my ex00–ex09 green + the project below done AI-free.

---

## Sources (verified 04/08/2026)

- CS50P course + psets: cs50.harvard.edu/python (ten weeks confirmed; week 0 topic list
  confirmed via cs50.harvard.edu/python/weeks/0; psets at cs50.harvard.edu/python/psets/) —
  free; the £150 cert is skipped per plan (community verdict: learning excellent, cert
  worthless).
- Method (psets-first, lectures-as-rescue, walls-are-curriculum): plan v3 Parts 1–3.
- Python semantics in these notes: Python 3.12+ stdlib behaviour, exercised against your
  local 3.14.5 by `exercises/check.py` (run it — it self-verifies the harness before testing
  you).
