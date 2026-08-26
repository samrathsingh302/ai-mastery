# CARD-RULES.md — Samrath's own card-making reference

> OWNERSHIP RULING (26/08/2026 evening; scribe amendment same night): **Samrath AUTHORS
> all his own Anki cards — Claude sessions never draft or invent card content.** At session
> end: the session presents card NOTES (facts worth carding + recommended count) in chat and
> `anki/notes/`; Samrath TYPES his cards in the terminal in his own words; the session acts
> as SCRIBE ONLY (fixes spelling/typos, applies this document's format mechanics — never
> rephrases or "improves" his wording) and imports them via `tools/anki_import.py`. This
> document is SAMRATH'S style reference for the cards he writes.
> Sources: SuperMemo's Twenty Rules (supermemo.com/en/blog/twenty-rules-of-formulating-knowledge)
> + Andy Matuschak's prompt-writing guide (andymatuschak.org/prompts) + Samrath's own rules.
> Reddit r/Anki was unreachable from the session that built this (26/08/2026); these two are
> the sources that community itself canonises.

## Samrath's format law (overrides everything below on conflict)

1. **Cloze for ALL cards, question and answer on SEPARATE lines (his layout law,
   26/08/2026).** Note type = Anki's built-in **Cloze** (default formatting, no custom
   CSS). Line 1 = the question, fully visible, holding NO blanks and no answer fragments.
   Line 2 = the answer, fully inside {{c1::…}} blanks — only scaffold labels/separators
   ("Training = …", "·", "→") may sit outside a blank. In the tsv the line break is the
   `¶` character (the importer turns it into a real line break and enforces the shape):
   `What is a token, in LLMs?¶{{c1::The chunk-of-text unit models read and write}}`
2. **Never repeat the question in the answer.** `What is X? X is Y` is banned — the cloze
   holds `Y` alone. Reading time is review time.
3. **Multi-part answer = multiple {{c1::…}} blanks — NEVER c2/c3 (his law, 26/08/2026:
   "never ever use c2, it doesn't work").** All blanks share the number c1, so they hide
   together on ONE card: question → recall every part → flip once, like a Q→A card.
   "Three properties of a hash? {{c1::one-way}} · {{c1::deterministic}} ·
   {{c1::collision-resistant}}". The importer hard-fails any c2+.
4. **Too big → split into more notes.** One idea per note. If a card teaches two things,
   it is two cards.
5. **The cloze = ONLY the direct answer; Back Extra = the explanation (his final ruling,
   26/08/2026, superseding both earlier versions).** The blank holds exactly what answers
   the question as asked — "In Python, what does "2" + 2 do?" → {{c1::TypeError}} — and
   NOTHING more. Everything that explains, illustrates, or contextualises the answer
   without directly answering the question (the why, the hook, the example, the gotcha)
   goes in Back Extra, which shows on the flip. Test per card: "does this phrase answer
   the question, or explain the answer?" Answer → cloze; explanation → Extra. Extra must
   never contain the answer itself; the cloze must never contain explanation.
6. **The question must STAND ON ITS OWN (his correction, 26/08/2026).** A random person with
   the knowledge must be able to answer from the visible text alone — name the domain and the
   subject explicitly, phrase it as a real question or a complete sentence. `"2" + 2 → ?`
   means nothing; `In Python, what does "2" + 2 evaluate to?` stands. `Attention recipe:`
   is a fragment; `What are the four steps of the attention recipe?` is a question.
   Minimum-information compresses the ANSWER, never the question's context. Think before
   making each card: read the visible text cold and ask "could a stranger answer this?"
7. **ONE correct answer per blank (his rule, 26/08/2026).** Given the visible text, a
   stranger with unlimited knowledge must converge on EXACTLY the clozed answer (synonyms
   fine) — never on a different, equally-correct one. Multiple answers are allowed only
   when the card is deliberately multi-part AND the visible text says so.

## The pre-import checklist (added 26/08/2026 after the red-team pass — apply to EVERY card
## BEFORE import; this checklist IS the review, so no post-hoc red-team should be needed)

Run each drafted card through all seven, in character as the knowledgeable stranger:

1. **Stranger test**: reading only the visible text — is exactly the clozed answer the one
   I'd give? If an alternative is equally right, the question is broken (fix via check 2).
   Real catches from 26/08: "de-duplicate a list" (set() vs dict.fromkeys() — the visible
   "need order" actually pointed at the answer the card marked wrong); "count-dict idiom"
   (Counter and defaultdict equally canonical); "unstage a file" (restore vs reset HEAD).
