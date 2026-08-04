# Module 01 — The Video Canon, taught directly

> **What this is:** the complete companion notes for the fast track's item 1. These notes ARE the
> content — read them for the ideas, then use the videos as optional review (the plan's rule:
> watching becomes revision, not the source). **Time: ~2–3h reading + exercises; the videos
> themselves total ~4h14m at 1× if you choose to watch.**
> **You can start this with zero programming knowledge.** Every technical term is explained
> before it's used (the baby rule), and each explained term is also in the repo-root
> [GLOSSARY.md](../../GLOSSARY.md).

## The canon, verified (04/08/2026)

| # | Video | Channel | Runtime | Published | Link |
|---|-------|---------|---------|-----------|------|
| 1 | The "vibe coding" mind virus explained… | Fireship | 4:46 | 26/03/2025 | youtube.com/watch?v=Tw18-4U7mts |
| 2 | How to make vibe coding not suck… | Fireship | ~5:47 | 14/10/2025 | youtube.com/watch?v=PLKrSVuT-Dg |
| 3 | Deep Dive into LLMs like ChatGPT | Andrej Karpathy | 3:31:00 | 05/02/2025 | youtube.com/watch?v=7xTGNNLPyMI |
| 4 | How I'd Learn AI Engineering in 2026 (Complete Roadmap) | Dave Ebbelaar | 19:29 † | 29/10/2025 | youtube.com/watch?v=O2UmHpNlwUw |
| 5 | Learning to code has changed | Tech With Tim | 13:19 † | 02/02/2026 | youtube.com/watch?v=eZJtpSVYDIY |

† runtime from corroborated search snippets, not primary YouTube metadata (medium confidence).
Two plan corrections found while verifying (details in `reports/red-team-findings.md`): the plan
lists video 2 as "16m" (it's ~6m) and video 4 as "~1h" (it's ~19m); the plan's Tech With Tim
title ("How I'd learn to code in 2026") doesn't exist on his channel — video 5 above is the real
nearest match, published 02/02/2026, and it says exactly what the plan wanted that slot to say.
Net effect: the canon is ~4h14m, close to the plan's "~4h" — but ~83% of it is one video
(Karpathy), which is why Part A below is most of this module.

## The 80/20 map — five ideas the whole canon converges on

Read this first. Everything else in the module is depth behind these five sentences.

1. **An LLM is a next-word prediction machine grown from internet text** — not a database, not a
   mind. Almost everything weird about it (confident nonsense, failing at counting letters,
   needing to "think step by step") follows mechanically from how it was made. *(Karpathy)*
