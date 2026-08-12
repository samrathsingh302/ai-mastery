# Project 14 🔐 — Audit three real schemes against the module's own laws

**What:** `crypto-audit.md` here — you take three integrity schemes that already run on this
machine and say, for each, what it actually defends against and what it does not. ~1.5h.
**Read-only: you change nothing.** TEACH handed you monk-mode's answers; this asks you to
produce them yourself, then apply the same questions where nobody has written them down.

## The three targets (all yours, all currently on disk)

1. **monk-mode's config integrity** — `repos\monk-mode\MonkMode\ConfigIntegrity.vb`.
   Read it cold, then write the threat model in your own words: *who* is the attacker, *what*
   do they already have, and *what one thing* must not happen. Then place each defence:
   `BuildCanonical` (:178), `ComputeConfigMac` (:198), `ConfigMacIsValid` (:210), `PartnerKdf`
   (:308), `ProtectKey`/`UnprotectKey` (:353, :366). One line each: which part of the threat
   model does this piece close? Two are not obvious — the schema-version tag (:81) and the
   fact that `[Integrity] Key` and `Mac` are excluded from the canonical (:33). Say why both.
2. **git** — `git cat-file -p HEAD` and `git fsck` in any of your repos. Every object is named
   by the SHA of its own contents, so corruption is caught immediately. Now the question:
   could you rewrite a commit's contents and have `git fsck` stay silent? What does that tell
   you about which of the module's two words — *integrity* or *authentication* — git's hashes
   actually buy, and what supplies the missing one in practice?
3. **The daily backup** — `Claude-Vault-Daily-Backup` (Ready) runs
   `tools\backup\claude-vault-backup.ps1`, which writes `backup-<stamp>.zip` (:76–78). A zip
   stores a CRC32 per entry. Answer honestly: what does that CRC detect, what can it not
   detect, and does it matter here? The script's own header (:10) says the zip holds secrets —
   let that change your threat model rather than your alarm level.

## The write-up (per scheme)

**Threat model in one sentence · what the scheme detects · what it cannot detect · what the
consequence of a failed check is (does it fail open or closed?) · and whether the strength is
spent where the threat is.** That last question is the module's law, and it is the one that
separates an audit from a recitation.

Close with **one improvement you'd make** and why — plus whether it's a code fix, a config
fix, or a decision only you can take (if the last, it goes to MANUAL-TASKS). "None needed,
here's why" is a valid answer if you can defend it; targets 2 and 3 may well earn it.

## Acceptance checklist

- [ ] monk-mode's threat model written from the source, not from TEACH, before re-reading TEACH
- [ ] All five named functions placed against that threat model, one line each
- [ ] The schema-version tag and the excluded `[Integrity]` fields both explained
- [ ] git: integrity vs authentication answered, with what supplies the missing half
- [ ] The backup zip's CRC32 answered honestly — including "does it matter here?"
- [ ] Fail-open or fail-closed stated for all three
- [ ] One improvement proposed, correctly routed (code / config / MANUAL-TASKS)
- [ ] Nothing on the machine was modified
