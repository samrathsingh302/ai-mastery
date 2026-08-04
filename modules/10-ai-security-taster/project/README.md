# Project 10 — Threat-model your own agent stack (the differentiator artefact)

**What:** `threat-model.md` here — a real, evidence-based security review of YOUR Claude
estate. ~3h. This is the artefact almost nobody operating agent fleets has; it is CV-worthy
and interview-worthy, and it makes your own machine safer. Read-only: you inspect and
recommend, you don't change configuration in this project (changes are a separate decision,
and irreversible ones go to MANUAL-TASKS).

## 1 · Inventory (evidence, not memory — paste each command's output)

- Permission mode + hooks: read `~/.claude/settings.json` (expect `bypassPermissions`, 4 hook
  types — confirm, don't assume).
- Agents + skills: count `~/.claude/agents/*.md` and `~/.claude/skills/*`.
- Unattended automation: `Get-ScheduledTask | Where TaskName -like '*Claude*'`.
- Connectors: which MCP servers a session lists (Gmail, Drive, Calendar, Notion, …).
- Sensitive stores: `secrets\`, tribunal/committee material, `OneDrive\dev` (no remotes).

## 2 · Per-asset table (the core deliverable)

For each asset above: **what could go wrong · who could cause it (incl. "nobody — structural")
· what stops it today · cheapest control that would actually help · would I accept the
inconvenience?** Be honest on the last column — a control you'd never tolerate isn't a
control, it's a wish.

## 3 · The trifecta audit

List every session shape you actually run (repo session, estate session, overnight loop,
scheduled task) and mark its legs: private data? untrusted content? external comms? Any row
with all three gets a paragraph: what would a single poisoned document achieve?

## 4 · Three findings, severity-ordered

Written as your `auditor` agent would: title · evidence (file/command) · impact · concrete
fix · effort. Ledger item 108 is a worked example of the format and can be finding #0 (it's
already logged — cite it, don't duplicate it).

## 5 · One decision for Samrath

End with a single recommendation and its cost, phrased for a pop-up: what you'd change
first, what it breaks, what it buys. If you agree with yourself, it goes to MANUAL-TASKS —
that's the loop closing.

## Acceptance checklist

- [ ] Every inventory line has pasted evidence, dated
- [ ] Per-asset table complete; the "would I accept it?" column honestly answered
- [ ] Trifecta audit covers all four session shapes; complete-trifecta rows analysed
- [ ] Three findings in auditor format, severity-ordered, with real fixes
- [ ] One recommendation written pop-up-ready; ledger entry created if you agree with it
- [ ] Nothing in the estate was modified while writing this
