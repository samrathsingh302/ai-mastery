# Module 11 — Neural nets + transformers: intuition you can compute

> **What this is:** the mechanism under module 01. There you learned what LLMs ARE and how
> they're made (three stages, tokens, hallucination, RLHF). Here you learn what's inside the
> box — and you compute a forward pass and an attention head **by hand, with a calculator**,
> because arithmetic you performed yourself never becomes mystical again. **~5h.**
> **B-lane** (theory/absorb — pairs with a code-heavy A-lane item; treadmill-compatible).
> **Prerequisites:** module 01 (tokens, parameters, training/inference, context window are
> assumed and live in GLOSSARY.md). No calculus required — I'll show where it hides.

## The video canon for this module (verified 04/08/2026)

3Blue1Brown's *Neural networks* series — the consensus exception to "no long lectures".
**Correction to the plan: the series runs to chapter 7, not 8.**

| Ch | Title | ~Runtime | Published |
|----|-------|----------|-----------|
| 1 | But what is a neural network? | ~19 min | 05/10/2017 |
| 2 | Gradient descent, how neural networks learn | ~21 min | 2017 |
| 3 | What is backpropagation really doing? | ~15 min † | 03/11/2017 |
| 4 | Backpropagation calculus | ~15 min † | 2017 |
| 5 | But what is a GPT? Visual intro to transformers | ~27 min | 01/04/2024 |
| 6 | Attention in transformers, step-by-step ‡ | ~26 min | 07/04/2024 |
| 7 | How might LLMs store facts | ~23 min | 31/08/2024 |

† runtimes for ch.3/4 come from one source cluster and may be off by a few minutes.
‡ some listings title it "…visually explained"; same video. Series ≈ 2.5h at 1×.
Also verified and worth your time: **bbycroft.net/llm** (Brendan Bycroft — a 3D, navigable
transformer you can fly through: nano-GPT, GPT-2 small/XL, GPT-3) and **Transformer
Explainer** (poloclub.github.io/transformer-explainer — runs a real GPT-2 small in your
browser and lets you turn the temperature dial). Both free, both open in a tab.

**Read these notes first**, then watch — the notes make the videos revision, per the house
method. Sections map to the chapters.

---

# Part A — Neural networks (chapters 1–4)

## A1 · A neuron is a weighted vote

- **Neuron** *(plain words)*: a tiny function that takes several numbers in, multiplies each
  by its own importance number, adds them up with an offset, and passes the total through a
  squashing function. *(Analogy: a committee member deciding "should I be excited?" by
  weighting several signals — "the venue is free" ×2, "it clashes with exams" ×−3 — adding a
  personal bias, then deciding how loudly to speak.)*
- **Weight** = how much one input matters to this neuron (learned). **Bias** = the neuron's
  built-in eagerness or reluctance (learned). Both are just numbers — the **parameters**
  from module 01, seen up close.