2. **The job market is splitting around it.** Producing first-draft code is commoditising;
   *verifying* code — reading it critically, testing it, judging it — is appreciating. The more
   code AI writes, the scarcer verification skill gets. *(Fireship, Tim, the plan's Part 1)*
3. **Vibe coding is real leverage AND a real trap, and the dividing line is you.** Letting AI
   write code is safe exactly in proportion to your ability to read and debug what it wrote.
   Kernighan's Law is why: debugging is twice as hard as writing, so code at the edge of your
   comprehension is undebuggable by you. *(Fireship ×2)*
4. **"AI engineer" is a software engineering role, not a research role.** The stack is: Python
   foundations → system design → production backends → retrieval → monitoring/evals →
   deployment. Your plan's tiers map onto it almost one-to-one. *(Ebbelaar)*
5. **Learning to code has genuinely changed:** AI is a tutor-multiplier for people with
   fundamentals and an illusion-of-knowing machine for people without them. Same tool, opposite
   outcomes — the difference is the contract you use it under. *(Tim, the plan's Part 2)*

**Checkpoint — you can now:** say, in one sentence each, why this plan front-loads verification
skill, why the 20% AI-free rule exists, and why module 02 installs a tutor *contract* rather
than just "use Claude".

---

# Part A — Karpathy's "Deep Dive into LLMs like ChatGPT" (the spine)

This 3h31m video is the best single general-audience explanation of what things like ChatGPT and
Claude actually are. These notes cover all of it. Sections follow his three stages: pretraining
→ supervised fine-tuning → reinforcement learning, then the practical consequences.

## A0. First words: what a "model" is

- **Model** *(plain words)*: a computer program whose behaviour was **learned from examples**
  rather than written line-by-line by a programmer. *(Analogy: a recipe nobody wrote — a cook
  who tasted a million dishes until they could improvise their own.)* *(Example: your phone
  keyboard suggesting your next word — a tiny model, learned from what people type.)*
- **Large Language Model (LLM)**: a very big model whose one trick is: given some text, predict
  what text comes next. ChatGPT, Claude, Gemini — all LLMs. *(Example: given "The capital of
  France is", it continues " Paris".)*
- **Parameters (weights)**: the millions-to-billions of numbers inside the model that got tuned
  during learning. They ARE the model. *(Analogy: a mixing desk with billions of sliders; "
  training" nudges sliders until the output sounds right.)*
- **Training vs inference**: training = the slow, expensive phase where the sliders get tuned on
  data. Inference = using the finished model to generate text (what happens every time you chat).
  *(Analogy: years of piano practice vs playing a song tonight.)*

## A1. Stage 1 — Pretraining: growing a text-prediction engine

**The data.** You start by downloading a huge filtered slice of the internet. Karpathy shows
FineWeb — a public dataset of roughly 44 terabytes of cleaned web text. Filtering removes spam,
adult content, duplicates, and personal data — what's left is trillions of words of books,
articles, forums, code.

- **Token** *(plain words)*: the chunk-of-text unit models actually read and write — usually a
  word, part of a word, or punctuation, each mapped to an ID number. Models never see letters;
  they see token IDs. *(Analogy: LEGO bricks — you build with bricks, not with the plastic
  molecules inside them.)* *(Example: "unbelievable" might be three tokens: `un` + `believ` +
  `able`.)*
- **Tokenisation**: converting text into tokens. Done with an algorithm (byte-pair encoding)
  that gives common chunks their own ID so frequent text is cheap to represent.
- **Why you should care already:** because models see tokens, not letters, they are famously
  shaky at "how many r's in strawberry" — the letters are hidden inside the bricks. This is
  idea #1 (weirdness follows from construction), first sighting.

**The training loop.** Take a random window of internet text. Show the model all tokens up to a
point; ask it to predict the next one. It outputs a probability for every possible token. Score
how wrong it was (**loss** — a single number meaning "how bad was that guess"). Nudge all the
parameters a tiny step in the direction that would have made the right answer more likely
(**gradient descent** — *analogy: standing on a foggy hillside and always stepping downhill;
the valley floor is "good predictions"*). Repeat trillions of times on thousands of specialised
processors (**GPUs**) for months. That's pretraining, and it's the expensive part — the famous
training runs cost millions of pounds.

**What you end up with: a base model.**
- **Base model** *(plain words)*: an internet-document *simulator*. Give it the start of
  anything and it continues in the statistically likely way. It does NOT answer questions —
  asked "What is the capital of France?", a base model may continue with *more exam questions*,
  because that's what often follows one question on the internet.
- **The compression intuition** (Karpathy's key frame): the parameters are like a lossy zip file
  of the internet — a few gigabytes-to-terabytes of numbers holding a *vague recollection* of
  trillions of words. It can quote famous passages nearly exactly (seen thousands of times) but
  only has a fuzzy gist of a page seen once. **Remember "vague recollection" — it's the seed of
  hallucination, coming in A2.**

**Checkpoint — you can now:** explain to a friend what "training" physically is (guess next
token → score → nudge sliders → repeat), what a token is and one consequence of tokens, and why
a base model is a simulator rather than an assistant.

## A2. Stage 2 — Post-training: turning the simulator into an assistant

- **Fine-tuning** *(plain words)*: continuing to train an already-trained model on a smaller,
  carefully chosen dataset, to change its *behaviour* rather than its knowledge. *(Analogy: a
  classically trained chef doing a two-week bootcamp in one restaurant's house style.)*
- **Supervised fine-tuning (SFT)**: the specific fine-tune where human labellers write ideal
  conversations — "here's a user question; here's the perfect helpful answer, per our
  guidelines" — and the model is trained to imitate them. Conversations are turned into token
  streams with special separator tokens marking who's speaking.

**The reframe that should permanently change how you read AI output:** when you talk to ChatGPT
or Claude, you are talking to a *statistical simulation of a helpful human labeller following a
style guide*. Not a database. Not an oracle. A trained imitation of "what would the ideal
assistant write here?".

**Hallucination — why it happens and what patches it.**
- **Hallucination** *(plain words)*: the model stating false things fluently and confidently.
  *(Example: ask about a plausible-sounding person who doesn't exist — older models would
  invent a biography.)* Why: the base model holds *vague recollections*, and SFT taught it the
  *style* of confident helpful answers. Style says "answer confidently"; memory has nothing
  solid; the prediction machinery fills the gap with plausible tokens. It is not lying — it has
  no concept of truth, only likelihood.
- **Patch 1 — train honesty:** probe what the model actually knows; where it's blank, add
  training examples whose ideal answer is "I don't know / I'm not sure". Models can then say so.
- **Patch 2 — tools:** let the model emit a special token sequence meaning "do a web search",
  paste the results into the conversation, and answer from *that*.
- **Context window** *(plain words)*: the model's working memory — the text of the current
  conversation plus anything pasted in, which it can attend to directly and reliably.
  *(Analogy: knowledge in the weights = things you vaguely remember from school; knowledge in
  the context window = the open book on your desk.)* **Practical law: if you need accuracy,
  put the source in the context. Open-book beats memory.**
- **"Knowledge of self":** the model has no persistent identity or memory of past chats. Asked
  "who are you / what model are you", it answers from training or from instructions injected
  into the context — it is not introspecting. Don't interrogate it about itself and treat the
  answer as ground truth.

**"Models need tokens to think."** The amount of computation the model can do *per token it
emits* is fixed and fairly shallow. So a hard problem answered in one token ("42") gets almost
no compute, while the same problem worked through step by step spreads the thinking across
hundreds of tokens — each token a small step, the chain adding up to real computation.
- **Chain of thought** *(plain words)*: the model writing out intermediate reasoning before the
  final answer — not a gimmick; it is literally how the model buys itself compute. *(Example:
  Karpathy shows a maths word problem: forced to answer immediately, the model errs; allowed to
  reason first, it nails it.)* **Practical law: never force an instant verdict on anything
  hard; let it reason first. And distrust its arithmetic — that's what calculators/tools are
  for.**
- **Jagged intelligence**: the capability surface is Swiss cheese — PhD-level on some tasks,
  then "9.11 > 9.9" or miscounting letters. One impressive win tells you nothing about the
  neighbouring task. **Practical law: calibrate trust per task-type, never per model.**

**Checkpoint — you can now:** explain why hallucination happens using "vague recollection +
confident style", say what the context window is and why pasting sources works, and explain why
"think step by step" isn't superstition.

## A3. Stage 3 — Reinforcement learning: beyond imitation

- **Reinforcement learning (RL)** *(plain words)*: learning by trying many attempts and keeping
  whatever led to a good outcome — rather than imitating examples. *(Analogy: a child learning
  to ride a bike: nobody can *tell* you the balance; you wobble, fall, and keep what worked.)*
- In domains where answers can be **checked automatically** (maths with known answers, code with
  tests), you can run RL at scale: sample thousands of solution attempts, keep and reinforce the
  ones that reach the verified-correct answer. The model then *discovers its own* chains of
  thought — Karpathy shows DeepSeek-R1's reasoning growing longer and more careful purely
  because it worked, including "aha"-style self-corrections nobody wrote for it.
- **The AlphaGo analogy:** imitation of experts caps you at expert level; RL against the real
  goal can exceed it — AlphaGo's famous "move 37" was a move no strong human would play, found
  by optimising for winning rather than imitating. The hope/hype around "reasoning models" is
  exactly this dynamic applied to thinking-in-text.
- **RLHF — RL from human feedback** — is the version for *uncheckable* domains (jokes, prose,
  helpfulness): humans *compare* pairs of model outputs (can't score them objectively, but can
  say which is better); a **reward model** (*plain words: a second model trained to predict
  which output a human would prefer*) is built from those comparisons; the main model is then
  optimised to please the reward model.
- **Karpathy's caveat you must keep:** the reward model is a *simulation* of human preference,
  and simulations can be gamed — push optimisation too far and the model finds adversarial
  nonsense the reward model loves but humans hate. So RLHF is run briefly and carefully. It's a
  finishing pass, not an engine of open-ended self-improvement. **Practical law: "the model was
  trained to be preferred" ≠ "the model is right" — this is the mechanical root of sycophancy,
  and why your plan's anti-sycophancy rule says verify against docs/tests/runs, never against
  the model's confidence.**

**Checkpoint — you can now:** explain RL vs imitation with the bike/AlphaGo analogies, say in
which domains RL-with-verification works and why, and derive *from the mechanism* why models
tend to agree with confident users.

## A4. Where that leaves you (Karpathy's closing frames + practice)

- Thinking/reasoning models (o1-style, R1-style) = the RL stage turned up: slower, token-hungry,
  better at hard verifiable problems. Non-thinking models = mostly stages 1–2: faster,
  shallower. Pick per task.
- LLMs are best held as **"people spirits"** — statistical simulations of the humans in the
  data and the labellers in the fine-tune: astonishingly capable, shallowly grounded, no
  persistent self, jagged. Use them as tools; **check their work** — which is precisely the
  skill this whole plan exists to build in you.

---

# Part B — The Fireship pair: vibe coding (10 minutes that name the trap)

**B1. "The 'vibe coding' mind virus explained…" (4:46).** *Vibe coding* (*plain words*: telling
an AI what you want and accepting the code it writes without really reading it — the term is
Karpathy's own Feb 2025 coinage, "give in to the vibes, forget the code exists") went from joke
to hiring-page buzzword in weeks. The video's sober core under the memes: it genuinely works for
prototypes, small scopes, and stacks the *human* already knows — and it collapses exactly where
comprehension runs out: unreviewed code accumulates, bugs compound, and nobody on the team can
debug what nobody wrote. The success stories (a vibe-coded flight-sim MMO) are people who could
have written it themselves, faster.

**B2. "How to make vibe coding not suck…" (~5:47).** The fix is not "prompt better" — it's
**context + verification wiring**. The video is organised around **MCP servers** (*plain words:
Model Context Protocol — a standard plug letting an AI tool connect to outside systems: your
docs, your error tracker, your infra — so the model works from live truth instead of stale
memory*), in seven categories: current framework docs into context · design-to-code fidelity
(Figma) · API executors (Stripe, AWS) · error catchers (Sentry) · QA/testing · infra scaling ·
custom integrations. Generalise past the tool list and it's three principles: **(1) feed the
model current, true context; (2) let it see real errors; (3) wire automatic verification around
it.**

**The bridge to your own house:** those three principles are literally your Claude estate —
skills feeding doctrine into context, verifier agents, hooks, MANUAL-TASKS gates. You already
run industrial-grade "vibe coding that doesn't suck" as an *operator*. The plan's job is to make
the *engineer* underneath match — so the leverage stays safe as scope grows (idea #3).

**Checkpoint — you can now:** define vibe coding, state when it's rational and when it's a trap
in one sentence (comprehension is the dividing line), and name the three generalised principles
behind "make it not suck".

---

# Part C — Ebbelaar: the AI-engineer roadmap (19:29)

Dave Ebbelaar's roadmap (video + his written version in the ai-cookbook repo) defines the *job*
this plan aims you at. Six stages — with plain-word first-contact definitions for the new terms
(each gets full treatment in its own later module; these are previews):

1. **AI foundations** — Python, a working dev environment, Git, and calling models via an
   **API** (*plain words: a programme-to-programme doorway — your code sends a request, the
   service sends back an answer; example: your script sends a prompt to Claude's API and gets
   text back*). ≈ your fast track (steps 2–5).
2. **AI system design** — knowing the standard shapes (chat, pipeline, retrieval, agent) and
   when NOT to use an **agent** (*plain words: an LLM given tools and a loop so it can act —
   search, run code, edit files — not just answer; example: the Claude session that built this
   module*). ≈ Tier 4.
3. **Production-ready backends** — FastAPI, Pydantic, Celery, Docker, PostgreSQL: the plumbing
   that turns a script into a service. ≈ Tier W's production layer + Tier SE.
4. **RAG — retrieval-augmented generation** (*plain words: before answering, the system fetches
   relevant documents and pastes them into the context window, so the model answers open-book;
   example: a chatbot over YOUR notes that quotes them instead of guessing*). Chunking,
   embeddings, vector databases, re-ranking. ≈ Tier 4's RAG-with-evals. — And note you already
   understand *why* RAG works: A2's law, "context beats weights".
5. **Monitoring & evaluation** — **evals** (*plain words: written-down tests for AI behaviour —
   fixed tasks + a scoring method, so "did the change help?" gets a measured answer, not a
   vibe*) plus **observability** (*plain words: logging what the system actually did — every
   prompt, answer, cost, error — so you can inspect failures; example tool: Langfuse*). ≈ your
   step 9 and Tier 3's eval literacy.
6. **Deployment** — cloud hosting, HTTPS, secrets management, CI/CD. ≈ Tier SE's cloud literacy.

**The takeaway sentence:** *AI engineer = software engineer who can wire LLMs into reliable
systems* — stages 3 and 6 are ordinary software engineering, which is why your plan spends most
of its hours on fundamentals rather than model theory.

**Checkpoint — you can now:** name the six stages, give a one-line plain-words definition of
API, RAG, agent, eval, and observability, and say which tier of your plan covers each stage.

---

# Part D — Tech With Tim: "Learning to code has changed" (13:19)

*(The plan's listed title doesn't exist; this is the real video in that slot — published
02/02/2026, it argues exactly the thesis the plan wanted.)* The old way: docs, books, Stack
Overflow, long unaided struggle — slow but it *built* debugging muscle. The new pitfall:
AI-first learners produce working projects while learning almost nothing — the illusion of
competence, exposed the moment the AI is taken away (an interview, an outage, a novel bug). The
AI advantage, used right: an always-on explainer that can unblock you at your exact level. His
2026 method and the canon's closing consensus: **fundamentals first · AI as tutor, not
autocomplete · build real things · keep deliberate no-AI reps.** Which is, one-to-one, your
plan's Tutor Contract, 20% AI-free quota, project-per-module structure, and weekly outage test —
module 02 installs them.

**Checkpoint — you can now:** explain the illusion-of-knowing failure mode and name the four
habits that prevent it — and you know why module 02 (the tutor setup) exists before any Python
is learned.

---

## Sources (all verified 04/08/2026)

- Fireship, "The 'vibe coding' mind virus explained…", 26/03/2025 — youtube.com/watch?v=Tw18-4U7mts (runtime via archive.org metadata)
- Fireship, "How to make vibe coding not suck…", 14/10/2025 — youtube.com/watch?v=PLKrSVuT-Dg (runtime via archive.org metadata)
- Andrej Karpathy, "Deep Dive into LLMs like ChatGPT", 05/02/2025 — youtube.com/watch?v=7xTGNNLPyMI (runtime via Karpathy's announcement: x.com/karpathy/status/1887211193099825254)
- Dave Ebbelaar, "How I'd Learn AI Engineering in 2026 (Complete Roadmap)", 29/10/2025 — youtube.com/watch?v=O2UmHpNlwUw · written roadmap: github.com/daveebbelaar/ai-cookbook/blob/main/roadmaps/ai-engineer-2026.md (runtime medium-confidence: corroborated snippets)
- Tech With Tim, "Learning to code has changed", 02/02/2026 — youtube.com/watch?v=eZJtpSVYDIY (runtime medium-confidence: corroborated snippets)

*Companion note content for Part A is distilled from the Karpathy video's published chapter
structure + its widely-documented content; Parts B–D from the verified outlines above. Where a
runtime or fact was only medium-confidence, it is flagged inline.*
