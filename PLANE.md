# ✈️ PLANE.md — the offline study guide

> Verified working with **no internet**, 10/08/2026, before your flight.
> Read this one file. Don't go hunting through the other thirteen.

**The one thing that does not work offline is me.** No `/study-session`, no Socratic questions,
no harsh grading, no end-of-session quiz. Everything else in this repo was built to teach without
me, and this guide is how you run it alone.

---

# Part 0 — Before you close the lid

Sixty seconds, on the ground, while you still have signal:

- [ ] **Anki is loaded** — 262 cards are already in your collection (see Part 2). Open Anki once
      now and let it settle, so the first launch at 35,000 ft isn't the first launch ever.
- [ ] **Battery** — the Karpathy video is 453 MB of screen-on time and will eat your battery
      faster than anything else here. Plan for it (Part 6).
- [ ] Nothing else. The videos, the deck, and pandas are already on disk.

---

# Part 1 — The rules, now that you have no tutor

The tutor contract still binds you; it just has nobody to enforce it. So enforce it yourself:

1. **The 30-minute wall rule.** Stuck? Set a timer. Struggle for a genuine 30 minutes before you
   open anything labelled `solutions/`. Below 30 minutes you're not stuck, you're uncomfortable.
2. **When you do break, break cheaply.** In order: re-read the TEACH section → check `GLOSSARY.md`
   (182 lines, every term already taught) → read the *worked* answer in `solutions/`, not the code.
3. **Log every miss, don't resolve every miss.** You have no one to ask, so write the question down
   in `journal.md` under a `## For Claude` heading. That list is the first thing we do when you land.
   A flight's worth of good questions is worth more than a flight's worth of guessed answers.
4. **Never paste an answer you don't understand into a file and call it done.** The whole point of
   this ladder is the outage score — what survives when the AI vanishes. Today the AI has vanished.
   This is the real exam.

---

# Part 2 — Anki (do this first, every session)

**262 cards, 13 subdecks, already imported into your "Year 3" profile.** Your 30 existing Default
cards are untouched. Reviewing is 100% offline — only *syncing* needs WiFi, and it'll catch up by
itself when you land.

| Deck | Cards | | Deck | Cards |
|---|---|---|---|---|
| 01 video canon | 30 | | 08 how the web works | 20 |
| 02 tutor setup | 16 | | 09 eval harness mini | 14 |
| 03 cs50p accelerated | 33 | | 10 ai security taster | 20 |
| 04 automate boring stuff | 18 | | 11 nn transformers intuition | 24 |
| 05 git properly | 20 | | 12 first ai free build | 11 |
| 06 repo archaeology | 17 | | 13 cyb shell bandit | 22 |
| 07 data taster hevy | 17 | | | |

### How to actually use it

