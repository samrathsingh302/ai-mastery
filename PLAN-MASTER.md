# PLAN-MASTER — the numbered master order the module factory follows

> Provenance: produced 04/08/2026 by step 0 (red-team) of MISSION.md, from `PLAN-v3-notion-export.md`
> (Notion page `3b104e06-5e70-8193-8ae7-fc35a5c28b64` stays canonical and UNEDITED — Samrath decides
> plan edits in the morning from `reports/red-team-findings.md`). This file is the loop's law for
> what gets built and in what order.

## Laws

1. **Fast track order is untouched** (Samrath 04/08/2026): steps 1–12 below are exactly
   PROGRESS.md's steps 1–12. Findings about their internal ordering are recommendations in the
   findings report, absorbed as sidebars inside modules — never reorders.
2. **Cyber = light interleave** (Samrath 04/08/2026): four SECONDARY modules (13–16), each
   clearly marked secondary, each hooked after a related core step. The AI order is untouched;
   the hooks tell Samrath *when* to study them (D-lane); the numbers are the *build* order.
3. **Dedupe law**: anything done in the fast track is NOT rebuilt in its parent tier — post-12
   modules cover the REMAINDER only (the fast track is extracts of Tiers 1/2/D/W/3/C2; Part 6's
   tier totals double-count those hours).
4. **Build order ≠ study gating**: Samrath studies in Part 6b's lanes (A build · B theory ·
   C micro-daily · D variety). Quick card: items 1 and 11 are B-lane from week one; 10 and the
   cyber interleaves are D-lane; everything else queues through A. Dojo 20m + Anki 10m daily.
5. **Free-first**: every step must be startable with £0. Paid components are marked
   `[PAID-decision]` and have a free fallback wired in; the decision lives in MANUAL-TASKS
   (items 105–107 as of tonight).
6. **Module contract** (MISSION.md): each step ships `modules/NN-<slug>/` with TEACH.md
   (baby rule, 80/20 first, checkpoints), exercises/ with self-checks + spoiler-safe solutions,
   project/ against HIS real estate, interactive/ HTML, drills.md (Anki-importable), sources
   cited. GLOSSARY.md at repo root is cumulative.

## The ladder

### Fast track (fixed — PROGRESS.md steps 1–12)

| # | Module dir | Content | Hours (corrected) |
|---|-----------|---------|-------------------|
| 1 | `modules/01-video-canon` | Companion notes that make the canon optional: Fireship ×2 · Karpathy "Deep Dive into LLMs" (**3h31m**, verified) · Ebbelaar 2026 roadmap · Tech With Tim skim | 4–6h (plan said ~4h; true at 1.5–2× only) |
| 2 | `modules/02-tutor-setup` | START-HERE ritual (operational file, not description) · tutor contract card · Anki install + first deck · dojo protocol · **toolchain checklist** (Python/VS Code/git verify — gap G2 absorbed) | ~3h |
| 3 | `modules/03-cs50p-accelerated` | Python from zero, psets-first; baby-rule ladder; rescue notes per topic; **git survival minimum sidebar** (finding O1) | ~40h |
| 4 | `modules/04-automate-boring-stuff` | 5 ATBS chapters applied to HIS files/vault; debugger-not-print sidebar (gap G3) | ~15h |
| 5 | `modules/05-git-properly` | learngitbranching path → narrate his own repos' workflow | ~8h |
| 6 | `modules/06-repo-archaeology` | Guided walkthroughs ×2: psoc-portal + monk-mode | ~16h |
| 7 | `modules/07-data-taster-hevy` | Kaggle Learn Python+pandas equivalents taught directly, applied to HIS Hevy data | ~10h |
| 8 | `modules/08-how-the-web-works` | HTTP by hand against HIS live site · DNS/TLS trace · auth in one sitting | ~12h |
| 9 | `modules/09-eval-harness-mini` | 10 tasks × 2 models, blind-graded table | ~8h |
| 10 | `modules/10-ai-security-taster` | Gandalf · OWASP LLM Top 10 · threat-model his own agent stack | ~8h |
| 11 | `modules/11-nn-transformers-intuition` | 3B1B NN + transformer chapters companion · bbycroft.net/llm | ~5h |
| 12 | `modules/12-first-ai-free-build` | Spec + rubric + grading script for the AI-free CLI build **+ the fast-track exit interview sim** (gap G4 absorbed) | ~8h |

