# Drills — module 14 🔐 (SECONDARY track)

## Anki-importable block (tab-separated: Front ⇥ Back)

Three properties of a hash function?	One-way (can't reverse) · deterministic (same in, same out — so you can VERIFY) · collision-resistant (two inputs, one fingerprint is infeasible).
What is the avalanche effect?	One changed letter rewrites the whole digest. sha256("hello") = 2cf24dba… but sha256("hellp") = fdd7585e… — nothing survives.
Hashing vs encryption — and why passwords are HASHED?	Encryption is reversible by design (someone holds the key); hashing is not reversible at all. A password system never needs to READ it back, only to check it — so "we encrypt passwords" is sloppy language or a real bug.
What is a salt, and what does it defeat?	Random data mixed in before hashing, stored alongside the result. It defeats rainbow tables: one precomputed chart can no longer crack everybody at once.
What is a rainbow table?	A precomputed fingerprint→input lookup. It works because an unsalted hash of the same input is the same for everyone — a salt makes each search independent.
monk-mode's salt: size, scope, and its own stated reason?	16 bytes, FRESH PER CODE, from a CSPRNG. Its comment: "The per-code salt makes each block's offline search independent and rainbow-tables useless."
What is a KDF and why is it deliberately slow?	A key derivation function: a slow, salted hash for secrets humans handle. SHA-256 does billions/sec on a GPU — for a guessable code, fast is the ATTACKER's friend.
monk-mode's KDF, exactly?	PBKDF2-HMAC-SHA256 · 600,000 iterations · 16-byte salt · 32-byte output. All three pinned by unit tests so a retune is "one loud edit".
The 600,000-iteration asymmetry, in numbers?	≈0.39 s on this machine. You pay it ONCE per code check; the attacker pays it PER GUESS. Against a 10-char code from a 32-symbol alphabet that is the whole defence.
What does a MAC add over a plain hash?	A key. Anyone can hash anything, so a bare hash proves nothing against an attacker who can recompute it. A MAC is a wax seal whose stamp only you own — anyone can see it, nobody else can forge it.
What is HMAC?	The standard construction for building a MAC out of a hash function. HMAC-SHA256 = a keyed signature built on SHA-256.
monk-mode's ComputeConfigMac, in one line?	HMAC-SHA256 over the canonical string's Unicode (UTF-16LE) bytes, Base64-encoded, keyed with a 32-byte per-block random key.
The encoding trap?	The same text HMAC'd as UTF-16LE and as UTF-8 gives COMPLETELY different MACs. .NET's Encoding.Unicode means UTF-16LE, not UTF-8 — cross-language reimplementations die here.
What is canonicalisation?	Turning data into ONE exact string before signing it — same fields, same order, same formatting, every time. No canonical form, no meaningful signature.
monk-mode's canonical shape?	`Name=value` one per line, `\n`-terminated, in a FIXED order, built from the DECRYPTED values so it's byte-identical whoever writes it.
Why must every protected field be inside the canonical?	A field OUTSIDE the canonical is a field an attacker may freely edit — the MAC still verifies. Coverage is the protection.
The AllSessionKill example — what would omitting it allow?	Flipping an armed all-session block back to session-0-only, then running a blocked app in a second logged-in session. Inside the canonical, that edit fails the MAC instead.
Why is gluing fields (`"Until=" + u + "Committed=" + c`) forgeable?	A value can contain the separator and swallow its neighbour, so two DIFFERENT field-sets produce the SAME string — and therefore the same valid MAC. One MAC, two meanings.
The general law of §5?	Sign a form that can only be read one way. Ambiguity in the signed representation is a hole no matter how strong the cipher is.
What is a timing side-channel?	Learning a secret from how LONG an operation takes, without ever seeing it. `==` stops at the first differing byte, so a closer guess is rejected fractionally slower — repeat and recover the MAC byte by byte.
The constant-time fix, both languages?	.NET: CryptographicOperations.FixedTimeEquals over the raw bytes. Python: hmac.compare_digest. Always compare everything; never exit early.
Fail-closed vs fail-open?	Fail-closed = if the check breaks, DENY (a blocker must). Fail-open = if the check breaks, allow — how convenience wins and security dies.
What does ConfigMacIsValid do on a blank/malformed/non-Base64 MAC?	Returns False, never throws. Any verification failure leaves the block STANDING — the safe state is chosen on doubt, always.
What is DPAPI machine scope protecting here, and what doesn't it protect against?	Windows encrypts the 32-byte HMAC key so only THIS machine can decrypt it. It's a safe bolted to the building — no use against someone who has the building.
Why is Simple3Des documented-weak-by-design and still a correct decision?	Because the threat is TAMPERING, not secrecy. Confidentiality of a file the user already owns buys almost nothing; the HMAC layer above does the real work.
The design law of module 14?	Name your threat model, then spend your strength where the threat is. Crypto misused as decoration is worse than none — it buys false confidence.

## Quick-fire (aloud, 30 seconds)

1. What does a salt defeat? 2. What does a key add to a hash? 3. Why is `==` on MACs a bug?
4. On a malformed MAC, does the block lift or stand?
*(rainbow tables · unforgeability by non-key-holders · it leaks through the clock · it stands — fail closed)*