1. Open Anki → click **AI Mastery**.
2. **Raise the new-card limit for the flight.** This matters: Anki defaults to ~20 new cards a day,
   so on a long flight you'll hit the wall in ten minutes and think you're finished.
   → click the deck → **Custom Study** → *Increase today's new card limit* → set **60**.
   (Do this per subdeck you're working, not globally. Back to 10–20/day once you're home —
   module 02's cap exists for a reason: 60/day sustained will bury you in reviews next week.)
3. **Study only the subdeck matching what you're doing that block.** Reviewing module 07's pandas
   cards while watching Karpathy is interference, not studying.
4. **Grade honestly.** "I sort of knew it" is *Again*. The deck is worthless the moment you flatter
   yourself with it.

**Add your own cards as you go.** Every miss from a `check.py` run becomes a card, written in your
words, immediately — while the sting is fresh. That is the single highest-value thing you can do
on this flight, because it's the one thing that compounds.

---

# Part 3 — The videos (587 MB, local, subtitles embedded)

`modules/01-video-canon/videos/`

| # | File | Runtime | Pairs with |
|---|---|---|---|
| 1 | `1-vibe-coding-mind-virus.mp4` | 4:46 | module 01 TEACH |
| 2 | `2-vibe-coding-not-suck.mp4` | 5:47 | module 01 TEACH |
| 3 | `3-karpathy-deep-dive-llms.mp4` | **3:31:00** | **module 11 TEACH** ← the flight-sized pairing |
| 4 | `4-ai-engineering-roadmap-2026.mp4` | 19:29 | module 01 TEACH |
| 5 | `5-learning-to-code-has-changed.mp4` | 13:19 | module 01 TEACH |

### How to watch them so it isn't television

Passive watching at altitude is how three hours disappear with nothing to show. Instead:

1. Open `modules/11-nn-transformers-intuition/TEACH.md` **beside** the video.
2. Watch in **20–30 minute segments**, not in one sitting.
3. At the end of each segment, **pause and close the video.** Write, from memory, three sentences
   on what that segment claimed. No scrubbing back. If you can't produce three sentences, rewatch
   that segment — that's the signal, and it's the only honest one you have without me.
4. When Karpathy reaches tokenisation, attention, or sampling/temperature, **stop the video** and go
   do the matching by-hand exercise in module 11 (Part 4). Doing the arithmetic immediately after
   seeing it explained is worth roughly triple the same exercise done tomorrow.
5. Anything he says that you can't restate → straight into `journal.md` under `## For Claude`.

Module 01's TEACH already distils all five videos, so if the battery is dying, **read instead of
watch** — you lose very little.

---

# Part 4 — The code modules (machine-graded, fully offline)

Every checker runs offline and grades you honestly. I fixed a crash in all eleven of them today —
they used to die on your *first wrong answer* because of the console's code page, which would have
been a miserable thing to discover mid-Atlantic.

**Run each one from inside its own folder:**

```
cd modules/03-cs50p-accelerated/exercises
python check.py
```

### Which module to pick

| Module | What you actually do | Grading | Good on a plane? |
|---|---|---|---|
| **12 first AI-free build** | Build `studylog` to spec, then the **exit interview sim** | 8-test black-box harness, 7-criterion rubric | ⭐ **Best.** AI-free by rule — my absence costs you nothing |
| **11 nn/transformers** | Forward pass, attention, temperature — **by hand, on paper** | 12 numeric answers, 3 dp | ⭐ **Best.** Pen and paper, pairs with Karpathy |
| **03 CS50P** | 10 rungs, Python from zero | 34 tests | ⭐ Very good — long, self-contained, incremental |
| **04 Automate the Boring Stuff** | 5 missions on your real files | 5 tests, sandboxed to temp dirs | Good — never touches real files |
| **05 git properly** | Build a history playground, break it, fix it | graph-grading checker | Good — all local git |
| **07 data taster (Hevy)** | pandas on your own 305 workouts | 9 tests | Good — venv pre-installed |

**Module 07 has one wrinkle**, by design: pandas lives in a venv, so plain `python` won't see it.

```
cd modules/07-data-taster-hevy/exercises
../.venv/Scripts/python.exe check.py
```

That is the venv lesson working correctly, not a fault.

### The method for any module

1. Read the TEACH section for **one** rung/mission only. Not the whole file.
2. Close it. Write the exercise from memory of the *idea*, not the *example*.
3. Run `check.py`. Read the failure message properly — these checkers explain, they don't just fail.
4. Fix it yourself. Timer on. Thirty minutes before `solutions/`.
5. Every miss → an Anki card, in your words, now.
6. Move to the next rung. Do not read ahead.

`solutions/` exists for modules 01–11 and 14. Modules 12 and 13 deliberately have none — 12 is the
AI-free build and 13 is the shell gym, and both are spoiled by a solution.

---

# Part 5 — The 12 interactives

Double-click any of them; they open in your browser with no server and no network. I checked every
one today: zero `fetch()`, zero CDN links, nothing that breaks under `file://`.

```
modules/*/interactive/*.html
```

The three worth your tray table:

- **`11-nn-transformers-intuition/interactive/attention-lab.html`** — drag a key vector and watch the
  softmax weights move; toggle the causal mask; turn the temperature dial. Do this *right after* the
  by-hand attention exercise and the arithmetic stops being arithmetic.
- **`06-repo-archaeology/interactive/trace-the-request.html`** — predict-then-step through a real
  request in your own psoc-portal. Predicting before stepping is the whole exercise; peeking makes
  it a slideshow.
- **`02-tutor-setup/interactive/study-cockpit.html`** — runs your timed dojo and tracks the streak.
  Use it to enforce the 20-minute blocks below.

---

# Part 6 — The flight plan

Battery is your real constraint, and video is the hog. So: **code while the battery is high, video
when you're plugged in or when the battery is dying and you can dim the screen right down.**

### Short flight (2–3 hours)

| Block | What |
|---|---|
| 0:00–0:10 | Fill the **baseline block** in `journal.md`. It's still empty — this is genuinely day one. |
| 0:10–0:30 | Anki: module 01 + 02 decks, new limit 60. |
| 0:30–1:40 | **Module 03 CS50P**, rungs 1–3. TEACH one rung → exercise → `check.py` → cards. |
| 1:40–2:00 | Videos 1, 2 and 5 (24 min total, the short ones). |
| 2:00–2:15 | Closing ritual (Part 7). |

### Long flight (8+ hours)

| Block | What |
|---|---|
| 0:00–0:15 | `journal.md` baseline. Then Anki, new limit 60, decks 01–02. |
| 0:15–1:15 | **Module 11 TEACH, Part A** (neurons → loss → gradient descent → backprop) + the forward-pass exercise by hand. |
| 1:15–1:30 | Break. Screen off. Actually off. |
| 1:30–3:00 | **Karpathy**, first segment, three-sentences-from-memory after each 20–30 min chunk. |
| 3:00–4:00 | **Module 11 Part B** + the attention exercise by hand, then `attention-lab.html`. |
| 4:00–4:20 | Anki: module 11 deck (24 cards) — you'll now actually know these. |
| 4:20–5:30 | Karpathy, second segment, same rules. |
| 5:30–7:00 | **Module 12** — read the spec and rubric, score yourself *before* any AI contact, start the AI-free build. |
| 7:00–7:30 | **The exit interview sim** — 6 questions, cold, no notes. 9+/12 to proceed. |
| 7:30–8:00 | Closing ritual, then sleep. |

Swap module 03 in for 11/12 at any point if you'd rather build fluency than intuition. Never run
two heavy-code lanes back to back — that's the plan's own rule and it's right.

---

# Part 7 — The closing ritual (you run it, since I can't)

Do this before you shut the laptop, every single session. It is the part that compounds.

1. **The quiz.** I normally ask five cold questions. Instead: close every file, open `journal.md`,
   and write five questions *you'd* ask someone claiming to have learned what you just learned.
   Then answer them. The ones you can't answer are the real output of the flight.
2. **The cards.** Every miss from step 1 and from every `check.py` → Anki, in your own words.
3. **The journal line:**
   ```
   dd/mm — module NN · what you learned in ≤10 words · struggle: what+mins · AI-free? Y/N · misses→cards: N
   ```
4. **Commit** (works offline, no network needed):
   ```
   git add -A
   git commit -m "study: <what you did>"
   ```

---

# Part 8 — When you land

- [ ] `git push` from `repos/ai-mastery`
- [ ] Open Anki once on WiFi — it syncs itself
- [ ] Bring me the `## For Claude` list from `journal.md`. That's our first session back.

---

## Known gaps, stated honestly

| Not available offline | Why |
|---|---|
| `/study-session`, tutoring, harsh grading | Needs my API |
| Module 13 Bandit levels | SSH to overthewire.org |
| Module 10 Gandalf | Web game |
| Module 09 live eval run | Needs the `claude` CLI — its `--dry-run` fixtures do work offline |
| `git push` | Commit freely; push on landing |
| Module 14 (crypto/monk-mode) drills | Module is WIP — TEACH and 2 exercises exist, no drills deck yet |

Everything else in this repo works at 35,000 ft.