### Cyber light interleave (SECONDARY — built 13–16, studied at their hooks, D-lane)

| # | Module dir | Hook (study after) | Content | Hours |
|---|-----------|--------------------|---------|-------|
| 13 | `modules/13-cyb-shell-bandit` | step 5 | Shell/Linux survival + OverTheWire Bandit (free). THM Linux rooms `[PAID-decision: ledger 106]` optional | ~6h |
| 14 | `modules/14-cyb-crypto-monkmode` | step 6 | Hashing · MACs · signatures in plain words, via monk-mode's REAL MAC scheme | ~4h |
| 15 | `modules/15-cyb-websec-first-contact` | step 8 | OWASP Top 10 · first PortSwigger free labs · DVWA local · psoc-portal as thought-exercise | ~6h |
| 16 | `modules/16-cyb-aisec-continuation` | step 10 | HackAPrompt · Willison's prompt-injection corpus · PortSwigger LLM labs · follow Embrace the Red | ~5h |

### Continuation (Part-6 order, REMAINDERS only — dedupe law applies)

| # | Module dir | Content (remainder after fast track) |
|---|-----------|--------------------------------------|
| 17 | `modules/17-tier1-remainder` | Exercism drills · SQL (SQLBolt + his Supabase schema) · testing literacy · debugging-as-a-skill (the full deliberate-practice item) |
| 18 | `modules/18-tier2-remainder` | Repo archaeology ×4 more · three-pass paper method on "Attention Is All You Need" · read-the-audit exercises |
| 19 | `modules/19-tierD-remainder` | Kaggle viz + intro-ML · stats JIT ladder (10 ideas) · Hevy deep analysis (dissertation-metrics rehab stays ◇ deprioritised) |
| 20 | `modules/20-tierW-core` | MDN selective · auth properly · stack-de-black-box · Ebbelaar production layer (FastAPI/Docker/Postgres/observability) · capstone spec |
| 21 | `modules/21-tier3-classical-ml` | Géron chs 1–9 `[PAID-decision ≈£45]` (free fallback: Ng audit + scikit-learn docs path) |
| 22 | `modules/22-tier3-zero-to-hero-1` | micrograd → makemore (MANDATORY AI-free) |
| 23 | `modules/23-tier3-zero-to-hero-2` | GPT build + PyTorch properly (blitz → idiomatic rebuild on real data) |
| 24 | `modules/24-tier3-evals-full` | Extend step-9 harness to 20 tasks · DeepLearning.AI short courses ×4 |
| 25 | `modules/25-tierSE` | Ousterhout · refactoring on own repos · patterns JIT · CI/CD + Docker · Google code-review guide · cloud literacy + one bare-VPS deploy `[PAID-decision ≈£4/mo]` |
| 26 | `modules/26-tier4-first-five` | Anthropic Academy → starter template → agent-with-evals → MCP server → RAG-with-evals |
| 27 | `modules/27-tierC1-full` | THM Pre-Security/Network/Linux `[PAID-decision: ledger 106]` · DVWA properly · full threat model (builds on 13/15) |
| 28 | `modules/28-tierC2-full` | The moat, completed: full AI-security incl. the atlas-pipeline ingestion security review artifact (builds on 10/16) |
| 29 | `modules/29-breadth-pack-1` | Survey level: computers bottom-up · OS & shell · databases · networks |
| 30 | `modules/30-breadth-pack-2` | Survey level: cloud · internet economy · mobile · AI landscape |
| 31 | `modules/31-tier6-systems` | Missing Semester → System Design Primer → Alex Xu vol.1 → Chip Huyen `[PAID-decision ≈£40]` → NeetCode when interviews near |
| 32 | `modules/32-tier7-money` | Portfolio · Mom Test `[PAID-decision ≈£15]` · one real client automation · networking/hackathon habit |

Beyond 32 (not module work — standing ◇ decisions Samrath takes with real information): n8n +
certs as breaks · Tier C3 full PortSwigger path · the C4 committed-pivot ladder.

## Tonight's reach

Hard cap 16 iterations (MISSION budget guard): step 0 + steps 1–12 + at most 13–15. `carry-on`
in the closing handoff points at the first unbuilt step.
