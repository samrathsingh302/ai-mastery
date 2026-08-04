# Project 01 — The Barbell Audit v0 (your baseline outage score)

**What:** apply the canon's worldview to YOUR actual setup, and produce the baseline number the
plan's weekly outage test will track forever. ~45–60 min. No code is written or modified —
this is an audit of how you currently use AI. Output: one markdown file,
`project/barbell-audit-v0.md` (in this folder, committed).

**Why this is the right first project:** idea #5 (same tool, opposite outcomes) is comfortable
in the abstract and uncomfortable applied to yourself. The plan's whole strategy is a barbell —
max AI leverage on one side, genuine unassisted fundamentals on the other. Tonight you find out
what your barbell actually looks like before the plan starts moving it.

## Steps

1. **Inventory (15 min).** List every place AI currently touches your work. Prompt your memory
   with your own estate (read-only — just look): `repos\` (monk-mode, psoc-portal, hevy-brain,
   life-os, atlas-pipeline, loop-runner, cv-editor…), the Claude session workflow you run daily
   (orchestrator sessions, skills, subagents, handoffs), uni work, PSOC work. One row each in a
   table: **surface · what AI does there · what YOU do there**.
2. **Classify (15 min).** Add a column with ONE of:
   - **LEVERAGE** — AI does work you *could* do (or verify line-by-line); you'd survive its loss.
   - **CRUTCH** — AI does work you could *not* currently do or verify; its loss strands the thing.
   - **LEARNING-THEFT** — AI does work that, if you did it yourself, would be teaching you the
     exact skills this plan targets.
   Be harsh. "I could probably figure it out" = CRUTCH until proven otherwise.
3. **Score (10 min).** The baseline outage score: *"if Anthropic went down for a week, what % of
   my current productivity survives?"* One honest number, plus the two rows that most drive it
   down.
4. **Pick the first conversion (5 min).** Choose ONE CRUTCH or LEARNING-THEFT row this plan
   should convert to LEVERAGE first, and note which fast-track step does it (e.g. "psoc-portal
   is a crutch → steps 6 + 8 make it mine").
5. **Journal it (5 min).** Three sentences in the file: the score, the biggest surprise, the
   chosen conversion. This entry is your baseline for every future weekly outage test.

## Acceptance checklist

- [ ] Inventory table has ≥8 rows spanning code, uni, and PSOC/life surfaces
- [ ] Every row classified LEVERAGE / CRUTCH / LEARNING-THEFT (no blanks, no "mixed")
- [ ] One outage-score % written down, with the two biggest drivers named
- [ ] One conversion target chosen and mapped to a fast-track step number
- [ ] File committed to this repo (module 05 teaches git properly; for now the survival
      three-liner from TEACH — or ask your tutor session to walk you through the commit, which
      is allowed: operating git ≠ the learning work)
