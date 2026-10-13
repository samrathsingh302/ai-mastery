# 08-how-the-web-works — like you're 5

Taught in `C:\Users\samra\repos\ai-mastery\modules\08-how-the-web-works\TEACH.md`; the one-line reminders are `GLOSSARY.md` → `## Module 08 — how the web works`. The commands run from any folder; `curl.exe` and `nslookup` work in PowerShell, and the lines with `grep` or `/dev/null` need Git Bash. The whole journey is animated in `C:\Users\samra\repos\ai-mastery\modules\08-how-the-web-works\interactive\page-load-journey.html` (`start` it from PowerShell). None of them is an exercise answer: ex01's quiz still needs you to read the wire yourself.

### CDN / edge cache
**Like you're 5:** The big toy shop is far away, so little vending machines near your house keep copies of the most-wanted toys. You press the button, the nearest machine answers, and the far shop never even hears about it. A sticker says how long that toy has sat in the machine.
**The real words:** Cache servers near users answering for the origin; the `Age` header (seconds a copy has sat in a cache) is the tell. → [08 §8](../modules/08-how-the-web-works/TEACH.md)
**See it:** `curl.exe -sSI https://www.leedspunjabisociety.com/` twice, a minute apart, and compare the `Server:` and `Age:` lines; the 04/08 capture of the same headers is in `C:\Users\samra\repos\ai-mastery\modules\08-how-the-web-works\exercises\fixtures\trace-2026-08-04.txt`.

### Certificate
**Like you're 5:** A passport for a website. When you visit, the site shows a card saying "I really am this shop", and a grown-up everyone trusts has stamped it. If the stamp is fake or the card is out of date, your browser shouts a warning.
**The real words:** The identity half of TLS: proof you reached the real site, vouched for by an authority your browser already trusts, with an expiry date. → [08 §4](../modules/08-how-the-web-works/TEACH.md)
**See it:** open `https://www.leedspunjabisociety.com/` in the browser → the padlock icon → view the certificate; note who issued it and when it expires.

### Cookie (session)
**Like you're 5:** At a party the door person puts a wristband on you. Every time you walk back in, you show the wristband and they let you through without asking your name again. A good wristband is tied tight: only the door staff read it, it only works at the real door, and no other party can borrow it.
**The real words:** A ticket the server sets with `Set-Cookie` and the browser re-presents on every request; `HttpOnly` (page scripts can't read it), `Secure` (HTTPS only) and `SameSite` (other sites can't ride it) are its armour. → [08 §7](../modules/08-how-the-web-works/TEACH.md)
**See it:** log in at `https://www.leedspunjabisociety.com/`, press F12 → Application → Cookies, and read the HttpOnly, Secure and SameSite columns on the session cookie.

### DNS
**Like you're 5:** Your phone knows "Grandma", but the phone network only knows her number. The contacts list turns the name into the number. DNS is the internet's contacts list: you type a website's name, and it hands back the number the computers really use.
**The real words:** The phone book: it turns names into IP addresses, and one name can return several addresses (load spreading, redundancy). → [08 §2](../modules/08-how-the-web-works/TEACH.md)
**See it:** `nslookup www.leedspunjabisociety.com`, then `nslookup psoc-portal.vercel.app` — the same app behind two different sets of numbers.

### HSTS
**Like you're 5:** A shop tells you: "From now on, only ever come in through the locked, safe door, never the open side door, and remember that for two years." Your browser writes the promise down and keeps it, even if a link later points at the side door.
**The real words:** The `Strict-Transport-Security` header, committing browsers to HTTPS-only for `max-age` seconds (63072000 = 2 years on his site's vercel.app response). → [08 §4](../modules/08-how-the-web-works/TEACH.md)
**See it:** `curl.exe -sSI https://psoc-portal.vercel.app/` and find the `Strict-Transport-Security:` line; `max-age` is in seconds.

### HTTP status families
**Like you're 5:** When you knock on a door you get one of four kinds of answer: "here you go", "not here, try next door", "you knocked wrong", or "sorry, we're broken inside". The first number of the code tells you which of the four it is.
**The real words:** 2xx worked · 3xx go elsewhere · 4xx you erred · 5xx the server erred; 307 (temporary) and 308 (permanent) redirects promise the method won't change. → [08 §5](../modules/08-how-the-web-works/TEACH.md)
**See it:** `curl.exe -sSI https://www.leedspunjabisociety.com/no-such-page` — the first line is the status line; its first digit names the family.

### IP address / port
**Like you're 5:** A block of flats has one street number, and each flat inside has its own door number. The IP address is the building's number; the port is which door you knock on. Door 443 is the door for safe, locked web pages.
**The real words:** A machine's numeric address on the internet (e.g. `172.67.183.218`) / a numbered door on it (443 = HTTPS, 80 = old HTTP). → [08 §2–3](../modules/08-how-the-web-works/TEACH.md)
**See it:** in PowerShell, `Test-NetConnection www.leedspunjabisociety.com -Port 443` — `RemoteAddress` is the IP, and `TcpTestSucceeded` says whether door 443 answered.

### JWT (preview)
**Like you're 5:** A party wristband with your name written on it in special ink. If anyone scribbles on it, the ink smudges and the door staff can tell. The staff read who you are right off the band, without looking you up in their book.
**The real words:** A signed token carrying identity in its own body: tamper-evident, not secret (anyone can read the middle part); Supabase sessions use them under the hood, and Tier 4 treats it properly. → [08 §7](../modules/08-how-the-web-works/TEACH.md)
**See it:** a JWT is three base64url chunks joined by dots, `header.payload.signature`; paste the sample token `https://jwt.io` shows (never a real one of yours) and watch the middle chunk decode into plain JSON.

### TCP
**Like you're 5:** A postcard might get lost and nobody tells you. A phone call is different: you both stay on the line, and if a word drops out you say "pardon?" and it's said again, in order. TCP is the phone call that web pages travel along.
**The real words:** The reliable, ordered two-way pipe to a port on the server (lost pieces re-sent, order kept) that HTTP rides on; `Connection: keep-alive` keeps the call open for the next request. → [08 §3](../modules/08-how-the-web-works/TEACH.md)
**See it:** in Git Bash, `curl.exe -sv https://www.leedspunjabisociety.com/ -o /dev/null 2>&1 | grep -i connected` — that line is the call being placed, port number included.

### TLS
**Like you're 5:** Before you whisper a secret on the phone, you and your friend agree a secret code nobody else knows, and your friend shows a passport proving it's really them. Now anyone listening in hears only gibberish.
**The real words:** Envelope + passport around the TCP pipe: encryption so nobody between can read or alter it, plus a certificate proving you reached the real site. → [08 §4](../modules/08-how-the-web-works/TEACH.md)
**See it:** in Git Bash, `curl.exe -v https://www.leedspunjabisociety.com/ -o /dev/null` — the `*` lines after `Connected to` and before the first `> GET` are the TLS handshake.
