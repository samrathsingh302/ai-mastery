# GLOSSARY — cumulative, repo-wide (baby rule enforcement)

> Law (MISSION.md): NO term, concept, or notation appears in any TEACH.md before it has been
> explained in plain words + one analogy + one concrete example. First explanation lives in its
> module; the term is then added HERE with a one-line reminder + a link back to the full
> explanation. Later modules link here instead of re-explaining. Alphabetical within sections;
> one section per module in build order.

## Module 01 — the video canon

- **Agent** — an LLM given tools and a loop so it can act, not just answer. → [01 Part C](modules/01-video-canon/TEACH.md)
- **API** — a programme-to-programme doorway: send a request, get an answer back. → [01 Part C](modules/01-video-canon/TEACH.md)
- **Base model** — what pretraining produces: an internet-document simulator that continues text rather than answering. → [01 A1](modules/01-video-canon/TEACH.md)
- **Chain of thought** — the model writing intermediate reasoning tokens to buy itself computation. → [01 A2](modules/01-video-canon/TEACH.md)
- **Context window** — the model's reliable working memory: the current conversation + anything pasted in. → [01 A2](modules/01-video-canon/TEACH.md)
- **Eval** — written-down tests for AI behaviour: fixed tasks + scoring, so changes are measured not vibed. → [01 Part C](modules/01-video-canon/TEACH.md)
- **Fine-tuning** — further training on a small chosen dataset to change behaviour, not knowledge. → [01 A2](modules/01-video-canon/TEACH.md)
- **Gradient descent** — nudging all parameters a tiny step in the direction that reduces wrongness; "stepping downhill in fog". → [01 A1](modules/01-video-canon/TEACH.md)
- **Hallucination** — fluent confident falsehood: confident SFT style over vague recollection; no concept of truth involved. → [01 A2](modules/01-video-canon/TEACH.md)
- **Inference** — using a trained model to generate (what every chat is). → [01 A0](modules/01-video-canon/TEACH.md)
- **Jagged intelligence** — Swiss-cheese capability: brilliant and broken on neighbouring tasks; trust is per-task. → [01 A2](modules/01-video-canon/TEACH.md)
- **Kernighan's Law** — debugging is twice as hard as writing; hence code at your comprehension edge is undebuggable by you. → [01 Part B](modules/01-video-canon/TEACH.md)
- **LLM (large language model)** — a very big model whose one trick is predicting the next token. → [01 A0](modules/01-video-canon/TEACH.md)
- **Loss** — the single number scoring how wrong a training guess was. → [01 A1](modules/01-video-canon/TEACH.md)
- **MCP (Model Context Protocol)** — a standard plug connecting an AI tool to outside systems (docs, errors, infra) so it works from live truth. → [01 Part B](modules/01-video-canon/TEACH.md)
- **Model** — a program whose behaviour was learned from examples rather than written by hand. → [01 A0](modules/01-video-canon/TEACH.md)
- **Observability** — logging what an AI system actually did (prompts, answers, cost, errors) so failures can be inspected. → [01 Part C](modules/01-video-canon/TEACH.md)
- **Parameters / weights** — the millions–billions of learned numbers that ARE the model. → [01 A0](modules/01-video-canon/TEACH.md)
- **Pretraining** — the expensive stage: predict-next-token over internet-scale text until the dials settle. → [01 A1](modules/01-video-canon/TEACH.md)
- **RAG (retrieval-augmented generation)** — fetch relevant documents, paste into context, answer open-book. → [01 Part C](modules/01-video-canon/TEACH.md)
- **Reinforcement learning (RL)** — learning by trying many attempts and keeping what led to verified-good outcomes. → [01 A3](modules/01-video-canon/TEACH.md)
- **Reward model** — a second model trained on human comparisons to predict which output a person would prefer. → [01 A3](modules/01-video-canon/TEACH.md)
- **RLHF** — RL from human feedback: optimise the model to please the reward model — briefly, because it's gameable. → [01 A3](modules/01-video-canon/TEACH.md)
- **SFT (supervised fine-tuning)** — training on labeller-written ideal conversations; turns the simulator into an assistant. → [01 A2](modules/01-video-canon/TEACH.md)
- **Sycophancy** — the agree-with-the-user tendency; mechanical result of optimising for preferred-ness. → [01 A3](modules/01-video-canon/TEACH.md)
- **Token** — the chunk-of-text unit (→ ID number) models read and write; never letters. → [01 A1](modules/01-video-canon/TEACH.md)
- **Tokenisation** — converting text into tokens (byte-pair encoding: common chunks get their own ID). → [01 A1](modules/01-video-canon/TEACH.md)
- **Training** — the slow phase where parameters get tuned on data. → [01 A0](modules/01-video-canon/TEACH.md)
- **Vibe coding** — accepting AI-written code without really reading it; safe in proportion to your ability to verify. → [01 Part B](modules/01-video-canon/TEACH.md)

