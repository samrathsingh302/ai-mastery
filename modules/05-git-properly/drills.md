# Drills — module 05

## Anki-importable block (tab-separated: Front ⇥ Back)

A commit is…	A snapshot of ALL files + parent pointer(s) + message — a full photo, never a diff.
A branch is…	A movable sticky note on ONE commit — creating one copies nothing.
HEAD is…	Where you're standing — usually on a branch's sticky note; committing moves that note forward.
The staging area / index is…	The loading dock: you place exactly what the next snapshot will contain (git add).
git diff vs git diff --staged?	Working tree vs index · index vs last commit (read --staged before every commit).
What makes a merge commit special?	TWO parents — it ties two histories together.
When does merge fast-forward instead?	When the target branch never diverged — git just slides the sticky note forward; no new commit.
What does rebase actually do?	REPLAYS your commits as new snapshots on top of the target — straight line, new IDs, originals abandoned (reflog keeps them).
The iron rebase rule?	Never rebase commits others already have — rewriting a shared graph breaks everyone downstream.
Undo a PUSHED bad commit?	git revert <hash> — adds an anti-commit; rewrites nothing; always safe.
Undo tools that REWRITE history (local-only)?	reset · rebase · commit --amend — fine while private, forbidden once shared.
"Everything's broken, I'm lost" — first command?	git reflog — the journal of everywhere HEAD has been (~90 days); reset --hard to a good hash.
Staged the wrong file?	git restore --staged <file>
fetch vs pull?	fetch = update your copy of the remote's graph, touch nothing of yours; pull = fetch + merge (or rebase) into your branch.
Why do dev/brain/~/.claude have NO remotes?	Estate law: doctrine/life material never leaves the machine — pre-push guards enforce it; OneDrive is their carrier.
Why do dev/brain keep .git OUTSIDE OneDrive?	Syncing thousands of tiny hash files corrupts/slows — files sync via OneDrive, history lives in C:\Users\samra\.gitdirs\.
What ate the atlas merge commit on 04/08/2026?	An every-5-min `pull --rebase` (bridge worker) replayed the branch linearly mid-merge — rebase doing its exact job at the wrong moment (ledger 108).
The one command to read a repo's shape?	git log --oneline --graph --all
git -C <path> does what?	Runs git as if standing in <path> — how sessions operate many repos without cd.
git stash is for…	Parking half-done work to get a clean tree — and stash pop to get it back (don't forget it exists).

## Quick-fire (aloud, 30 seconds)

1. Commit = diff or snapshot? 2. Branch = copy or sticky note? 3. Shared-safe undo?
4. Lost? First command? 5. Rebase rewrites — when is that fine?
*(snapshot · sticky note · revert · reflog · only while private)*
