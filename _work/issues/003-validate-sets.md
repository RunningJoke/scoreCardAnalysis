---
id: 003
title: Validate rebuilt sets and log dropped ones
status: open
depends: [002]
---

## Goal

Make sure only sets that reconcile enter the model.

## Acceptance criteria

- [ ] The rebuilt final score equals the printed set score
- [ ] Every substitution score lies on the rebuilt score path
- [ ] At most 6 substitutions per team per set; every number is on the roster
- [ ] The number of service rounds matches the number of sideouts
- [ ] Failed sets are dropped and listed in a log with the reason; a summary gives the share of sets kept

## Notes

Step 3 in [_doc/02_pipeline.md](../../_doc/02_pipeline.md).
