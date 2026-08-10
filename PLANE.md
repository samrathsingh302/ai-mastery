# ✈️ PLANE.md — the offline study kit

> Everything below runs with **no internet**. Verified 10/08/2026 before your flight.
> The one thing that does NOT work offline is **Claude** — so no tutoring, no grading,
> no end-of-session quiz from me. Every checker in here grades you instead.

---

## Start here (first 45 min, zero decisions)

1. **Fill the baseline** in `journal.md` — the block is still empty, so this is genuinely day one.
2. Read `modules/02-tutor-setup/tutor-contract.md` once. Out loud.
3. Open the cockpit and run a 20-minute dojo:
   `modules/02-tutor-setup/interactive/study-cockpit.html` (double-click it — no server needed)
4. Then pick a lane below.

---

## Lane A — the videos (now local, 587 MB, subtitles burned in)

`modules/01-video-canon/videos/`

| # | File | Runtime |
|---|------|---------|
| 1 | `1-vibe-coding-mind-virus.mp4` | 4:46 |
| 2 | `2-vibe-coding-not-suck.mp4` | 5:47 |
| 3 | `3-karpathy-deep-dive-llms.mp4` | **3:31:00** ← the flight-sized one |
| 4 | `4-ai-engineering-roadmap-2026.mp4` | 19:29 |
| 5 | `5-learning-to-code-has-changed.mp4` | 13:19 |

Karpathy pairs with `modules/11-nn-transformers-intuition/TEACH.md` — watch a section, then do
that module's by-hand attention arithmetic. That combination is the single best use of a long flight.

---

## Lane B — code, graded by machine

Every checker works offline. Run from inside its own folder:

```
cd modules/03-cs50p-accelerated/exercises && python check.py
```

| Module | What you do | Checker |
|---|---|---|
| 03 CS50P | 10 rungs, Python from zero | 34 tests |
| 04 Automate the Boring Stuff | 5 missions on your real files (sandboxed) | 5 tests |
| 11 Neural nets / transformers | forward pass + attention **by hand, on paper** | 12 numeric answers |
| 12 First AI-free build | the studylog build + **exit interview sim** | 8-test black-box harness |

**Module 12 is the one designed for exactly this** — it is AI-free by rule, so my absence costs you nothing.

Module 07 (pandas on your Hevy data) also works — its venv is pre-installed. Run it with:
```
cd modules/07-data-taster-hevy/exercises && ../.venv/Scripts/python.exe check.py
```
(the plain `python` won't see pandas — that's the venv lesson, working as designed)

---

## Lane C — the 12 interactives

Double-click any of them. All self-contained, no CDN, no network:

```
modules/*/interactive/*.html
```

Best two with a seat-back tray: `attention-lab.html` (drag the key vectors, watch softmax move)
and `trace-the-request.html` (walk your own psoc-portal request, predict-then-step).

---

## Anki

Installed, profile **"Year 3"**. Reviews work fully offline — only *syncing* needs WiFi, and it
syncs on its own when you land. Clear the queue first thing, as the daily loop says.

---

## What is NOT available up there

| Blocked | Why |
|---|---|
| `/study-session`, tutoring, harsh grading | Needs my API |
| Module 13 Bandit levels | SSH to overthewire.org |
| Module 10 Gandalf | Web game |
| Module 09 live eval run | Needs the `claude` CLI — but its `--dry-run` fixtures work offline |
| `git push` | Commit freely; push when you land |

---

## The end-of-flight ritual (do it yourself, since I can't)

1. One line in `journal.md` — `dd/mm — module NN · what you learned · struggle: what+mins · AI-free? Y/N · misses→cards: N`
2. Write your misses straight into Anki as cards while they still sting.
3. `git add -A && git commit -m "study: <what you did>"` — push after landing.
