# Exercise 01 — Read the wire

**Part A (live, ~30 min):** re-run every command in `fixtures/trace-2026-08-04.txt` yourself
(they're all in TEACH §2–§7). Note what CHANGED since 04/08/2026 (Age will differ; X-Vercel-Id
always differs; maybe more). Changes are data, not errors.

**Part B (quiz):** answer from the fixture + TEACH, then `python check.py`. T/F or a–d.

1. T/F — The vercel.app address still serves the site's pages directly.
2. What status did `/` on psoc-portal.vercel.app return? (a) 200 (b) 307 (c) 308 (d) 404
3. Its `Location:` sends you to… (a) /login (b) www.leedspunjabisociety.com (c) supabase.co (d) nowhere
4. Logged out, `/dashboard` on the live domain answered… (a) 200 (b) 401 (c) 307 → /login (d) 500
5. The custom domain's IP addresses belong to… (a) Vercel (b) Cloudflare (c) Supabase (d) the university
6. `Age: 6282` means… (a) server uptime (b) the cached copy's age in seconds (c) TLS days left (d) cookie lifetime
7. Which header forbids the portal being iframed? (a) X-Frame-Options (b) Age (c) Referrer-Policy (d) Content-Type
8. The CSP-Report-Only header names which backend? (a) Firebase (b) Supabase (c) AWS (d) MongoDB
9. T/F — a HEAD request (`curl -I`) returns the body too.
10. HSTS commits the browser to… (a) caching for 2 years (b) HTTPS-only for max-age (c) refusing cookies (d) refusing redirects
11. T/F — 307 and 308 both redirect; the difference that matters in YOUR two captures is permanence.
12. T/F — because proxy.ts bounces strangers, server actions may safely skip their own auth checks.
