---
id: 014
title: "First slice: baseline models and a report that reproduces v0"
status: open
depends: [003, 004, 011]
---

## Goal

Run the whole pipeline end to end with the simplest models before building the real one.

## Acceptance criteria

- [ ] `team_only` and `plus_minus` implement `RatingModel`
- [ ] `impact ingest`, `impact fit --model plus_minus` and `impact report --team "<team>"` produce a static HTML squad report
- [ ] On the four LL4 2026/27 sheets the rallies on court and the +/- per player match the v0 Burladingen 2 report
- [ ] The expected values for that check live under `data/` (they contain names); the test skips without them

## Notes

This proves parsing, rally rebuilding, identity and reporting together. `rapm_sams` (005) then only swaps the model.
