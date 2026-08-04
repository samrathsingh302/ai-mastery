# Module 06 — Repo archaeology ×2: psoc-portal + monk-mode

> **What this is:** you learn to read an unfamiliar codebase the way a senior engineer does —
> then you do it twice, on your OWN flagships, with guided dig maps built from a fresh survey
> of both repos (04/08/2026, file:line evidence throughout). **~16h (≈8h per repo).**
> **Read-only law:** you change NOTHING in either repo during archaeology. You are a
> historian, not a renovator. (Both repos are LIVE — one in production, one enforcing blocks
> on this very machine.)
> **The endgame:** "You can explain every project you've shipped, cold, in an interview."
> These two digs are the first half of that sentence.

## Part 1 — The method (works on any repo, forever)

Six passes, outside-in — never start by reading code files alphabetically:

1. **The signs** (~20 min): README, CLAUDE.md, docs/. What does it CLAIM to be? Write the
   claim down — the dig checks it.
2. **The map** (~30 min): top-level directories, 2 levels. Annotate each: what plausibly
   lives there? (Your module-03 repo-census tool literally does the counting.)
3. **The doors** (~30 min): entry points — where does execution START? (main functions, route
   roots, service starts, scheduled tasks). List them ALL; most repos have more doors than
   you expect.
4. **One vertical slice** (~2h): pick ONE real user action and trace it through every layer,
   writing each hop as `file:line — what happens here`. This is the highest-value hour in
   the method: one true slice teaches more than ten skimmed folders.
5. **Crown jewels** (~2h): the 2–3 files everything else orbits. Read them properly (close-
   window-rebuild the core function's logic in pseudocode).
6. **The verdict** (~1h): tests (where, how many, what they protect), the audit trail, and
   your dig log's answer to: *does the code match the claim?*

**Dig-log discipline:** every session appends to `exercises/dig-log.md` — hop tables, "I
believed X, code says Y" corrections, and questions for your tutor session. The log IS the
learning; the repo is just where you dug. **Tutor rule:** Claude may explain CONCEPTS you hit
(what's a server action? what's a Windows service?) but never summarise the repo for you —
the dig is a struggle rep.

## Part 2 — Dig 1: psoc-portal (the production web app)

**The claim** (CLAUDE.md:13-14): committee portal for PSOC 2026-27 — events, tasks, calendar,
money, marketing — replacing shared folders + an Excel tracker. Live, in production, used by
a real committee. **Stack:** Next.js 16 (App Router) + React 19 + TypeScript + Tailwind 4 +
Supabase; Vitest + Playwright; deployed on Vercel (app/package.json).

**Your map checkpoints** (verify each with your own eyes): `app/src/app` = routes ·
`app/src/lib` = business logic · `supabase/migrations` = 45 SQL files, the data model's full
history · `coordination/ACTIVE.md` = the session claim/audit log (1,252 lines) · `p7/` =
pixel-baseline screenshots · `.github/workflows` = CI + weekly backup cron (`0 3 * * 0`).

**The doors:** every request passes `app/src/proxy.ts:5` (the auth gate — 31 lines, read it
FIRST; it's the whole site's front door) · routes under `app/src/app/(portal)/` · admin
scripts `app/scripts/*.mjs` · the weekly backup workflow.

**The vertical slice to trace — adding a task** (verify every hop live):

| # | Hop | Where | What happens |
|---|-----|-------|--------------|
| 1 | Page | `app/src/app/(portal)/tasks/page.tsx:31` | Server component fetches tasks/assignees/profiles |
| 2 | Form | `.../tasks/add-task-form.tsx:32` | Client component; submits via `useActionState` |
| 3 | Action | `.../tasks/actions.ts:101` `addTask()` | Server action: RE-CHECKS auth, parses the form |
| 4 | Insert | `.../tasks/actions.ts:48` → `:55-62` | `supabase.from("tasks").insert(...)` |
| 5 | Table | `supabase/migrations/0001_initial_schema.sql:74-83` | Where `public.tasks` was born |
| 6 | Refresh | `.../tasks/actions.ts:122` | `revalidateTasks()` + `redirect("/tasks")` |
| 7 | Render | `.../tasks/task-list.tsx` | The list re-reads the fresh rows |

New concepts you'll meet (plain words, in dig order): **server component** (React that runs
on the server and ships HTML), **client component** (runs in the browser, handles clicks),
**server action** (a function the form calls that executes on the server — note hop 3
re-checks auth even though hop 1 already did: servers never trust the browser), **migration**
(a numbered SQL file changing the database's shape — 45 of them = the schema's git history),
**revalidate** (tell Next.js a cached page is stale).

**Crown jewels to read properly:** `actions.ts` (439 lines — auth re-checks, optimistic
concurrency, soft delete: your no-data-loss law in production code) · `proxy.ts` +
`lib/supabase/session.ts` (the auth spine, ~100 lines total) · `0001_initial_schema.sql`
(the original data model in one page).

**The verdict pass:** ~170 test files under `app/src` (thousands of assertions; CI runs
lint/typecheck/unit/build/perf + Playwright against the prod build). Audit trail =
`coordination/ACTIVE.md`: read the last 3 session entries — verifier verdicts, migration
numbers, incident write-ups. TODO/FIXME count in `app/src`: **zero** (grep it yourself —
then say in one sentence what that tells you about how this repo is run).