## Module 02 — the tutor setup

- **Active recall** — answering from memory instead of re-reading; the best-evidenced study technique; what the contract's quizzes/explain-backs force. → [02 Piece 1](modules/02-tutor-setup/TEACH.md)
- **Dojo** — the daily 20-minute planted-bug hunt run with the root-cause method; levels L0–L4. → [02 dojo.md](modules/02-tutor-setup/dojo.md)
- **FSRS** — Anki's built-in modern scheduler; learns your forgetting curve and sets each card's next review. → [02 Piece 2](modules/02-tutor-setup/TEACH.md)
- **Illusion of knowing** — feeling you could do what you only watched being done; the failure the tutor contract exists to block. → [02 Piece 1](modules/02-tutor-setup/TEACH.md)
- **Spaced repetition** — reviewing just before you'd forget, at stretching intervals ("water the plant the day the soil dries"). → [02 Piece 2](modules/02-tutor-setup/TEACH.md)
- **Tutor contract** — the 10-rule paste block that makes Claude a tutor, not a solver. → [02 tutor-contract.md](modules/02-tutor-setup/tutor-contract.md)

## Module 03 — CS50P accelerated

- **Accumulator pattern** — start · visit each · fold in · return; half of beginner code. → [03 rung 2](modules/03-cs50p-accelerated/TEACH.md)
- **Argument / parameter** — the value you pass / the placeholder that receives it. → [03 rung 0](modules/03-cs50p-accelerated/TEACH.md)
- **Boolean** — a value that is only True or False; comparisons produce them. → [03 rung 1](modules/03-cs50p-accelerated/TEACH.md)
- **Class / object** — cookie cutter / cookie: a blueprint bundling data with its functions, and its instances. → [03 rung 8](modules/03-cs50p-accelerated/TEACH.md)
- **Dictionary (dict)** — labelled values looked up by key: `row["name"]`; built with `.get(k, 0) + 1`. → [03 rung 6](modules/03-cs50p-accelerated/TEACH.md)
- **Exception / traceback** — Python's "cannot continue" alarm, and the report you read bottom-up. → [03 rung 3](modules/03-cs50p-accelerated/TEACH.md)
- **f-string** — `f"hello, {name}"`: text with values dropped in. → [03 rung 0](modules/03-cs50p-accelerated/TEACH.md)
- **List** — ordered collection, indexed from 0; loops visit it item by item. → [03 rung 2](modules/03-cs50p-accelerated/TEACH.md)
- **List comprehension** — a loop that builds a list in one line. → [03 rung 9](modules/03-cs50p-accelerated/TEACH.md)
- **Method** — a function living on a value, called with a dot: `name.strip()`. → [03 rung 0](modules/03-cs50p-accelerated/TEACH.md)
- **Module / import** — someone else's tested functions pulled into your program. → [03 rung 4](modules/03-cs50p-accelerated/TEACH.md)
- **Mutation / aliasing** — changing a jar's contents while two labels point at it; the list surprise. → [03 tracer 5](modules/03-cs50p-accelerated/interactive/code-tracer.html)
- **Regex** — a mini-language for text PATTERNS ("police description"), via `re`. → [03 rung 7](modules/03-cs50p-accelerated/TEACH.md)
- **REPL** — run `python` alone: the interactive one-line-at-a-time laboratory. → [03 rung 4](modules/03-cs50p-accelerated/TEACH.md)
- **return vs print** — hand a value back (usable/testable) vs show pixels to a human. → [03 rung 0](modules/03-cs50p-accelerated/TEACH.md)
- **Scope** — the function's private workbench; its names vanish when it returns. → [03 tracer 4](modules/03-cs50p-accelerated/interactive/code-tracer.html)
- **Type** — what kind a value is (str/int/float…); operations mean different things per type. → [03 rung 0](modules/03-cs50p-accelerated/TEACH.md)
- **Unit test / assert** — a small program that checks one behaviour of another, forever. → [03 rung 5](modules/03-cs50p-accelerated/TEACH.md)
- **Variable** — a name stuck on a value; reassignment moves the label, not the jar. → [03 rung 0](modules/03-cs50p-accelerated/TEACH.md)
- **with open(...)** — the safe file idiom: closes the file for you, even on errors. → [03 rung 6](modules/03-cs50p-accelerated/TEACH.md)

