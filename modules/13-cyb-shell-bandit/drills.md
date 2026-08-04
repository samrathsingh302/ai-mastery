# Drills — module 13 🔐 (SECONDARY track)

## Anki-importable block (tab-separated: Front ⇥ Back)

Shell sentence structure?	command --flags arguments — verb, adverbs, objects. `ls -la /etc` = "list, long and all, /etc".
Where's the dictionary?	man <command> · <command> --help · help <builtin>. Reading it beats guessing — that's the skill.
pwd / cd - / cd ~ ?	Where am I · back to the previous directory · home.
What does `tail -f` do and when?	Follows a growing file live — the command you'll use most on real logs.
. / .. / ~ / - ?	Here · parent · home · previous directory.
Globbing: * ? ** ?	Any characters · exactly one character · any depth (modern shells).
What does a pipe | do?	Sends one command's output into the next command's input — a conveyor of small single-purpose machines.
> vs >> ?	Replace the file vs append to it (module 04's "w" vs "a", at the shell).
What does 2>&1 mean?	Send stderr (2) wherever stdout (1) currently goes — so pipes and log files capture errors too.
Why must sort come before uniq -c?	uniq only collapses ADJACENT duplicates; it has no memory of earlier lines. Unsorted input silently gives wrong counts.
sort -rn does what?	Sorts numerically (-n) and reversed (-r) — biggest first.
find vs grep — which question does each answer?	find = "which FILES?" (name/type/time/size/permissions) · grep = "which LINES?" (content).
grep flags: -r -n -i -l -c -v ?	recursive · line numbers · case-insensitive · filenames only · counts · invert the match.
What does xargs do?	Feeds a list of items into another command: find . -name '*.log' | xargs wc -l
Read -rw-r--r-- aloud.	Type, then owner rw-, group r--, others r-- → only the owner can write.
chmod 600 secret.txt means?	Owner read+write; group and others nothing.
Why does `cat -oddly-named` fail, and the two fixes?	It looks like flags. Use `cat ./-oddly-named` or `cat -- -oddly-named`.
SSH in one sentence?	An encrypted remote terminal — you type here, it runs there. ssh user@host -p PORT.
What is the first-connect fingerprint prompt for?	The server proving its identity/continuity — accept once, and be suspicious if it ever changes unexpectedly.
Bandit's connection line?	ssh bandit0@bandit.labs.overthewire.org -p 2220 (level-0 password: bandit0)
The house rule for Bandit?	No walkthroughs — 30 minutes of struggle, then man pages, then concept-only hints. Every walkthrough read is a rep not done.
bash vs PowerShell, three differences?	ls/cat/grep vs Get-ChildItem/Get-Content/Select-String · $VAR vs $env:VAR · /dev/null vs $null.
"Labs are the curriculum" means?	Cyber videos are on-ramps; hands-on labs (Bandit, PortSwigger, DVWA) are where competence actually forms.

## Quick-fire (aloud, 30 seconds)

1. Which files vs which lines? 2. Before uniq -c you must…? 3. Who can write -rw-r--r--?
4. Two ways to cat a file starting with a dash?
*(find vs grep · sort · only the owner · ./name or -- name)*
