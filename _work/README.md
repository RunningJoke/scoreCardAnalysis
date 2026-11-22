# Work tracking

This is temporary until the project moves to GitHub; each file then becomes a GitHub issue.

## Conventions

- One issue per file: `issues/NNN-short-slug.md`, numbered in order of creation.
- The frontmatter holds `id`, `title`, `status` (`open` · `in-progress` · `blocked` · `done`) and `depends` (a list of issue ids).
- The body has **Goal**, **Acceptance criteria** (a checklist) and **Notes**, linking the relevant `_doc/` file.
- When an issue's status changes, update the table below in the same change.

## Backlog

Ordered by pipeline step. See [_doc/02_pipeline.md](../_doc/02_pipeline.md) for the steps.

| ID | Title | Status | Depends |
|---|---|---|---|
| [000](issues/000-tech-stack.md) | Choose tech stack and project skeleton | open | – |
| [001](issues/001-parse-score-sheet.md) | Parse a SAMS score sheet into a match record | open | 000 |
| [002](issues/002-rebuild-rallies.md) | Rebuild the rally sequence per set | open | 001 |
| [003](issues/003-validate-sets.md) | Validate rebuilt sets and log dropped ones | open | 002 |
| [004](issues/004-player-identity.md) | Player identity across matches, teams and seasons | open | 001 |
| [005](issues/005-fit-rally-model.md) | Fit the rally model per window (season and form) | open | 002, 003, 004 |
| [006](issues/006-set-markov-chain.md) | Set win-probability chain (leverage, line-up predictor) | open | 005 |
| [007](issues/007-uncertainty.md) | Uncertainty bands and reliability flags | open | 005 |
| [008](issues/008-player-profile.md) | Player profile output | open | 005, 006, 007 |
| [009](issues/009-modules.md) | Modules: scouting, line-up, form alerts | open | 008 |
| [010](issues/010-backtest.md) | Backtest against baselines | open | 005 |
