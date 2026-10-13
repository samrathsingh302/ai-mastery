# Semester 1 theory — like you're 5

The Semester 1 theory terms, one section per lane: Java, KRR, Data Science, coding tests and writing.

- **Drivers:** each lane is driven from the table in `C:\Users\samra\repos\ai-mastery\START-HERE.md` lines 23–30. Its grader decides.
- **Lane facts:** they come from that table and from `C:\Users\samra\OneDrive\dev\life\uni\UNI.md` §3 and §8, read only.
- **Not answers:** code lines are illustrations. Never a formative, a coursework task or a NeetCode answer.
- **Prolog:** lines run in the browser at `https://lpn.swi-prolog.org/` (no install).
- **Python:** lines run in `python`.
- **Java:** lines need a class and a `main` around them to compile.

---

## Java (COMP5911M)

### Class and object (Java)
**Like you're 5:** A class is a cookie cutter; an object is one cookie made with it. One cutter can make lots of cookies, all the same shape, and each cookie gets its own icing.

**The real words:** A class declares fields (what each object knows) and methods (what it does); `new` builds one object, an instance with its own field values. → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** `class Dog { String name; }` then `Dog rex = new Dog(); rex.name = "Rex";` — one class, one object.

### Interface (Java)
**Like you're 5:** A plug socket in the wall. Any lamp, kettle or charger with the right plug fits, and the wall doesn't care which one it is. An interface says "whatever you are, you must have this plug".

**The real words:** A named set of method signatures with no state; any class that `implements` it promises those methods, so code can depend on the interface and accept any implementation (SE lecture 2: "interfaces & multiple implementation"). → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** `interface Shape { double area(); }` then `class Square implements Shape { public double area() { return 4.0; } }` — and `Shape s = new Square();` works for any shape.

### JUnit 5 test
**Like you're 5:** A little robot checker. You tell it, "when I add 2 and 3, the answer must be 5". Every time you change your code, the robot checks again and shouts if the answer isn't 5 any more.

**The real words:** A method marked `@Test` that calls your code and asserts the result (`assertEquals(expected, actual)`); COMP5911M's Exercise 2 ships JUnit 5 (`MoneyTest.java` plus the console jar), while MOOC.fi is frozen on JUnit 4. → [Java lane: Exercism Java](https://exercism.org/tracks/java)

**See it:** `@Test void addsUp() { assertEquals(5, 2 + 3); }`, with `import org.junit.jupiter.api.Test;` and `import static org.junit.jupiter.api.Assertions.assertEquals;` — `jupiter` in the package name is how you know it's JUnit 5, not 4.

### Test-driven development (TDD)
**Like you're 5:** Before you build a sandcastle, you draw a line in the sand showing how tall it must be. Then you build until it reaches the line, then tidy it up. Line first, castle second, tidying third.

