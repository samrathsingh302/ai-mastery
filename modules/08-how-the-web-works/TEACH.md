# Module 08 — How the web works: HTTP by hand, against YOUR live site

> **What this is:** one page load of YOUR production site, dismantled layer by layer — every
> claim demonstrated with a command you run yourself. Tonight's live captures are in
> `exercises/fixtures/trace-2026-08-04.txt`; re-running them is the exercises. **~12h.**
> **The discovery that makes it fun:** the repo's guides still say the site lives at
> `psoc-portal.vercel.app` — but the wire says that address now **308-redirects** to
> `www.leedspunjabisociety.com`, which is served by **Cloudflare in front of Vercel**. The
> stale doc + the live truth = your first lesson in trusting the wire over the docs.

## The journey (the map to hold)

```
URL → DNS (name→address) → TCP (a call is placed) → TLS (the call goes secret)
    → HTTP request → [Cloudflare edge → Vercel → Next.js proxy.ts → route]
    → HTTP response → browser renders (and asks for more: css/js/images, same loop)
```

Everything below walks this left to right, on your site.

## 1 · The URL (the instruction you type)

`https://www.leedspunjabisociety.com/dashboard?tab=tasks` = **scheme** (`https` — which
protocol) + **host** (`www.leedspunjabisociety.com` — which machine, by name) + **path**
(`/dashboard` — which thing there) + **query** (`?tab=tasks` — options). *(Analogy: postal
system — country / building / room / delivery note.)*

## 2 · DNS — the phone book

Computers route by **IP address** *(plain words: the numeric address of a machine on the
internet, like 172.67.183.218 — the phone number behind the contact name)*. **DNS** turns
names into addresses. Do it by hand: `nslookup www.leedspunjabisociety.com`.

**Your site's real answer tonight:** four addresses — two IPv6 (`2606:4700:…`) and two IPv4
(`172.67.183.218`, `104.21.18.225`). Those ranges belong to **Cloudflare**, not Vercel —
proof the name points at a protective front layer, not the origin. Meanwhile
`psoc-portal.vercel.app` resolves to different addresses entirely (`64.29.17.67`,
`216.198.79.67`) — same app, two doors. (Why multiple addresses at all? Load spreading +
redundancy: any of them answers.)

## 3 · TCP and ports — placing the call

With an address in hand, the browser opens a **TCP connection** *(plain words: a reliable
two-way pipe between your machine and a **port** — a numbered door — on the server; the
pipe re-sends lost pieces and keeps order; analogy: a phone call, not a postcard)*. Web
doors: **443** for HTTPS, 80 for old HTTP. `Connection: keep-alive` in your capture = the
call stays open for the next request instead of redialling.

## 4 · TLS — the call goes secret

**TLS** wraps the connection so nobody between you and the server can read or alter it
*(plain words: envelope + passport — encryption for secrecy, and a **certificate** proving
you reached the real site, vouched for by an authority your browser already trusts)*. See a
certificate yourself: padlock icon → view certificate; note who issued it and its expiry.
Your site goes further — the vercel.app response carries
`Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`: an instruction
telling browsers "speak ONLY HTTPS to me for the next two years, and ship that rule inside
the browser itself" (**HSTS**). This is why http:// is dead as a habit.

## 5 · HTTP — the actual conversation (do it by hand now)

```
curl.exe -v https://www.leedspunjabisociety.com/        # the whole conversation, narrated
curl.exe -sSI https://www.leedspunjabisociety.com/      # -I = HEAD: headers only, no body
curl.exe -sSL https://psoc-portal.vercel.app/           # -L = follow redirects; watch the hop
```

A request is: **method + path + headers** (`GET / HTTP/1.1`, `Host: …`). A response is:
**status line + headers + body**. The families you must know cold: **2xx** worked (200 OK) ·
**3xx** go elsewhere (301/308 permanent, 302/307 temporary — the 30**8**/30**7** variants
promise the METHOD won't change) · **4xx** you erred (401 not signed in, 403 forbidden,
404 no such thing) · **5xx** the server erred (500).

