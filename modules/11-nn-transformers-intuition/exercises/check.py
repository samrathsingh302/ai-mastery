#!/usr/bin/env python3
"""Checker for module 11's by-hand arithmetic (ex01 forward pass, ex02 attention,
ex03 temperature). Stdlib only — no pandas/numpy needed.

  python check.py            all three
  python check.py ex02       just one
Answers are compared to 3 dp, so small rounding differences pass.
"""
import math
import sys

TOL = 5e-4


def ask(label):
    while True:
        raw = input(f"  {label}: ").strip().replace(",", " ")
        try:
            return [float(p) for p in raw.split()]
        except ValueError:
            print("    numbers please (space-separated if more than one)")


def close(got, want):
    return len(got) == len(want) and all(abs(g - w) < TOL for g, w in zip(got, want))


def check(label, want, hint):
    got = ask(label)
    if close(got, want):
        print("    ✓")
        return 1
    print(f"    ✗ expected {' '.join(f'{w:.4f}' for w in want)}  — {hint}")
    return 0


def ex01():
    print("\n=== ex01 · forward pass ===")
    s = 0
    s += check("z1 and z2 (two numbers)", [0.0, 2.625],
               "z = w1*x1 + w2*x2 + b, per neuron")
    s += check("a1 and a2 after ReLU", [0.0, 2.625], "ReLU = max(0, z)")
    s += check("z_out", [-2.125], "1.0*a1 + (-1.0)*a2 + 0.5")
    s += check("y = sigmoid(z_out)", [0.1067], "1 / (1 + e^(-z))")
    return s, 4


def ex02():
    print("\n=== ex02 · attention ===")
    s = 0
    s += check("A1 · three scores for token 2", [0.0, 0.7071, 0.7071],
               "(Q2 · K_i) / sqrt(2)")
    s += check("A2 · three softmax weights", [0.1978, 0.4011, 0.4011],
               "e^s_i / sum(e^s); they must sum to 1")
    s += check("A3 · output vector (two numbers)", [0.7967, 2.0056],
               "weighted average of the V vectors")
    s += check("B4 · two masked weights", [0.3302, 0.6698],
               "drop token 3, softmax over the remaining two")
    s += check("B5 · masked output (two numbers)", [0.6605, 2.679],
               "weighted average of V1 and V2 only")
    return s, 5


def ex03():
    print("\n=== ex03 · temperature ===")
    s = 0
    s += check("T=1.0 · three probabilities", [0.659, 0.2424, 0.0986], "softmax(logits)")
    s += check("T=0.5 · three probabilities", [0.8638, 0.1169, 0.0193],
               "softmax(logits / 0.5) — sharper")
    s += check("T=2.0 · three probabilities", [0.5017, 0.3043, 0.194],
               "softmax(logits / 2.0) — flatter")
    return s, 3


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else None
    parts = {"ex01": ex01, "ex02": ex02, "ex03": ex03}
    total = maxi = 0
    for name, fn in parts.items():
        if which and not name.startswith(which):
            continue
        got, mx = fn()
        total += got
        maxi += mx
    print(f"\n{total}/{maxi} numeric answers correct.")
    if total == maxi:
        print("You computed a neural network and an attention head by hand. "
              "The box is no longer black — do the project.")
    else:
        print("Re-do the misses ON PAPER (not by reading the answer): the point is the "
              "arithmetic passing through your hand.")


if __name__ == "__main__":
    main()
