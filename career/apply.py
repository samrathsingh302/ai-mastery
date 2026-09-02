#!/usr/bin/env python3
"""Graduate-application tracker for the 2027 barbell (CAREER.md 6B / 7C / 7I).

    python career/apply.py list     [--limb L] [--status S]
    python career/apply.py due      [--days N]
    python career/apply.py draft    <id> [--force]
    python career/apply.py status   <id> <new-status> [--note TEXT]
    python career/apply.py render   [--out PATH]
    python career/apply.py validate

targets.json is the data; TARGETS.md is generated from it. This tool drafts
and tracks. SUBMISSION IS ALWAYS SAMRATH'S: it never logs in, never submits.
"""
import sys as _sys  # keep the marks printable on a cp1252 console
if hasattr(_sys.stdout, "reconfigure"):
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import argparse
import json
import re
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TARGETS = HERE / "targets.json"
DEFAULT_RENDER = Path(r"C:\Users\samra\OneDrive\dev\repos\ai-mastery\career\TARGETS.md")
FACTS = r"C:\Users\samra\OneDrive\dev\repos\ai-mastery\career\FACTS.md"
CV = r"C:\Users\samra\OneDrive\dev\repos\ai-mastery\career\CV.md"

SCHEMA_VERSION = 1
LIMBS = ("london", "north", "clearance", "consulting")
STATUSES = (
    "unverified", "verified", "draft-ready", "submitted", "online-test",
    "interview", "assessment-centre", "offer", "rejected", "closed", "withdrawn",
)
ELIGIBILITY = ("yes", "no", "unclear")
# statuses that mean "not sent yet" - everything else is at or past submission
OPEN_STATUSES = ("unverified", "verified", "draft-ready")
TARGET_KEYS = (
    "id", "employer", "scheme", "limb", "location", "url", "opens", "closes",
    "eligibility_2027", "salary", "priority", "status", "status_date", "notes",
    "sources", "log",
)
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LIMB_TITLE = {
    "london": "London / high-pay limb",
    "north": "North / diversified limb",
    "clearance": "Clearance-cyber limb (insurance)",
    "consulting": "Consulting limb",
}


class UserError(Exception):
    """Anything the operator can fix. Printed to stderr, never a traceback."""


# ---------------------------------------------------------------- data access

def load(path):
    path = Path(path)
    if not path.exists():
        raise UserError("no targets file at " + str(path))
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise UserError("{0} is not valid JSON: {1}".format(path, exc))


def save(data, path):
    with Path(path).open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def targets_of(data):
    if not isinstance(data, dict) or not isinstance(data.get("targets"), list):
        raise UserError("targets.json must be an object with a 'targets' list")
    return data["targets"]


def find(data, tid):
    for t in targets_of(data):
        if t.get("id") == tid:
            return t
    raise UserError("no target with id '{0}' (run: apply.py list)".format(tid))


def drafts_dir(path):
    return Path(path).resolve().parent / "drafts"


# ------------------------------------------------------------------- helpers

def parse_iso(value):
    """Return a date, or None if the value is not an ISO date string."""
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def uk(value):
    """ISO date -> dd/mm/yyyy. 'rolling' passes through; empties become '-'."""
    if value in (None, ""):
        return "-"
    d = parse_iso(value)
    return d.strftime("%d/%m/%Y") if d else str(value)


def by_priority(rows):
    return sorted(rows, key=lambda t: (t.get("priority") is None, t.get("priority") or 0))


