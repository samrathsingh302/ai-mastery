# Module 14 🔐 — Crypto by example, on YOUR real scheme *(SECONDARY track)*

> **⚠ SECONDARY module.** D-lane, hooked **after module 06 (repo archaeology)** — you've
> already read `ConfigIntegrity.vb` once; now you'll understand every line of it. If it ever
> competes with an A-lane module, A wins. **~4h, free.**
> **The premise:** most crypto teaching is toy examples. Yours isn't — monk-mode implements a
> genuinely well-designed tamper-evidence scheme on this machine, with comments explaining
> *why*. We'll read the real thing, rebuild each piece in Python, and steal the design
> lessons. Every number below was read from the source tonight.

## 1 · Hashing: the one-way fingerprint

**Hash function** *(plain words: takes any input, returns a fixed-size fingerprint; the same
input always gives the same fingerprint, and you cannot work backwards from it; analogy: a
smoothie — trivially made from fruit, impossible to un-blend)*.

```python
sha256("hello") = 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
sha256("hellp") = fdd7585e08c4e2afd71dcabdb4636c89d557a3f42db9e2040c8bbd1708aa4ce7
```

One letter changed; the entire output is unrecognisable (**the avalanche effect**). Three
properties that matter: **one-way** (can't reverse) · **deterministic** (same in, same out —
which is why you can *verify* with it) · **collision-resistant** (finding two inputs with the
same fingerprint is infeasible).

**Hashing ≠ encryption.** Encryption is *reversible by design* (someone holds the key);
hashing is *not reversible at all*. If you ever hear "we encrypt passwords", that's either
sloppy language or a real bug — passwords should be **hashed**, because the system never
needs to read them back, only to check them. monk-mode makes exactly this choice, and its
comments say so.

## 2 · Salt: why identical inputs must not look identical

A plain hash of a code is guessable by brute force *once for everybody* — precompute
fingerprints for every likely input (**rainbow table**) and look them up. A **salt** *(plain
words: random data mixed in before hashing, stored alongside the result; analogy: everyone's
smoothie gets a different secret spice, so one tasting chart can't identify them all)*
defeats that: with a per-item random salt, an attacker must attack each item separately.

**monk-mode's actual choice** (`ConfigIntegrity.vb`, PD3): a **fresh 16-byte salt per code**
from a cryptographic random generator. Its own comment states the reason: *"The per-code salt
makes each block's offline search independent and rainbow-tables useless."*

## 3 · Slow on purpose: KDFs and the 600,000

SHA-256 is *fast* — billions per second on a GPU. For anything guessable (a 10-character
code), fast is the attacker's friend. So you use a **key derivation function** *(plain words:
a deliberately slow, salted hash designed for secrets that humans handle; analogy: a lock
that takes half a second to turn — irrelevant when you unlock it twice a day, ruinous if you
must try a billion keys)*.

**monk-mode's actual choice:** `PBKDF2-HMAC-SHA256`, **600,000 iterations**, 16-byte salt,
32-byte output — all three pinned by unit tests so a retune is "one loud edit".

Measured on this machine tonight: **600,000 iterations ≈ 0.39 s**. Feel the asymmetry — you
pay 0.39 s once when checking a code; an attacker pays 0.39 s *per guess*. Against a
10-character code from a 32-symbol alphabet, that is the whole defence.

## 4 · MAC / HMAC: integrity with a key

A hash proves data hasn't changed **only if the attacker can't recompute it** — but anyone
can hash anything. Add a secret key and you get a **MAC** *(message authentication code —
plain words: a signature over data that only a key-holder can produce or verify; analogy: a
wax seal whose stamp only you own — anyone can see the seal, nobody else can forge it)*.
**HMAC** is the standard construction for building a MAC from a hash function.

**monk-mode's actual line** (`ComputeConfigMac`): HMAC-SHA256 over the canonical string's
**Unicode (UTF-16LE) bytes**, Base64-encoded, keyed with a 32-byte per-block random key.

