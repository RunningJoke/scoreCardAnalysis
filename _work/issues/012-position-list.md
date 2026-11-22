---
id: 012
title: "Manual position list: format, loader, coverage"
status: open
depends: [004, 011]
---

## Goal

Let us maintain player positions by hand and join them to the rally data.

## Acceptance criteria

- [ ] Format as in `data/positions/_template.csv`: `season, team, jersey, name, position, valid_from`; positions `S, OH, MB, OPP, L, U`
- [ ] The template is tracked; real lists are git-ignored
- [ ] Loader validates values and matches names via the identity step (004); unmatched names are reported
- [ ] Coverage report per team: share of on-court rally slots with a known position
- [ ] `valid_from` (match day) handles position changes during a season

## Notes

[_doc/08_architecture.md](../../_doc/08_architecture.md#enrichment)
