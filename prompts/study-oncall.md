---
type: brief
used-by: C:\Users\samra\tools\study-launch.ps1 (the Claude-Study-Launch scheduled task, ledger 899)
---
# Kickoff brief — study-oncall (ledger 899; chain 20261012-a-ai-mastery ticket 2) — 12/10/2026

## Role
- Seat kickoff: you are a routine seat (`-Role routine`, launched `-Model opus` — the sanctioned study exception in `skills/open-session/SKILL.md`); chainless.

## Standing rules (verbatim)
- Do the slice yourself; spawn no subagents (Opus workers).
- Edit surgically; never rewrite a file.
- Keep the change to what the brief asks; report extras as follow-ups, do not fix them.
- Verify every path/name by listing it before use.
- Never write code through a Bash heredoc — Write tool or a script file.
- One builder per slice; a ~/.claude, money, auth, data-loss or outward-facing surface gets a bare Opus verifier.
- Anything only Samrath can do → append to `OneDrive\dev\_global\MANUAL-TASKS.md` the moment it surfaces (plain first sentence).
- No open-ended waits: rely on completion notifications; a wait > 10 min with no signal is written down as BLOCKED.

## Context to read first
Only these files/sections: `C:\Users\samra\repos\ai-mastery\TUTOR-CONTRACT.md` (the whole contract; on-call mode is step 1) and what it names (`anki\CARD-RULES.md`) — nothing else.

## Task
1. Read `C:\Users\samra\repos\ai-mastery\TUTOR-CONTRACT.md` and run it in **on-call** mode (step 1).
2. Run `python modules\03-cs50p-accelerated\exercises\check.py` from `C:\Users\samra\repos\ai-mastery` yourself and take the FIRST `TODO  exNN_<name>: not written yet` line as `<exNN>`; its file is `C:\Users\samra\repos\ai-mastery\modules\03-cs50p-accelerated\exercises\<exNN>.py`.
3. Your first message is exactly two lines and nothing else:
   - line 1, the on-call sentence from `TUTOR-CONTRACT.md` step 1, verbatim: `On call. Paste your attempt or the red checker line — nothing else gets an answer.`
   - line 2: `<absolute path of that file> is open — type line 1 now, then paste it or the red line from: cd C:\Users\samra\repos\ai-mastery && python modules\03-cs50p-accelerated\exercises\check.py <exNN>`
   - When `check.py` prints no TODO line (the ladder is complete), line 2 instead names MOOC.fi Python Programming 2026 Part 1 per `START-HERE.md`: `Ladder complete — open https://programming-26.mooc.fi/part-1/1-getting-started, type line 1 of the next exercise now, then paste it.`
4. Then silence. Answer only a pasted attempt or a pasted red line, one wall at a time. Contract rule 12 binds: he types first.
5. When he says he is done, run the closing ritual (step 3) unprompted, write the session handoff, then close with `node C:\Users\samra\tools\seat-exit.js --handoff <that handoff>`.

**Do not**: teach, propose a target, summarise the day, suggest what to do next or ask how it is going before he pastes; run a posting check or any career work.

## Footer
The echo line is added by the launcher (`launch-brief.ps1`) — this brief does not carry it. Commit pathspec-scoped. Push only repos with remotes.
