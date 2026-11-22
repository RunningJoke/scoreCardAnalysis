# Landesliga Player Impact

Rates volleyball players by their impact on rallies, using only the SAMS score sheets every Landesliga game produces. The ratings feed opponent scouting, line-up decisions and form tracking.

**Status:** concept done, implementation not started.

## How it works, in one paragraph

Each score sheet's service rounds and line-ups are turned into a rally-by-rally table: who was on court for each team, who served, who won. A ridge-regularized logistic regression (adjusted plus-minus, as used in basketball) estimates how much each player shifts the chance that her team wins a rally, after accounting for teammates, opponents, the server and home advantage. It is fitted for the season so far and for the last few matches, which gives a season rating and a form signal. Details: [_doc/00_overview.md](_doc/00_overview.md).

## Repository

```
data/            score-sheet PDFs (git-ignored; structure only)
_doc/            concept docs and the published concept canvas
_work/           backlog and issues, until we move to GitHub
.claude/skills/  Claude Code skills for this project
CLAUDE.md        context and rules for Claude Code
```

## Getting started

1. Copy the score sheets into `data/LL_2526/` and `data/LL4_2627/` (see [data/README.md](data/README.md)).
2. Read [_doc/00_overview.md](_doc/00_overview.md).
3. Pick the next open issue from [_work/README.md](_work/README.md).
