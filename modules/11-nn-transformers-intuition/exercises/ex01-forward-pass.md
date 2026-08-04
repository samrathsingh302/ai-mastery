# Exercise 01 — A forward pass, by hand (paper + calculator, no code)

**Why by hand:** arithmetic you performed yourself stops being mystical. ~25 min.
Round to 4 decimal places. Check with `python check.py` (it asks for your numbers).

## The network

Two inputs → two ReLU neurons → one sigmoid output.

```
x  = [1.0, 0.5]

hidden neuron 1:  weights [ 0.5, -1.0 ]   bias 0.0
hidden neuron 2:  weights [ 2.0,  0.25 ]  bias 0.5
        activation: ReLU  →  max(0, z)

output neuron:    weights [ 1.0, -1.0 ]   bias 0.5
        activation: sigmoid  →  1 / (1 + e^(-z))
```

## Compute, in order (write every intermediate down)

1. `z1` for hidden neuron 1 = w·x + b
2. `z2` for hidden neuron 2
3. `a1`, `a2` — after ReLU
4. `z_out` = output weights · [a1, a2] + bias
5. `y` = sigmoid(z_out)

## Then answer these (they're the actual lesson)

6. One hidden neuron output 0. What does that mean for the OUTPUT neuron's dependence on
   that neuron's weights right now? (This is "dead ReLU", and it's why people worry about it.)
7. If you removed both activation functions, the whole three-neuron network would collapse
   into what kind of function of `x`? Why does that make deep stacks pointless without them?
8. The output is a probability-shaped number. Name one thing this network could be
   predicting, and what a loss would compare it against.
