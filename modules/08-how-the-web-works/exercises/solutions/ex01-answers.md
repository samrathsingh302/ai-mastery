# Ex01 — answers + the why (open after check.py)

1 **F** — it answers 308 and forwards; the body lives at the custom domain now.
2 **C** — 308 Permanent Redirect (and its `Refresh:` twin for old browsers).
3 **B** — `Location: https://www.leedspunjabisociety.com/`.
4 **C** — 307 → /login: proxy.ts bouncing a session-less request, in 0.17s.
5 **B** — 104.21.x / 172.67.x / 2606:4700:: are published Cloudflare ranges; Vercel sits behind.
6 **B** — seconds this response sat in the edge cache: Cloudflare answered, origin slept.
7 **A** — X-Frame-Options: DENY (anti-clickjacking; CSP's frame-ancestors 'none' is its modern twin — the page sends both).
8 **B** — `connect-src … *.supabase.co wss://*.supabase.co`: one header names the backend AND its live websocket.
9 **F** — HEAD is "headers only"; that's why -I is the polite way to probe.
10 **B** — speak HTTPS only, for max-age seconds (2 years here), preload = shipped inside browsers.
11 **T** — 308 marked the old ADDRESS permanently moved; 307 marked the bounce TEMPORARY (log in and /dashboard serves again). Both promise the method won't change.
12 **F** — gates filter; the check beside the data (addTask re-auth) is the one a forged request can't skip. Module 06 hop 4 = module 08 §7, same law.
