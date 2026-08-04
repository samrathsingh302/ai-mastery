# Module 04 — Automate the Boring Stuff ×5, applied to YOUR files

> **What this is:** five missions from *Automate the Boring Stuff with Python* (3rd ed., May
> 2025, free online at automatetheboringstuff.com — CC-licensed), each taught here directly and
> aimed at YOUR estate: `repos\`, the OneDrive dev folders, your Hevy export, your scheduled
> tasks. The book is the optional deep end; these notes + exercises are the path. **~15h.**
> **Prerequisite:** module 03 rungs 0–6 (you'll use functions, loops, dicts, exceptions,
> files). Regex mission assumes rung 7 or teaches-as-you-go.
> **The five** (3rd-edition chapter numbers, verified 04/08/2026): Ch 10 files · Ch 11
> organising · Ch 9 regex · Ch 18 CSV/JSON · Ch 19 scheduling/launching.

## ⚠️ The safety laws (before ANY script touches real files)

Your house law is no-data-loss. Automation multiplies mistakes as happily as work, so:

1. **Dry-run first, always:** every destructive script gets a `--dry-run` mode that only
   PRINTS what it would do. Run it, read every line, only then run for real. (My ex02
   makes the dry-run flag part of the spec.)
2. **Quarantine, never delete:** scripts move files to a dated `_quarantine/2026-08-04/`
   folder; a human empties it later. `os.remove` doesn't appear in this module.
3. **Practise in the sandbox:** the exercises build a fake file tree in a temp folder —
   your scripts prove themselves there before meeting OneDrive.
4. **Idempotent** *(plain words: safe to run twice — the second run finds nothing left to do
   and does nothing; analogy: a light switch you can flick to "on" repeatedly vs a lever that
   pours another kettle every pull)*: check before acting (`if not target.exists():`).

## Mission 1 — Paths & files, fluently *(Ch 10)*

- **pathlib** is the modern way — paths as objects, not strings:

  ```python
  from pathlib import Path
  repo = Path(r"C:\Users\samra\repos\ai-mastery")   # r"" — backslashes stay literal
  for p in repo.rglob("*.md"):                      # recursive glob: every .md below
      print(p.name, p.suffix, p.stat().st_size)     # name, ".md", bytes
  ```

- The vocabulary that covers 90% of use: `Path.home()`, `/` to join (`repo / "PROGRESS.md"`),
  `.exists()`, `.is_dir()`, `.mkdir(parents=True, exist_ok=True)`, `.read_text(encoding=
  "utf-8")`, `.write_text(...)`, `.glob("*.py")` vs `.rglob` (recursive), `.relative_to(root)`.
- **Wall:** Windows backslashes. Use raw strings for literals and let pathlib join with `/` —
  never glue paths with `+`.

## Mission 2 — Organising: move, copy, rename, zip *(Ch 11)*

- **shutil** does the heavy lifting: `shutil.copy2(src, dst)` (copy with timestamps),
  `shutil.move(src, dst)`, `shutil.make_archive("backup-2026-08-04", "zip", folder)`.
- The organiser pattern (ex02's shape):

  ```python
  def organise(folder, dry_run=True):
      for p in Path(folder).iterdir():
          if p.is_file():
              dest = Path(folder) / p.suffix.lstrip(".").lower()    # pdfs -> pdf/
              action = f"{p.name} -> {dest.name}/"
              if dry_run:
                  print("DRY-RUN:", action)
              else:
                  dest.mkdir(exist_ok=True)
                  shutil.move(str(p), dest / p.name)
  ```

- **Walls:** moving a file onto itself (skip when already sorted); name collisions (append
  `-1`, `-2` — ex02 tests this); iterating a folder WHILE moving things in it (collect the
  list first: `list(p.iterdir())`).

## Mission 3 — Regex on your real text *(Ch 9)*

Your handoffs are named `YYYY-MM-DD-HHmm-<slug>.md`; your ledger items carry `dd/mm/yyyy`
dates; your markdown has `[[wiki-links]]`. That's three real patterns:

```python
import re
handoff = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(\d{4})-([\w-]+)\.md")
ledger_date = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
wikilink = re.compile(r"\[\[([^\]]+)\]\]")          # [^\]]+ = "anything but ]"
```

- New tools over rung 7: `re.compile` (name a pattern once, reuse), named groups
  (`(?P<year>\d{4})` → `m.group("year")`), `re.MULTILINE` for line-anchored `^`.
- **Wall:** `.` matches almost anything — escape literal dots (`\.md`); greedy `.*` eats
  brackets — prefer negated classes (`[^\]]+`), exactly as `wikilink` does.
- The playground (`interactive/regex-playground.html`) has these three preloaded — build
  variations there before writing code.

## Mission 4 — CSV & JSON: your data's two native tongues *(Ch 18)*

- **CSV** (spreadsheets as text — your Hevy export): `csv.DictReader` yields each row as a
  dict keyed by the header line. Numbers arrive as STRINGS — convert before maths (rung 0's
  lesson, again, forever).
- **JSON** *(plain words: a text format for nested data — dicts/lists/strings/numbers written
  down; the lingua franca of APIs and exports; example: your LifeOS exports)*:
  `json.loads(text)` → Python objects; `json.dumps(obj, indent=2)` → pretty text.
- The bridge pattern (ex04): read messy CSV → compute per-group summaries into a dict →
  `json.dumps` → write. CSV in, JSON out is half of all data plumbing.
- **Walls:** `encoding="utf-8"` on open() for real-world files; `newline=""` when WRITING
  csv on Windows (else blank lines); missing keys (`row.get("Weight", "0")`).

## Mission 5 — Launching & scheduling: automation that runs itself *(Ch 19)*

- **subprocess** *(plain words: your script running another program, like you typing a
  command; analogy: delegating to a colleague and reading their reply)*:

  ```python
  import subprocess
  r = subprocess.run(["git", "log", "--oneline", "-3"],
                     capture_output=True, text=True, cwd=repo)
  print(r.returncode, r.stdout)      # 0 = success; stdout = what it printed
  ```

  Law: pass args as a LIST (no shell string-gluing — that's how injection bugs are born;
  module 15 will weaponise this lesson properly).
- **Scheduling on YOUR machine:** Windows Task Scheduler runs things on cron-like triggers —
  you already own examples: `Claude-CLI-AutoUpdate` and `Claude-Doctrine-Mirror` (daily
  tasks; `tools\claude-autoupdate\`). Inspect them: `schtasks /query /tn "Claude-CLI-
  AutoUpdate" /v /fo LIST` — the module's point is that these stop being magic: a trigger +
  an action + a working directory, nothing more.
- `time.sleep(seconds)` and `datetime` you met in rung 4; Ch 19 combines them into "run
  forever, act hourly" loops — on your machine prefer Task Scheduler (survives reboots).

**Checkpoint — you can now:** walk any folder tree and answer questions about it in code;
sort a messy folder with a dry-run-first, collision-safe organiser; pull structured facts out
of your own markdown with compiled regexes; convert Hevy-style CSV into a summary JSON; and
explain what your two Claude scheduled tasks actually do under the hood.

## Sources (verified 04/08/2026)

- *Automate the Boring Stuff with Python*, 3rd edition, Al Sweigart, May 2025 — free online
  (CC): automatetheboringstuff.com; chapter mapping via nostarch.com/automate-boring-stuff-
  python-3rd-edition (Ch 9/10/11/18/19 as used above).
- Python behaviour: stdlib (pathlib/shutil/re/csv/json/subprocess), exercised by
  `exercises/check.py` on your 3.14.5 (self-verify: `--solutions`).
- Your scheduled-task examples: `tools\claude-autoupdate\` (per doctrine; inspect with
  schtasks to see it live).
