# Red-team findings — AI Mastery Plan v3 (step 0, 04/08/2026, overnight factory)

Scope per MISSION.md: ordering · gaps · redundancy · hour-estimates · cyber light-interleave
placement. Source reviewed: `PLAN-v3-notion-export.md` (Notion page unedited — every item below
is either ABSORBED into PLAN-MASTER/module design tonight, or flagged as a MORNING DECISION for
Samrath). Verdict up front: **the plan is sound — 0 critical findings.** 4 medium, 5 low,
3 informational. The fast-track order survives adversarial review intact; the real work was
dedupe rules, missing operational pieces, and placing the cyber interleave.

## Medium

**M1 · HOURS · Video canon booked at ~4h; the canon is ~5.5–6.5h at 1× speed.**
Karpathy "Deep Dive into LLMs like ChatGPT" alone is **3h31m** — verified 04/08/2026 against
Karpathy's own announcement (x.com/karpathy/status/1887211193099825254). The ~4h total only
works at 1.5–2× playback. Absorbed: PLAN-MASTER books 4–6h; module 01 will state per-video
runtimes and a playback strategy. Morning decision (optional): correct the Notion table cell.

**M2 · REDUNDANCY · Fast track double-counts against the tiers it extracts from.**
Deep Dive (item 1) + 3B1B (item 11) reappear in Tier 3's intuition stack; Kaggle Python/pandas
(item 7) in Tier D; HTTP-by-hand (item 8) in Tier W; the 10-task harness (item 9) vs Tier 3's
20-task; Gandalf/OWASP-LLM (item 10) vs C2. Not a design error (the fast track is deliberately
extracts) but Part 6's tier totals count those hours twice, and a naive continuation would
rebuild them. Absorbed: PLAN-MASTER law 3 (dedupe) + steps 17–28 framed as REMAINDERS.
Morning decision (optional): footnote the Notion totals.

**M3 · GAP · "Zero decisions to start" rests on two artefacts that don't exist yet.**
The plan's own start instruction is "open START-HERE or type /study-session" — no START-HERE.md
exists in this repo and no study-session skill is installed (checked the live skill list,
04/08/2026). Absorbed: step 2 builds START-HERE as an operational file + ships a draft
/study-session skill inside the module. Morning decision: install the skill globally
(MANUAL-TASKS item 107 — global-estate change, his call).

**M4 · CYBER PLACEMENT · A "light interleave" must not carry a paid dependency.**
The natural interleave source is Tier C1, whose spine is TryHackMe (≈£10/mo). Wiring THM into
the interleave would make the secondary track the only paid-gated part of the fast-track months.
Absorbed: interleaves 13–16 are built free-first (OverTheWire Bandit, monk-mode's real MAC
scheme, PortSwigger free labs + DVWA, HackAPrompt/Willison corpus); THM rooms are marked
optional inside them. Morning decision: THM subscription GO/no-go = MANUAL-TASKS item 106.

## Low

**L1 · ORDERING · Git (step 5) lands after ~55h of CS50P+ATBS — psets go uncommitted.**
Recommendation (not a reorder — order is law): module 03 opens with a 30-minute "git survival
minimum" sidebar (init/add/commit/push, nothing else) so work is versioned from day one; step 5
stays the real Git module. Absorbed into module 03 design.

**L2 · GAP · No environment checkpoint before local work.** CS50P runs in cs50.dev's cloud
VS Code, but ATBS and every project/ need a working local Python. Absorbed: module 02 gets a
15-minute toolchain checklist (verify python/pip/venv, VS Code, git identity) against HIS
Windows 11 machine.

**L3 · GAP · Debugger-first practice only arrives in Tier 1's remainder.** The fast track's
bug-hunts risk cementing print-debugging for ~150h. Absorbed: modules 03/04 exercises include
"hunt with the VS Code debugger" sidebars; the full deliberate-practice item stays in step 17.

**L4 · GAP · The fast-track exit test has no owner.** "Cold 30-minute interview sim" is defined
but no item builds it. Absorbed: module 12 ships the sim script + grading rubric alongside the
AI-free build spec.

**L5 · MONEY · Paid items are scattered and unlabelled as decisions** (THM £10/mo, Géron ≈£45,
VPS ≈£4/mo, Chip Huyen ≈£40, Mom Test ≈£15, certs). All are ◇ or have free fallbacks; none
blocks the free path through step 16. Absorbed: `[PAID-decision]` tags in PLAN-MASTER; first
live one (THM) is ledger item 106.

## Informational

**I1 · ORDERING · The numbered ladder is not a queue.** The plan itself schedules items 1/11 as
B-lane and 10 as D-lane from week one (Part 6b). PLAN-MASTER law 4 carries the lane quick-card
so the ladder can't be misread as strictly serial study.

**I2 · HOURS · Fast-track table sums to ~137h** vs the stated "≈140–150h" — consistent. ✓

**I3 · FACT DISCIPLINE · Community-evidence claims (652-pt thread, 105-pt comment, etc.) are
carried provenance from the 06/07/2026 sweeps**, not re-verified tonight. Modules re-verify any
resource fact they themselves assert (MISSION research-first law); tonight's one load-bearing
verification was M1.

### M1-ADDENDUM (04/08/2026, module 01 research — supersedes M1's totals)

Full canon verified per-video: Fireship mind-virus **4:46** · Fireship not-suck **~5:47** (plan
said 16m — wrong) · Karpathy **3:31:00** (plan said 2h — wrong) · Ebbelaar **19:29** (plan said
~1h — wrong; real title "How I'd Learn AI Engineering in 2026 (Complete Roadmap)", 29/10/2025) ·
Tech With Tim: the plan's title **doesn't exist** — real nearest is **"Learning to code has
changed"** (02/02/2026, 13:19), which argues exactly the intended thesis. Net: canon ≈ **4h14m**
at 1× — the plan's ~4h TOTAL was roughly right, but three of five line items were wrong, in both
directions. Morning Notion edits (optional): the three runtime cells + the TWT title swap.

## Cyber interleave placement (the required step-0 output)

| Interleave | Hook — study after | Why this hook |
|-----------|--------------------|---------------|
| 13 shell + Bandit | step 5 (Git) | Terminal comfort just peaked; Bandit turns the shell into a game |
| 14 crypto via monk-mode | step 6 (archaeology) | He has just read monk-mode's REAL MAC scheme — teach hashing/MACs on his own code |
| 15 web-sec first contact | step 8 (how the web works) | HTTP/auth fresh in hand; OWASP Top 10 lands as "attacks on what you just learned" |
| 16 AI-sec continuation | step 10 (AI-security taster) | Direct continuation of the taster into the moat (C2) |

All four are marked SECONDARY, D-lane, free-first. Full C1/C2 modules (27/28) later build on
them under the dedupe law. AI order untouched throughout.

## Morning decisions for Samrath (batched — also in MANUAL-TASKS 105–107)

1. Install Anki + (optional) AnkiWeb account — unblocks the module-02 ritual (item 105).
2. THM subscription ≈£10/mo GO/no-go — upgrades interleaves 13/15 and Tier C1; free path exists
   regardless (item 106).
3. Install the /study-session skill from module 02's draft into ~/.claude — global-estate
   change (item 107).
4. Optional Notion edits: M1 hours cell, M2 totals footnote, L1 git sidebar note. The page was
   NOT touched tonight, per MISSION.
