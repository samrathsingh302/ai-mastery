# Drills — module 10

## Anki-importable block (tab-separated: Front ⇥ Back)

Prompt injection, in one sentence?	Text the model reads as DATA gets obeyed as INSTRUCTIONS — because everything in the context is just tokens with no trust label.
Direct vs indirect injection?	Typed by the user vs planted in a document/email/web page/repo file the agent reads — indirect is the dangerous one for agents.
The five injection families?	Direct override · role-play framing · encoding tricks · output-channel abuse · indirect (planted content).
The lethal trifecta (Willison, 16/06/2025)?	Private data + untrusted content + external comms — all three means one poisoned document can exfiltrate.
Why can't prompt hardening fix the trifecta?	The model cannot reliably distinguish injected instructions from data; the mixing IS the vulnerability.
LLM01?	Prompt injection.
LLM02?	Sensitive information disclosure.
LLM03?	Supply chain (models, packages, and the skills/agents you install).
LLM05?	Improper output handling — model output executed without review.
LLM06?	Excessive agency — capability beyond the task's contract.
LLM07?	System prompt leakage — assume CLAUDE.md and skills are extractable.
LLM09?	Misinformation — confident wrong output acted upon.
LLM10?	Unbounded consumption — runaway loops, quota/cost burn.
Which two defences survive a smart attacker?	Capability narrowing and human gates on irreversible acts — both architectural, not prompting.
Why are input/output filters only speed bumps?	Paraphrase and encoding defeat them; they judge strings, not intent.
Your estate's own excessive-agency finding?	ClaudeBridgeWorker pushes the WHOLE repo every ~5 min though its contract is machines/context/ — flattened a merge commit, made "don't push" unenforceable (ledger 108).
What does bypassPermissions remove?	The last human gate between model output and the machine — which makes LLM05/LLM06 the dominant risks in this estate.
Which connector is the classic untrusted-content leg?	Email (Gmail): anyone who can email you can place text in a session's context.
The threat-model question set (4 parts)?	What could go wrong · who could cause it · what stops it today · cheapest control that would actually help.
A control you'd never tolerate is…	Not a control — it's a wish. (Honesty column in the per-asset table.)

## Quick-fire (aloud, 30 seconds)

1. Trifecta's three legs? 2. LLM01? 3. The only structural fix? 4. Filters are…?
*(private data / untrusted content / external comms · prompt injection · capability narrowing · speed bumps)*
