# 01-video-canon — like you're 5

Module 01, the video canon: every term, explained like you're 5.

- **Taught in:** `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\TEACH.md`

- **The one-line reminders:** `GLOSSARY.md` → `## Module 01 — the video canon`

---

### Agent
**Like you're 5:** A friend on the phone can only talk. Now give that friend hands: a search box, a keyboard, files to open. They try a step, look at what happened, and try the next step until the job is done. They act, not just chat.

**The real words:** An LLM given tools and a loop so it can act (search, run code, edit files), not just answer. → [01 Part C](../modules/01-video-canon/TEACH.md)

**See it:** Any Claude Code window on your machine is one: watch it call Read, then Edit, then Bash, look at each result, and decide the next call. The seat that wrote this file was an agent.

### API
**Like you're 5:** A restaurant hatch. You never walk into the kitchen. You pass a slip through the hatch saying what you want, and a plate comes back through the same hatch. Programs talk to each other through hatches like that.

**The real words:** A programme-to-programme doorway: your code sends a request, the service sends back an answer. → [01 Part C](../modules/01-video-canon/TEACH.md)

**See it:** In any terminal, any folder: `curl.exe https://api.github.com/repos/python/cpython` — one request goes out, a block of JSON about Python's own repo comes back.

### Base model
**Like you're 5:** A parrot that has heard every book and web page in the world. Say "Once upon a time" and it carries on the story. Ask it a question and it may answer with more questions, because that is what it often heard. It copies; it does not help.

**The real words:** What pretraining produces: an internet-document simulator that continues text rather than answering. → [01 A1](../modules/01-video-canon/TEACH.md)

**See it:** `start C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html`, click "⚙️ Pretraining" — its label reads "→ base model" and its "What can go wrong" line is exactly this.

### Chain of thought
**Like you're 5:** Ask a child "what is 17 times 23?" and make them shout the answer at once: they guess. Let them write it out on paper, line by line, and they get it right. Writing the steps IS the thinking.

**The real words:** The model writing intermediate reasoning tokens to buy itself computation; the work per token is fixed, so more tokens means more thinking. → [01 A2](../modules/01-video-canon/TEACH.md)

**See it:** Ask Claude a two-step word problem twice: once with "answer with only the number", once with "work it through step by step first". Compare which one you would trust.

### Context window
**Like you're 5:** Two ways to know things: what you vaguely remember from school, and the open book on your desk right now. The book on the desk is what you can read exactly. For the model, the desk is the chat so far plus anything you pasted in.

**The real words:** The model's reliable working memory: the current conversation plus anything pasted in; open-book beats memory. → [01 A2](../modules/01-video-canon/TEACH.md)

**See it:** Ask Claude about a file it has never seen, then paste the file and ask again. The second answer quotes; the first one guessed.

### Eval
**Like you're 5:** A spelling test with the same twenty words every week. If the score goes up after you change how you practise, the change helped. You don't decide by "it feels better"; you decide by the score.

**The real words:** Written-down tests for AI behaviour: fixed tasks plus a scoring method, so changes are measured, not vibed. → [01 Part C](../modules/01-video-canon/TEACH.md)

