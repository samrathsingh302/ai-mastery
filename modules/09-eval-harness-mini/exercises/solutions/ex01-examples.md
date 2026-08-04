# Ex01 — example task designs (open after writing yours)

## Good programmatic ×2

1. `{"type":"exact"}` — "Convert 14:30 UK time on 04/08/2026 to a dd/mm/yyyy HH:MM string
   in Tokyo (UTC+9, no DST). Reply with only the string." Expected: `04/08/2026 22:30`.
   *One skill (timezone arithmetic), crisp output contract, checker-decidable.*
2. `{"type":"code-tests"}` — "Write slugify(title) lowercasing, replacing spaces with
   hyphens and dropping non-alphanumerics." Tests incl. `("Hello,  World!", "hello-world")`
   — *the double-space case is the discriminator.*

## Good rubric ×2

3. "Rewrite this committee announcement (120 words, three typos, buried call-to-action)
   for Instagram in ≤60 words." Criteria: CTA now first or last · typos gone · no invented
   details · fits limit. *Representative for PSOC; a stranger could score it.*
4. "A teammate's PR adds a working feature but copies a 30-line function instead of
   importing it. Draft the review comment." Criteria: names the duplication precisely ·
   proposes the import · tone a colleague would thank you for. *Judgement task with
   observable criteria.*

## Deliberately BAD, annotated

- BAD programmatic: "What's the best Python web framework? (expected: FastAPI)" — *opinion
  dressed as exact-match; measures agreement with you, not capability.*
- BAD rubric: "Write something creative about Leeds. Criteria: is it good?" — *no stranger
  reaches your score ±0; "good" is not criteria, it's vibes with paperwork.*

The meta-lesson: every bad eval fails the same way — the score stops meaning anything
outside your head. Criteria are the eval; the harness is just plumbing.
