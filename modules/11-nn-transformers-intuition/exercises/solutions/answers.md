# Module 11 — worked answers (open AFTER check.py, or after 30 min stuck)

## Ex01 — forward pass

```
z1 = 0.5(1.0) + (-1.0)(0.5) + 0.0 = 0.0
z2 = 2.0(1.0) + 0.25(0.5) + 0.5  = 2.625
a1 = max(0, 0.0)   = 0.0          a2 = max(0, 2.625) = 2.625
z_out = 1.0(0.0) + (-1.0)(2.625) + 0.5 = -2.125
y = 1 / (1 + e^2.125) = 0.1067
```

**6.** With a1 = 0, the output is completely insensitive to hidden-neuron-1's weights *for
this input* — and during training, gradients flowing back through a ReLU that output 0 are
also 0. If a neuron outputs 0 for *every* input it stops learning entirely: a **dead ReLU**.

**7.** It would collapse to a single linear (straight-line) function of x — a weighted sum of
weighted sums is still a weighted sum. Depth would buy nothing: you could always replace the
stack with one layer. Activations are what make extra layers able to represent new shapes.

**8.** Anything binary: "will this workout be logged today?", "is this email spam?". A loss
(e.g. binary cross-entropy) compares y against the true 0/1 label and returns one number
saying how wrong it was — the thing gradient descent pushes down.

## Ex02 — attention

**Part A** (token 2 as the query; Q₂ = [0,1]):

```
s1 = ([0,1]·[1,0])/√2 = 0/1.4142    = 0.0000
s2 = ([0,1]·[0,1])/√2 = 1/1.4142    = 0.7071
s3 = ([0,1]·[1,1])/√2 = 1/1.4142    = 0.7071
softmax → 0.1978, 0.4011, 0.4011      (sums to 1.0000)
output = 0.1978·[2,0] + 0.4011·[0,4] + 0.4011·[1,1] = [0.7967, 2.0056]
```

**Part B** (mask token 3):

```
softmax over (0.0000, 0.7071) → 0.3302, 0.6698
output = 0.3302·[2,0] + 0.6698·[0,4] = [0.6605, 2.6790]
```

**6.** The mask cost token 2 all access to token 3's value — the output moved from
[0.80, 2.01] to [0.66, 2.68]. It's required because a generating model must predict token 3
*before it exists*: if training let position 2 peek ahead, the model would learn to cheat and
then fail at inference, where the future genuinely isn't there.

**7.** Q₂ = [0,1]; K₂ = [0,1] gives dot 1; K₃ = [1,1] also gives dot 1 (the extra 1 in the
first slot is multiplied by Q₂'s 0). They tie because the query only "cares about" dimension
2. For token 3 to win, its K would need a *larger* component in the dimension Q₂ queries —
e.g. K₃ = [1, 2] → dot 2 → score 1.4142.

**8.** Dot products of long vectors grow roughly with √d, so unscaled scores become huge;
softmax of huge numbers is effectively a hard max — one weight ≈ 1, the rest ≈ 0 — and
gradients through it vanish. Dividing by √d keeps scores in a range where softmax stays soft
and trainable.

**9.** With 8 heads you'd run this whole calculation 8 times in parallel, each with its own
learned projections producing different Q/K/V (so different heads attend to different
relationships). The 8 output vectors are concatenated and passed through one more learned
weight matrix that mixes them back into a single vector per token.

## Ex03 — temperature

```
T = 1.0 → 0.6590, 0.2424, 0.0986
T = 0.5 → 0.8638, 0.1169, 0.0193      (sharper — the leader takes more)
T = 2.0 → 0.5017, 0.3043, 0.1940      (flatter — outsiders gain)
```

**5.** T = 2.0. Rule: **higher temperature flattens the distribution** (more randomness),
lower sharpens it toward the top token.

**6.** Tutor/explanations: low (≈0–0.3) — you want the same correct explanation twice.
Brainstorming: higher (≈0.8–1.0) — you want to see the tail. (Note evals: module 09's
programmatic tasks want low temperature so results are comparable.)

**7.** Greedy decoding gets stuck in loops and bland phrasing — it can repeat a sentence
forever, because the locally-likeliest token at each step doesn't optimise the sequence.
It also always produces the identical output, which hides a model's uncertainty from you.

**8.** Not sufficient. Hallucination's mechanism (module 01) is confident-answer *style*
applied where the weights hold only vague recollection — that happens at temperature 0 too,
deterministically. Temperature changes how much the sampling wanders; it doesn't create or
remove the missing knowledge. Grounding (context, tools) attacks the cause; the temperature
dial only shapes the noise.