## Module 04 — automate the boring stuff

- **Dry-run** — the mode that only PRINTS what a script would do; run it first, always. → [04 safety laws](modules/04-automate-boring-stuff/TEACH.md)
- **Idempotent** — safe to run twice: the second run finds nothing to do ("light switch, not kettle lever"). → [04 safety laws](modules/04-automate-boring-stuff/TEACH.md)
- **JSON** — text format for nested data (dicts/lists/numbers/strings); the lingua franca of APIs and exports. → [04 mission 4](modules/04-automate-boring-stuff/TEACH.md)
- **pathlib / Path** — paths as objects: join with /, `.rglob` walks trees, `.read_text` reads. → [04 mission 1](modules/04-automate-boring-stuff/TEACH.md)
- **Quarantine** — where automation "deletes" to: a dated folder a human empties later; `os.remove` is banned here. → [04 safety laws](modules/04-automate-boring-stuff/TEACH.md)
- **shutil** — the move/copy/zip toolbox (`copy2`, `move`, `make_archive`). → [04 mission 2](modules/04-automate-boring-stuff/TEACH.md)
- **subprocess** — your script running another program and reading its output; args as a LIST, never a glued string. → [04 mission 5](modules/04-automate-boring-stuff/TEACH.md)
- **Task Scheduler** — Windows' cron: a trigger + an action + a working directory; how your Claude auto-update task runs. → [04 mission 5](modules/04-automate-boring-stuff/TEACH.md)

## Module 05 — git properly

- **Branch** — a movable sticky note on one commit; creating one copies nothing. → [05 five sentences](modules/05-git-properly/TEACH.md)
- **Commit** — a full snapshot + parent pointer(s) + message; never a diff. → [05 five sentences](modules/05-git-properly/TEACH.md)
- **Fast-forward** — a merge with nothing to merge: the sticky note just slides forward; no merge commit. → [05 branching](modules/05-git-properly/TEACH.md)
- **fetch vs pull** — update your copy of the remote's graph vs fetch-and-merge into your branch. → [05 drills](modules/05-git-properly/drills.md)
- **HEAD** — where you're standing; committing moves the note you stand on. → [05 five sentences](modules/05-git-properly/TEACH.md)
- **Merge commit** — a snapshot with TWO parents, tying two histories together. → [05 branching](modules/05-git-properly/TEACH.md)
- **Rebase** — replaying commits as new snapshots on another tip: straight line, new IDs, originals abandoned; never on shared commits. → [05 branching](modules/05-git-properly/TEACH.md)
- **Reflog** — the ~90-day journal of everywhere HEAD has been; the "I'm lost" safety net. → [05 undo toolbox](modules/05-git-properly/TEACH.md)
- **Remote / origin** — another copy of the graph (your GitHub) with its own sticky notes. → [05 five sentences](modules/05-git-properly/TEACH.md)
- **Revert** — the shared-safe undo: an anti-commit that cancels changes without rewriting history. → [05 undo toolbox](modules/05-git-properly/TEACH.md)
- **Staging area / index** — the loading dock: what the next snapshot will contain. → [05 three places](modules/05-git-properly/TEACH.md)
