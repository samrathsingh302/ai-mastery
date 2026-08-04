# Project 08 — The full trace, narrated (your site, your evidence)

**What:** produce `trace.md` — the complete story of one page load of YOUR live site, every
claim backed by a command output YOU captured. ~3h. This is the artefact that makes
"psoc-portal is no longer magic" true, and it slots straight into interview answers.

## The captures (all read-only; be polite — a handful of requests, not a load test)

1. **DNS:** `nslookup` both hostnames; screenshot/paste. Name whose IP ranges answered.
2. **TLS:** browser padlock → certificate: issuer, expiry, subject. One sentence on what
   the certificate actually proves (and what it doesn't).
3. **The redirect chain:** `curl.exe -sSIL https://psoc-portal.vercel.app/` — paste the
   hops; annotate each status line.
4. **The headers tour:** final 200 from `/` — one line per header you can see, in your own
   words (the fixture's annotations are your crib, not your copy source).
5. **The auth bounce:** `/dashboard` logged out (curl) vs logged IN (browser DevTools →
   Network tab, first request) — capture both; explain the difference and find the session
   cookie's flags (HttpOnly/Secure/SameSite) in DevTools → Application → Cookies.
6. **The cache tell:** request `/` twice a minute apart; compare `Age`. Who served each?

## The narration

Assemble into trace.md as the journey (TEACH's map), each stage: your evidence + 2–3
sentences. Close with three answered whys: why 308 at the old address but 307 at the gate ·
why re-check auth behind the gate · why `Age` can be non-zero while `max-age=0`.

## Acceptance checklist

- [ ] Every stage has YOUR capture (dated), not the fixture's
- [ ] At least one live value differed from the 04/08 fixture, and you noted it
- [ ] The three whys answered without notes first, then checked against TEACH
- [ ] The stale-URL guide line (guides/PUBLIC-SITE-UPDATES.md:7) flagged to a psoc session
      or fixed via one — your repo, your call; note what you chose
- [ ] trace.md committed here; cold-explain rehearsed once (5 min, out loud)
