# 06-repo-archaeology — like you're 5

Module 06, repo archaeology: every term, explained like you're 5.

- **Taught in:** `C:\Users\samra\repos\ai-mastery\modules\06-repo-archaeology\TEACH.md`

- **The one-line reminders:** `GLOSSARY.md` → `## Module 06 — repo archaeology`

- **Read-only:** the digs are read-only. Every "See it" below only looks.

- **Line numbers have drifted:** TEACH.md's `file:line` numbers were taken on 04/08/2026 and have drifted since.

- **So these point by name:** they use names and `git grep`, which still finds the line.

---

### Atomic write
**Like you're 5:** You write the new menu on a fresh card at the back of the café, and only when it's finished do you swap it onto the board in one go. Nobody ever sees a half-written menu.

**The real words:** Write a temp file completely, then swap it in; no half-written file can exist (monk-mode's AtomicHosts). → [06 dig 2](../modules/06-repo-archaeology/TEACH.md)

**See it:** `C:\Users\samra\repos\monk-mode\MonkMode\AtomicHosts.vb` — `cd C:\Users\samra\repos\monk-mode` then `git grep -n "Sub WriteAtomic"` and read that one routine.

### Entry point
**Like you're 5:** The front door of a building. Before you wander the corridors, find every door people actually come in by. Most buildings have more doors than you expect.

**The real words:** Where execution starts: mains, route roots, service starts, scheduled tasks. → [06 method](../modules/06-repo-archaeology/TEACH.md)

**See it:** The last two lines of `C:\Users\samra\repos\ai-mastery\tools\check_docs.py`: `if __name__ == "__main__":` is that script's front door.

### Fail-closed
**Like you're 5:** If the lock on the sweet cupboard gets confused, it stays locked. When anything looks wrong, pick the safe choice, even if it's annoying.

**The real words:** On any doubt, choose the SAFE state (monk-mode: keep blocking). → [06 dig 2](../modules/06-repo-archaeology/TEACH.md)

**See it:** `cd C:\Users\samra\repos\monk-mode` then `git grep -n "Function ClassifyHeartbeat"` — read what it returns when `macValid` is `False`.

### HMAC (preview)
**Like you're 5:** A wax seal only you can press, because only you have the stamp. If anyone changes even one letter of the letter, the seal no longer matches, and anyone who holds the same stamp can tell it was tampered with.

**The real words:** A keyed signature over data: no key, no valid stamp for modified content; full treatment in module 14. → [06 dig 2](../modules/06-repo-archaeology/TEACH.md)

**See it:** In `python`: `import hmac, hashlib` then `hmac.new(b"key", b"block x.com", hashlib.sha256).hexdigest()[:12]`, then again with `b"block y.com"` — one letter changed, a totally different stamp.

### Middleware
**Like you're 5:** The guard at the school gate. Every visitor walks past the guard before they reach any classroom, and the guard checks their badge first.

**The real words:** Code every request passes before the routes (psoc-portal's `proxy.ts` auth gate). → [06 dig 1](../modules/06-repo-archaeology/TEACH.md)

**See it:** `C:\Users\samra\repos\psoc-portal\app\src\proxy.ts` — its first line says Next 16 renamed `middleware.ts` to `proxy.ts`; the whole gate is one call, `updateSession(request)`.

### Migration
**Like you're 5:** Numbered building instructions for a doll's house: "1. build the walls. 2. add a window. 3. add a door." Follow them in order and you always get the same house. The list is the house's history.

**The real words:** A numbered SQL file changing the database's shape; the sequence is the schema's version history. → [06 dig 1](../modules/06-repo-archaeology/TEACH.md)

**See it:** `C:\Users\samra\repos\psoc-portal\supabase\migrations\` — the files run in number order, starting at `0001_initial_schema.sql`.

### PBKDF2 (preview)
**Like you're 5:** A mincer you have to turn six hundred thousand times. Easy to mince the secret code and check it matches; impossible to turn the mince back into the code, and far too slow for a thief to try every code.

**The real words:** A deliberately slow, salted, one-way hash; verifiable, never recoverable (monk-mode's partner code). → [06 dig 2](../modules/06-repo-archaeology/TEACH.md)

**See it:** In `python`: `import hashlib` then `hashlib.pbkdf2_hmac("sha256", b"code", b"salt", 600000).hex()[:12]` — feel the pause; that slowness is the defence.

### Server action / server component
**Like you're 5:** You fill in a form at the counter, but the decision is made in the back office, and the back office checks your ID again even though the counter already did. And some pages are drawn in the back office and handed out finished.

**The real words:** A form-called function that runs on the server and re-checks auth because browsers are never trusted / React rendered on the server. → [06 dig 1](../modules/06-repo-archaeology/TEACH.md)

**See it:** `C:\Users\samra\repos\psoc-portal\app\src\app\(portal)\tasks\actions.ts` — line 1 is `"use server";`; `git grep -n "export async function addTask"` finds the action.

### Vertical slice
**Like you're 5:** Follow one letter from the moment you post it to the moment it lands on a doormat: postbox, van, sorting office, van, door. One real journey teaches more than staring at ten empty vans.

**The real words:** One real user action traced through every layer, `file:line` per hop; the highest-value dig pass. → [06 method](../modules/06-repo-archaeology/TEACH.md)

**See it:** `start C:\Users\samra\repos\ai-mastery\modules\06-repo-archaeology\interactive\trace-the-request.html` → "psoc-portal · add a task" → ▶ Next hop.

### Watchdog
**Like you're 5:** A guard can't wake himself up if he's knocked out. So a second guard watches the first one, and if the first falls asleep, the second wakes him up.

**The real words:** A separate process that restarts a killed one; a process can't resurrect itself. → [06 dig 2](../modules/06-repo-archaeology/TEACH.md)

**See it:** `C:\Users\samra\repos\monk-mode\MM_guard\MM_guard\Program.vb` — `cd C:\Users\samra\repos\monk-mode` then `git grep -n "Sub Main" -- MM_guard` finds where the watchdog starts.

### Windows service
**Like you're 5:** Building security staff, not shop assistants. They start before the shop opens, work with no window to the street, and keep going whoever is behind the till.

**The real words:** A background program run by the OS from boot, no window, as a system account. → [06 dig 2](../modules/06-repo-archaeology/TEACH.md)

**See it:** Press Win+R, type `services.msc` — every row is one; monk-mode's enforcer is `C:\Users\samra\repos\monk-mode\MonkMode_srv\MonkMode_srv\Service1.vb`.
