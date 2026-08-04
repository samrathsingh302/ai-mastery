# The fast-track exit interview (cold, 30 minutes, no notes)

**Setup:** timer visible. No tabs, no notes, no AI. Speak answers ALOUD (writing is easier —
that's why we don't). Read one question, then cover the model answer until you've finished
answering. Score 0–2. **9+/12 = proceed to the full tiers.**

Scoring: **2** = you'd satisfy a technical interviewer · **1** = right idea, incomplete or
muddled · **0** = missed the core.

---

## Q1 (projects, 5 min) — "Walk me through a project you've built."

*Pick psoc-portal. Expect the follow-up: "what happens between me clicking submit and the
data being saved?"*

<details><summary>Model answer</summary>

Committee portal for PSOC — Next.js + Supabase, in production, replacing a shared folder and
an Excel tracker. The add-task path: every request first hits `proxy.ts`, the middleware auth
gate; the `/tasks` page is a server component that fetches current data; the form is a client
component that submits to a **server action**, `addTask()`, which **re-checks auth** (the
browser is never trusted) and validates, then inserts via Supabase into `public.tasks` — a
table defined in migration `0001`. Then `revalidateTasks()` invalidates the cached page and
redirects, so the list re-renders with fresh rows. **2** = names the gate, the server-side
re-check, the DB write and the cache invalidation. **1** = "form posts, it saves to Supabase".
</details>

## Q2 (Python, 4 min) — "What's the bug?"

```python
def add_task(task, tasks=[]):
    tasks.append(task)
    return tasks
```

<details><summary>Model answer</summary>

Mutable default argument: `[]` is created **once, when the function is defined**, so every
call that omits `tasks` shares and grows the *same* list — results leak between calls. Fix:
default to `None`, then `if tasks is None: tasks = []` inside. **2** = names the mechanism
(created once at definition) and the sentinel fix. **1** = "the list keeps growing".
</details>

## Q3 (Python, 4 min) — "Read me this traceback and tell me what you'd do."

```
Traceback (most recent call last):
  File "studylog.py", line 42, in week
    total += entry["mins"]
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

<details><summary>Model answer</summary>

Read bottom-up: the error is a type mismatch — `entry["mins"]` is a **string** where an int
was expected, at line 42 in `week()`. Likely cause: the value was written to JSON as a string
(or came from `input()`/argv without conversion). I'd inspect one entry to confirm, then fix
at the **write** side (convert on `add`), not by patching `int()` at every read — plus a
test for the boundary. **2** = bottom-up reading, named cause, fix at the source, regression
test. **1** = "convert it to int".
</details>

## Q4 (LLMs, 5 min) — "How does something like ChatGPT actually work?"

<details><summary>Model answer</summary>

Three stages. **Pretraining**: predict the next token over trillions of tokens of internet
text, nudging billions of parameters downhill on a loss — producing a base model that
*continues* text (a lossy compression of the web). **Supervised fine-tuning**: imitate
labeller-written ideal conversations, which installs assistant behaviour. **RL**: on
verifiable tasks (maths/code) reinforce what reaches correct answers — this is where
reasoning chains come from; on unverifiable ones, RLHF optimises a learned model of human
preference. Inside, it's a transformer: tokens → embeddings + position → repeated
[attention (tokens exchange context via Q/K/V) → MLP (where facts live)] → unembedding →
softmax → sample. **2** = the three stages plus the architecture sketch. **1** = "it predicts
the next word".
</details>

## Q5 (judgement, 6 min) — "It confidently told you something false. Why, and what do you do?"

<details><summary>Model answer</summary>

Mechanism: the weights hold a *vague recollection*, and fine-tuning installed a confident
answering style — so where memory is thin, plausible tokens fill the gap. No intent, no
concept of truth. Responses: put the source **in the context** (open-book beats memory —
that's why RAG works); use tools/search for facts; ask for citations and check them; prefer
verification over confidence — and note the model will fold if I push back, so agreement is
not evidence. Also relevant: temperature changes wandering, not knowledge. **2** = mechanism
+ at least two structural fixes. **1** = "it hallucinates, so double-check it".
</details>

## Q6 (security/judgement, 6 min) — "You give an agent access to your email and your files. What worries you?"

<details><summary>Model answer</summary>

The **lethal trifecta**: private data + untrusted content + the ability to communicate
externally. Email is attacker-writable, so anyone can place instructions in the agent's
context (**indirect prompt injection**, OWASP LLM01) — and because the model can't reliably
distinguish injected instructions from data, prompt hardening won't fix it. The fixes that
survive are architectural: **narrow the capability** (no send/push in a session that reads
untrusted mail), split the legs across sessions, and put **human gates on irreversible or
outward acts**. Filters are speed bumps. **2** = names the trifecta and a structural fix.
**1** = "prompt injection is a risk".
</details>

---

## After the sim

Total ___/12. Log it in `journal.md` with the date. Every 0 or 1 becomes: one Anki card, one
drill topic, and a line in the next week's plan. Re-sit in a fortnight — the *trend* is the
instrument, not any single sitting.
