# Exercise 02 — One attention head, by hand (the module's centrepiece)

**~35 min, paper + calculator.** Three tokens, 2-dimensional vectors (real models use
thousands; the arithmetic is identical). Round to 4 dp. Verify with `python check.py`.

## The setup

```
token 1        token 2        token 3
Q: [1, 0]      Q: [0, 1]      Q: [1, 1]
K: [1, 0]      K: [0, 1]      K: [1, 1]
V: [2, 0]      V: [0, 4]      V: [1, 1]

d = 2   (so the scaling divisor is √2 ≈ 1.4142)
softmax(s)_i = e^(s_i) / Σ_j e^(s_j)
```

## Part A — unmasked attention for TOKEN 2

1. Score token 2's Q against each K: `s_i = (Q₂ · K_i) / √2` — three numbers.
2. Softmax those three scores → three weights that sum to 1.
3. Output = weighted average of the three V vectors (one 2-number vector).

## Part B — now apply causal masking

Token 2 may only attend to tokens 1 and 2 (never the future). Set token 3's score to −∞ —
in practice: drop it before the softmax — and redo steps 2–3.

4. The two masked weights.
5. The masked output vector.

## Part C — the understanding questions

6. Compare your Part A and Part B outputs. In one sentence: what did the mask cost token 2,
   and why is that cost *required* for a text-generating model?
7. Tokens 2 and 3 scored identically (0.7071) in Part A. Look at the Q and K vectors and
   explain why — then say what would have to change for token 3 to win.
8. Why divide by √d at all? (Hint: imagine d = 12,288 and dot products of large vectors —
   what happens to the softmax if the scores get huge?)
9. In one sentence each, what would change in this calculation if you had **8 heads** instead
   of one, and what does the model do with the 8 results?
