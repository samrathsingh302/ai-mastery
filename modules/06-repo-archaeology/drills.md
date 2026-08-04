# Drills — module 06

## Anki-importable block (tab-separated: Front ⇥ Back)

The six archaeology passes, in order?	Signs (README/claims) · map · doors (entry points) · one vertical slice · crown jewels · verdict (tests+audit).
Why trace ONE vertical slice instead of skimming folders?	One true end-to-end trace teaches the architecture; ten skimmed folders teach nothing testable.
What is an entry point?	Where execution starts: main functions, route roots, service starts, scheduled tasks — most repos have more than you expect.
psoc-portal: what does every request hit first?	app/src/proxy.ts — 31-line Next.js middleware auth gate, before any route.
What is a server action (and its trust rule)?	A function forms call that runs on the server — and it re-checks auth/validation because the browser is never trusted.
What is a migration?	A numbered SQL file changing the DB's shape — the sequence is the schema's version history (psoc has 45).
Server component vs client component?	Runs on the server, ships HTML vs runs in the browser, handles interaction.
What is a Windows service?	A background program the OS runs from boot, no window, as a system account — monk-mode's enforcer is one.
Why is monk-mode's watchdog a separate program?	A killed process can't resurrect itself — recovery must live OUTSIDE the thing being killed.
monk-mode's 10-second tick, in order?	Read config → verify HMAC → classify heartbeat → Hold/Lift → re-apply hosts block + app kills.
Fail-closed means…	On any doubt or verification failure, choose the SAFE state — monk-mode keeps blocking; a fire door that fails locked-open.
The atomic-write pattern (AtomicHosts)?	Write a temp file completely, then swap it in — no half-written file can ever exist.
Why is monk-mode's weak cipher acceptable?	The threat is tampering, not secrecy — the HMAC stamp over every protected field is the real defence (edit anything, stamp breaks, block holds).
What is an HMAC, in one sentence (preview)?	A keyed signature over data: without the key you can't forge a valid stamp for modified content (full treatment: module 14).
Why store the partner code as a PBKDF2 hash?	Verifiable but not recoverable: salted, deliberately-slow one-way hash — the file never contains anything reversible.
What did the TODO greps teach (both repos)?	Read grep results before believing them: psoc's 0 was real discipline; monk-mode's "13" were placeholder-text false positives.
The read-the-audit exercise is…	Ending every dig by explaining one REAL audit finding in your own code — real findings beat synthetic exercises.

## Quick-fire (aloud, 30 seconds)

1. First pass of any dig? 2. psoc's front door file? 3. monk-mode's safe state? 4. One slice or ten folders?
*(the signs/README · proxy.ts · blocking (fail-closed) · one slice)*