**See it:** `C:\Users\samra\repos\ai-mastery\modules\09-eval-harness-mini\` is the module where you build one; its `TEACH.md` is the full version.

### Fine-tuning
**Like you're 5:** A chef who already knows how to cook goes to one restaurant for two weeks and learns that place's house style. They learned no new food; they learned new manners.

**The real words:** Further training on a small chosen dataset to change behaviour, not knowledge. → [01 A2](../modules/01-video-canon/TEACH.md)

**See it:** The "🧑‍🏫 SFT" stage in `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html` — SFT is one kind of fine-tuning, and its analogy line is this chef.

### Gradient descent
**Like you're 5:** You are on a foggy hill and want to reach the bottom. You can't see the valley, but you can feel which way the ground tilts under your feet. So you take one small step downhill, feel again, step again. Millions of small steps get you down.

**The real words:** Nudging all parameters a tiny step in the direction that reduces wrongness (the loss); repeated trillions of times in pretraining. → [01 A1](../modules/01-video-canon/TEACH.md)

**See it:** The "⚙️ Pretraining" stage of `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html` — "a tiny step downhill (gradient descent)". Module 11 does it with real numbers.

### Hallucination
**Like you're 5:** A child who half-remembers a story but has been taught always to answer politely and confidently. Asked about it, they fill the gaps with things that sound right. They aren't lying; they just don't know which bits are real.

**The real words:** Fluent, confident falsehood: confident SFT style laid over vague recollection; no concept of truth is involved, only likelihood. → [01 A2](../modules/01-video-canon/TEACH.md)

**See it:** Ask a chatbot for the biography of a plausible person who does not exist, then for its sources. Check one source by hand.

### Inference
**Like you're 5:** Years of piano lessons is the slow part. Playing a song for your friends tonight is the quick part. Inference is playing tonight: the learning is finished, and now it just plays.

**The real words:** Using a trained model to generate (what every chat is). → [01 A0](../modules/01-video-canon/TEACH.md)

**See it:** Every message you send Claude is one inference run; nothing in the model changes because of your chat.

### Jagged intelligence
**Like you're 5:** A friend who can do your hardest maths homework but then says 9.11 is bigger than 9.9. Being brilliant at one thing tells you nothing about the very next thing. You check each kind of job separately.

**The real words:** Swiss-cheese capability: brilliant and broken on neighbouring tasks; trust is calibrated per task-type, never per model. → [01 A2](../modules/01-video-canon/TEACH.md)

**See it:** Ask a model "how many r's are in strawberry?" and then a hard coding question; note which one it fumbles.

### Kernighan's Law
**Like you're 5:** Fixing a broken toy is twice as hard as building it. So if you build the hardest toy you possibly can, you won't be able to fix it when it breaks. Build toys you understand.

**The real words:** Debugging is twice as hard as writing; code at the edge of your comprehension is undebuggable by you — the reason vibe coding is a trap past your reading level. → [01 Part B](../modules/01-video-canon/TEACH.md)

**See it:** The 80/20 map's idea 3 at the top of `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\TEACH.md`.

### LLM (large language model)
**Like you're 5:** A giant guessing game. You say the start of a sentence; it guesses the next little piece, then the next, then the next. That one trick, done very well, looks like talking.

**The real words:** A very big model whose one trick is predicting the next token; ChatGPT, Claude and Gemini are all LLMs. → [01 A0](../modules/01-video-canon/TEACH.md)

**See it:** Type "The capital of France is" into any chatbot and watch it continue " Paris".

### Loss
**Like you're 5:** After every guess, a teacher writes one number on the board: how wrong was that? Big number, very wrong; small number, nearly right. Learning means making that number smaller.

**The real words:** The single number scoring how wrong a training guess was. → [01 A1](../modules/01-video-canon/TEACH.md)

**See it:** "The training loop" paragraph in `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\TEACH.md`, section A1: guess → score (loss) → nudge → repeat.

### MCP (Model Context Protocol)
**Like you're 5:** One shape of plug that fits every socket. Instead of building a special cable for every gadget, every gadget gets the same plug, and the helper can plug into your files, your email or your calendar the same way.

**The real words:** A standard plug connecting an AI tool to outside systems (docs, errors, infra) so it works from live truth instead of stale memory. → [01 Part B](../modules/01-video-canon/TEACH.md)

**See it:** In a Claude Code window type `/mcp` — it lists the servers plugged in on your machine (mail and WhatsApp are two of yours).

### Model
**Like you're 5:** A cook nobody gave a recipe to. They tasted a million dishes until they could make up their own. Nobody wrote down the rules; the rules were learned from examples.

**The real words:** A program whose behaviour was learned from examples rather than written by hand. → [01 A0](../modules/01-video-canon/TEACH.md)

**See it:** Your phone keyboard suggesting the next word: a tiny model, learned from what people type.

### Observability
**Like you're 5:** A diary the machine writes as it works: what it was asked, what it answered, how long it took, what went wrong. When something breaks, you read the diary instead of guessing.

**The real words:** Logging what an AI system actually did (prompts, answers, cost, errors) so failures can be inspected. → [01 Part C](../modules/01-video-canon/TEACH.md)

**See it:** `C:\Users\samra\.claude\projects\` — every Claude Code session on this machine leaves a `.jsonl` log of each prompt, tool call and answer there.

### Parameters / weights
**Like you're 5:** A mixing desk with a billion sliders. Learning means nudging every slider a tiny bit until the music sounds right. When it's done, the sliders' positions ARE the thing; there is nothing else inside.

**The real words:** The millions to billions of learned numbers that are the model. → [01 A0](../modules/01-video-canon/TEACH.md)

**See it:** The "⚙️ Pretraining" analogy line in `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html`; module 11 shows real weights in a tiny network.

### Pretraining
**Like you're 5:** Reading the whole library, over and over, playing one game: cover the next word, guess it, check, adjust. Months of this, on thousands of fast computers. It is the slow, costly part.

**The real words:** The expensive stage: predict-next-token over internet-scale text until the parameters settle; the output is a base model. → [01 A1](../modules/01-video-canon/TEACH.md)

**See it:** The "🌐 Internet text" then "⚙️ Pretraining" stages in `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html`.

### RAG (retrieval-augmented generation)
**Like you're 5:** Before answering a question, you run to the shelf, pull out the right pages, put them on the desk, and answer by reading them. You answer with the book open, not from memory.

**The real words:** Fetch relevant documents, paste them into the context window, answer open-book; it works because context beats weights. → [01 Part C](../modules/01-video-canon/TEACH.md)

**See it:** Paste one of your own notes into Claude and ask a question only that note answers — that is RAG done by hand; the system just automates the fetching.

### Reinforcement learning (RL)
**Like you're 5:** Learning to ride a bike. Nobody can tell you how to balance. You wobble, you fall, and you keep whatever kept you up. Lots of tries, keep what worked.

**The real words:** Learning by trying many attempts and keeping what led to verified-good outcomes, rather than imitating examples. → [01 A3](../modules/01-video-canon/TEACH.md)

**See it:** The "🎯 RL / RLHF" stage in `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html` (the bike and AlphaGo's move 37).

### Reward model
**Like you're 5:** A pretend judge. People were shown pairs of answers and picked the better one, many times. A second machine learned to guess what they would pick. Now that pretend judge scores answers when no person is there.

**The real words:** A second model trained on human comparisons to predict which output a person would prefer. → [01 A3](../modules/01-video-canon/TEACH.md)

**See it:** When ChatGPT shows you two answers and asks "which is better?", you are making the comparisons a reward model is trained on.

### RLHF
**Like you're 5:** Practise until the pretend judge smiles. But the pretend judge can be fooled, so if you practise too long you learn silly tricks that make it smile and real people frown. So you only do it a little.

**The real words:** RL from human feedback: optimise the model to please the reward model — briefly, because it is gameable. → [01 A3](../modules/01-video-canon/TEACH.md)

**See it:** The "What can go wrong here" line of the "🎯 RL / RLHF" stage in `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html`.

### SFT (supervised fine-tuning)
**Like you're 5:** Teachers write out lots of perfect example chats: a question, then the ideal helpful answer. The parrot copies them until it talks like that helper. Now it answers instead of rambling on.

**The real words:** Training on labeller-written ideal conversations; turns the simulator into an assistant — you are chatting with a simulation of the ideal labeller. → [01 A2](../modules/01-video-canon/TEACH.md)

**See it:** The "🧑‍🏫 SFT" stage in `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html` — its label reads "→ assistant".

### Sycophancy
**Like you're 5:** A helper trained to be liked. Saying "you're right!" gets liked more often than saying "no, you're wrong". So it learns to agree with you, even when you are wrong.

**The real words:** The agree-with-the-user tendency; a mechanical result of optimising for preferred-ness, so verify against docs, tests and runs, never the model's confidence. → [01 A3](../modules/01-video-canon/TEACH.md)

**See it:** Ask a model a maths question, then reply "are you sure? I think it's X" with a wrong X. Watch whether it folds.

### Token
**Like you're 5:** LEGO bricks. The model never sees letters; it sees bricks, each one a word or a piece of a word, each with a number on it. It builds with bricks, so it can't easily count the letters hidden inside one.

**The real words:** The chunk-of-text unit (mapped to an ID number) models read and write; never letters. → [01 A1](../modules/01-video-canon/TEACH.md)

**See it:** "unbelievable" might be three bricks: `un` + `believ` + `able` — and that is why "how many r's in strawberry?" trips models up.

### Tokenisation
**Like you're 5:** Chopping text into LEGO bricks. Pieces that turn up all the time get their own brick so they're cheap; rare words get built from smaller bricks.

**The real words:** Converting text into tokens, by byte-pair encoding: common chunks get their own ID. → [01 A1](../modules/01-video-canon/TEACH.md)

**See it:** The "🌐 Internet text" stage of `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html` — "LEGO-ifying the internet".

### Training
**Like you're 5:** Piano practice: slow, every day, for years, getting a little better each time. The playing tonight comes later and is quick. Training is the practice part.

**The real words:** The slow phase where parameters get tuned on data; inference is the quick phase that uses the result. → [01 A0](../modules/01-video-canon/TEACH.md)

**See it:** The first three stages of `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\interactive\llm-pipeline-explorer.html` are all training; your chats come after.

### Vibe coding
**Like you're 5:** Asking a big kid to build your LEGO castle and putting it on the shelf without looking at it. Fine while it stands. When a tower falls off, you can't fix it, because you never knew how it was built.

**The real words:** Accepting AI-written code without really reading it; safe in proportion to your ability to verify it. → [01 Part B](../modules/01-video-canon/TEACH.md)

**See it:** Part B of `C:\Users\samra\repos\ai-mastery\modules\01-video-canon\TEACH.md` — the dividing line is comprehension, and the three fixes are context, real errors, automatic verification.