def table(headers, rows):
    """Space-aligned plain-text table."""
    cols = [headers] + rows
    widths = [max(len(str(r[i])) for r in cols) for i in range(len(headers))]
    out = ["  ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers)).rstrip()]
    out.append("  ".join("-" * w for w in widths))
    for r in rows:
        out.append("  ".join(str(c).ljust(widths[i]) for i, c in enumerate(r)).rstrip())
    return "\n".join(out)


def due_rows(data, days, today=None):
    """Dated closes inside the window, then the open rolling ones."""
    today = today or date.today()
    horizon = today + timedelta(days=days)
    dated, rolling = [], []
    for t in targets_of(data):
        closes = t.get("closes")
        if closes == "rolling":
            if t.get("status") in OPEN_STATUSES:
                rolling.append(t)
            continue
        d = parse_iso(closes)
        if d and today <= d <= horizon:
            dated.append((d, t))
    dated.sort(key=lambda pair: (pair[0], pair[1].get("priority") or 0))
    return [t for _, t in dated] + by_priority(rolling)


# ------------------------------------------------------------------ commands

def cmd_list(args):
    data = load(args.file)
    rows = by_priority(targets_of(data))
    if args.limb:
        rows = [t for t in rows if t.get("limb") == args.limb]
    if args.status:
        rows = [t for t in rows if t.get("status") == args.status]
    if not rows:
        print("no targets match that filter")
        return 0
    print(table(
        ["id", "employer", "scheme", "limb", "closes", "status", "status_date"],
        [[t.get("id", ""), t.get("employer", ""), t.get("scheme", ""),
          t.get("limb", ""), uk(t.get("closes")), t.get("status", ""),
          uk(t.get("status_date"))] for t in rows],
    ))
    print("\n{0} of {1} targets".format(len(rows), len(targets_of(data))))
    return 0


def cmd_due(args):
    data = load(args.file)
    rows = due_rows(data, args.days)
    if not rows:
        print("nothing due in the next {0} days, and no open rolling targets"
              .format(args.days))
        return 0
    print("due inside {0} days (plus open rolling):\n".format(args.days))
    print(table(
        ["closes", "id", "employer", "scheme", "status"],
        [[uk(t.get("closes")), t.get("id", ""), t.get("employer", ""),
          t.get("scheme", ""), t.get("status", "")] for t in rows],
    ))
    return 0


BRIEF = """# {employer} - {scheme}

> Brief generated by `career/apply.py draft {id}` on {today}.
> Fields come from `career/targets.json`. Re-run with --force rather than
> hand-editing the table below.

| Field | Value |
|---|---|
| id | `{id}` |
| Employer | {employer} |
| Scheme | {scheme} |
| Limb | {limb} |
| Location | {location} |
| URL | {url} |
| Opens | {opens} |
| Closes | {closes} |
| 2027 eligible | {eligibility} |
| Salary | {salary} |

**Notes:** {notes}

**Sources:**
{sources}

## JD snapshot

paste or WebFetch the live JD here

## Application questions

<!-- one line per question, with its word limit, copied from the live form -->

## Drafting prompt

Run this in a Claude session with this folder as the working context.

1. Read the fact base: `{facts}`
2. Read the master CV: `{cv}`
3. Read this brief in full, including the JD snapshot and the questions above.
4. Write `cv-{id}.md` in this folder: a one-page CV variant, reordered and
   reworded for {employer} and the {scheme}. Every bullet must trace to a line
   in FACTS.md. Nothing new may be introduced - no invented metrics, no
   invented employers, nothing from the FACTS.md do-not-claim list (section 0).
5. Write `answers-{id}.md`: each application question from the section above,
   with an answer at or under the stated word limit. Put the word count after
   each answer.
6. Write `cover-{id}.md` ONLY if this scheme asks for a cover letter.
7. If the JD wants something FACTS.md does not evidence, do not invent it.
   Put it under a `## Gaps - Samrath decides` heading in `answers-{id}.md`.
8. Style: British English, dd/mm/yyyy dates, no em-dashes, no AI-tell
   vocabulary (delve, leverage, tapestry, testament, seamless, robust,
   passionate about, in today's fast-paced world).
9. Then run:

       python career/apply.py status {id} draft-ready --note "drafted <what>"

Submission is Samrath's. Never submit, never log in, never send email.
"""


def cmd_draft(args):
    data = load(args.file)
    t = find(data, args.id)
    folder = drafts_dir(args.file) / t["id"]
    if folder.exists() and not args.force:
        raise UserError("{0} already exists - pass --force to overwrite".format(folder))
    folder.mkdir(parents=True, exist_ok=True)
    sources = t.get("sources") or []
    brief = BRIEF.format(
        id=t["id"],
        employer=t.get("employer", ""),
        scheme=t.get("scheme", ""),
        limb=t.get("limb", ""),
        location=t.get("location", ""),
        url=t.get("url") or "(not verified yet)",
        opens=uk(t.get("opens")),
        closes=uk(t.get("closes")),
        eligibility=t.get("eligibility_2027", ""),
        salary=t.get("salary") or "-",
        notes=t.get("notes", ""),
        sources="\n".join("- " + s for s in sources) or "- (none recorded yet)",
        today=date.today().strftime("%d/%m/%Y"),
        facts=FACTS,
        cv=CV,
    )
    (folder / "brief.md").write_text(brief, encoding="utf-8", newline="\n")
    save({"id": t["id"], "created": date.today().isoformat(), "files": []},
         folder / "tracking.json")
    print("draft folder: {0}".format(folder))
    print("next: open {0}, paste the JD, then follow its drafting prompt"
          .format(folder / "brief.md"))
    print('then: python career/apply.py status {0} draft-ready --note "..."'
          .format(t["id"]))
    return 0


def cmd_status(args):
    if args.new_status not in STATUSES:
        raise UserError("'{0}' is not a status. Allowed: {1}"
                        .format(args.new_status, ", ".join(STATUSES)))
    data = load(args.file)
    t = find(data, args.id)
    today = date.today().isoformat()
    was = t.get("status")
    t["status"] = args.new_status
    t["status_date"] = today
    if not isinstance(t.get("log"), list):
        t["log"] = []
    t["log"].append({"date": today, "status": args.new_status, "note": args.note or ""})
    data["updated"] = today
    save(data, args.file)
    print("{0}: {1} -> {2} ({3})".format(t["id"], was, args.new_status, uk(today)))
    return 0


def render_markdown(data, today=None):
    today = today or date.today()
    rows = by_priority(targets_of(data))
    out = [
        "> GENERATED by career/apply.py render on {0} - edit targets.json,"
        " not this file.".format(today.strftime("%d/%m/%Y")),
        "",
        "# Application targets - 2027 graduate schemes",
        "",
        "Schema {0} - targets.json last updated {1} - {2} targets.".format(
            data.get("schema_version"), uk(data.get("updated")), len(rows)),
        "",
    ]
    header = ("| # | Employer | Scheme | Location | Opens | Closes |"
              " 2027 eligible | Salary | Status | Link |")
    rule = "|---|---|---|---|---|---|---|---|---|---|"
    for limb in LIMBS:
        limb_rows = [t for t in rows if t.get("limb") == limb]
        if not limb_rows:
            continue
        out += ["## {0} ({1})".format(LIMB_TITLE[limb], len(limb_rows)), "",
                header, rule]
        for t in limb_rows:
            url = t.get("url") or ""
            link = "[apply]({0})".format(url) if url else "-"
            out.append("| " + " | ".join([
                str(t.get("priority", "")), t.get("employer", ""),
                t.get("scheme", ""), t.get("location", ""), uk(t.get("opens")),
                uk(t.get("closes")), t.get("eligibility_2027", ""),
                t.get("salary") or "-", t.get("status", ""), link,
            ]) + " |")
        out.append("")
    out += ["## Next due", ""]
    due = due_rows(data, 30, today=today)
    if due:
        out += ["| Closes | Employer | Scheme | Status |", "|---|---|---|---|"]
        for t in due:
            out.append("| " + " | ".join([
                uk(t.get("closes")), t.get("employer", ""), t.get("scheme", ""),
                t.get("status", ""),
            ]) + " |")
    else:
        out.append("Nothing closing in the next 30 days, no open rolling targets.")
    counts = {}
    for t in rows:
        counts[t.get("status")] = counts.get(t.get("status"), 0) + 1
    tally = " | ".join("{0} {1}".format(s, counts[s]) for s in STATUSES if s in counts)
    out += ["", "## Counts", "", "{0} | total {1}".format(tally, len(rows)), ""]
    return "\n".join(out)


def cmd_render(args):
    data = load(args.file)
    out = Path(args.out) if args.out else DEFAULT_RENDER
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_markdown(data), encoding="utf-8", newline="\n")
    print("wrote {0}".format(out))
    return 0


