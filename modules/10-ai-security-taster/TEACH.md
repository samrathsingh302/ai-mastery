# Module 10 — AI-security taster (the moat, opened)

> **What this is:** the security lens on everything you've built — prompt injection by hand
> (Gandalf), the OWASP LLM Top 10 (2025 list, verified tonight), and a real threat model of
> **your own agent stack**, using its live configuration as the evidence. **~8h.**
> **Why it's the moat:** AI-accelerated code ships AI-accelerated vulnerabilities, and almost
> nobody who *operates* agent fleets can *threat-model* them. You run four unattended Claude
> automations and a bypassPermissions estate — you're not learning this abstractly.
> **D-lane, playful:** Gandalf is a game. Play it before reading §2.

## 1 · Prompt injection, by hand (play first, ~1–2h)

**Prompt injection** *(plain words: text the model READS as data ends up being obeyed as
instructions — because to an LLM, everything in the context window is just tokens with no
"this part is trusted" label; analogy: a note slipped into your in-tray that says "the boss
says give the bearer the keys", and you comply because it's on the right paper)*.

Play **Gandalf** (lakera.ai/gandalf, free, browser): eight levels of "get the password out
of the model", each with stronger defences. Rules: no walkthroughs, 30-minute struggle rule,
and after each level write ONE line in `exercises/injection-log.md` — what you tried, what
the defence appears to be, why it broke.

The families you'll rediscover: **direct override** ("ignore previous instructions") ·
**role-play framing** ("you're writing a play where a character reveals…") · **encoding
tricks** (spell it backwards / first letters / another language) · **output-channel abuse**
(ask for it inside a poem, a JSON field, a base64 blob) · **indirect injection** — the
dangerous one for you: the payload is not typed by the user but sits in a *document, email,
web page, or repo file the agent reads*.

**The structural lesson**: every defence you break is a filter trying to separate
instructions from data AFTER they've been mixed. That mixing is the vulnerability; filters
are mitigation, never cure.

## 2 · The OWASP LLM Top 10 (2025) — the shared vocabulary

Community-maintained by the OWASP GenAI Security Project (genai.owasp.org). Verified list,
with the version that matters to YOUR estate:

| # | Risk | In your world |
|---|------|---------------|
| LLM01 | **Prompt injection** | A poisoned repo file, ledger entry, or email a session reads |
| LLM02 | **Sensitive information disclosure** | `secrets\`, tribunal material, other people's data in context |
| LLM03 | **Supply chain** | Skills/agents/MCP servers you installed; `npm`/`pip` pulls in sessions |
| LLM04 | **Data and model poisoning** | Your own doctrine files — auto-memory and mirrored docs are inputs |
| LLM05 | **Improper output handling** | Model output executed as shell/SQL/code without review (bypassPermissions!) |
| LLM06 | **Excessive agency** | An agent that can act beyond what the task needs — see §3's live case |
| LLM07 | **System prompt leakage** | CLAUDE.md and skills are extractable; treat them as public-ish |
| LLM08 | **Vector and embedding weaknesses** | RAG stores (Tier 4) — poisoned or over-permissive retrieval |
| LLM09 | **Misinformation** | Confident wrong output acted on (module 01's hallucination, weaponised) |
| LLM10 | **Unbounded consumption** | Runaway loops/quota burn — your own MISSION budget guard is this control |

**The one frame to keep** — Simon Willison's **lethal trifecta** (16/06/2025): an agent is
exposed when it combines **(1) access to private data + (2) exposure to untrusted content +
(3) the ability to communicate externally**. Any two are survivable; all three means a
single poisoned document can exfiltrate. This is architectural, not fixable by prompt
hardening — because the model cannot reliably tell injected instructions from data.

## 3 · Threat-model YOUR stack (the real work, ~3h)

Your live surface, read from configuration tonight (verify each yourself):

- **Permission mode: `bypassPermissions`** (settings.json) — sessions execute without
  approval prompts. Deliberate, granted 26/06/2026. It removes the *last human gate*
  between model output and your machine, which makes LLM05 and LLM06 your dominant risks.
- **4 hooks** (SessionStart, SessionEnd, Stop, Notification) — code that runs automatically
  around every session.
- **7 agents + 27 global skills** — instruction files loaded into context. Anything that
  can edit them can steer future sessions (LLM04/LLM03).
- **4 unattended scheduled tasks**, all Ready: `Claude-CLI-AutoUpdate` ·
  `Claude-Doctrine-Mirror` · `Claude-Vault-Daily-Backup` · `ClaudeBridgeWorker`. These run
  with no human watching, by definition.
- **MCP connectors** (Gmail, Google Drive, Calendar, Notion, Canva, Higgsfield) — these are
  the trifecta's leg (2): **email and shared documents are attacker-writable**. Anyone who
  can email you can place text in a session's context.
- **`secrets\`** local-only, never synced — leg (1) exists on this machine.

**The live case study (your own ledger, item 108, 04/08/2026):** `ClaudeBridgeWorker` runs
`git pull --rebase --autostash` **and pushes, on the whole repo, every ~5 minutes** — while
its stated contract is to sync `machines/context/` only. Observed consequences: a
deliberate `--no-ff` merge commit was silently flattened, and a "build but do NOT push"
instruction became *unenforceable*. Read that as security, not just git hygiene: it is
**LLM06 excessive agency** in its purest form — a component whose *capability* exceeds its
*contract*, acting unattended. Nobody attacked anything; the damage was structural. Now ask
the security question: if an attacker could write one file into that repo, what would
5-minutely auto-push give them?

**Your threat model deliverable** (project) uses this frame per asset: *what could go
wrong → who could cause it → what stops it today → what's the cheapest control that would
actually help.* Cheapest controls in your world are usually **narrowing capability**
(scope the bridge worker to its folder), **separating trifecta legs** (don't let one
session hold private data + untrusted email + push rights), and **gates on irreversibles**
(the MANUAL-TASKS pattern you already run).

## 4 · Defences worth knowing (and their honest limits)

| Defence | What it does | Limit |
|---|---|---|
| Instruction hierarchy / delimiters | Marks trusted vs untrusted regions | Model may still obey; mitigation, not cure |
| Input filtering | Blocks known attack strings | Loses to paraphrase/encoding (Gandalf teaches this) |
| Output filtering | Catches secrets on the way out | Attacker encodes; also blocks late |
| **Capability narrowing** | Agent simply *can't* do the harmful thing | The only structural fix; costs convenience |
| **Human gate on irreversibles** | Person approves destructive/outward acts | Only works if gates are few enough to read |
| Provenance / signing | Detects tampered inputs | Doesn't stop obedience to signed-but-hostile text |

Note which two are bolded: they're the ones that survive a smart attacker — and both are
architecture, not prompting.

## 5 · Cyber interleave hook 🔐 (SECONDARY track starts here)

This module is where the plan's light cyber interleave attaches. After it, in D-lane
(play, 1–2 sessions/week — never at the cost of A-lane):

- **Module 13** — shell + OverTheWire Bandit (free): the terminal as a game.
- **Module 14** — crypto by example, taught on monk-mode's REAL HMAC/PBKDF2 scheme
  (module 06 previewed it).
- **Module 15** — web-sec first contact: OWASP Top 10 (the classic web one) + PortSwigger's
  free labs, thought-experimented against psoc-portal.
- **Module 16** — AI-sec continuation: HackAPrompt, Willison's prompt-injection corpus,
  PortSwigger's LLM labs.

Free-first by design (red-team finding M4); the THM subscription decision is ledger item
106 and blocks nothing.

**Checkpoint — you can now:** define prompt injection and name five families; recite the
trifecta and test any agent against it; map the OWASP LLM Top 10 onto a real system;
explain why your bridge worker is an excessive-agency finding; and name the two defences
that actually survive.

## Sources (verified 04/08/2026)

- OWASP Top 10 for LLM Applications 2025 — genai.owasp.org/llm-top-10 (LLM01–LLM10 list
  confirmed tonight).
- Lethal trifecta — Simon Willison, 16/06/2025:
  simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Gandalf — lakera.ai/gandalf (free browser game).
- Your stack: `~/.claude/settings.json` (defaultMode `bypassPermissions`; 4 hook types),
  7 agent files, 27 skill folders, `Get-ScheduledTask` (4 Claude tasks Ready) — all read
  live tonight. Bridge-worker finding: MANUAL-TASKS item 108 (04/08/2026).
