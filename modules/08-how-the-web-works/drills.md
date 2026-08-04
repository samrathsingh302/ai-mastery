# Drills — module 08

## Anki-importable block (tab-separated: Front ⇥ Back)

The page-load journey in one line?	URL → DNS → TCP → TLS → HTTP request → (edge → gate → origin) → response → render, repeated per asset.
URL anatomy?	scheme://host/path?query — protocol · machine-by-name · thing-there · options.
What does DNS do?	Names → numeric IP addresses (the phone book); nslookup does it by hand.
Whose IPs answer for www.leedspunjabisociety.com?	Cloudflare's (104.21.x/172.67.x/2606:4700::) — the edge, not the Vercel origin.
TCP in one sentence?	A reliable, ordered two-way pipe to a numbered port (443 for HTTPS) — a phone call, not a postcard.
TLS gives you which two things?	Secrecy (encryption) + identity (certificate vouched by a trusted authority).
What does HSTS commit a browser to?	HTTPS-only for max-age seconds (2 years on your site; preload = baked into browsers).
The status families?	2xx worked · 3xx go elsewhere · 4xx you erred · 5xx server erred.
307/308 vs 301/302 — the 7/8 promise?	The method won't change on the redirect (a POST stays a POST).
Your site's two real redirects and why they differ?	vercel.app → 308 permanent (address moved for good) · /dashboard logged-out → 307 temporary (log in and it serves again).
What is the Age header the tell of?	A cache served you: seconds the copy sat on the edge shelf — origin never woke.
HEAD (-I) returns…	Headers only, no body — the polite probe.
The session cookie's three protective flags?	HttpOnly (scripts can't read it) · Secure (HTTPS only) · SameSite (other sites can't ride it).
Why re-check auth AFTER the proxy gate?	Gates filter traffic; forged requests skip gates — the check beside the data is the one they can't skip.
What is a CDN?	Cache servers near users answering for the origin — vending machines stocked from one warehouse.
Your site's serving chain?	Cloudflare (DNS + edge cache) in front of Vercel (Next.js origin).
Which one header revealed the backend?	CSP's connect-src: *.supabase.co (+ its live websocket wss://).
X-Frame-Options: DENY defends against…	Clickjacking — nobody may iframe the site (CSP frame-ancestors 'none' is the modern twin).
curl flags: -I · -L · -v?	HEAD headers-only · follow redirects · narrate the whole conversation.
Docs said vercel.app, the wire said the custom domain — the lesson?	Trust the wire over the docs; docs drift, evidence doesn't.

## Quick-fire (aloud, 30 seconds)

1. Port for HTTPS? 2. Age header means? 3. 4xx vs 5xx? 4. Cookie flag scripts can't beat?
*(443 · cache age in seconds · you erred vs server erred · HttpOnly)*
