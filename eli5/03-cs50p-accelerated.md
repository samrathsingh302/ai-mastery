# 03-cs50p-accelerated — like you're 5

Module 03, CS50P accelerated: every term, explained like you're 5.

- **Taught in:** `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\TEACH.md`

- **The one-line reminders:** `GLOSSARY.md` → `## Module 03 — CS50P accelerated`

- **Not answers:** every "See it" below is a different example from the ones `check.py` grades. None of them is an exercise answer.

- **To try one:** `cd C:\Users\samra\repos\ai-mastery`, then `python` to open the REPL. Type the lines, then `exit()` to leave.

---

### Accumulator pattern
**Like you're 5:** An empty bucket. You walk past each sweet on the table, drop it in the bucket, and at the end you hand over the bucket. Start empty, visit each, add it in, hand it back.

**The real words:** Start · visit each · fold in · return; half of beginner code has this shape. → [03 rung 2](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `initials = ""` then `for w in ["leeds", "york"]: initials += w[0]` then `initials` → `'ly'`.

### Argument / parameter
**Like you're 5:** A form has an empty box labelled "Name:". The box is the parameter. Whatever you write in the box today, "Sam", is the argument. Same box, different writing each time.

**The real words:** The value you pass in a call / the placeholder name in the definition that receives it. → [03 rung 0](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `def shout(word): return word.upper() + "!"` — `word` is the parameter; in `shout("go")`, `"go"` is the argument.

### Boolean
**Like you're 5:** A light switch: on or off, nothing in between. Every yes-or-no question the computer asks gets one of those two answers: True or False.

**The real words:** A value that is only `True` or `False`; comparisons (`==`, `<`, `in`…) produce them. → [03 rung 1](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** In the REPL: `3 > 2` → `True`; `"z" in "leeds"` → `False`.

### Class / object
**Like you're 5:** A cookie cutter and the cookies. The cutter is the shape you design once. Each cookie you press out is its own cookie, with its own icing, but they all share the cutter's shape.

**The real words:** Cookie cutter / cookie: a blueprint bundling data with its functions, and the instances made from it. → [03 rung 8](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `class Dog:` / `    def __init__(self, name): self.name = name` / then `rex = Dog("Rex")` and `rex.name` → `'Rex'`.

### Dictionary (dict)
**Like you're 5:** A row of coat hooks, each with a name tag. You don't count along the hooks; you go straight to the hook that says "Sam" and take what's hanging there.

**The real words:** Labelled values looked up by key: `row["name"]`; built up with `.get(k, 0) + 1`. → [03 rung 6](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `ages = {"sam": 20}` then `ages["sam"]` → `20`; `ages.get("tom", 0)` → `0` instead of an error.

### Exception / traceback
**Like you're 5:** A fire alarm. Everything stops and the building empties, unless someone has a plan for that exact alarm. The note the fire officer leaves says what happened at the bottom and where it started above it.

**The real words:** Python's "cannot continue" alarm, and the report you read bottom-up: last line is what, the lines above are where. → [03 rung 3](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** In the REPL type `int("cat")` and read only the last line: `ValueError: invalid literal for int() with base 10: 'cat'`.

### f-string
**Like you're 5:** A birthday card with a blank where the name goes. You write the card once, and the right name drops into the blank each time.

**The real words:** `f"hello, {name}"`: text with values dropped in. → [03 rung 0](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `city = "Leeds"` then `f"I study in {city}"` → `'I study in Leeds'`.

### List
**Like you're 5:** A queue of children holding hands. Each has a place in line, and the first child is number 0, not number 1. You can walk down the line visiting each child in turn.

**The real words:** Ordered collection, indexed from 0; loops visit it item by item. → [03 rung 2](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `days = ["mon", "tue", "wed"]` then `days[0]` → `'mon'` and `len(days)` → `3`.

### List comprehension
**Like you're 5:** Instead of saying "take a bowl, then for each apple, peel it and put it in the bowl", you say in one breath: "a bowl of every apple, peeled".

**The real words:** A loop that builds a list in one line; if it needs two thoughts, write a normal loop. → [03 rung 9](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `[w.title() for w in ["leeds", "york"]]` → `['Leeds', 'York']`.

### Method
**Like you're 5:** A toy that comes with its own buttons. A teddy has a "squeeze" button; you press it on that teddy. A method is a button that belongs to a value, and the dot is how you reach it.

**The real words:** A function living on a value, called with a dot: `name.strip()`. → [03 rung 0](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `"  hi  ".strip()` → `'hi'`; `"leeds".upper()` → `'LEEDS'`.

### Module / import
**Like you're 5:** Borrowing a neighbour's power drill instead of making your own drill out of metal. Someone already built it and tested it; you just bring it into your shed.

**The real words:** Someone else's tested functions pulled into your program with `import`. → [03 rung 4](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `import math` then `math.sqrt(16)` → `4.0`.

### Mutation / aliasing
**Like you're 5:** One sweet jar with two name tags on it, "Sam's" and "Tom's". If Tom adds a sweet, Sam's jar has one more too, because it was only ever one jar.

**The real words:** Changing a jar's contents while two labels point at it; the list surprise. → [03 tracer 5](../modules/03-cs50p-accelerated/interactive/code-tracer.html)

**See it:** `start C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\interactive\code-tracer.html` → tracer "5 · Two labels, ONE jar (list aliasing)".

### Regex
**Like you're 5:** A police description: "tall, red coat, hat". It doesn't name one person; it matches anyone who fits. A regex describes the shape of some text, and finds every bit that fits.

**The real words:** A mini-language for text patterns, used through `re`; always write patterns as raw strings, `r"..."`. → [03 rung 7](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `import re` then `re.findall(r"\d+", "3 sets of 5 reps")` → `['3', '5']`.

### REPL
**Like you're 5:** A science table where you try one thing and see what happens straight away. Mix two drops, look, mix again. No big plan; one small try at a time.

**The real words:** Run `python` alone: the interactive one-line-at-a-time laboratory (Read, Evaluate, Print, Loop). → [03 rung 4](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `cd C:\Users\samra\repos\ai-mastery`, `python`, then type `2 + 2` and see `4`; `exit()` leaves.

### return vs print
**Like you're 5:** A friend can hand you a sandwich, or show you a photo of a sandwich. Only the handed sandwich can be eaten later. Return hands a value back; print only shows a picture of it.

**The real words:** Hand a value back (usable, testable) vs show pixels to a human. → [03 rung 0](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `def a(): print(5)` and `def b(): return 5`; then `x = a()` shows 5 but `x` is `None`, while `y = b()` makes `y` equal `5`.

### Scope
**Like you're 5:** A workbench in a private shed. Whatever you put on the bench inside the shed is tidied away when you leave. Nobody outside can see it.

**The real words:** A function's private workbench; its names vanish when it returns. → [03 tracer 4](../modules/03-cs50p-accelerated/interactive/code-tracer.html)

**See it:** `def f(): inside = 1` then `f()` then `inside` → `NameError: name 'inside' is not defined`.

### Type
**Like you're 5:** Words and numbers are different kinds of thing. Two plus two numbers makes four; stick the word "two" next to the word "two" and you get "twotwo". What you can do depends on what kind of thing it is.

**The real words:** What kind a value is (`str`, `int`, `float`…); operations mean different things per type. → [03 rung 0](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `2 + 2` → `4`, but `"2" + "2"` → `'22'`; `type("2")` → `<class 'str'>`.

### Unit test / assert
**Like you're 5:** A smoke alarm you fit once. It stays quiet while everything is fine and shouts the moment something burns, every day, even while you sleep.

**The real words:** A small program that checks one behaviour of another, forever; `assert` is silent if true and raises `AssertionError` if false. → [03 rung 5](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `assert len("abc") == 3` → nothing happens; `assert len("abc") == 4` → `AssertionError`.

### Variable
**Like you're 5:** A sticky label on a jar. The label is not the jam. If you peel the label off and stick it on a different jar, the first jar still has its jam; the label just moved.

**The real words:** A name stuck on a value; reassignment moves the label, not the jar. → [03 rung 0](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `x = 1`, `y = x`, `x = 2`, then `y` → still `1`. Tracer 1 in `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\interactive\code-tracer.html` animates it.

### with open(...)
**Like you're 5:** A library book that returns itself. You borrow it, read, and the moment you walk out of the room it flies back to the shelf, even if you tripped on the way out.

**The real words:** The safe file idiom: the file is closed for you, even on errors. → [03 rung 6](../modules/03-cs50p-accelerated/TEACH.md)

**See it:** `with open(r"C:\Users\samra\repos\ai-mastery\START-HERE.md", encoding="utf-8") as f: print(f.readline())` prints START-HERE's first line, then the file is closed.
