# Module 14: crypto by example — like you're 5

Module 14 🔐, the secondary track, taught in `C:\Users\samra\repos\ai-mastery\modules\14-cyb-crypto-monkmode\TEACH.md`.

- **One-line reminders:** `GLOSSARY.md` → `## Module 14 🔐 — crypto by example *(secondary track)*`.
- **The real scheme:** `C:\Users\samra\repos\monk-mode\MonkMode\ConfigIntegrity.vb`. Read it, never edit it from here.
- **Git Bash:** the `printf` and `openssl` lines run there.
- **Either shell:** the `git grep` lines run from `cd C:\Users\samra\repos\monk-mode`.
- **Not answers:** none of them is an answer to `ex01_primitives.py` or `ex02_canonical.py`. Those you type, in Python.

---

### Avalanche effect
**Like you're 5:** Change one tiny letter in your message, and its fingerprint doesn't change a little: it changes completely, as if it belonged to a whole new person. So even the smallest edit can never sneak past unnoticed.

**The real words:** Change one letter of the input and the entire digest is unrecognisable; why a hash detects any edit at all. → [14 §1](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `printf hello | sha256sum` then `printf hellp | sha256sum` — one letter apart, two unrelated 64-character fingerprints (the first starts `2cf24dba`, as in TEACH.md §1).

### Canonicalisation
**Like you're 5:** Before you stamp a list with your seal, everyone agrees exactly how it's written: same items, same order, same spacing, every time. Otherwise two different lists could be squashed into the same-looking words, and one seal would fit both.

**The real words:** Turning data into ONE exact string before signing it (same fields, same order, same formatting, every time); ambiguity in the signed form is a hole however strong the cipher. → [14 §5](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `git grep -n "Function BuildCanonical" -- MonkMode/ConfigIntegrity.vb` → line 261, the real one; `start C:\Users\samra\repos\ai-mastery\modules\14-cyb-crypto-monkmode\interactive\canonical-forge.html` shows why the delimiters matter.

### Collision resistance
**Like you're 5:** Finding two different people with exactly the same fingerprint would take so long that nobody could ever do it. A good hash is like that: nobody can find two different messages that make the same print.

**The real words:** Finding two inputs with the same fingerprint is infeasible; one of the three properties (with one-way and deterministic) that make a hash usable. → [14 §1](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** SHA-256 has 2²⁵⁶ possible fingerprints: `python -c "print(len(str(2**256)))"` → `78`, a 78-digit number of them; even the best shortcut (the birthday trick) still needs about 2¹²⁸ tries.

### Constant-time comparison
**Like you're 5:** A guard checks your password letter by letter and sends you away at the first wrong one, so by timing him you learn how many letters you got right. A careful guard checks every letter, every time, taking the same time whatever you said.

**The real words:** Compare every byte with no early exit (`FixedTimeEquals` in .NET, `hmac.compare_digest` in Python), so the timing carries no information. → [14 §6](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `git grep -n FixedTimeEquals -- MonkMode/ConfigIntegrity.vb` → line 340 is the real check inside `ConfigMacIsValid`.

### DPAPI
**Like you're 5:** A safe bolted to the floor of your house. Nobody can carry it away and open it somewhere else. But anyone who gets inside your house can stand right in front of it, and the safe does nothing to stop them.

**The real words:** Windows encrypting data with OS-held keys so only this machine can decrypt it (monk-mode uses machine scope); a safe bolted to the building, useless against someone who has the building. → [14 §8](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `git grep -n DataProtectionScope.LocalMachine -- MonkMode/ConfigIntegrity.vb` → lines 474 (protect) and 489 (unprotect).

### Fail-open
**Like you're 5:** A shop alarm that, when its battery dies, just opens all the doors. Handy if you're in a rush, terrible against burglars. The safe kind does the opposite: if it breaks, everything stays locked.

**The real words:** If the check breaks, allow: the opposite of fail-closed (module 06), and how convenience wins while security dies; monk-mode fails closed, so a broken check keeps the block standing. → [14 §7](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `C:\Users\samra\repos\monk-mode\MonkMode\ConfigIntegrity.vb` lines 24–28 and 42–48 — the comments that choose fail CLOSED and say why.

### Hash function
**Like you're 5:** A smoothie maker. Put in any fruit and you always get a cup the same size; the same fruit always makes the same smoothie; but nobody can ever un-blend it to get the fruit back.

**The real words:** Any input → a fixed-size fingerprint: one-way, deterministic, collision-resistant; not encryption, which is reversible by design. → [14 §1](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `printf 'a whole paragraph of text' | sha256sum` and `printf x | sha256sum` — wildly different inputs, the same 64-character size out.

### Key derivation function (KDF)
**Like you're 5:** A lock that takes half a second to turn. You only open your door twice a day, so you barely notice. A burglar trying a billion keys would need years. Making it slow on purpose is the whole point.

**The real words:** A deliberately SLOW salted hash for secrets humans handle (monk-mode: PBKDF2-HMAC-SHA256, 600,000 iterations, ≈ 0.39 s here); the slowness is the defence, not a cost. → [14 §3](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `git grep -n "PartnerKdfIterations As Integer" -- MonkMode/ConfigIntegrity.vb` → line 378, `= 600000`, pinned by the unit tests.

### MAC (message authentication code)
**Like you're 5:** A wax seal on a letter. Anyone can look at the seal, but only you own the stamp that makes it. If someone opens the letter and changes it, they can't make a fresh seal that matches.

**The real words:** A tag over data that only a key-holder can produce or verify (HMAC builds one from a hash plus a secret key); a wax seal whose stamp only you own. → [14 §4](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `printf hello | openssl dgst -sha256 -hmac key1`, then the same with `-hmac key2` — same message, different stamp, a completely different seal.

### Rainbow table
**Like you're 5:** A cheat book listing the fingerprint of every common password, made once, in advance. A thief with a pile of stolen fingerprints just looks each one up and gets everyone's password at once, unless every password had its own secret spice added first.

**The real words:** A precomputed fingerprint→input lookup (strictly, a compressed chain-based form of one) that cracks every unsalted hash at once; exactly what a per-item salt destroys. → [14 §2](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `printf password | sha256sum` → `5e884898…` on every machine on earth, so it is already in every cheat book.

### Salt
**Like you're 5:** Everyone's smoothie gets its own secret spice before blending, and the spice is written on the cup. Two people with the same fruit get different smoothies, so one cheat chart can't name them all: the thief must work on each cup separately.

**The real words:** Random data mixed in before hashing and stored alongside; it makes each item's offline search independent (monk-mode: a fresh 16-byte salt per code). → [14 §2](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `printf saltApassword | sha256sum` vs `printf saltBpassword | sha256sum` — the same password, two unrelated fingerprints; monk-mode's salt size is `PartnerSaltBytes`, line 379 of `ConfigIntegrity.vb`.

### Tamper-evidence vs confidentiality
**Like you're 5:** Two different jobs. A seal on a jar shows whether anyone opened it, but you can still see the jam through the glass. A locked tin hides what's inside. First decide which job you need; using the wrong one is just decoration.

**The real words:** Proving nothing was changed vs hiding what it says; monk-mode's weak `Simple3Des` cipher is acceptable because its threat is tampering, and the HMAC layer above it does the real work. → [14 §8](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `C:\Users\samra\repos\monk-mode\CLAUDE.md` line 22 — the standing "documented-weak by design" note on `Simple3Des`.

### Timing side-channel
**Like you're 5:** Guessing a safe's combination by listening to how long the dial turns before it clicks. You never see the secret, but how long each try takes gives it away, bit by bit.

**The real words:** Learning a secret from how long an operation takes; `==` exits at the first wrong byte, so a closer guess is rejected slower. → [14 §6](../modules/14-cyb-crypto-monkmode/TEACH.md)

**See it:** `python -c "import timeit; s='a'*10**7; x='b'+s[1:]; y=s[:-1]+'b'; print(timeit.timeit(lambda: s==x, number=100), timeit.timeit(lambda: s==y, number=100))"` — wrong at the first letter is rejected almost instantly; wrong at the last letter takes far longer.
