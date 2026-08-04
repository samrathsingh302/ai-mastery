# Ex01 — the three planted bugs (open AFTER committing to answers)

1. **Step 8 — "Skip these files" on duplicates.** Root cause: skipping means files that changed
   since an earlier backup are NEVER updated — the backup silently goes stale. Correct: choose
   "Replace" (or compare dates). *This is the classic "error path silently swallows" bug.*
2. **Step 10 — deleting originals.** Root cause: a copy you haven't VERIFIED is not a backup —
   one unreadable stick and the coursework exists nowhere. Correct: verify the copy opens
   (spot-check files, compare counts/sizes) before deleting anything — and ideally never treat
   one copy as licence to delete (the house no-data-loss law). *Bug class: acting on an
   unverified assumption.*
3. **Step 3 — "files modified this term".** Root cause: boundary/selection bug — files created
   BEFORE term but still needed (templates, references, earlier drafts) are excluded; the
   backup is incomplete by design. Correct: back up the whole folder. *Bug class: wrong filter
   / off-by-boundary.*

*(Step 9 — ejecting when the bar closes — is acceptable on modern Windows with write-caching
off, which is the default for removable drives; if you flagged it, half-credit and a good
instinct: "progress bar gone" ≠ "writes flushed" on all systems.)*

**The lesson under the lesson:** all three are bugs you'll meet in real code as: swallowed
error branches · unverified side-effects before destructive ops · wrong predicate on a filter.
L0 teaches the method; the classes recur at every level.