def problems(data):
    """Return a list of human-readable schema problems. Empty list = clean."""
    bad = []
    for key in ("schema_version", "updated", "targets"):
        if key not in data:
            bad.append("top level: missing key '{0}'".format(key))
    if data.get("schema_version") != SCHEMA_VERSION:
        bad.append("top level: schema_version should be {0}, found {1!r}"
                   .format(SCHEMA_VERSION, data.get("schema_version")))
    if parse_iso(data.get("updated")) is None:
        bad.append("top level: 'updated' is not an ISO date ({0!r})"
                   .format(data.get("updated")))
    if not isinstance(data.get("targets"), list):
        bad.append("top level: 'targets' is not a list")
        return bad
    seen_ids, seen_priorities = {}, {}
    for i, t in enumerate(data["targets"]):
        tid = t.get("id") if isinstance(t.get("id"), str) else "<index {0}>".format(i)
        where = tid + ":"
        for key in TARGET_KEYS:
            if key not in t:
                bad.append("{0} missing key '{1}'".format(where, key))
        if not isinstance(t.get("id"), str) or not KEBAB.match(t.get("id") or ""):
            bad.append("{0} id is not kebab-case".format(where))
        elif t["id"] in seen_ids:
            bad.append("{0} duplicate id (also at index {1})"
                       .format(where, seen_ids[t["id"]]))
        else:
            seen_ids[t["id"]] = i
        if t.get("limb") not in LIMBS:
            bad.append("{0} limb {1!r} not one of {2}"
                       .format(where, t.get("limb"), ", ".join(LIMBS)))
        if t.get("status") not in STATUSES:
            bad.append("{0} status {1!r} not one of {2}"
                       .format(where, t.get("status"), ", ".join(STATUSES)))
        if t.get("eligibility_2027") not in ELIGIBILITY:
            bad.append("{0} eligibility_2027 {1!r} not one of {2}"
                       .format(where, t.get("eligibility_2027"), ", ".join(ELIGIBILITY)))
        for key in ("opens", "status_date"):
            v = t.get(key)
            if v is not None and parse_iso(v) is None:
                bad.append("{0} {1} {2!r} is not an ISO date or null"
                           .format(where, key, v))
        closes = t.get("closes")
        if closes is not None and closes != "rolling" and parse_iso(closes) is None:
            bad.append("{0} closes {1!r} is not an ISO date, 'rolling' or null"
                       .format(where, closes))
        url = t.get("url")
        if not isinstance(url, str) or (url and not url.startswith("https://")):
            bad.append("{0} url {1!r} must be https or an empty string"
                       .format(where, url))
        srcs = t.get("sources")
        if not isinstance(srcs, list):
            bad.append("{0} sources must be a list".format(where))
        else:
            for s in srcs:
                if not isinstance(s, str) or not s.startswith("https://"):
                    bad.append("{0} source {1!r} must be https".format(where, s))
        if not isinstance(t.get("log"), list):
            bad.append("{0} log must be a list".format(where))
        p = t.get("priority")
        if not isinstance(p, int) or isinstance(p, bool):
            bad.append("{0} priority {1!r} is not an integer".format(where, p))
        elif p in seen_priorities:
            bad.append("{0} duplicate priority {1} (also on {2})"
                       .format(where, p, seen_priorities[p]))
        else:
            seen_priorities[p] = tid
    return bad


