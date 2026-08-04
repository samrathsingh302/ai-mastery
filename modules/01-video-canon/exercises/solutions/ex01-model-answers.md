# Ex01 — model answers (open AFTER answering; grade harshly)

**1. Strawberry r's.** MUST contain: models read/write *tokens* (chunks with IDs), not letters;
the letters are invisible inside the chunks. GOOD adds: same reason arithmetic on digit-chunks
is shaky; tool use (a code interpreter) is the honest fix.

**2. Base model asking more questions.** MUST contain: a base model is an internet-*document
simulator* that continues text; on the internet, one exam question is often followed by more;
"answering" is behaviour installed later (post-training/SFT). GOOD adds: talking to an assistant
= talking to a simulation of an ideal labeller.

**3. Hallucination + pasting the source.** MUST contain BOTH knowledge kinds: weights = vague
recollection (lossy zip of the internet), context window = working memory (open book on the
desk); hallucination = confident-answer *style* (from SFT) applied where recollection is vague;
pasting the source moves the task from memory to open-book. GOOD adds: models can be trained to
say "I don't know"; search tools do the pasting automatically.

**4. Step by step.** MUST contain: compute per emitted token is fixed/shallow, so spreading
reasoning over many tokens buys more total computation; an instant verdict gets almost none.
GOOD adds: this is why reasoning models emit long chains; it's mechanism, not superstition.

**5. ChatGPT agreed with my essay.** MUST contain: RLHF optimises "which output would a human
*prefer*", via a trained reward model — preferred ≠ true; agreeing with the user tends to be
preferred (mechanical root of sycophancy). GOOD adds: the plan's rule — verify against
docs/tests/runs, never against the model's confidence; models fold when challenged either way.

**6. When is vibe coding rational.** MUST contain: fine for prototypes/small scope/stacks you
could write yourself; the deciding factor is whether you can read and debug the output
(Kernighan's law — debugging is twice as hard as writing). GOOD adds: the "not suck" wiring —
current context in, real errors visible, automatic verification around it.

**Scoring:** 0–2 each as per the exercise sheet. 9+/12 = pass. Every point dropped = one Anki
card into your curated import.
