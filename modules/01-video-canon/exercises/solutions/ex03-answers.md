# Ex03 — answers (open AFTER attempting; check.py gives the same verdicts interactively)

| # | Answer | One-line why | Review |
|---|--------|--------------|--------|
| 1 | **F** | No database — a lossy compression of training text into parameters; vague recollection, not lookup | A1 |
| 2 | **F** | The difference is post-training (SFT installs assistant behaviour), not data volume | A2 |
| 3 | **T** | Tokens are the model's only alphabet | A1 |
| 4 | **F** | No concept of truth — confident style + fuzzy memory, no intent | A2 |
| 5 | **T** | Context window = working memory; weights = vague recollection | A2 |
| 6 | **F** | No knowledge of self — the answer is trained/injected, not introspected | A2 |
| 7 | **T** | Fixed compute per token → more tokens = more total computation | A2 |
| 8 | **F** | Jagged intelligence — capability is Swiss cheese, not a single level | A2 |
| 9 | **T** | Automatic checking gives RL a reliable signal at scale | A3 |
| 10 | **F** | RLHF optimises human-preferred-ness via a reward model; preferred ≠ true | A3 |
| 11 | **T** | Kernighan's law — comprehension is the safety budget | B |
| 12 | **F** | It's software engineering with LLM integration (Ebbelaar's six stages) | C |
