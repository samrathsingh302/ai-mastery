# Module 05 — Git, properly (it stops being magic today)

> **What this is:** the mental model that makes every git command predictable, the undo
> toolbox, drills on learngitbranching.js.org (free, verified live), and — the part no course
> can give you — YOUR OWN estate's git doctrine, narrated until it's obvious. **~8h.**
> **You already USE git daily** (module 03's survival three-liner, every session-close). This
> module upgrades use → understanding: after it, you can predict what a command will do to the
> graph before running it.

## The five sentences that are the whole of git

1. A **commit** is a snapshot of ALL your files, plus a pointer to its parent commit(s), plus
   a message — never a diff, always a full photo (stored efficiently behind the scenes).
2. History is therefore a **graph** of snapshots (a DAG — *plain words: boxes with arrows
   pointing at their parents, no loops; analogy: a family tree of photos*).
3. A **branch** is a movable sticky note stuck on ONE commit — nothing more; creating a
   branch creates a sticky note, not a copy of anything.
4. **HEAD** is "where you're standing": usually on a branch's sticky note; committing moves
   that sticky note forward to the new snapshot.
5. A **remote** (like `origin` = your GitHub copy) is just ANOTHER copy of the graph, with
   its own sticky notes; push/pull/fetch reconcile the two graphs.

Every git operation is: *make snapshots, move sticky notes, or reconcile graphs.* When
confused, ask "where are the sticky notes right now?" — the visualiser and learngitbranching
both exist to drill exactly this question.

## The three places your changes live

```
working tree  --git add-->  index / staging area  --git commit-->  the graph (history)
(your files)                (the loading dock)                     (permanent snapshots)
```

- **Working tree**: the actual files you edit. **Index/staging** *(plain words: the loading
  dock — you place exactly what the next snapshot should contain; analogy: laying out
  tomorrow's outfit before wearing it)*. `git add -A` loads everything changed; `git add
  file` loads one thing. **`git status`** tells you what's where — the single most-typed
  command for a reason.
- `git diff` = working tree vs index (what's NOT yet staged). `git diff --staged` = index vs
  last commit (what the next commit WILL contain). Read `--staged` before every commit and
  you'll never commit a surprise.

## Branching, merging, rebasing — on the graph

- `git branch feature` = new sticky note where you stand. `git switch feature` = stand on it.
  (`switch` is the modern verb; you'll see `checkout` doing three jobs in older docs.)
- **Merge** (`git switch main; git merge feature`): if main moved since the fork, git makes a
  **merge commit** — a snapshot with TWO parents that ties the histories together. If main
  never moved, git just slides the sticky note forward (**fast-forward** — no new commit).
- **Rebase** (`git rebase main`, standing on feature): *replay* your branch's commits one by
  one on top of main — the graph becomes a straight line, but the replayed commits are NEW
  snapshots (new IDs); the originals are abandoned (reflog still knows them).
- **House judgement call:** merge preserves what really happened (two lines existed); rebase
  makes tidy lines but REWRITES history — so the iron rule: **never rebase commits that
  others already have** (a shared graph rewritten under someone's feet = the mess pull
  --rebase exists to paper over).
- **Live case study from YOUR estate (last night!):** atlas-pipeline's bridge worker runs
  `git pull --rebase` on the whole repo every ~5 minutes — and it silently FLATTENED a
  deliberate `--no-ff` merge commit into a straight line while a session was mid-merge
  (ledger item 108, 04/08/2026). Content survived; the merge commit didn't. That is rebase
  doing exactly what rebase does, at a moment nobody wanted it. When you read item 108's
  decision options, you now know precisely what each one trades away.

## The undo toolbox (pin this)

| Situation | Command | Safe when |
|-----------|---------|-----------|
| Staged the wrong file | `git restore --staged <file>` | always (nothing rewritten) |
| Ruined an uncommitted edit | `git restore <file>` | destroys ONLY that uncommitted change |
| Wrong last commit (not pushed) | `git commit --amend` | local only — house style prefers a new commit anyway |
| Committed on the wrong branch | `git branch right; git reset --hard HEAD~1; git switch right` | local only |
| Need a pushed commit undone | `git revert <hash>` | ALWAYS safe — adds an anti-commit, rewrites nothing |
| "Everything's broken, I'm lost" | `git reflog` → `git reset --hard <good-hash>` | reflog = the journal of where HEAD has BEEN; almost nothing is truly lost for ~90 days |
| Half-done work, need a clean tree | `git stash` / `git stash pop` | remember to pop |

The deep rule under the table: **reset/rebase/amend rewrite history — fine while private,
forbidden once shared; revert adds history — always fine.** (Your no-data-loss law, in git.)

## Your estate's git doctrine, narrated (read with fresh eyes)

- **Every session-close commits and pushes** → because GitHub is the code carrier between
  Daddykins and Sonnykins (two-laptop law). A close that doesn't push strands work on one
  machine. You watched this module's factory do it every iteration tonight.
- **`repos\*` get PRIVATE GitHub remotes; `OneDrive\dev`, `brain`, `~/.claude` must NEVER
  get remotes** — those three hold doctrine/life/keys-adjacent material; pre-push guards
  enforce the law mechanically, and their working copies travel via OneDrive instead.
- **dev and brain keep their `.git` databases OUTSIDE OneDrive** (`C:\Users\samra\.gitdirs\`)
  — OneDrive syncing thousands of tiny hash-named files inside `.git` is slow and corruption-
  prone, so the estate splits: files sync via OneDrive, history lives locally. (`git init
  --separate-git-dir` — the repo's `.git` is a FILE pointing elsewhere. Look: type
  `cat C:\Users\samra\OneDrive\dev\.git`.)
- **The handoff pattern**: a dated file + a commit at every close = the repo's state is
  always reconstructable from `git log` + newest handoff — which is why "resume from digest,
  never rescan" works at all.
- **Sessions use `git -C <path>`** (run git as if standing elsewhere) and commit with
  trailer lines (`Co-Authored-By`, `Claude-Session`) — provenance stamped into history.

*(Project 05 has you narrate psoc-portal's workflow the same way, unaided.)*

## The drill map (~4h of the budget)

1. **learngitbranching.js.org** (free, browser): Main → "Introduction Sequence" (all) +
   "Ramping Up" (all); then Remote → "Push & Pull" levels 1–4. You'll recognise every
   picture — it's the five sentences, animated.
2. **Pro Git** (free at git-scm.com/book): chapters 1–3 as bedtime depth — skim what the
   drills already taught, slow down on 2.4 (undoing) and 3.2 (merge mechanics).
3. **My gym**: `exercises/ex01-history-gym.md` — build a specific history by hand;
   `check.py` inspects your playground repo and grades the graph you produced.

**Checkpoint — you can now:** predict a command's effect on the graph before running it;
undo the six common accidents without searching; explain WHY dev has no remote and WHY the
bridge worker ate a merge commit; and read `git log --oneline --graph --all` like a map.

## Sources (verified 04/08/2026)

- learngitbranching.js.org — live, free (github.com/pcottle/learnGitBranching).
- Pro Git, Chacon & Straub — free under open licence at git-scm.com/book.
- Estate doctrine: CLAUDE.md layout/two-laptop sections + ledger item 108 (04/08/2026) for
  the rebase case study; `.gitdirs` layout verified in the estate docs.
- Git behaviour: exercised live by `exercises/check.py` on your git 2.54.0.