def cmd_validate(args):
    data = load(args.file)
    bad = problems(data)
    if bad:
        print("{0} problem(s) in {1}:".format(len(bad), args.file), file=_sys.stderr)
        for n, msg in enumerate(bad, 1):
            print("  {0}. {1}".format(n, msg), file=_sys.stderr)
        return 1
    print("OK: {0} targets".format(len(data["targets"])))
    return 0


# ---------------------------------------------------------------------- main

def build_parser():
    parser = argparse.ArgumentParser(
        prog="apply.py", description=__doc__.splitlines()[0])
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--file", default=str(DEFAULT_TARGETS),
                        help="targets.json to read/write (default: beside this script)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list", parents=[common], help="table of every target")
    p.add_argument("--limb", choices=LIMBS)
    p.add_argument("--status", choices=STATUSES)
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("due", parents=[common], help="what closes soon, plus rolling")
    p.add_argument("--days", type=int, default=30)
    p.set_defaults(func=cmd_due)

    p = sub.add_parser("draft", parents=[common], help="create a draft folder + brief")
    p.add_argument("id")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_draft)

    p = sub.add_parser("status", parents=[common], help="move a target's status")
    p.add_argument("id")
    p.add_argument("new_status", metavar="new-status")
    p.add_argument("--note", default="")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("render", parents=[common], help="write TARGETS.md")
    p.add_argument("--out")
    p.set_defaults(func=cmd_render)

    p = sub.add_parser("validate", parents=[common], help="schema + enum checks")
    p.set_defaults(func=cmd_validate)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except UserError as exc:
        print("error: {0}".format(exc), file=_sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