- **Activation function** *(plain words)*: the squash. Without one, stacking layers is
  pointless (a pile of straight-line functions is still a straight line). Two you need:
  **ReLU** — `max(0, x)`: negative becomes 0, positive passes through (*analogy: a one-way
  valve*), and **sigmoid** — squeezes any number into 0…1 (*analogy: a dimmer switch that
  can't go below off or above full*).

```
one neuron:   out = squash( w1*x1 + w2*x2 + ... + bias )
```

## A2 · A network is layers of neurons

A **layer** is a row of neurons all looking at the same inputs; the next layer looks at
their outputs. **Input layer** (your data as numbers) → **hidden layers** (intermediate
features nobody named) → **output layer** (the answer). *(3B1B's example: 784 pixel
brightnesses → hidden layers → 10 digit scores.)*

The seductive story is that hidden neurons learn tidy human concepts ("this one detects a
loop"). Ch.1 shows the honest version: they learn *whatever numerical patterns reduce
error*, which mostly look like noise to us. Hold that thought — it's the root of
interpretability being hard, and of module 01's "jagged intelligence".

**Your by-hand forward pass** (exercise 1 makes you do it; here's the shape):
inputs `[1, 0.5]` → two ReLU neurons → one sigmoid output. Every step is multiply, add,
squash. That's the whole computation — a trillion times over, in a big model.

## A3 · Learning = adjusting the dials to reduce a number

- **Loss / cost** *(plain words)*: one number saying how wrong the network was on this
  example (module 01 met it; now you see it steer). *(Analogy: your score in a round of
  golf — lower is better, and it's the ONLY thing you optimise.)*
- **Gradient descent** *(plain words)*: for each parameter, work out which direction of
  change would lower the loss, and take a small step that way. Repeat forever. *(Analogy:
  standing on a foggy hillside, feeling which way is downhill with your feet, stepping,
  repeating. You reach a valley — not necessarily the deepest valley, and that's fine.)*
- **Learning rate**: how big each step is. Too small = crawling; too big = leaping over the
  valley and bouncing. Nearly every "training didn't work" story starts here.
- **Gradient** *(plain words)*: the list of "which way is downhill" numbers, one per
  parameter — the direction of steepest increase, so you step against it. Where the calculus
  lives; you can drive without opening this bonnet.

## A4 · Backpropagation = blame, propagated backwards

**Backprop** *(plain words)*: an efficient way to compute how much EACH parameter
contributed to the error, by starting at the output and passing blame backwards, layer by
layer. *(Analogy: a project goes wrong; you ask the last team what went wrong, they
apportion blame to the teams that fed them, who apportion further back — one pass, everyone
gets their share, nobody recomputes the whole project.)*

Ch.3 gives the intuition (each output neuron "wants" changes in the previous layer's
activations, weights and biases, and those wants are averaged over the batch); ch.4 shows
it's the **chain rule** applied repeatedly. What matters for you: backprop is not a
different learning idea — it's the *fast bookkeeping* that makes gradient descent possible
on billions of parameters. Karpathy's Zero to Hero (Tier 3, mandatory AI-free) has you build
it from nothing; this module just needs you to lose the mystery.

**Checkpoint A — you can now:** compute a small forward pass by hand; explain weights,
biases, activations, loss, gradient descent, learning rate and backprop with your own
analogies; and say why activation functions exist at all.

---

# Part B — Transformers (chapters 5–7)

A **transformer** is the architecture behind GPT/Claude/Gemini. Same ingredients as Part A —
weighted sums and squashes — arranged so that **words can look at each other**.

## B1 · Text becomes vectors

- **Embedding** *(plain words)*: each token becomes a long list of numbers (a **vector**)
  that positions it in a "meaning space" — similar meanings land near each other. *(Analogy:
  a map where Leeds and Manchester sit close together, and "Tuesday" is somewhere else
  entirely; the coordinates ARE the meaning, learned from data.)* *(Example: GPT-3 uses
  12,288 numbers per token; the tokeniser from module 01 decides what a token is first.)*
- **Position** matters too — "dog bites man" ≠ "man bites dog" — so positional information
  is added to each embedding. Without it, a transformer sees a bag of words.

## B2 · Attention: every token asks a question of every other token

This is the idea the whole architecture is named for. Each token produces three vectors:

- **Query (Q)** — what I'm looking for *(analogy: a personal ad: "seeking an adjective that
  describes me")*
- **Key (K)** — what I offer *(analogy: the label on my jar: "I am an adjective")*
- **Value (V)** — what I'd actually hand over if you picked me *(analogy: the contents)*

Mechanically, for each token: **score every other token** by dot-product of my Q with their
K (bigger = better match), **divide by √d** (keeps numbers sane as vectors get longer),
**softmax** the scores into weights that sum to 1 (*plain words: turn a list of scores into
percentages, exaggerating the leader; analogy: a vote share*), then take the **weighted
average of their V vectors**. That result is folded back into my own vector.

The famous line: *"attention is how the word 'blue' in 'fluffy blue creature' gets moved
into the vector for 'creature'."* Context updates meaning, arithmetically.

**Causal masking**: in a text-generating model, a token may only attend to earlier tokens —
future ones are scored −∞ before the softmax so their weight is 0. *(Analogy: an exam where
you may look at your earlier answers but not the pages ahead.)* Exercise 2 has you compute
an attention head by hand, twice — unmasked and masked — and the two answers differ, which
is the lesson.

**Multi-head attention**: run many attention operations in parallel with different learned
Q/K/V projections, then combine. *(Analogy: several readers of the same sentence — one
tracking grammar, one tracking who-did-what-to-whom, one tracking tone — then pooling
notes.)* GPT-3: 96 heads per layer, 96 layers.

## B3 · The MLP layers: where facts seem to live (ch.7)

Between attention blocks sit ordinary Part-A layers (an **MLP** — multi-layer perceptron —
*plain words: a plain feed-forward stack, the thing you computed in exercise 1*). Ch.7's
argument, with the "Michael Jordan plays basketball" worked example: attention MOVES
information between tokens, while these MLPs are where stored facts get looked up and added.
They hold about two-thirds of the parameters.

- **Superposition** *(plain words)*: a network stores far more concepts than it has neurons
  by giving each concept a *direction* in the space rather than its own neuron — directions
  can overlap, like many radio stations sharing a band. *(Consequence: single neurons rarely
  mean one clean thing — the honest version of A2's caution, and why interpretability is a
  research field rather than a lookup.)*

## B4 · The whole stack, one sentence

Tokens → embeddings (+ position) → **[attention: tokens exchange context] → [MLP: facts and
transformations]**, repeated dozens of times → a final vector per position → **unembedding**
into a score for every possible next token → **softmax** → probabilities → sample one →
append → do it all again for the next token.

- **Temperature** *(plain words)*: a dial applied before the softmax that flattens or
  sharpens the probabilities — low = predictable/repetitive, high = surprising/incoherent.
  *(Analogy: the "how adventurous?" knob on a playlist shuffle.)* You compute this in
  exercise 3; the Transformer Explainer lets you drag it live on a real GPT-2.

**Now re-read module 01's laws** — every one is now mechanical, not folklore: *"models need
tokens to think"* (each token is one pass through this entire stack — that IS the compute
budget) · *"context beats weights"* (context arrives via attention over exact tokens;
weights are the lossy MLP store) · *"jagged intelligence"* (superposed features, not clean
concepts).

**Checkpoint B — you can now:** explain embeddings, Q/K/V attention, masking, multi-head,
MLP-as-fact-store, superposition and temperature in your own words; compute one attention
head by hand; and trace a single token's journey through the whole stack.

## The optional deep end (not this module)

Karpathy's **Neural Networks: Zero to Hero** — 8 videos, starting with "The spelled-out
intro to neural networks and backpropagation: building micrograd" (~2h26m, 16/08/2022) —
builds all of the above from scratch in code. It's Tier 3 core and **mandatory AI-free**.
This module is deliberately the intuition, so that when you get there you're only fighting
the code, not the ideas.

## Sources (verified 04/08/2026, with honest confidence)

- 3Blue1Brown *Neural networks* chapters 1–7 — 3blue1brown.com lesson pages + YouTube
  (playlist `PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi`). Chapter set confirmed to END AT 7; ch.3/4
  runtimes single-sourced (flagged above); ch.6 title varies by listing.
- bbycroft.net/llm — Brendan Bycroft, 3D LLM visualisation (nano-GPT, GPT-2 small/XL,
  GPT-3); source at github.com/bbycroft/llm-viz.
- Transformer Explainer — poloclub.github.io/transformer-explainer (Georgia Tech; runs
  GPT-2 small in-browser; arXiv:2408.04619).
- Karpathy Zero to Hero — karpathy.ai/zero-to-hero.html + github.com/karpathy/nn-zero-to-hero
  (8 videos confirmed from both).
- All exercise arithmetic in this module was computed and verified numerically tonight.
