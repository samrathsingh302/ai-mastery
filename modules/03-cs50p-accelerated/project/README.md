# Project 03 — repo-census.py (your first real tool, AI-FREE)

**What:** a command-line tool that surveys YOUR `C:\Users\samra\repos\` and reports what's
actually in there. **Rules: fully AI-free** (docs + these modules only — counts toward the 20%
quota). Do it after rung 6; it exercises rungs 0–6 honestly. ~2–4h including walls. Walls are
the point.

## Spec (build to this, nothing more)

`python repo_census.py C:\Users\samra\repos` prints, for each immediate subfolder (each repo):

```
psoc-portal      412 files   .py 61%  .html 22%  .css 9%  other 8%   newest: 28/07/2026
monk-mode        198 files   .py 84%  .md 11%  other 5%              newest: 15/07/2026
...
TOTAL            2,341 files across 14 repos
```

- Skip `.git` folders entirely (and `node_modules` if you meet one).
- "newest" = the most recently modified file's date, dd/mm/yyyy.
- Top 3 extensions by count, as percentages of that repo's files; the rest lumped into other.
- Take the root path from `sys.argv[1]`; if missing, exit politely with a usage line (rung 4).

**Toolbox you already own:** `pathlib.Path.rglob("*")` (or `os.walk`), `.suffix`, `.stat().
st_mtime` + `datetime.fromtimestamp`, dicts with `.get(k, 0) + 1`, `sorted(key=...)`,
f-strings with `:>8` style padding for the columns.

## Acceptance checklist

- [ ] Runs on your real repos folder without crashing (unicode names, empty dirs included)
- [ ] `.git` contents excluded (file counts drop hugely when you get this right — sanity-check)
- [ ] Handles a nonsense path with a clean message, not a traceback (rung 3)
- [ ] Output columns line up (f-string padding, not manual spaces)
- [ ] ≤ ~80 lines, functions with returns (main() + helpers), no AI involved at any point
- [ ] Journal the walls you hit + the AI-free hours; commit the script into this folder

*(After module 05 you'll git-log this file and see your own before/after. Keep the first
version forever — it's your baseline artefact.)*
