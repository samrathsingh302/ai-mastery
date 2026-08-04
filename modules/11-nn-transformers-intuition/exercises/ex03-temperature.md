# Exercise 03 — Temperature, by hand (why models get boring or unhinged)

**~15 min.** The model's final layer produced these three **logits** *(plain words: raw
scores before they become probabilities)* for the next token:

```
"the" : 2.0        "a" : 1.0        "banana" : 0.1
```

Temperature T divides the logits BEFORE the softmax: `softmax(logit / T)`.

1. Compute the three probabilities at **T = 1.0** (the plain softmax).
2. Recompute at **T = 0.5**.
3. Recompute at **T = 2.0**.
4. Sanity: each set must sum to 1.0000.

## The understanding questions

5. Which temperature makes "banana" most likely? State the general rule in one sentence.
6. Your tutor sessions want reliable, repeatable explanations; a brainstorming session wants
   variety. Which temperature for each, and why?
7. At T → 0 the model always picks the top token (**greedy decoding**). Give one concrete
   failure mode of always-greedy output. (Hint: think about what happens in a long
   generation when the top token is "the".)
8. Connect to module 01: hallucination is often blamed on "high temperature". Using what you
   now know about WHERE hallucination comes from, is that explanation sufficient? Two
   sentences.

Check with `python check.py`.