**Read your real headers** (fixture, then live): `Server: Vercel` (who answered) ·
`Location:` (where a redirect sends you) · `Cache-Control: public, max-age=0,
must-revalidate` (caches may store it but must re-check freshness) · `Age: 6282` (this copy
sat in a cache for ~105 minutes — proof Cloudflare served you, not Vercel) ·
`Content-Type: text/html; charset=utf-8` (what the body IS) · the security trio
`X-Frame-Options: DENY` (nobody may iframe the portal — anti-clickjacking),
`X-Content-Type-Options: nosniff`, `Referrer-Policy` · and the
`Content-Security-Policy-Report-Only` naming `*.supabase.co` — the browser-side allowlist
of who the page may talk to, currently in report-only rehearsal mode. One header, and you
know the backend.

## 6 · The redirect chain — a migration, caught on the wire

`psoc-portal.vercel.app` answered **308 Permanent Redirect** with `Location:
https://www.leedspunjabisociety.com/`. Someone (you, via a session) moved the site to a
real domain and left a permanent forward at the old address; the repo's
`guides/PUBLIC-SITE-UPDATES.md` still names the old URL. Lessons: redirects are how the web
moves house without breaking links; "permanent" tells browsers/search engines to update
their records; and **docs drift — the wire doesn't**. (Worth a one-line fix to that guide —
your call, it's your repo.)

## 7 · Auth in one sitting — the gate, observed

Logged out, `GET /dashboard` answered **307 Temporary Redirect → /login** in 0.17s. That is
`app/src/proxy.ts` — the 31-line front door you READ in module 06 — acting on the wire:
no session cookie → you're bounced before any page code runs. The pieces: after login the
server sets a **session cookie** (`Set-Cookie` header) *(plain words: a ticket the browser
re-presents on every request so the server recognises you; analogy: a wristband from the
door staff)* — flagged `HttpOnly` (page scripts can't read it), `Secure` (HTTPS only),
`SameSite` (other sites can't ride it — the CSRF defence). Why 307 not 308? Temporary: once
you're logged in, /dashboard should serve normally again — nothing should remember the
bounce as permanent. And why does `addTask()` STILL re-check auth after all this?
Module 06's answer, now visible end-to-end: gates filter traffic, but **the server trusts
no browser** — a forged request can skip every gate except the check beside the data.
(**JWT**, preview for Tier 4: a signed token carrying who-you-are in its own body — the
wristband with tamper-evident writing; Supabase sessions use them under the hood.)

## 8 · The CDN sandwich — who actually served you

**CDN** *(plain words: a network of cache servers near users that answer for the origin;
analogy: vending machines stocked from one warehouse)*. Your chain: **Cloudflare** (DNS +
edge cache + the `Report-To: cf-nel` telemetry header) in front of **Vercel** (the platform
running your Next.js origin). The `Age` header is the tell: 6282 seconds means Cloudflare
answered from its shelf without waking the origin. Fast, cheap — and why cache-invalidation
(`revalidateTasks()` from module 06, hop 6!) is a real engineering topic: stale shelves are
the price of fast shelves.

**Checkpoint — you can now:** dismantle any URL; resolve a name and say whose addresses
came back; explain TCP vs TLS vs HTTP in one sentence each; read a status line + ten common
headers cold; narrate your site's real redirect chain and auth bounce; and say who served a
response (origin or cache) from evidence.

## Sources (all captured live, 04/08/2026, this machine)

- `exercises/fixtures/trace-2026-08-04.txt` — the raw captures (curl 8.19.0, nslookup).
- Repo cross-references: `app/src/proxy.ts` (module 06 dig) · `guides/PUBLIC-SITE-
  UPDATES.md:7` (the stale URL) · `docs/OWNER-MANUAL.md` (site surfaces).
- Cloudflare IP attribution: 104.21.0.0/16, 172.67.0.0/16, 2606:4700::/32 are published
  Cloudflare ranges (cloudflare.com/ips); Vercel per `Server: Vercel` header.
