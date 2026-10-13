# 05-git-properly — like you're 5

Module 05, git properly: every term, explained like you're 5.

- **Taught in:** `C:\Users\samra\repos\ai-mastery\modules\05-git-properly\TEACH.md`

- **The one-line reminders:** `GLOSSARY.md` → `## Module 05 — git properly`

- **Safe to run:** every command below is read-only unless it says otherwise.

- **Where to run them:** after `cd C:\Users\samra\repos\ai-mastery`

- **The animated version of most of these:** `start C:\Users\samra\repos\ai-mastery\modules\05-git-properly\interactive\branch-visualiser.html`, then press ▶ Step.

---

### Branch
**Like you're 5:** A sticky note with a name on it, stuck on one photo in the family album. Making a new sticky note doesn't copy the album; it's just a note you can move to another photo later.

**The real words:** A movable sticky note on one commit; creating one copies nothing. → [05 five sentences](../modules/05-git-properly/TEACH.md)

**See it:** `git branch -v` — each line is a note's name and the one commit it is stuck on.

### Commit
**Like you're 5:** A photo of your whole room at one moment, with a caption, and an arrow pointing to the photo taken before it. Never "what changed"; always the whole room.

**The real words:** A full snapshot + parent pointer(s) + message; never a diff. → [05 five sentences](../modules/05-git-properly/TEACH.md)

**See it:** `git cat-file -p HEAD` — a `tree` line (the snapshot), a `parent` line (the arrow back), the author, then the message.

### Fast-forward
**Like you're 5:** Your friend went ahead on the path and you stayed still. To catch up you don't need to meet in the middle; you just walk forward to where they are. Nothing new is built.

**The real words:** A merge with nothing to merge: the sticky note slides forward and no merge commit is made. → [05 branching](../modules/05-git-properly/TEACH.md)

**See it:** Branch visualiser, scenario "4 · Rebase (replayed copies)", last step `git switch main && git merge feature`: main's note just slides to D′.

### fetch vs pull
**Like you're 5:** Fetch is looking at the new photos in your friend's album without touching yours. Pull is looking AND sticking them into your album straight away.

**The real words:** Update your copy of the remote's graph vs fetch-and-merge into your branch. → [05 drills](../modules/05-git-properly/drills.md)

**See it:** `git fetch` then `git status` — it says whether you are behind `origin/main`; nothing in your files moved.

### HEAD
**Like you're 5:** A "you are here" pin on the map. When you take a new photo, the pin and the sticky note you're standing on both move to the new photo.

**The real words:** Where you're standing; committing moves the note you stand on. → [05 five sentences](../modules/05-git-properly/TEACH.md)

**See it:** `git log --oneline -1` — the top line reads `(HEAD -> main…)` when you stand on main.

### Merge commit
**Like you're 5:** Two friends walked different paths and meet up again. They take one photo together that points back to both of their last photos. That shared photo has two "before" arrows.

**The real words:** A snapshot with TWO parents, tying two histories together. → [05 branching](../modules/05-git-properly/TEACH.md)

**See it:** `git cat-file -p 5b22961` — the merge of this chain's ticket 1 shows two `parent` lines.

### Rebase
**Like you're 5:** Instead of two paths meeting, you redo your walk as if you'd started from where your friend is now. It looks like one straight path, but they are brand-new photos; the old ones get thrown away.

**The real words:** Replaying commits as new snapshots on another tip: straight line, new IDs, originals abandoned; never on commits others already have. → [05 branching](../modules/05-git-properly/TEACH.md)

**See it:** Branch visualiser, scenario "4 · Rebase (replayed copies)", step `git rebase main`: D is replayed as a new D′ and old D fades. Don't run it on a shared repo.

### Reflog
**Like you're 5:** A diary of everywhere your "you are here" pin has been, for about three months. Lost? Read the diary, find where you were happy, go back there.

**The real words:** The ~90-day journal of everywhere HEAD has been; the "I'm lost" safety net. → [05 undo toolbox](../modules/05-git-properly/TEACH.md)

**See it:** `git reflog -5` — your last five moves, newest first.

### Remote / origin
**Like you're 5:** A copy of your photo album kept at a friend's house, with its own sticky notes. Sending and fetching photos keeps the two albums matching.

**The real words:** Another copy of the graph (your GitHub) with its own sticky notes; `origin` is the usual name for it. → [05 five sentences](../modules/05-git-properly/TEACH.md)

**See it:** `git remote -v` — `origin` points at `https://github.com/samrathsingh302/ai-mastery.git`.

### Revert
**Like you're 5:** You can't un-take a photo everyone has already seen. So you take a new photo that puts the room back how it was. The history keeps both photos, honestly.

**The real words:** The shared-safe undo: an anti-commit that cancels changes without rewriting history. → [05 undo toolbox](../modules/05-git-properly/TEACH.md)

**See it:** Branch visualiser, scenario "5 · Revert vs reset", step `git revert C`: a new anti-commit C̄ appears and C stays in the graph.

### Staging area / index
**Like you're 5:** Laying out tomorrow's clothes on a chair before you get dressed. Whatever is on the chair is what you'll wear; the rest stays in the wardrobe.

**The real words:** The loading dock: what the next snapshot will contain; `git add` loads it, `git diff --staged` shows it. → [05 three places](../modules/05-git-properly/TEACH.md)

**See it:** `git status` — "Changes to be committed" is the chair; "Changes not staged" is the wardrobe.
