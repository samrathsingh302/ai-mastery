# Ex02 — reference diagram (open AFTER rebuilding from memory)

```
INTERNET TEXT (~44TB filtered, e.g. FineWeb)
        │  tokenise (text → token IDs; BPE)
        ▼
┌─────────────────────────────────────────────┐
│ STAGE 1 · PRETRAINING                       │  in: trillions of tokens
│ predict next token → loss → gradient descent│  out: BASE MODEL
│ months of GPUs, ~£millions                  │  (internet-document simulator;
└─────────────────────────────────────────────┘   lossy zip; vague recollection)
        ▼
┌─────────────────────────────────────────────┐
│ STAGE 2 · SUPERVISED FINE-TUNING (SFT)      │  in: labeller-written ideal convos
│ imitate the ideal helpful assistant         │  out: ASSISTANT MODEL
└─────────────────────────────────────────────┘  (simulation of an ideal labeller)
        ▼
┌─────────────────────────────────────────────┐
│ STAGE 3 · REINFORCEMENT LEARNING            │  in: many attempts + checkers
│ verifiable: keep what reaches right answers │  out: REASONING / POLISHED MODEL
│ unverifiable: RLHF via reward model (brief!)│
└─────────────────────────────────────────────┘
```

**One failure mode per stage (any correct mapping counts):**
- Stage 1 → strawberry-r's / spelling / 9.11-vs-9.9 (tokens; lossy compression; jaggedness)
- Stage 2 → hallucination (confident style over vague recollection); "no knowledge of self"
- Stage 3 → sycophancy / reward-gaming (preferred ≠ true; reward model is gameable)

**The five practical laws (you needed any two):**
1. If you need accuracy, put the source in the context — open-book beats memory.
2. Never force an instant verdict on anything hard — tokens are thinking.
3. Calibrate trust per task-type, never per model (jagged intelligence).
4. "Trained to be preferred" ≠ right — verify against docs/tests/runs, not confidence.
5. AI leverage is safe in proportion to your ability to verify the output (Kernighan).
