# Project 13 🔐 — Read your own automation (shell literacy, applied)

**What:** `automation-audit.md` here — you read, in the shell, the automation that already
runs on your machine unattended, and explain what each command actually does. ~1.5h.
**Read-only: you change nothing.** This is module 10's threat model given hands.

## The targets (all yours, all currently running)

1. **The four scheduled tasks** — `Claude-CLI-AutoUpdate`, `Claude-Doctrine-Mirror`,
   `Claude-Vault-Daily-Backup`, `ClaudeBridgeWorker`.
   Inspect: `schtasks /query /tn "<name>" /v /fo LIST` (or PowerShell
   `Get-ScheduledTask -TaskName '<name>' | Select-Object -ExpandProperty Actions`).
   For each: what triggers it, what command it runs, in which working directory, as which
   user, and **what it can reach**.
2. **The bridge worker's actual line** — find the `git pull --rebase` in
   `repos\atlas-pipeline\machines\bridge-worker.ps1` (module 05 and ledger 108 both name
   it). Read the surrounding 20 lines with `sed -n '30,60p'` or `less`. Explain the whole
   command including every flag (`--rebase`, `--autostash`, `--quiet`) in your own words.
3. **Your Claude hooks** — `~/.claude/settings.json` has 4 hook types. Read them
   (`python -c "import json;print(json.dumps(json.load(open('settings.json'))['hooks'],indent=2))"`
   from `~/.claude`, or just `less settings.json`). What runs at session start? At stop?

## The write-up (per target)

**Trigger · command · what each flag does · what it can touch · what would break if it
failed silently for a week.** That last question is the one nobody asks, and it's where
real findings live.

Close with **one improvement you'd make** and why — plus whether it's a shell fix, a
config fix, or a decision only you can take (if the last, it goes to MANUAL-TASKS).

## Acceptance checklist

- [ ] All four tasks documented from their real definitions (pasted, dated)
- [ ] The bridge worker's git line explained flag by flag, in your words
- [ ] The four hooks named and their timing explained
- [ ] "Silent failure for a week" answered honestly per target
- [ ] One improvement proposed, correctly routed (shell / config / MANUAL-TASKS)
- [ ] Nothing on the machine was modified
