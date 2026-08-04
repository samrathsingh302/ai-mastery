# Ex01 — model answers (open AFTER answering)

**1.** `app/src/proxy.ts` (`proxy()`, line 5) — Next.js middleware, the auth gate: every
request passes it before any route runs. MUST name proxy.ts and "every request / auth gate".
GOOD adds: it leans on `lib/supabase/session.ts`; 31 lines guarding the whole site.

**2.** Server actions are callable endpoints — the browser is untrusted, and a crafted
request could invoke the action without ever loading the page. Re-checking auth server-side
blocks forged/expired-session submissions. MUST contain: servers never trust the browser.
GOOD adds: defence in depth; the same reason validation re-runs server-side.

**3.** A migration is a numbered SQL file that changes the database's shape; the sequence is
the schema's version history. 45 of them = the data model evolved 45 recorded, replayable
steps — you can rebuild the DB's shape from zero and see WHEN each table/column appeared.
MUST contain: versioned schema change. GOOD adds: migrations are append-only history — the
schema's git.

**4.** Changes land through a gate: tests + CI + session claims + verifier verdicts
(ACTIVE.md logs "SHIP 0 P0/P1/P2" style verdicts per slice). Zero TODOs means debt is either
fixed or tracked OUTSIDE code comments — the repo's discipline lives in process, not
margins. MUST contain: tested + process-gated. GOOD adds: 2,800+ assertions; weekly backup
cron as the same discipline applied to data.

**5.** CLI (Program.vb — parse commands, write config), service (Service1.vb — LocalSystem
enforcer, 10s tick), guardian (MM_guard — restarts a killed service), notifier (MM_notify —
user-session toasts). Separate watchdog because a process cannot reliably resurrect ITSELF —
the thing being killed can't also be the thing that recovers from the kill; two processes
watching each other survive what one cannot. MUST contain: all four + self-resurrection
impossibility.

**6.** Tick (`timer_Elapsed`, every 10s): read config → verify its HMAC
(`ConfigMacIsValid`) → classify heartbeat (`ClassifyHeartbeat`) → Hold or Lift → re-apply
hosts block + app kills. Any verification failure = treat block as fully active
(fail-closed). MUST contain: MAC check BEFORE trusting contents + fail-closed on failure.

**7.** The threat is TAMPERING (user editing config to end the block early), not secrecy.
Defence: HMAC-SHA256 over a fixed-order serialisation of every protected field, key
DPAPI-protected — any hand-edit breaks the stamp, and a broken stamp means the block stays
on. Confidentiality of the file is nearly irrelevant; integrity is everything. MUST contain:
tamper-evidence beats encryption for this threat + fail-closed consequence.

**8.** The code must be VERIFIABLE but never RECOVERABLE from disk: encryption is
reversible by design (whoever holds the key can decrypt — and the app holds the key), while
a salted, deliberately-slow one-way hash (PBKDF2, 600k iterations) lets the app check a
submitted code without the file ever containing anything reversible; the iterations price
out brute-force. MUST contain: one-way vs reversible + slow-on-purpose.
