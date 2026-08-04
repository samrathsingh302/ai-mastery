# Drills — module 03 (import after starting rung 2; add misses as you go)

## Anki-importable block (tab-separated: Front ⇥ Back)

A variable is…	A name stuck on a value ("a labelled jar") — reassigning moves the label, not the contents.
The three starter types and their literals?	str "text" · int 42 · float 12.5
"2" + "2" equals…	"22" — + on strings glues text; convert with int() first if you meant maths.
return vs print?	return hands a value back to the caller (usable, testable); print only shows pixels to a human.
Parameter vs argument?	Parameter = placeholder name in the def; argument = actual value passed in the call.
What does input() always give you?	A str — even if the user typed a number. Convert before arithmetic.
= vs ==?	= assigns (sticks the label); == compares (asks a True/False question).
Why does branch order matter in if/elif chains?	Python runs the FIRST true branch and skips the rest — narrowest/highest test goes first.
What owns the indented block?	The if/for/while/def line above it — indentation IS the syntax; four spaces.
for vs while, in one line each?	for = "for each thing in a collection"; while = "keep going until this stops being true".
The accumulator pattern's four steps?	Start an accumulator · visit each item · fold it in · return the result.
First index of a Python list?	0 — items[0]; len(items) counts; items[len(items)] is an IndexError.
How do you read a traceback?	Bottom-up: last line = what went wrong; lines above = where it happened.
Why never bare `except:`?	It swallows EVERY alarm — including the typo you needed to hear. Catch the specific exception.
The retry-until-valid idiom?	while True: + try: return/break on success + except ValueError: ask again.
What is sys.argv[0]?	The script's own name — your first real argument is sys.argv[1].
The fastest laboratory you own?	The REPL: run `python` alone, experiment one line at a time, exit().
What makes a unit test GOOD (3 things)?	It fails when behaviour breaks · it tests boundaries (0/empty/negative) · its name says what it guards.
Why can't you assert on print?	print returns None — structure logic in functions that RETURN, then assert on the value.
The safe file-reading idiom?	with open(path) as f: — closes the file for you, even when errors happen.
"w" vs "a" mode?	"w" REPLACES the file's contents; "a" appends. Know which you meant before you run it.
The phantom \n bug?	Lines read from files keep their newline — .strip() (or .rstrip("\n")) before comparing.
Build-a-count dict idiom?	counts[key] = counts.get(key, 0) + 1
Regex survival kit (6 pieces)?	\d digit · \w word-char · + one-or-more · ? optional · [abc] one-of · () capture group
Why raw strings for regex?	r"\d+" stops Python eating backslashes before the regex engine sees them.
Regex for every dd/mm/yyyy date?	r"\d{2}/\d{2}/\d{4}" with re.findall
Class vs object?	Class = cookie cutter (blueprint); object/instance = the cookie. "hi".upper() is a method on a str object.
What is self?	The object being operated on — Python passes it to methods automatically.
@property does what?	Makes a method readable like an attribute: w.volume, no parentheses.
__str__ controls what?	What print(obj) and str(obj) show — the human face of your object.
A list comprehension is…	A loop that builds a list in one line: [x*x for x in nums if x % 2 == 0]
Sort a dict's items by value, descending, ties alphabetical?	sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))
De-duplicate a list in one call?	set(items) — order not guaranteed; sorted(set(items)) if you need order.

## Quick-fire (aloud, 45 seconds)

1. First list index? 2. input() returns what type? 3. Read a traceback from which end?
4. "w" does what to an existing file? 5. Raw string prefix for regex?
*(0 · str · bottom · replaces it · r"...")*
