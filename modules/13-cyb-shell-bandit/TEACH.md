# Module 13 🔐 — Shell fluency + OverTheWire Bandit *(SECONDARY track)*

> **⚠ This is a SECONDARY module.** The AI order is untouched: study this in **D-lane**
> (the fun/variety slot, 1–2 sessions a week), hooked **after module 05 (Git properly)**.
> If it ever competes with an A-lane module, A wins — that's the interleave's whole contract.
> **~6h.** Free-first: everything here costs £0. (TryHackMe's guided rooms would slot in here
> too — that's ledger item 106, still your call, and nothing depends on it.)
> **Why the shell, for you specifically:** every agent you run, every hook, every scheduled
> task, and every CI job is *a shell command someone wrote*. Reading them is not optional
> literacy any more — and it's the on-ramp to every security lab in the plan.

## Your kit (verified on this machine, 04/08/2026)

| Tool | Version here | What it's for |
|------|--------------|---------------|
| Git Bash | GNU bash **5.3.9** (Cygwin) | Your everyday POSIX shell on Windows |
| WSL | present (`wsl.exe`) | A real Linux when you want one |
| OpenSSH | **10.3p1** | Logging into other machines — Bandit needs this |
| PowerShell | 5.1 | Windows-native; different language, same job |

**Two shells, two languages** — the trap that catches everyone: `ls`, `cat`, `grep` in bash
vs `Get-ChildItem`, `Get-Content`, `Select-String` in PowerShell; `$VAR` vs `$env:VAR`;
`/dev/null` vs `$null`. Your own CLAUDE.md warns sessions about exactly this. Know which
shell you're in before you type — `echo $SHELL` (bash) tells you; a PowerShell prompt
usually shows `PS`.

## Part A — The shell as a language (~2h)

### A1 · The sentence: `command --flags arguments`

- **Command** = the verb; **flags** = adverbs (`-l` long, `-a` all, `-r` recursive);
  **arguments** = the objects. `ls -la /etc` = "list, long and all, the /etc directory".
- **The manual is the dictionary:** `man ls` (or `ls --help`, or `help cd` for builtins).
  *Reading the manual instead of guessing is the actual skill this module installs.*

### A2 · Moving and looking

`pwd` (where am I) · `cd` (go; `cd -` = back where I was; `cd ~` = home) · `ls` ·
`tree` (if present) · `cat` (dump a file) · `less` (page through it; `q` quits, `/word`
searches) · `head -n 20` / `tail -n 20` (ends) · `tail -f` (**follow** a growing log — the
one you'll use most in real work) · `file x` (what IS this?) · `wc -l` (count lines).

### A3 · Paths, absolute and relative

`/c/Users/samra/repos` (absolute — from the root) vs `../modules` (relative — from here).
`.` = here, `..` = parent, `~` = home, `-` = previous. **Wildcards (globbing)**: `*.md`
(any name ending .md), `?` (one character), `**` (any depth, in modern shells).
*(Analogy: a postcode vs "second left, then the blue door".)*

### A4 · Pipes and redirection — the idea that makes the shell powerful

- **Pipe `|`** *(plain words: send one command's output straight into the next command's
  input; analogy: a factory conveyor — each machine does one thing and passes the part
  along)*.
- **Redirect `>` `>>`** — send output to a file (`>` replaces, `>>` appends: module 04's
  `"w"` vs `"a"`, at the shell). `2>` redirects errors specifically; `2>&1` merges them.
- **The Unix philosophy in one line:** small tools that each do one thing, composed with
  pipes. That's why `grep`, `sort`, `uniq`, `wc` are tiny and everywhere.

```bash
# "which file extensions am I actually carrying, most common first?"
find . -type f -name '*.*' | sed 's/.*\.//' | sort | uniq -c | sort -rn | head
```

Read that as a sentence: *find files → strip everything before the last dot → sort so equal
lines are adjacent → count runs (`uniq -c` needs sorted input — the classic gotcha) → sort
by count, numerically, descending → show the top.* You wrote this same tool in Python in
module 03's project; here it's one line, and now you can read BOTH.

### A5 · Finding things

- **`find`** = by name/type/time/size: `find . -name '*.py' -newermt '-7 days'`.
- **`grep`** = by content: `grep -rn "TODO" .` (recursive, line numbers); `-i` insensitive,
  `-l` just filenames, `-c` counts, `-v` invert. (`rg`/ripgrep is the fast modern cousin —
  your Grep tool is built on it.)
- **`xargs`** = feed a list into another command: `find . -name '*.log' | xargs wc -l`.

### A6 · Permissions, briefly (the security half)

`ls -l` shows `-rw-r--r--`: type, then **owner / group / others**, each with **r**ead,
**w**rite, e**x**ecute. `chmod 600 secret.txt` = owner read+write, nobody else. On Windows
these are approximate (NTFS ACLs are the real thing — `icacls`), but Bandit runs on Linux
where they're exact, and half its puzzles are permission puzzles.

**The security instinct to build:** *who can read this, and who can change it?* Your own
estate answers this deliberately — `secrets\` is local-only and never synced; `dev`/`brain`
have no remotes. Those are permission decisions in the same family.

### A7 · SSH — logging into another machine

**SSH** *(plain words: an encrypted remote terminal — you type here, it runs there;
analogy: a secure phone line into another computer's keyboard)*.
`ssh user@host -p 2220`. Keys beat passwords (`ssh-keygen`, then the public half goes on the
server); the fingerprint prompt on first connect is the server proving continuity — say yes
once, and be suspicious if it ever changes unexpectedly.

## Part B — Bandit: the shell as a game (~4h)

**OverTheWire Bandit** (overthewire.org/wargames/bandit — free, verified live tonight):
34 levels; each gives you a password to the *next* level, hidden behind one shell skill.
It is the single best free shell teacher in existence, and levels 0–15 are pure Part-A
practice.

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220      # password: bandit0
```

**House rules for playing:**

1. **No walkthroughs.** The internet is full of them; every one you read is a rep you
   didn't do. The 30-minute struggle rule applies, then `man` — *then* a hint from a tutor
   session (concepts only: "what does `find` do with `-size`?", never "the answer is…").
2. **Log every level** in `exercises/bandit-log.md`: level · what the puzzle taught ·
   the command that cracked it · time. That log is your evidence and your revision.
3. **Read the level page fully** before typing — the puzzle statement names the skill.
4. Levels 0–15 in this module; 16+ are optional overspill into module 27's C1 work.

**What the early levels teach** (so you know what you're building):
files with strange names (`./-` and `cat ./spaces\ in\ this\ filename`), `file`-based
detective work, `find` with predicates (size/user/permissions), `grep` for needles in
haystacks, `sort`/`uniq` for the odd-one-out, base64/rot13/hexdump decoding, and finally
`ssh` with keys. Every one of those is a real workday skill wearing a game costume.

## Part C — What this unlocks (the honest framing)

The plan's sweep is blunt about cyber: **it is not entry-level**, and infotainment videos
are on-ramps, not curricula — **labs are the curriculum**. This module is your first lab
hours. It leads to module 27 (full C1: networks, Linux fundamentals, DVWA) and, if the
pull is real, to the C4 pivot decision with actual information rather than vibes.

**Checkpoint — you can now:** navigate and inspect any filesystem from a terminal; build a
pipeline of 4+ tools and explain each stage; find files by name, content, size and age;
read `-rw-r--r--` aloud correctly; ssh into a remote host; and you have Bandit 0–15 logged
in your own words.

## Sources (verified 04/08/2026)

- OverTheWire Bandit — overthewire.org/wargames/bandit (HTTP 200 tonight); connection
  `ssh bandit0@bandit.labs.overthewire.org -p 2220`, password `bandit0` (level-0 page).
- Your local kit: `bash --version` (5.3.9 Cygwin), `wsl.exe` present, `ssh -V`
  (OpenSSH_10.3p1) — read live tonight.
- Cyber framing + "labs are the curriculum": plan v3 Tier C.
- Exercise sandbox and its expected answers: machine-verified in this repo tonight.
