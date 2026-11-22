---
id: 004
title: Player identity across matches, teams and seasons
status: open
depends: [001]
---

## Goal

Give every person one stable ID, because jersey numbers are only valid within a match.

## Acceptance criteria

- [ ] ID = normalized name (Unicode NFC, case-folded, "Surname, Firstname")
- [ ] The same name on another team or in another season maps to the same ID
- [ ] Near-matches (one letter off, double names) go to a review list and are not merged automatically
- [ ] Liberos are flagged

## Notes

Step 4 in [_doc/02_pipeline.md](../../_doc/02_pipeline.md). The review list contains names, so it stays under `data/` and out of git.
