---
id: 001
title: Parse a SAMS score sheet into a match record
status: open
depends: [000]
---

## Goal

Turn one SAMS PDF into a structured match record.

## Acceptance criteria

- [ ] Match fields: league, season, game number, date, home team, away team, venue, result
- [ ] Per set: starting six in rotation order I–VI for both teams, substitutions (in, out, score at the change), service-round end scores, timeouts, set score and duration
- [ ] Roster: number → name, libero flag, captain flag, used flag (X), MVP
- [ ] Umlaut encoding fixed
- [ ] Runs over all sheets in `data/`; every sheet either parses or is logged with a reason

## Notes

See [_doc/01_data.md](../../_doc/01_data.md) and step 1 in [_doc/02_pipeline.md](../../_doc/02_pipeline.md). The layout differs slightly between the 2025/26 sheets and the 2026/27 sheets (SAMS Score 6.4.1); check both.
