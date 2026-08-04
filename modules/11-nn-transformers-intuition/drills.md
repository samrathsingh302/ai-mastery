# Drills — module 11

## Anki-importable block (tab-separated: Front ⇥ Back)

What does one neuron compute?	squash(w1*x1 + w2*x2 + ... + bias) — a weighted vote with a personal bias, then a squash.
Weight vs bias?	How much an input matters to this neuron vs the neuron's built-in eagerness; both learned numbers.
Why do activation functions exist?	Without them a stack of layers collapses to one straight-line function — depth would buy nothing.
ReLU in one line?	max(0, x) — a one-way valve: negatives become 0, positives pass through.
What is a dead ReLU?	A neuron outputting 0 for every input: no gradient flows back through it, so it stops learning entirely.
Loss / cost is…	One number saying how wrong this prediction was — the only thing optimisation pushes down.
Gradient descent, in one analogy?	Foggy hillside: feel which way is downhill, take a small step, repeat.
Learning rate too big / too small?	Leaping over the valley and bouncing / crawling forever. Most "training didn't work" starts here.
Backpropagation is…	Efficient blame-assignment: start at the output, pass responsibility backwards layer by layer (the chain rule, applied repeatedly).
Backprop vs gradient descent?	Backprop computes the gradients (bookkeeping); gradient descent uses them to step. Different jobs.
An embedding is…	A token turned into a vector positioning it in a learned "meaning space" — nearby vectors, related meanings.
Why add positional information?	Otherwise the model sees a bag of words: "dog bites man" and "man bites dog" would be identical.
Q, K, V in one line each?	Query = what I'm looking for · Key = what I offer · Value = what I hand over if picked.
The attention recipe (4 steps)?	Score Q·K for every token → divide by √d → softmax into weights → weighted average of the V vectors.
Why divide by √d?	Long vectors make dot products huge; softmax of huge scores becomes a hard max and gradients vanish. Scaling keeps it soft and trainable.
What is causal masking and why?	Future tokens get score −∞ (weight 0) — a generating model must predict the next token WITHOUT seeing it, or it learns to cheat.
Multi-head attention?	Many attention operations in parallel with different learned projections, concatenated and mixed — several readers of one sentence, pooling notes.
What do the MLP layers do (3B1B ch.7)?	Attention MOVES information between tokens; the MLPs store and retrieve facts — about two-thirds of the parameters.
Superposition?	More concepts than neurons: each concept is a DIRECTION in the space, and directions overlap — so a single neuron rarely means one clean thing.
The full stack, in order?	Tokens → embeddings + position → [attention → MLP] ×N layers → unembedding → softmax → sample → repeat.
Temperature does what?	Divides logits before softmax: low = sharper/repeatable, high = flatter/more surprising. It changes wandering, not knowledge.
Greedy decoding's failure mode?	Always taking the top token — loops, blandness, and it hides the model's uncertainty from you.
"Models need tokens to think" — mechanically?	Each generated token is one full pass through the whole stack; more tokens = more total computation spent.
Why does context beat weights for accuracy?	Context arrives via attention over the exact tokens present; weights are the lossy, vague-recollection store (module 01's law, now mechanical).

## Quick-fire (aloud, 30 seconds)

1. Q, K, V? 2. Why √d? 3. What does masking prevent? 4. Where do facts seem to live?
*(query/key/value · keeps softmax soft · peeking at future tokens · the MLP layers)*
