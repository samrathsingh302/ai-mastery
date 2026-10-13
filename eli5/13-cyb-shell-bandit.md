# Module 13: shell + Bandit — like you're 5

Module 13 🔐, the secondary track, taught in `C:\Users\samra\repos\ai-mastery\modules\13-cyb-shell-bandit\TEACH.md`.

- **One-line reminders:** `GLOSSARY.md` → `## Module 13 🔐 — shell + Bandit *(secondary track)*`.
- **Git Bash only:** every command here runs in Git Bash, not PowerShell. `echo $SHELL` proves you're in it.
- **Pipeline builder:** one-liners can be taken apart stage by stage in `C:\Users\samra\repos\ai-mastery\modules\13-cyb-shell-bandit\interactive\pipeline-builder.html`. `start` it from PowerShell.
- **Not answers:** none of them answers a `check.py` sandbox question or a Bandit level.

---

### find vs grep
**Like you're 5:** Two questions in a library. "Which books are red and thin?" You look at the covers. "Which pages say 'dragon'?" You read inside. find looks at the covers of files; grep reads the lines inside them. Ask the right question and you pick the right helper.

**The real words:** Which FILES (by name, type, time, size) vs which LINES (by content); picking the right question picks the tool. → [13 A5](../modules/13-cyb-shell-bandit/TEACH.md)

**See it:** `cd /c/Users/samra/repos/ai-mastery` then `find modules -name TEACH.md | head -3` (files) vs `grep -rn "lethal trifecta" modules | head -3` (lines).

### Globbing
**Like you're 5:** Wildcards are blank tiles in a word game. A star tile stands for any number of letters, so "star dot md" means "any name ending in .md". A question-mark tile stands for exactly one letter.

**The real words:** Wildcard name matching done by the shell: `*` any run of characters, `?` exactly one, `**` any depth (in bash only after `shopt -s globstar`). → [13 A3](../modules/13-cyb-shell-bandit/TEACH.md)

**See it:** `cd /c/Users/samra/repos/ai-mastery/modules` then `ls -d 1?-*` (the five modules numbered 10–14) and `ls */TEACH.md | wc -l` → `14`.

### Permissions (rwx)
**Like you're 5:** Every file has three boxes of rules: one for its owner, one for the owner's group of friends, one for everyone else. Each box says whether you may read the file, change it, or run it. A dash means "no".

**The real words:** Owner/group/others triples of read, write, execute; `-rw-r--r--` = everyone reads, only the owner writes; `chmod 600` = owner read+write, nobody else. → [13 A6](../modules/13-cyb-shell-bandit/TEACH.md)

**See it:** `ls -l /c/Users/samra/repos/ai-mastery/GLOSSARY.md` → it starts `-rw-r--r--`; read it aloud as type, owner, group, others. On Windows these are approximate (NTFS ACLs are the real thing); on Bandit's Linux they're exact.

### Pipe (`|`)
**Like you're 5:** A conveyor belt between machines in a toy factory. The first machine makes something and drops it on the belt; the next machine picks it up and does its one job; and so on down the line. The pipe is the belt.

**The real words:** One command's output becomes the next one's input; small tools that each do one thing, composed — the Unix philosophy in one character. → [13 A4](../modules/13-cyb-shell-bandit/TEACH.md)

**See it:** `cd /c/Users/samra/repos/ai-mastery` then `cat GLOSSARY.md | grep '^## Module' | wc -l` → `14`: dump the file, keep the module headings, count them.

### Redirection (`>`, `>>`, `2>&1`)
**Like you're 5:** Instead of shouting your answer out loud, you write it in a notebook. One arrow means "rub the page out and write fresh"; two arrows mean "add to the bottom". The last sign means "write your complaints in the same notebook too".

**The real words:** `>` replaces a file, `>>` appends to it (module 04's `"w"` vs `"a"`, at the shell), and `2>&1` sends errors where the output goes. → [13 A4](../modules/13-cyb-shell-bandit/TEACH.md)

**See it:** `cd /tmp` then `echo one > r.txt; echo two >> r.txt; cat r.txt` → `one`, `two`; then `ls nope > r.txt 2>&1; cat r.txt` — the error landed in the file; `rm r.txt` to tidy up.

### SSH
**Like you're 5:** A secret, locked phone line into another computer's keyboard. You type here, it runs there, and nobody listening can understand. The first time you call, the other computer shows you its face; if that face ever changes, be suspicious.

**The real words:** An encrypted remote terminal (`ssh user@host -p port`); keys beat passwords, and the first-connect fingerprint prompt is the server proving identity continuity. → [13 A7](../modules/13-cyb-shell-bandit/TEACH.md)

**See it:** `ssh bandit0@bandit.labs.overthewire.org -p 2220` (password `bandit0`, from the level-0 page): read the fingerprint prompt before you type yes; once accepted it is kept in `~/.ssh/known_hosts`.

### `sort | uniq -c`
**Like you're 5:** Counting sweets by colour. First line them up so all the reds sit together, then all the blues. Now counting is easy: "two reds, one blue". Skip the lining-up and you'd count "one red, one blue, one red", which is wrong.

**The real words:** The counting idiom; `uniq` only collapses ADJACENT duplicates, so the `sort` is load-bearing. → [13 A4](../modules/13-cyb-shell-bandit/TEACH.md)

**See it:** `printf 'red\nblue\nred\n' | uniq -c` counts red twice, separately; `printf 'red\nblue\nred\n' | sort | uniq -c` → `1 blue`, `2 red`.
