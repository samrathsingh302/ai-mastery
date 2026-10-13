# 04-automate-boring-stuff — like you're 5

Taught in `C:\Users\samra\repos\ai-mastery\modules\04-automate-boring-stuff\TEACH.md`; the one-line reminders are `GLOSSARY.md` → `## Module 04 — automate the boring stuff`. None of the "See it" lines below is an exercise answer. To try a Python one: `cd C:\Users\samra\repos\ai-mastery`, then `python`, type the lines, `exit()` to leave.

### Dry-run
**Like you're 5:** Before tidying your room for real, you walk round pointing: "this goes in the box, that goes on the shelf." Nothing moves yet. Only after a grown-up says the list looks right do you actually move things.
**The real words:** The mode that only prints what a script would do; run it first, always, and read every line. → [04 safety laws](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** `cd C:\Users\samra\repos\ai-mastery` then `git add -A --dry-run` — git lists what it would stage and stages nothing.

### Idempotent
**Like you're 5:** A light switch. Flick it to "on" once, the light is on. Flick it to "on" again, still on, nothing extra happens. Not like a tap that pours another cup every time you press it.
**The real words:** Safe to run twice: the second run finds nothing left to do and does nothing; check before acting (`if not target.exists():`). → [04 safety laws](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** In the REPL: `s = {1, 2}`, then `s.add(3)` twice, then `s` → `{1, 2, 3}`; the second add changed nothing.

### JSON
**Like you're 5:** A set of boxes inside boxes, written down as plain text with curly brackets and square brackets, so any program in any language can open the boxes and read what's inside.
**The real words:** A text format for nested data (dicts, lists, numbers, strings); the common tongue of APIs and exports. → [04 mission 4](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** `import json` then `json.loads('{"reps": [5, 5, 3]}')["reps"]` → `[5, 5, 3]`. A real one: `C:\Users\samra\repos\hevy-brain\data\meta.json`.

### pathlib / Path
**Like you're 5:** Instead of writing an address on a scrap of paper, you get a little map object that knows its own street, its own house name, and can tell you if the house is really there.
**The real words:** Paths as objects: join with `/`, `.rglob` walks trees, `.read_text` reads, `.exists()` checks. → [04 mission 1](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** `from pathlib import Path` then `p = Path(r"C:\Users\samra\repos\ai-mastery") / "START-HERE.md"`, then `p.exists()` → `True` and `p.suffix` → `'.md'`.

### Quarantine
**Like you're 5:** When you want to throw a toy away, you put it in a "maybe bin" with today's date on it instead. A grown-up checks the bin later and empties it. If you made a mistake, the toy is still there.
**The real words:** Where automation "deletes" to: a dated folder a human empties later; `os.remove` is banned in this module. → [04 safety laws](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** Your Windows Recycle Bin is the same idea; safety law 2 in `C:\Users\samra\repos\ai-mastery\modules\04-automate-boring-stuff\TEACH.md` names the `_quarantine\<date>\` shape.

### shutil
**Like you're 5:** The removal-van kit: boxes to copy things into, a trolley to move them, and tape to pack a whole room into one parcel.
**The real words:** The move/copy/zip toolbox (`copy2`, `move`, `make_archive`). → [04 mission 2](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** `import shutil, tempfile` then `shutil.copy2(r"C:\Users\samra\repos\ai-mastery\START-HERE.md", tempfile.gettempdir())` — it returns the path of the copy in your temp folder.

### subprocess
**Like you're 5:** Asking a friend to do a job for you and then reading the note they hand back: did it go well, and what did they say?
**The real words:** Your script running another program and reading its output; args as a LIST, never a glued string. → [04 mission 5](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** `import subprocess` then `r = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, cwd=r"C:\Users\samra\repos\ai-mastery")`, then `r.returncode` → `0`.

### Task Scheduler
**Like you're 5:** An alarm clock that, when it rings, doesn't wake you up; it does a job for you. It needs three things: when to ring, what job to do, and which room to do it in.
**The real words:** Windows' cron: a trigger + an action + a working directory; how your Claude auto-update and study-launch tasks run. → [04 mission 5](../modules/04-automate-boring-stuff/TEACH.md)
**See it:** In any terminal: `schtasks /query /tn "Claude-Study-Launch" /v /fo LIST` — read "Task To Run", "Start In" and the schedule lines.
