---
id: 011
title: "Layer contracts: canonical schema, capabilities, model interface, registry"
status: open
depends: [000]
---

## Goal

Put the contracts from [_doc/08_architecture.md](../../_doc/08_architecture.md) into code, so that sources and models can be swapped independently.

## Acceptance criteria

- [ ] `canonical.py`: rally table columns and types, with the optional libero columns
- [ ] `capabilities.py`: returns the capability set for a window; the positions coverage threshold comes from config
- [ ] `models/base.py`: `RatingModel` and `FittedModel` protocols; long-format ratings table (`player_id, window, metric, value, lo, hi, n`)
- [ ] `models/registry.py`: register models; `auto` picks the richest model whose `requires` is met; a config override wins
- [ ] Unit test with stub models: without positions `auto` picks `rapm_sams`, with positions it picks `rapm_positions`, and an explicit config choice overrides both

## Notes

Reports read only the ratings table, so a new model needs no report changes.