## Part 3 — Dig 2: monk-mode (the adversarial system program)

**The claim** (CLAUDE.md:6-7): a tamper-resistant website/app blocker — hardened Cold Turkey
fork (GPLv3) — where a started block can't be casually removed before expiry; bypass classes
B1–B9 defended, B10 (offline/admin) out of scope by design. **Stack:** VB.NET / .NET 8, four
projects + a C# xunit test project, CLI only, no GUI.

**The architecture in one breath** — four cooperating programs (find each `Main`):
CLI `MonkMode/Program.vb:47` (verb dispatch at `:62-75`) · Windows service
`MonkMode_srv/.../Service1.vb:87` (LocalSystem, the enforcer) · watchdog
`MM_guard/.../Program.vb:74` (restarts the service if killed) · notifier
`MM_notify/.../Program.vb:49` (tray toasts). A **Windows service** *(plain words: a program
the OS runs in the background, no window, from boot, as a system account — analogy: building
security staff vs shop assistants)*; a **watchdog** guards the guard.

**The vertical slice — `monkmode block --sites x.com --for 2h`:**

| # | Hop | Where | What happens |
|---|-----|-------|--------------|
| 1 | Dispatch | `MonkMode/Program.vb:47` → `:64` | `Case "block"` |
| 2 | Parse | `Program.vb:156` `DoBlock()` | Setup gate, flags, presets |
| 3 | Hosts | `Program.vb:321` → `AtomicHosts.vb` | Write the hosts-file block atomically |
| 4 | Config | `Program.vb:342` | Encrypt config + **compute its MAC** + mint partner code |
| 5 | Enforce | `Service1.vb:716` `timer_Elapsed` | Every 10s: MAC-verify → `ClassifyHeartbeat` (`:1338`) → Hold/Lift, **fail-closed** |
| 6 | Guard | `Guardian.vb` / `Notifications.vb` | Service killed? Restarted. User? Toasted. |

**Crown jewels, in on-ramp order:** 1) `AtomicHosts.vb` (119 lines — the atomic-write
self-heal pattern: write a temp file, swap it in, so no half-written hosts file ever exists;
small enough to fully understand in one sitting). 2) `ConfigIntegrity.vb` (377 lines, richly
commented — below). 3) `Service1.vb`'s `ClassifyHeartbeat` (`:1338`) — the fail-closed
state machine (*fail-closed, plain words: when anything looks wrong, choose the SAFE state —
here, keep blocking; analogy: a fire door that locks open, not shut, when its sensor dies*).

**The tamper-evidence scheme (preview — module 14 teaches the crypto properly):** two
mechanisms in `ConfigIntegrity.vb`: the config's protected fields are serialised in fixed
order (`BuildCanonical:178`) and stamped with **HMAC-SHA256** (`ComputeConfigMac:198`) — a
keyed signature: change ANY hand-edited byte and the stamp no longer matches, and
verification failure = block stays fully active (fail-closed, `ConfigMacIsValid:210`
compares in constant time). Separately the one-time partner exit code is stored only as a
**PBKDF2** hash — 600,000 iterations over a random salt (`ComputePartnerHash:315`) — a
deliberately SLOW one-way mash, so the stored file can't be reversed into the code. The
config cipher itself (`Crypto.vb`, `Simple3Des`) is documented-weak BY DESIGN (Phase-3-owned,
CLAUDE.md:23) — confidentiality is not the defence; tamper-EVIDENCE is. Sit with that
sentence until it clicks: it's the most instructive design decision in your whole estate.

**The verdict pass:** 682 test methods in `MonkMode.Tests` (pure unit tests — they never
touch real hosts/registry/SCM; the elevated live smoke test is manual and separate: 63/63 on
14/06/2026 per CLAUDE.md:16). Audit trail thin by design (`coordination/ACTIVE.md`, 21
lines). TODO/FIXME: zero genuine (13 grep hits are all `XXXXX-XXXXX` partner-code display
placeholders — a lesson in reading grep results before believing them).

## Part 4 — Read-the-audit (the Tier-2 exercise, done early)

For each repo, end the dig by reading its audit surface and EXPLAINING one finding as if to
the committee/a friend: psoc-portal → the last verifier verdict in ACTIVE.md (what was
checked? what would a FAIL have meant for real users?); monk-mode → the standing
Simple3Des note (why is a weak cipher acceptable HERE, and what specifically makes the HMAC
layer the real defence?). Real findings in your own code beat synthetic exercises — the
plan's own words.

**Checkpoint — you can now:** run the six-pass method on any repo; trace both slices from
memory (hop tables, close-window-rebuild); explain server actions re-checking auth, atomic
writes, fail-closed enforcement, and tamper-evidence-over-confidentiality; and answer "walk
me through your project" for both flagships without opening a file.

## Sources

Fresh read-only survey of both repos, 04/08/2026 (researcher pass, file:line cited inline
above; verify every claim live — that's the exercise). Repo docs: each repo's CLAUDE.md +
README. The plan v3 Tier 2 (method + read-the-audit).