> Encoding is not a detail: the same text HMAC'd as UTF-16LE and as UTF-8 gives **completely
> different** MACs (you'll prove this in exercise 1, `ex01_primitives.py`). Cross-language
> reimplementations break here constantly — a spec-fidelity lesson wearing a crypto costume.

## 5 · Canonicalisation: the subtle one, and the best lesson in the file

Before you can sign data, you must turn it into **one exact string** — the same fields, in
the same order, formatted the same way, every time. That's **canonicalisation**.

`BuildCanonical()` takes 15 fields and emits them one per line as `Name=value\n`, in a fixed
order. Two design decisions hide in that:

1. **Every protected field is inside** — Until, HighWater, CoolOffUntil, ProcessList,
   CustomSites, PartnerSalt/Hash/UnlockedAt, Committed, schedule fields, AllSessionKill.
   A field *outside* the canonical is a field an attacker may freely edit. The file's own
   comment on `AllSessionKill` spells out the attack that would enable if it were omitted:
   flip an armed all-session block back to session-0-only and run a blocked app in a second
   logged-in session.
2. **The delimiters matter.** Naively gluing fields (`"Until=" + until + "Committed=" + c`)
   is forgeable: values containing the separator can smuggle in a fake field, so two
   *different* field-sets produce the *same* string and therefore the same valid MAC.
   Exercise 2 (`ex02_canonical.py`, `forge_naive`) makes you build that collision by hand —
   it's the most instructive ten minutes in this module.

**The general law:** *sign a form that can only be read one way.* Ambiguity in the signed
representation is a hole regardless of how strong the cipher is.

## 6 · Constant-time comparison: leaking through the clock

Comparing two MACs with `==` usually stops at the first differing byte — so a wrong guess
that matches the first byte takes *fractionally longer* to reject. Repeat a few million
times and an attacker recovers the MAC byte by byte: a **timing side-channel** *(plain words:
learning a secret from how long an operation takes, without ever seeing the secret;
analogy: guessing a safe's combination from how far the dial turns before it clicks)*.

**monk-mode's actual choice:** `CryptographicOperations.FixedTimeEquals` over the raw bytes —
always compares everything, no early exit. Python's equivalent is `hmac.compare_digest`, and
you'll use it in exercise 1 (`ex01_primitives.py`, `safe_equals`).

## 7 · Fail-closed verification (the whole scheme's spine)

`ConfigMacIsValid` returns **False — never throws** — on a blank, malformed or
non-Base64 MAC. Combined with the service's tick (module 06), that means *any* verification
failure leaves the block **standing**. The safe state is chosen on doubt, always.

Compare the two failure philosophies: **fail-open** (if the check breaks, allow) is how
convenience wins and security dies; **fail-closed** (if the check breaks, deny) is how a
blocker must behave. Your estate uses the same instinct elsewhere — the MANUAL-TASKS gate
stops work rather than guessing.

## 8 · Key custody: DPAPI, and where the design admits its limits

The HMAC key is protected with **DPAPI at machine scope** *(plain words: Windows encrypts
data so that only this machine can decrypt it, using OS-held keys; analogy: a safe bolted to
the building — useful, but only against people who can't take the building)*.

And now the honest part, straight from `CLAUDE.md`: the config *cipher* (`Simple3Des`, a
SHA-1-derived 3DES key from the hardcoded passphrase `mm_textbox`, zero IV) is
**documented-weak by design** — Phase-3-owned, explicitly not a new finding. Why is that
acceptable? Because **the threat is tampering, not secrecy**. Confidentiality of a file the
user already owns buys almost nothing; *tamper-evidence* is what keeps the block standing.
The weak cipher is honest about what it is; the HMAC layer above it does the real work.

**That is the design lesson of this module**: name your threat model, then spend your
strength where the threat is. Crypto misused as decoration is worse than none, because it
buys false confidence.

**Checkpoint — you can now:** explain hashing vs encryption, salts, why KDFs are slow, what
an HMAC adds over a hash, why canonicalisation must be unambiguous, what a timing attack is,
and why a deliberately weak cipher can be a correct decision when the threat is tampering.

## Sources (read live from the repo, 04/08/2026)

- `C:\Users\samra\repos\monk-mode\MonkMode\ConfigIntegrity.vb` — `BuildCanonical` (15 fields,
  `Name=value\n`), `ComputeConfigMac` (HMAC-SHA256 over Unicode bytes → Base64),
  `ConfigMacIsValid` (FixedTimeEquals, returns False never throws), PD3 constants
  (`PartnerKdfIterations = 600000`, `PartnerSaltBytes = 16`, `PartnerHashBytes = 32`),
  `PartnerCodeAlphabet` (32 chars, Crockford-style), DPAPI protect/unprotect.
- `monk-mode\CLAUDE.md:22` — the standing "documented-weak by design" note on Simple3Des.
- Timing (0.39 s for 600k iterations) and every expected value in the exercises: measured and
  computed on this machine tonight.
