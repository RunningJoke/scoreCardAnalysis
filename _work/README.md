# Work tracking

This is temporary until the project moves to GitHub; each file then becomes a GitHub issue and each milestone a GitHub milestone.

## Conventions

- One issue per file: `issues/NNN-short-slug.md`, numbered in order of creation.
- The frontmatter holds `id`, `title`, `status` (`open` · `in-progress` · `blocked` · `done`) and `depends` (a list of issue ids).
- The body has **Goal**, **Acceptance criteria** (a checklist) and **Notes**, linking the relevant `_doc/` file.
- When an issue's status changes, update the table below in the same change.

## Milestones

The order puts a thin end-to-end slice first (M3: reproduce the v0 report with the simplest model), so every later model plugs into a pipeline that already works.

| Milestone | Outcome | Issues |
|---|---|---|
| **M1 Foundation** | Package, CLI stub, config, tests; layer contracts in code | 000, 011 |
| **M2 Data pipeline** | All sheets → validated canonical rally table | 001, 002, 003, 004 |
| **M3 First slice** | `impact report` reproduces the v0 Burladingen numbers; backtest harness runs the baselines | 014, 010 |
| **M4 Core model** | `rapm_sams` with season/form windows, set chain, uncertainty | 005, 006, 007 |
| **M5 Rich data** | Position list, libero inference, `rapm_positions` | 012, 013, 015 |
| **M6 Outputs** | Full profiles; scouting, line-up and form modules | 008, 009 |

M5 only depends on M2 and the contracts, so it can run in parallel with M4.

## Backlog

| ID | Title | Milestone | Status | Depends |
|---|---|---|---|---|
| [000](issues/000-project-skeleton.md) | Project skeleton: package, CLI, config, tests | M1 | done | – |
| [011](issues/011-contracts.md) | Layer contracts: canonical schema, capabilities, model interface, registry | M1 | open | 000 |
| [001](issues/001-parse-score-sheet.md) | Parse a SAMS score sheet into a match record | M2 | open | 000 |
| [002](issues/002-rebuild-rallies.md) | Rebuild the rally sequence per set | M2 | open | 001, 011 |
| [003](issues/003-validate-sets.md) | Validate rebuilt sets and log dropped ones | M2 | open | 002 |
| [004](issues/004-player-identity.md) | Player identity across matches, teams and seasons | M2 | open | 001 |
| [014](issues/014-first-slice.md) | First slice: baseline models and a report that reproduces v0 | M3 | open | 003, 004, 011 |
| [010](issues/010-backtest.md) | Model-agnostic backtest harness | M3 | open | 011, 014 |
| [005](issues/005-fit-rally-model.md) | `rapm_sams`: fit the rally model per window | M4 | open | 010, 011 |
| [006](issues/006-set-markov-chain.md) | Set win-probability chain (leverage, line-up predictor) | M4 | open | 005 |
| [007](issues/007-uncertainty.md) | Uncertainty bands and reliability flags | M4 | open | 005 |
| [012](issues/012-position-list.md) | Manual position list: format, loader, coverage | M5 | open | 004, 011 |
| [013](issues/013-libero-inference.md) | Infer libero changes from positions | M5 | open | 002, 012 |
| [015](issues/015-rapm-positions.md) | `rapm_positions`: position-aware model with individual liberos | M5 | open | 005, 012, 013 |
| [008](issues/008-player-profile.md) | Player profile output | M6 | open | 005, 006, 007 |
| [009](issues/009-modules.md) | Modules: scouting, line-up, form alerts | M6 | open | 008 |
