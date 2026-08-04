# History gym — reference transcript (open AFTER your attempt / when stuck >30 min)

```
cd exercises
mkdir playground && cd playground
git init
echo line1 > notes.md
git add -A && git commit -m "start"
echo line2 >> notes.md && git add -A && git commit -m "second"
echo line3 >> notes.md && git add -A && git commit -m "third"
git branch feature
git switch feature
echo the-idea > idea.md
git add -A && git commit -m "idea drafted"
git switch main
echo line4 >> notes.md && git add -A && git commit -m "main moves on"
git merge feature            # editor opens -> save/close (this IS the merge commit)
git tag v1
echo whoops > oops.md && git add -A && git commit -m "mistake"
git revert HEAD              # editor opens -> save/close
git reflog | head
cd .. && python check.py     # expect 6/6
```

Why each check exists: ≥7 commits proves the full journey · the merge commit proves main
diverged first (step 4 before step 5 — otherwise git fast-forwards and no merge commit is
born) · the revert proves you know the shared-safe undo · oops.md absent proves revert
actually restored the tree · the tag and branch prove sticky notes are cheap and permanent.
