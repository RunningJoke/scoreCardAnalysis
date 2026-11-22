---
id: 015
title: "rapm_positions: position-aware model with individual liberos"
status: open
depends: [005, 012, 013]
---

## Goal

Use positions and libero data where we have them.

## Acceptance criteria

- [ ] `requires = {rallies, server, positions}`; uses the libero columns when they are filled
- [ ] Player effect split into a position mean and an individual deviation, θ_i = μ_position + u_i, with u_i shrunk toward 0
- [ ] Liberos rated individually when libero data is present; the team term is then penalized more strongly
- [ ] The ratings table includes impact relative to position as well as overall impact
- [ ] Backtest against `rapm_sams` on the same teams; the registry default per league follows the result

## Notes

[_doc/08_architecture.md](../../_doc/08_architecture.md), [_doc/03_model.md](../../_doc/03_model.md)
