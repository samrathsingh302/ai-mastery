---
name: apply-draft
description: Draft a graduate application for one employer from the tracked target list — CV variant, application answers and (only if asked for) a cover letter, all traced to FACTS.md. Use when Samrath types /apply-draft <id>, says "draft an application for <employer>", "prepare my <employer> application", "do the Palantir application", or asks to get an application ready to submit.
---

# apply-draft — draft one application, end to end

Scaffold: `C:\Users\samra\repos\ai-mastery\career\` (`apply.py`, `targets.json`,
`drafts/`). Fact base and master CV: `C:\Users\samra\OneDrive\dev\repos\ai-mastery\career\`.

**The rule that governs everything here: SUBMISSION IS ALWAYS SAMRATH'S.** Never
submit a form, never log into an employer site, never send an email. This skill
ends with drafted files and a list of human steps.

## Procedure

1. **Resolve the id.** `python career/apply.py list` (add `--limb` to narrow).
   Match what Samrath said to an `id`. If two could match (Amazon has two rows),
   ask which one — do not pick for him.
2. **Create or reuse the draft folder.** If `career/drafts/<id>/` does not exist,
   run `python career/apply.py draft <id>`. If it does exist, reuse it; only pass
   `--force` if Samrath asks for a clean restart (it overwrites `brief.md`).
3. **Fill the JD snapshot.** WebFetch the target's `url` from `targets.json` and
   paste the live JD under `## JD snapshot` in `brief.md`, with the fetch date.
   If `url` is empty or the fetch fails, say so and ask Samrath for the live
   listing URL rather than drafting against a guessed JD. While you are there,
   record the real `opens`/`closes`/`salary` in `targets.json` with `sources`,
   and list the application questions and their word limits under
   `## Application questions`.
4. **Draft.** Follow the brief's own `## Drafting prompt`: read
   `career\FACTS.md`, read `career\CV.md`, then write into the draft folder
   `cv-<id>.md`, `answers-<id>.md`, and `cover-<id>.md` only if the scheme asks
   for a cover letter. Record the filenames in `tracking.json`'s `files` array.
5. **Anti-fabrication (hard rule).** Every claim in every file must trace to a
   line in FACTS.md. Nothing new: no invented metrics, no invented dates, no
   invented employers, nothing from the FACTS.md do-not-claim list (§0 — no
   "co-founder", no 2028 graduation, no unearned certs, no "150+ members access
   the portal", no unaided authorship of AI-built code). If the JD asks for
   something FACTS.md does not evidence, do **not** invent it: write it under
   `## Gaps — Samrath decides` in `answers-<id>.md`, one line per gap, with what
   would close it.
6. **No AI tells.** British English, dd/mm/yyyy, no em-dashes. Banned:
   delve, leverage, tapestry, testament, seamless, robust, passionate about,
   in today's fast-paced world, "I am excited to", triads of adjectives.
   Answers go at or under the stated word limit; print the word count after each.
7. **Mark it.** `python career/apply.py status <id> draft-ready --note "<what was drafted>"`.

## Ending

Finish by printing the exact human steps left, in order:

1. Open `<url>` and start the application.
2. Export `cv-<id>.md` to `cv-<id>.pdf` and upload it.
3. Paste each answer from `answers-<id>.md` (and `cover-<id>.md` if present).
4. Resolve anything under `## Gaps — Samrath decides` before submitting.
5. Submit.
6. Run `python career/apply.py status <id> submitted --note "submitted dd/mm/yyyy"`.
