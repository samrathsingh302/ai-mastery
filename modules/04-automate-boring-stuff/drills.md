# Drills — module 04

## Anki-importable block (tab-separated: Front ⇥ Back)

The four safety laws for file automation?	Dry-run first · quarantine never delete · practise in a sandbox · idempotent (safe to run twice).
Idempotent means…	Running it twice changes nothing the second time — check before acting.
Join paths in pathlib?	With / — repo / "PROGRESS.md"; never glue path strings with +.
.glob vs .rglob?	glob = this folder only; rglob = recursive, the whole tree below.
Copy with timestamps / move / zip a folder?	shutil.copy2 · shutil.move · shutil.make_archive(name, "zip", folder)
Why collect list(p.iterdir()) before moving files?	Never mutate a folder while iterating it — plan first, then act (the dry-run principle as code).
Name-collision idiom?	stem-1.suffix, stem-2.suffix… until free (unique_name).
re.compile buys you…	A named, reusable, once-built pattern — and a home for the regex comment.
Named group syntax + read-back?	(?P<year>\d{4}) → m.group("year")
Match [[wiki-links]] safely?	r"\[\[([^\]]+)\]\]" — negated class beats greedy .* inside brackets.
csv.DictReader gives you…	Each row as a dict keyed by the header line — values ALWAYS strings; convert before maths.
JSON in one sentence?	Text format for nested dicts/lists/strings/numbers — the lingua franca of APIs and exports.
json.loads vs json.dumps?	loads: text → Python objects; dumps: objects → text (indent=2 for humans).
Two Windows CSV/file gotchas?	encoding="utf-8" on open; newline="" when WRITING csv (else blank lines).
subprocess.run's argument law?	Pass a LIST of args, never a glued shell string — string-gluing is how injection bugs are born.
Where do subprocess results live?	r.returncode (0 = success) · r.stdout · r.stderr (capture_output=True, text=True).
What is Task Scheduler, demystified?	A trigger + an action + a working directory — your Claude-CLI-AutoUpdate task is just that.
Inspect a scheduled task from the shell?	schtasks /query /tn "<name>" /v /fo LIST

## Quick-fire (aloud, 30 seconds)

1. Delete or quarantine? 2. DictReader value types? 3. subprocess args as? 4. rglob does what?
*(quarantine · strings · a list · recursive glob)*