2. **Cue the family**: when legitimate alternatives exist, the question names the intended
   family — "using a plain dict and .get (no imports)", "(restore family)", "deduped AND
   sorted". The cue closes the alternatives WITHOUT leaking the answer.
3. **Enumerations**: each element its own {{c1::…}} blank (all hidden together — c1 only),
   and the COUNT named in the visible text ("What are the FOUR steps of…") so the reviewer
   knows when the recital is complete. Never a whole pipeline inside one blob cloze.
4. **No open lists**: "name three differences/examples of X" with no canonical set is
   banned — there are always dozens. Split into specific single-fact cards instead.
5. **No answer leakage**: examples, contrasts, or restatements that give the answer away
   go in Back Extra, never in the visible question text ("dog bites man = man bites dog"
   was the answer; sha256("hello")/("hellp") was the answer). Visible context orients;
   it never answers — Extra rewards the flip with the explanation.
6. **Dedup before import**: check the fact isn't already carded (module drill files first —
   a session miss-card restating an existing drill card is deleted, the drill card is
   enough; the importer only catches EXACT text duplicates, so this check is manual).
7. **Read it rendered**: fields are HTML — the importer escapes & < > automatically, but
   still sanity-check any card with symbols/code that it will display as intended.

## The Twenty Rules, distilled to what we actually apply

- **Understand before memorising** — cards are drafted from material he was TAUGHT this
  session, never from unread text (rules 1–3).
- **Minimum information principle** (rule 4) — the single most important rule: simple
  items, short answers, split complexity. Target: cloze answer ≤ ~8 words.
- **Cloze deletion is easy and effective** (rule 5) — our default by his law above.
- **Avoid sets and enumerations** (rules 9–10) — never ask "list everything about X" in one
  blank; break lists with one-cloze-per-element (his rule 3 = exactly this).
- **Combat interference** (rule 11) — similar cards (LLM01…LLM10, flag lists) get a
  distinguishing context cue in the visible text so they can't blur together.
- **Optimise wording** (rule 12) — compact trigger, compact answer; the question should
  fire the memory in one read.
- **Context cues** (rule 16) — lead with the domain when ambiguous: "Python:", "git:",
  "pandas:". Tags carry the rest.
- **Redundancy is allowed** (rule 17) — the same fact from two angles (what→name,
  name→what) is fine; identical restatements are not.
- **Sources & date stamps** (rules 18–19) — tags carry module provenance; session-miss
  cards carry `session::YYYY-MM-DD`.
- **Personalise** (rule 14) — his real estate (monk-mode, psoc-portal, his site, ledger
  incidents) beats generic examples; keep those references in.

## Matuschak additions (r/Anki's other canon)

- **Tractable**: aim for ~90% correct; if a card keeps failing, split it or add a cue.
- **Effortful**: no binary yes/no cards; no cards answerable by pattern-matching the
  phrasing without knowing the thing.
- **Consistent**: one card, one reliably-same answer — "name a…" open questions are banned
  unless any correct instance is acceptable and marked so.
- **No orphans**: every card connects to something he built, read, or was taught.

## Mechanics (this repo)

- Source of truth: `anki/cards/mNN-<slug>.tsv` (module drills) + `anki/sessions/YYYY-MM-DD.tsv`
  (per-session miss cards). Format: `Question¶{{c1::direct answer}}<TAB>Extra<TAB>tags`
  (Extra column = the explanation; may be empty) — tags space-separated and always LAST,
  cloze markup ({{c1::…}} only) after the ¶, never before it.
- Import: `python tools/anki_import.py <file> --deck "AI Mastery::NN <name>"` (AnkiConnect;
  cloze model; duplicate-safe on Text).
- Tags: `ai-mastery::mNN` per module + ONE topic tag (`python` `git` `web` `shell` `crypto`
  `security` `ml` `transformers` `pandas` `evals` `automation` `method`); session misses add
  `session::YYYY-MM-DD` instead of a module tag.
- Formatting: plain text only in fields — no HTML, no styling; Anki's stock Cloze template
  IS the formatting (his "default formatting" rule).
- **Image occlusion is manual and his**: when a fact is spatial/visual (a diagram, a stack,
  a graph shape, an annotated screenshot), do NOT force it into text cloze — flag it to him
  in chat as an image-occlusion candidate and move on. He makes those himself in Anki.
