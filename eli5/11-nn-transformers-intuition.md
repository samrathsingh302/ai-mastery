# 11-nn-transformers-intuition — like you're 5

Taught in `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\TEACH.md`; the one-line reminders are `GLOSSARY.md` → `## Module 11 — neural nets + transformers`. The `python -c` lines run from any folder in PowerShell or Git Bash; the attention dials are in `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\interactive\attention-lab.html` (`start` it from PowerShell). Every number below differs from the exercises' numbers: ex01–ex03 are still yours to compute by hand.

### Activation function
**Like you're 5:** A dimmer switch that can't go below off or above full. Each little brain cell in the machine passes its total through one of these. Without that squash, stacking a hundred layers of cells would be no cleverer than one layer.
**The real words:** The squash (ReLU: `max(0, x)`; sigmoid: 0…1) that stops stacked layers collapsing into one straight line. → [11 A1](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** `python -c "print([max(0, x) for x in [-2, -0.5, 0, 1.5, 3]])"` → `[0, 0, 0, 1.5, 3]` — ReLU, the one-way valve: negatives become 0, positives pass through.

### Attention (Q/K/V)
**Like you're 5:** Every word in a sentence holds up a sign saying what it's looking for, and wears a label saying what it is. Each word checks every other word's label against its own sign, listens most to the best matches, and borrows a bit of their meaning.
**The real words:** Every token scores every other (Q·K/√d), softmaxes the scores into weights, and takes a weighted average of their values; how "blue" in "fluffy blue creature" gets moved into "creature". → [11 B2](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** `start C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\interactive\attention-lab.html` and turn the dials; a real GPT-2 small runs in the browser at `https://poloclub.github.io/transformer-explainer/`.

### Backpropagation
**Like you're 5:** A team project goes wrong. You ask the last person what happened; they share out the blame to the people who handed them work, who pass it further back. One trip backwards, and everyone learns how much of the mess was theirs.
**The real words:** Efficient blame-assignment backwards through the layers (the chain rule, repeated); it computes the gradients that gradient descent then uses. → [11 A4](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** 3Blue1Brown chapter 3, "What is backpropagation really doing?" (~15 min) — the video table in `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\TEACH.md` lines 16–24.

### Causal masking
**Like you're 5:** An exam where you may look back at your earlier answers, but the pages ahead are glued shut. When the machine writes word five, it can only look at words one to four; otherwise it could just peek at the answer.
**The real words:** Future tokens are scored −∞ before the softmax so their weight is 0, so a generating model can't peek ahead. → [11 B2](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** the mask for three tokens, one row per token doing the looking: `[[0, -inf, -inf], [0, 0, -inf], [0, 0, 0]]` — add it to the scores, and every −∞ becomes weight 0 after the softmax.

### Embedding
**Like you're 5:** A map where every word has its own spot. Words that mean similar things live close together, like Leeds and Manchester; "Tuesday" lives far off. A word's spot on the map is how the machine holds its meaning.
**The real words:** A token as a vector in a learned meaning space (GPT-3: 12,288 numbers per token); position information is added on top, so "dog bites man" ≠ "man bites dog". → [11 B1](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** a two-number toy map: `python -c "import math; print(math.dist((53.8, -1.5), (53.5, -2.2)), math.dist((53.8, -1.5), (10, 40)))"` → about `0.76` (Leeds to Manchester) and `60.34` (Leeds to a made-up "Tuesday" spot); real embeddings do this with thousands of numbers.

### Gradient descent / learning rate
**Like you're 5:** You're on a foggy hill and want to reach the bottom. You can't see, so you feel with your feet which way slopes down and take a step. Repeat. Step size matters: tiny steps take forever, and giant leaps jump right over the valley.
**The real words:** Step downhill on the loss surface (against the gradient) / how big each step is: too small crawls, too big bounces. → [11 A3](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** loss = x², downhill = −2x: `python -c "x=5.0; print([round(x:=x-0.3*2*x, 3) for _ in range(5)])"` → `[2.0, 0.8, 0.32, 0.128, 0.051]` slides to the bottom at 0; change `0.3` to `1.1` → `[-6.0, 7.2, -8.64, 10.368, -12.442]`, bouncing further out each step.

### Logits
**Like you're 5:** Before the judges hold up neat percentages, each one scribbles a raw score on scrap paper: some big, some small, some below zero. Those scribbles are logits. Only afterwards are they turned into chances that add up to 100.
**The real words:** The raw scores the final layer gives every possible next token, before softmax turns them into probabilities. → [11 ex03](../modules/11-nn-transformers-intuition/exercises/ex03-temperature.md)
**See it:** the three logits at the top of `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\exercises\ex03-temperature.md` — scores, not yet probabilities; turning them into probabilities is that exercise, so do it there.

### MLP layers
**Like you're 5:** Between the rounds where words pass notes to each other, each word goes alone into a big library and looks things up. "Michael Jordan" walks in, and "plays basketball" gets added to what it carries. Most of the machine's size is that library.
**The real words:** The plain feed-forward stacks between attention blocks; where stored facts appear to be looked up and added (~2/3 of the parameters). → [11 B3](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** 3Blue1Brown chapter 7, "How might LLMs store facts" (~23 min), the Michael Jordan worked example — `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\TEACH.md` line 24.

### Multi-head attention
**Like you're 5:** Several friends read the same sentence at once. One watches the grammar, one watches who did what to whom, one watches the mood. Then they pool their notes. Each friend is one "head".
**The real words:** Many attention operations in parallel with different learned Q/K/V projections, concatenated and mixed; GPT-3 has 96 heads per layer and 96 layers. → [11 B2](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** 3Blue1Brown chapter 6, "Attention in transformers, step-by-step" (~26 min) — `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\TEACH.md` line 23.

### Neuron
**Like you're 5:** A committee member deciding whether to cheer. They weigh several clues ("the venue is free" counts double, "it clashes with exams" counts against), add their own mood, then decide how loudly to cheer, or whether to stay quiet.
**The real words:** squash(weighted sum + bias): a weighted vote with a personal bias; the weights and the bias are parameters that training learns. → [11 A1](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** free venue ×2, exam clash ×−3, bias 0.5: `python -c "print(max(0, 2*1 + (-3)*1 + 0.5))"` → `0` — the total is −0.5, so ReLU says stay quiet.

### Softmax
**Like you're 5:** Turning raw scores into slices of one cake. Whatever the scores were, the slices always make exactly one whole cake, and the top score's slice grows extra big, bigger than plain fair sharing would give it.
**The real words:** Turns a list of scores into probabilities summing to 1 (exponentiate each, divide by the total), exaggerating the leader. → [11 B2](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** the scores `[3, 1, 0]` become about `[0.84, 0.11, 0.04]` — 3 is 75% of the raw points, but it gets 84% of the cake.

### Superposition
**Like you're 5:** One small radio picks up far more stations than it has buttons, because the stations share the dial and overlap a little. The machine stores more ideas than it has cells the same way, so one cell rarely means just one thing.
**The real words:** More concepts than neurons: concepts as overlapping directions, which is why single neurons rarely mean one clean thing, and why interpretability is a research field. → [11 B3](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** three directions in two numbers: `(1, 0)`, `(-0.5, 0.87)`, `(-0.5, -0.87)` — three ideas in a space with room for two clean ones, each pair overlapping a little (dot product −0.5); real models do this in thousands of dimensions.

### Temperature
**Like you're 5:** The "how adventurous?" knob on a music shuffle. Turn it down and you hear your favourite song again and again. Turn it up and you get odd surprises, some brilliant, some nonsense. It changes how wild the picks are, not which songs you own.
**The real words:** Divides the logits before softmax: low sharpens and repeats, high flattens and surprises; it changes the wandering, not the knowledge. → [11 B4](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** drag the temperature dial in the Transformer Explainer, `https://poloclub.github.io/transformer-explainer/` (a real GPT-2 small in your browser); the by-hand version is `C:\Users\samra\repos\ai-mastery\modules\11-nn-transformers-intuition\exercises\ex03-temperature.md`.

### Transformer
**Like you're 5:** A word-guessing machine built like a factory line. Words go in as spots on the map; then, over and over, they pass notes to each other and look things up in the library. At the end it scores every possible next word, picks one, adds it, and starts again.
**The real words:** The architecture: embeddings → [attention → MLP] ×N → unembedding → softmax → sample, one full pass per generated token. → [11 B4](../modules/11-nn-transformers-intuition/TEACH.md)
**See it:** `https://bbycroft.net/llm` — Brendan Bycroft's 3D GPT you can fly through, from the input tokens to the output probabilities.
