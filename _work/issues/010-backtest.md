---
id: 010
title: Backtest against baselines
status: open
depends: [005]
---

## Goal

Prove that player ratings carry signal before anyone relies on them.

## Acceptance criteria

- [ ] Forward-chaining: fit on match days 1…d, predict day d+1, roll through the season
- [ ] Metrics: rally log-loss, Brier score, set-winner accuracy
- [ ] Baselines: league rate, team-only model, v0 plus-minus
- [ ] If the player model does not beat the team-only model, profiles state that the player differences are not distinguishable from noise

## Notes

[_doc/06_validation.md](../../_doc/06_validation.md)
