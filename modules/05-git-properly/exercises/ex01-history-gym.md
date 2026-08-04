# Exercise 01 — The history gym (build this exact graph by hand)

**Goal:** produce a practice repo whose HISTORY has a specific shape — divergence, a real
merge commit, a tag, a revert, and a reflog you can read. `check.py` grades the graph, not
your typing. ~40 min. No AI; TEACH.md and `git status` are your only helps.

Work in `exercises\playground\` (create it; it's gitignored by the parent repo — your mess
is private):

1. `git init` a repo there. Make `notes.md` with one line; add + commit ("start").
2. Two more commits on main, each changing `notes.md` ("second", "third").
3. Create branch `feature`, switch to it, add a NEW file `idea.md`, commit ("idea drafted").
4. Switch back to main; change `notes.md` again; commit ("main moves on"). *(Main and
   feature have now DIVERGED — draw it before continuing: two arrows out of "third".)*
5. Merge `feature` into main. Git opens an editor for the merge message — accept it. You
   now have a merge commit with TWO parents. Prove it: `git log --oneline --graph`.
6. Tag this moment: `git tag v1`.
7. Make a "bad" commit: add `oops.md`, commit ("mistake"). Now UNDO it the shared-safe way:
   `git revert HEAD` (accept the message). `oops.md` is gone, history shows both commits.
8. Read your journey: `git reflog | head` — every hop of HEAD, newest first. Find the merge
   and the revert in it.
9. Run the grader from the exercises folder: `python check.py`.

**Stretch (optional):** `git log --oneline --graph --all` and sketch the whole graph on
paper, sticky notes included. Then delete branch `feature` (`git branch -d feature`) and
re-run the log — what changed, and why is nothing lost?
