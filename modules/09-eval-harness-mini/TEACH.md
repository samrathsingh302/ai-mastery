# Module 09 — Eval harness mini: judge models with a method

> **What this is:** you build and run a real evaluation: **10 tasks × 2 models, blind-graded,
> one results table** — using your own `claude` CLI (verified on this machine: 2.1.221) so it
> runs on your Max subscription, no API key. **~8h.** Output: the plan's promise — *you judge
> models with a method*, never vibes.
> **Why this matters more than most modules:** verification is the appreciating asset (module
> 01, idea #2). An eval is verification INDUSTRIALISED — the exact skill Tier 3/4 build on
> (20-task harness, agent-with-evals, RAG-with-evals), started here at motorcycle size.

## The five ideas (80/20 first)

1. **An eval = fixed tasks + a scoring method + the discipline to not peek.** Remove any of
   the three and you're back to vibes. *(Analogy: a taste test with printed scorecards and
   blindfolds — versus "I reckon the left one's nicer".)*
2. **Two scoring families:** **programmatic** (a checker script decides: exact match, test
   cases pass, regex validates — cheap, objective, limited to checkable tasks) and
   **rubric/blind** (a human — you — grades against written criteria WITHOUT knowing which
   model wrote which answer). Real harnesses mix both; so does yours (6 programmatic + 4
   rubric).
3. **Blindness is the whole integrity of rubric grading.** You WILL favour the model you
   expect to be better — everyone does (module 01's trust-calibration lesson, pointed at
   yourself). The harness shuffles and anonymises to A/B before you see anything; the
   reveal comes only after scores are locked.
4. **Task design is where evals are won or lost:** representative (things you actually ask
   models), verifiable (a right answer or a written rubric), small (one skill per task),
   and stated crisply (a model failing because YOUR prompt was ambiguous measures you, not
   it). ex01 makes you write 4 tasks against these criteria.
5. **One run is an anecdote.** Models are stochastic; serious evals repeat (pass@k). Yours
   does 1 repeat per task for budget sanity — the findings file makes you say, in writing,
   what that limits: differences of one task are noise, patterns across task TYPES are
   signal.

## The harness (read the code — it's ~230 lines, all module-03/04 Python)

```
exercises/
  tasks.json        # the 10 tasks: id, prompt, scoring type, checker data, rubric
  run_eval.py       # asks both models everything, saves outputs (+ --dry-run fixtures)
  grade.py          # programmatic scores + blind rubric grading -> results.csv + table
  fixtures/         # canned model outputs so the pipeline tests OFFLINE
```

- `run_eval.py --model-a haiku --model-b sonnet` calls your CLI per task:
  `claude -p "<prompt>" --model <m>` (print mode: answer to stdout, no session). Models are
  FLAGS, not hardcoded — swap any two aliases/ids you like; the point is the method.
- `--dry-run` uses `fixtures/` instead of calling anything — the whole pipeline (run →
  grade → table) is testable offline; that's also how this module was verified tonight.
- Scoring types in tasks.json: `exact` (normalised string equality) · `contains-all` (every
  required token present) · `code-tests` (the answer's Python function must pass embedded
  test cases, run in a subprocess with a timeout) · `regex-cases` (the answer-regex must
  match/reject given cases) · `rubric` (criteria text; graded blind in grade.py).
- `grade.py` prints programmatic scores, then walks the rubric tasks: shows the task + the
  two answers as **A/B (shuffled per task)**, collects your 0–2 scores against the printed
  criteria, THEN reveals the mapping and writes `results.csv` + a markdown table.

## Running it for real (~1–2h incl. grading)

1. `python run_eval.py --dry-run` then `python grade.py --dry-run` — learn the flow on
   fixtures first (grade honestly even though it's canned; it's rubric practice).
2. Pick two models you actually care about comparing (e.g. your default vs the small one).
3. `python run_eval.py --model-a <one> --model-b <two>` (10 tasks × 2 = 20 CLI calls —
   watch them stream).
4. `python grade.py` — programmatic first, then blind rubric round. No peeking at raw
   output files before grading: that's the discipline the module exists to install.
5. `findings.md` (project): the table + three sentences — biggest gap, biggest surprise,
   and what you would NOT conclude from n=1.

## Reading the results like an engineer

- Per-family scores beat the single total: a model can win code-tests and lose rubric
  writing — that PROFILE is the useful fact (jagged intelligence, measured by you).
- Disagreements between your grade and your expectation are the gold: write down which task
  flipped your prior.
- What would make this harness lie to you? Contaminated tasks (answers memorised), leading
  prompts, unblinded grading, n=1 noise read as signal. You now know all four — which is
  the real graduation of this module.

**Checkpoint — you can now:** design a verifiable task; explain programmatic vs rubric vs
blind; run the harness end to end; and defend, out loud, why "model X felt smarter" is not
an acceptable engineering sentence.

## Sources

- Harness + fixtures: this module, machine-verified offline tonight (dry-run pipeline:
  run → grade → table green; `claude` CLI 2.1.221 present for the live path).
- Method: standard eval practice (task/rubric/blind separation) as taught by the plan's
  Tier 3 eval-literacy item; module 01's eval definition is the seed.
