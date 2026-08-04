# Project 11 — Explain the machine (teach-to-learn, on your own terms)

**What:** produce `explain-the-machine.md` — YOUR explanation of how an LLM works, written
for a specific real person, plus a diagram you drew. ~2h. The plan's teach-to-learn move:
you don't know it until you can hand it to someone else.

## Steps

1. **Pick a real audience** and name them in the file: a PSOC committee member, a Punjabi-soc
   friend doing a non-technical degree, or your parents. Their vocabulary sets your bar.
2. **Write ~800 words, no jargon unexplained**, covering: what a neuron does · why layers ·
   what training changes · what attention is for · why the model sometimes confidently makes
   things up. Every term you use must have been introduced by you first (the baby rule,
   applied by you rather than to you).
3. **Draw the stack by hand** — paper, photo it in. Tokens → embeddings → attention → MLP →
   ×N layers → unembedding → softmax → sample. Label what moves where. Hand-drawn beats
   copy-pasted: the wobbles are where your understanding is.
4. **The 3 hard questions** — answer at the end, in your own words:
   - Where do "facts" live in a model, and how confident should you be in that answer?
   - Why does more context beat more training for accuracy on YOUR data?
   - What does a model literally spend compute on when it "thinks step by step"?
5. **Test it**: read it aloud to the actual person (or send it). Note every question they
   asked — each one is a gap in your explanation, which is to say a gap in your model.

## Acceptance checklist

- [ ] Named audience; no unexplained jargon (get them to flag any — they will)
- [ ] Hand-drawn diagram photographed and committed
- [ ] The three hard questions answered without notes first
- [ ] Their questions logged, with a one-line fix for each
- [ ] Journalled: which explanation you found hardest to write (that's your weakest area,
      and it's your next drill topic)
