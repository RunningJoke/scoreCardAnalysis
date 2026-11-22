---
id: 002
title: Rebuild the rally sequence per set
status: open
depends: [001]
---

## Goal

Produce the rally table: one row per rally with both on-court sixes, the server and the winner.

## Acceptance criteria

- [ ] Walk each set from 0:0 using the service-round end scores; the receiving team rotates on each sideout
- [ ] Substitutions applied at their recorded score (substituting team's score first)
- [ ] Output columns: match, set, rally number, score before, serving team, server, serving six, receiving six, winner
- [ ] Unit test on one hand-checked set

## Notes

Schema and an example: step 2 in [_doc/02_pipeline.md](../../_doc/02_pipeline.md).