**The real words:** Red → green → refactor: write a failing test for the next behaviour, write the least code that passes it, then clean up with the test as the safety net. → [Java lane: Exercism Java](https://exercism.org/tracks/java)

**See it:** your own checker has the same rhythm: `cd C:\Users\samra\repos\ai-mastery` then `python modules\03-cs50p-accelerated\exercises\check.py ex02` — red first, then type until it's green.

### Refactoring under tests
**Like you're 5:** Tidying your bedroom while a grown-up checks after every move that nothing got broken or lost. You can move things around as much as you like, as long as the check still says "all here".

**The real words:** Changing code's structure without changing its behaviour, in small steps, with the tests run after each one so any break shows at once; the COMP5911M coursework is a "Design and Refactoring Task". → [Java lane: Gilded Rose kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/Java)

**See it:** the Gilded Rose kata's Java folder at that link — tangled code you must tidy without changing what it does, putting tests round it first.

### Code smell
**Like you're 5:** A funny smell in the kitchen doesn't prove the milk is off, but it tells you to go and check. A code smell is a bit of code that looks wrong: a reason to check, not proof of a bug.

**The real words:** A surface sign that a design may need refactoring (a very long method, duplicated code, a class doing too much); a hint, not a defect. → [Java lane: Gilded Rose kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/Java)

**See it:** `if (type == 1) { ... } else if (type == 2) { ... } else if (type == 3) { ... }` — a growing switch on a type code is the classic smell that the Strategy pattern below cures.

### SOLID
**Like you're 5:** Five tidy-room rules for code. Each toy box holds one kind of toy. Add new boxes instead of breaking old ones. A toy that says it's a car must drive like one. Don't make anyone carry boxes they don't need. Rely on the shape of a box, not one particular box.

**The real words:** Single responsibility · Open/closed · Liskov substitution · Interface segregation · Dependency inversion: five object-oriented design principles on the COMP5911M syllabus. → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** the S in two lines: `class Report { String text() { ... } }` and `class ReportPrinter { void print(Report r) { ... } }` — making the words and printing them are two jobs, so two classes.

### Design pattern (GoF)
**Like you're 5:** A recipe cooks have used so often that it has a name. Say "a sponge cake" and every baker knows the steps. Design patterns are named recipes for common code problems, so programmers can say one word instead of a page.

**The real words:** A named, reusable solution to a recurring design problem; "GoF" is the Gang of Four, the four authors of the 1994 book *Design Patterns* that catalogued 23 of them. → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** the target is in `C:\Users\samra\OneDrive\dev\life\uni\UNI.md` line 198, "three GoF patterns and SOLID"; the three entries below (Strategy, Observer, Factory) are the three this file explains.

### Strategy pattern
**Like you're 5:** A toy robot with a slot on its back for swappable cards: a "dance" card, a "sing" card, a "walk" card. The robot stays the same; you just swap the card to change what it does.

**The real words:** Put each interchangeable algorithm behind one interface and hand the object the one to use, instead of an `if/else` on a type code. → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** `interface Pricing { double price(double base); }` then `class StudentPricing implements Pricing { public double price(double b) { return b * 0.8; } }` — the till holds a `Pricing` and never asks which kind.

### Observer pattern
**Like you're 5:** Subscribing to a YouTube channel. You don't keep checking for new videos; when one is posted, everyone who subscribed gets told. The channel doesn't need to know who you are, only that you want telling.

**The real words:** A subject keeps a list of observers and calls each one when its state changes, so the subject never depends on who is listening. → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** `interface Listener { void onChange(int value); }` then `List<Listener> listeners = new ArrayList<>();` and `for (Listener l : listeners) l.onChange(42);` — the subject's whole job.

### Factory pattern
**Like you're 5:** A toy shop counter. You say "one teddy, please" and the shopkeeper fetches the right one from the back. You never go into the stockroom or need to know how teddies are made.

**The real words:** A method (or class) whose job is creating objects, so callers ask for "the shape for this name" and never call `new` on a concrete class themselves; GoF's formal versions are Factory Method and Abstract Factory. → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** `static Shape make(String kind) { return kind.equals("square") ? new Square() : new Circle(); }` — callers only ever write `Shape s = make("square");`.

### UML class diagram
**Like you're 5:** A family-tree picture, but for code. Each box is a class, showing its name, what it knows and what it can do. Lines between the boxes show who belongs to whom, and who is a kind of whom.

**The real words:** The standard drawing of classes (name / fields / methods, three stacked parts) and their relationships, such as association and inheritance (a hollow triangle); COMP5911M's Exercise 1 asks for one of a car-rental app, redrawn in diagrams.net. → [Java lane: MOOC.fi Java Programming I](https://java-programming.mooc.fi/part-1/1-starting-programming)

**See it:** `C:\Users\samra\OneDrive\dev\life\uni\UNI.md` line 53 — Exercise 1 "Creating Diagrams" (Customer, Rental, Car): what to draw and where to save it.

## KRR (COMP5450M)

### Proposition
**Like you're 5:** A sentence that is either true or false, like "it is raining". Not a question and not an order, just a claim you could check. "Is it raining?" isn't one; "it is raining" is.

**The real words:** A declarative statement with a truth value; propositional logic joins them with ¬ (not), ∧ (and), ∨ (or) and → (implies), and formative A on Gradescope is propositional. → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** P = "it is raining", Q = "the ground is wet": `P → Q` is false only when P is true and Q is false; in Prover9 it is written `raining -> wet.`

### Predicate
**Like you're 5:** A sentence with a gap in it, like "___ is a cat". Put "Tom" in the gap and it becomes true; put "a teapot" in and it's false. Whatever fills the gap decides.

**The real words:** A property or relation that becomes true or false once its arguments are filled: `cat(tom)`, `parent(ann, bob)`. → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** in Prolog, the fact `cat(tom).` then the queries `?- cat(tom).` → `true.` and `?- cat(teapot).` → `false.`

### First-order logic (FOL)
**Like you're 5:** Grown-up logic that can talk about things and groups of things. Not just "it is raining", but "every cat has whiskers" and "some dog is brown". It has words for "every" and "some", and gaps you fill with things.

**The real words:** Logic with constants, variables, predicates, functions and the quantifiers ∀ and ∃, expressive enough to translate English sentences ("English→FOL" in the skills list); formative B is first-order. → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** "every cat has whiskers" → `∀x (Cat(x) → HasWhiskers(x))`; in Prover9, `all x (cat(x) -> whiskers(x)).`

### Quantifiers (for all, there exists)
**Like you're 5:** Two magic words. "Every" means the rule holds for each thing, no exceptions. "Some" means at least one thing exists that fits. "Every child likes cake" and "some child likes cake" say very different things.

**The real words:** ∀x ("for all x") and ∃x ("there exists an x"); their order matters: ∀x∃y Loves(x, y) ("everyone loves someone") ≠ ∃y∀x Loves(x, y) ("someone is loved by everyone"). → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** Prover9 writes them `all x` and `exists x`: `exists x (dog(x) & brown(x)).` for "some dog is brown" but `all x (dog(x) -> brown(x)).` for "every dog is brown" — swapping `&` and `->` is the classic slip.

### Knowledge base
**Like you're 5:** A notebook of everything you know for sure: "Tom is a cat", "every cat is an animal". You can ask the notebook questions, and it works out answers you never wrote down, like "Tom is an animal".

**The real words:** A set of facts and rules in a formal language from which a reasoner derives new conclusions; the skills list asks for a "Prolog knowledge base". → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** in Prolog, `cat(tom).` and `animal(X) :- cat(X).` then `?- animal(tom).` → `true.` — never stated, worked out.

### Prolog fact, rule and query
**Like you're 5:** A fact is something you just say is true: "Ann is Bob's mum". A rule says how to work new things out: "your mum's mum is your grandma". A query is a question you ask, and Prolog hunts for the answer.

**The real words:** Fact: `parent(ann, bob).` · Rule: head `:-` body, true when the body is: `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).` · Query: `?- goal.`, which Prolog searches to make true. → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** `parent(ann, bob).` `parent(bob, carl).` plus the grandparent rule above, then `?- grandparent(ann, Who).` → `Who = carl.`

### Unification
**Like you're 5:** Matching two jigsaw pieces that both have blanks. "Tom likes ___" and "___ likes fish" fit together if the first blank is fish and the second is Tom. Unification finds the fillings that make two patterns exactly the same.

**The real words:** Finding a substitution for the variables that makes two terms identical (`likes(tom, X)` and `likes(Y, fish)` give X = fish, Y = tom); Prolog's matching step, and the heart of resolution. → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** type `?- likes(tom, X) = likes(Y, fish).` → `X = fish, Y = tom.`

### Backtracking
**Like you're 5:** Walking through a maze: at each fork you pick a path. Hit a dead end? Walk back to the last fork and try the next path. Keep going until you find the way out, or you've tried every path there is.

**The real words:** When a goal fails, or you ask for another answer, Prolog undoes its most recent choice and tries the next matching clause; typing `;` after an answer asks for the next one. → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** `colour(red).` `colour(green).` `colour(blue).` then `?- colour(C).` → `C = red`; press `;` → `C = green`; `;` again → `C = blue.`

### Resolution proof
**Like you're 5:** To prove something, pretend it's false and show that leads to nonsense. "The cake is gone, only you were here, and you say you didn't eat it" can't all be true at once, so you ate it.

**The real words:** Proof by refutation: add the negated goal to the clauses, repeatedly resolve pairs holding a literal and its negation, and deriving the empty clause proves the goal; the skills list wants one "on paper". → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** clauses `¬Cat(x) ∨ Animal(x)`, `Cat(tom)`, and the negated goal `¬Animal(tom)`: resolve the first two → `Animal(tom)`; resolve that with the third → the empty clause □, so `Animal(tom)` is proved.

### Prover9
**Like you're 5:** A robot that does proofs for you. You write down what you know and what you want to prove, in its special writing. The robot hunts for a proof, and either finds one or gives up.

**The real words:** An automated theorem prover for first-order logic; COMP5450M's formatives A/B/C are Prover9 template files you fill and submit on Gradescope, and CW1 includes a Prover9 task like them. → [KRR lane: Learn Prolog Now](https://lpn.swi-prolog.org/)

**See it:** the smallest input: `formulas(assumptions). cat(tom). all x (cat(x) -> animal(x)). end_of_list.` then `formulas(goals). animal(tom). end_of_list.`

## Data Science (COMP5122M)

### Clean, join, chart, findings
**Like you're 5:** Making a fruit salad. Wash the fruit and throw out the bad bits (clean), tip the bowls together (join), lay it out so people can see what's in it (chart), then say what you made (findings). Skip the washing and the whole salad is spoiled.

**The real words:** The pandas pipeline in the skills list, "clean → join → chart → findings": fix missing and wrong values, merge tables on a shared key, plot, then state what the data shows and its limits; COMP5122M's Practical 1 (Titanic, 15 questions) starts at clean. → [Data Science lane: Kaggle Learn Pandas](https://www.kaggle.com/learn/pandas)

**See it:** `df = df.drop_duplicates()` (clean) · `pd.merge(a, b, on="id")` (join) · `df["x"].plot()` (chart) — one line per step; the findings are sentences you write.

### Jupyter notebook
**Like you're 5:** A school workbook where each page has a box for your working and, right under it, the answer the computer worked out. You can redo any box and watch its answer change, and write notes between the boxes.

**The real words:** An `.ipynb` file of cells: code cells you run one at a time, each with its output saved beneath, and Markdown cells for prose; COMP5122M's case studies ship as notebooks, and KRR's Prover9 has a notebook front-end too. → [Data Science lane: Kaggle Learn Pandas](https://www.kaggle.com/learn/pandas)

**See it:** open `https://colab.research.google.com/` (the DS Starters folder lists Colab), start a new notebook, type `1 + 1` in the first cell and press Shift+Enter — the answer appears under the cell.

## Coding tests

### Big-O
**Like you're 5:** How much longer a job takes as the pile grows. Finding your name on a list by reading every line: twice the list, twice the time. Grabbing the top sweet off a pile: the same time, however big the pile.

**The real words:** How an algorithm's time (or memory) grows with the input size n, ignoring constant factors: O(1), O(log n), O(n), O(n log n), O(n²); the first thing an interviewer asks after "does it work?". → [Coding tests lane: HackerRank 3-Month Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit)

**See it:** at n = 1,000: O(1) = 1 step · O(log n) ≈ 10 · O(n) = 1,000 · O(n²) = 1,000,000.

### Array and list
**Like you're 5:** A row of numbered lockers. You can open locker 7 straight away without opening lockers 1 to 6 first. But squeezing a new locker into the middle means shoving all the later ones along.

**The real words:** Elements stored side by side and reached by index in O(1); inserting or deleting in the middle is O(n); Java's `int[]` is fixed-size, while Java's `ArrayList` and Python's `list` grow as needed. → [Coding tests lane: HackerRank 3-Month Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit)

**See it:** `xs = [10, 20, 30]` → `xs[2]` is instant; `xs.insert(0, 5)` has to shift every element one place to the right.

### Hash map
**Like you're 5:** A coat cloakroom. You hand over your coat and get ticket 42. Later you hand back ticket 42, and they go straight to hook 42 without searching every hook. The ticket tells them exactly where to look.

**The real words:** Key → value storage where a hash of the key picks the slot, so lookup, insert and delete are O(1) on average; Python's `dict`, Java's `HashMap`. → [Coding tests lane: HackerRank 3-Month Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit)

**See it:** `ages = {"ann": 30, "bob": 25}` then `ages["bob"]` → `25`, found without scanning through "ann" first.

### Stack and queue
**Like you're 5:** A stack is a pile of plates: you put one on top and take one off the top, so the last one on is the first one off. A queue is the line at the tuck shop: the first to join is the first served.

**The real words:** Stack = last in, first out (the call stack, undo, bracket matching); queue = first in, first out (breadth-first search); in Python, a `list` works as a stack and `collections.deque` as a queue. → [Coding tests lane: HackerRank 3-Month Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit)

**See it:** `s = [1, 2]; s.append(3); s.pop()` → `3`; `from collections import deque; q = deque([1, 2]); q.append(3); q.popleft()` → `1`.

### Recursion (call stack)
**Like you're 5:** Russian dolls. To find the tiniest doll, you open a doll, and inside is a smaller doll, which you open the same way, until one won't open. Then you close them back up, one by one, in reverse order.

**The real words:** A function that calls itself on a smaller input until a base case stops it; each waiting call sits on the call stack, so a missing base case ends in Python's `RecursionError`. → [Coding tests lane: HackerRank 3-Month Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit)

**See it:** `def depth(n): return 0 if n == 0 else 1 + depth(n - 1)` — `depth(3)` stacks up depth(3) → depth(2) → depth(1) → depth(0), then unwinds to 3; `depth(-1)` never reaches the base case.

### Two pointers
**Like you're 5:** Two friends start at opposite ends of a row of sweets sorted smallest to biggest, looking for two that add up to a number. Too big? The right friend steps in. Too small? The left friend steps in. They meet having checked each sweet only once.

**The real words:** Two indices moving through a (usually sorted) array, from both ends or one fast and one slow, to do in O(n) what nested loops do in O(n²). → [Coding tests lane: HackerRank 3-Month Preparation Kit](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit)

**See it:** `[1, 3, 4, 6, 9]`, target 12: 1 + 9 = 10 is too small, so the left pointer moves; 3 + 9 = 12, found in two steps.

## Writing (COMP5530M)

### LaTeX
**Like you're 5:** Instead of dragging words around a page, you write a recipe: "this is the title", "this is a heading", "put a list here". A machine follows the recipe and lays the page out neatly, the same way every time.

**The real words:** A typesetting language: plain-text source with commands (`\section{...}`, `\cite{...}`) compiled into a PDF; the Group Project uses the ACM "Bread" template, and the skills list wants one LaTeX report. → [Group Project lane: START-HERE.md](../START-HERE.md)

**See it:** the two-line document, saved as `hello.tex`: `\documentclass{article}` on line 1 and `\begin{document} Hello, Leeds. \end{document}` on line 2.

### tectonic
**Like you're 5:** The machine that reads your page recipe and bakes the finished page. You give it one file; it fetches anything else it needs by itself, and hands you back a PDF.

**The real words:** A self-contained LaTeX engine that downloads the packages a document needs on first use and compiles `.tex` to PDF in one command; it is installed on this machine (UNI.md §3). → [Group Project lane: START-HERE.md](../START-HERE.md)

**See it:** in PowerShell, `cd $env:TEMP`, save the two lines from the LaTeX entry above as `hello.tex`, then `tectonic hello.tex` → `hello.pdf` beside it.
