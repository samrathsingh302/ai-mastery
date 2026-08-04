# Project 05 — Narrate your own repos' workflow (the plan's exact ask)

**What:** produce `workflow-narration.md` (here) explaining, in your own words and from
evidence, how git actually flows through YOUR estate. Read-only everywhere. ~2h. This is the
plan's "narrate your own repos' workflow" made concrete — and it doubles as interview prep:
"walk me through your version-control workflow" is a standard opener.

## Do this, per repo — psoc-portal AND ai-mastery (this one)

Answer each with the COMMAND you used as evidence (paste command + trimmed output):

1. **Shape:** how many branches exist (`git branch -a`)? Is history linear or merged
   (`git log --oneline --graph -15`)? Any tags?
2. **Cadence:** what do the last 10 commits do, in one line each — and which were written by
   you at a keyboard vs by a Claude session (the trailer lines tell you)?
3. **Remote:** where does `git remote -v` point? Private or public? What would `git push`
   send right now (`git status`, `git log origin/main..HEAD --oneline`)?
4. **Recovery story:** pick any commit from last week and explain how you'd undo it today,
   with the toolbox table — which tool and WHY that one (shared vs local rule).
5. **Doctrine check:** confirm with your own eyes ONE estate law from TEACH — e.g. `cat
   C:\Users\samra\OneDrive\dev\.git` (a file, not a folder — pointing where?), or the
   absence of a remote on dev (`git -C C:\Users\samra\OneDrive\dev remote -v`).

Then close with **the two-laptop diagram**: hand-draw (photo or ASCII) how a commit made on
Daddykins reaches Sonnykins — naming which carrier moves code, which moves markdown, and
which moves doctrine.

## Acceptance checklist

- [ ] Both repos narrated, every answer with pasted evidence
- [ ] At least one "I did not know that" moment written down (there will be one)
- [ ] The two-laptop diagram exists and names all three carriers correctly
- [ ] A stranger (or interview panel) could follow your narration without seeing the repos
- [ ] Committed here — with a message that would make sense in `git log --oneline` in a year
