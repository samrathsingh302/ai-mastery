# Project 06 — Two ARCHITECTURE.md files + the cold explain

**What:** the dig's deliverables — one `ARCHITECTURE-psoc-portal.md` and one
`ARCHITECTURE-monk-mode.md` written HERE (not in those repos — read-only law), plus the
interview rehearsal. ~3h after both digs.

## Each ARCHITECTURE file (≤1 page, from your dig log, repo closed)

1. **One-paragraph claim** — what it is, for whom, in your words.
2. **The map** — directories that matter, one line each.
3. **The slice** — your hop table, from memory first, then verified.
4. **Three design decisions worth defending** — e.g. psoc: server actions re-checking auth ·
   soft deletes · migrations-as-history; monk-mode: fail-closed · four-process split ·
   tamper-evidence-over-confidentiality. For each: the decision, the alternative, why this
   one won HERE.
5. **What would break first** — your honest guess at the weakest point, and what evidence
   (test gap? single point of failure?) makes you say so.

## The cold explain (the exit test rehearsal)

Phone timer, 5 minutes per repo, out loud, nothing open: "Walk me through the project."
Then a tutor-session mock (tutor move #7): it plays interviewer, pushes on YOUR
architecture files ("why soft delete?", "what if the guardian dies too?"), grades harshly.

## Acceptance checklist

- [ ] Both files exist here, fit a page each, and cite file:line for every factual claim
- [ ] Slice tables written from memory first (mark which hops you had to look up)
- [ ] Six design decisions defended (three per repo) with the alternative named
- [ ] Both cold explains done — note where you stalled; stalls become tutor drills
- [ ] Mock interview run, score in the journal; misses → Anki cards
