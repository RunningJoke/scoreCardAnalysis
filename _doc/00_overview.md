# Rally Impact Model: overview

How much does a player change the chance that her team wins a rally, once teammates, opponents and the server are accounted for? This folder describes the algorithm that answers that from SAMS score sheets alone.

- **Concept canvas (live, private link):** https://claude.ai/artifact/WYPgxhR7gm2BTHDrGuNg1Z
- **Local copy:** [artifacts/rally-impact-model.html](artifacts/rally-impact-model.html), open it in a browser
- **Version:** v0.1, 2026-11-21. Concept only, no implementation yet.

## Decisions

| Topic | Decision | Why |
|---|---|---|
| Used for | Scouting · own line-up · form over time | Team's stated needs |
| Unit | Rally | About 180 per match, line-up known for each; far more signal than sets or matches |
| Core model | Batch RAPM per window | Statistically clean; form comes from a short window shrunk toward the season rating |
| Liberos | Team-level term | Libero changes are not on the sheet |
| Output | Full profile | Covers all three uses |
| Data scope | Generic | Leagues and seasons are configuration, not code |

## Documents

| File | Content |
|---|---|
| [01_data.md](01_data.md) | What a score sheet does and does not record |
| [02_pipeline.md](02_pipeline.md) | Steps 1–4: parse, rebuild rallies, validate, identify players; rally table schema |
| [03_model.md](03_model.md) | Step 5: formula, terms, fitting, units, leverage, windows |
| [04_uncertainty.md](04_uncertainty.md) | Step 6: bootstrap bands, separability and sample flags |
| [05_outputs.md](05_outputs.md) | Step 7: player profile and the scouting, line-up and form modules |
| [06_validation.md](06_validation.md) | Backtest, known limits, settings |
| [07_background.md](07_background.md) | How other sports rate players; concepts considered and rejected |

## Pipeline at a glance

| Step | What | Output | Doc | Issue |
|---|---|---|---|---|
| 0 | Score sheets | SAMS PDFs in `data/` | [01](01_data.md) | – |
| 1 | Parse | Match record | [02](02_pipeline.md) | [001](../_work/issues/001-parse-score-sheet.md) |
| 2 | Rebuild rallies | Rally table | [02](02_pipeline.md) | [002](../_work/issues/002-rebuild-rallies.md) |
| 3 | Validate | Clean sets and a drop log | [02](02_pipeline.md) | [003](../_work/issues/003-validate-sets.md) |
| 4 | Identify players | Stable player IDs | [02](02_pipeline.md) | [004](../_work/issues/004-player-identity.md) |
| 5 | Fit per window | θ, δ, σ, τ per window | [03](03_model.md) | [005](../_work/issues/005-fit-rally-model.md), [006](../_work/issues/006-set-markov-chain.md) |
| 6 | Uncertainty | Bands and flags | [04](04_uncertainty.md) | [007](../_work/issues/007-uncertainty.md) |
| 7 | Profiles and modules | Profiles, scouting, line-up, form | [05](05_outputs.md) | [008](../_work/issues/008-player-profile.md), [009](../_work/issues/009-modules.md) |
| – | Backtest | Proof that player ratings carry signal | [06](06_validation.md) | [010](../_work/issues/010-backtest.md) |

## Predecessor

v0 is "Burladingen 2 Squad Analysis" (`data/LL4_2627/`): raw on-court plus-minus per 100 rallies, shrunk toward the team average. Its own stated gaps are what this model closes: no opponent adjustment, no set-state adjustment, starters who always play together can't be separated, and the libero gap.
