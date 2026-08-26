# CARD-RULES.md — read this BEFORE drafting any Anki card

> Samrath's instruction (26/08/2026): every card-making session reviews this document first.
> Sources: SuperMemo's Twenty Rules (supermemo.com/en/blog/twenty-rules-of-formulating-knowledge)
> + Andy Matuschak's prompt-writing guide (andymatuschak.org/prompts) + Samrath's own rules.
> Reddit r/Anki was unreachable from the session that built this (26/08/2026); these two are
> the sources that community itself canonises.

## Samrath's format law (overrides everything below on conflict)

1. **Cloze for ALL cards.** Note type = Anki's built-in **Cloze** (default formatting, no
   custom CSS). The question/context stays VISIBLE; the answer is the cloze.
   `What is a token? {{c1::the chunk-of-text unit models read and write}}`
2. **Never repeat the question in the answer.** `What is X? X is Y` is banned — the cloze
   holds `Y` alone. Reading time is review time.
3. **Multi-part answer = multiple clozes.** "Three properties of a hash?
   {{c1::one-way}} · {{c2::deterministic}} · {{c3::collision-resistant}}" — each review
   shows the others as context, one easy blank at a time.
4. **Too big → split into more notes.** One idea per note. If a card teaches two things,
   it is two cards.
5. **No filler words.** Every word costs reading time at every future review. Cut
   parentheticals, hedges, and second explanations; keep one memorable hook at most.
6. **The question must STAND ON ITS OWN (his correction, 26/08/2026).** A random person with
   the knowledge must be able to answer from the visible text alone — name the domain and the
   subject explicitly, phrase it as a real question or a complete sentence. `"2" + 2 → ?`
   means nothing; `In Python, what does "2" + 2 evaluate to?` stands. `Attention recipe:`
   is a fragment; `What are the four steps of the attention recipe?` is a question.
   Minimum-information compresses the ANSWER, never the question's context. Think before
   making each card: read the visible text cold and ask "could a stranger answer this?"

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
  (per-session miss cards). Format: `Text<TAB>tags` — tags space-separated, cloze markup in Text.
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
