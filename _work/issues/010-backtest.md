---
id: 010
title: Model-agnostic backtest harness
status: open
depends: [011, 014]
---

## Goal

Compare any registered models on the same data, so we know which model to trust for which league and data level.

## Acceptance criteria

- [ ] `impact backtest --models ...` takes any models from the registry
- [ ] Forward-chaining: fit on match days 1…d, predict day d+1, roll through the season
- [ ] Metrics: rally log-loss, Brier score, set-winner accuracy; one HTML or CSV summary per league
- [ ] Runs with `team_only` and `plus_minus` from 014; later models are added without changes to the harness
- [ ] If a player model does not beat `team_only`, profiles state that the player differences are not distinguishable from noise

## Notes

[_doc/06_validation.md](../../_doc/06_validation.md). Also used to choose the λ values for 005.
