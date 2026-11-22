---
id: 013
title: Infer libero changes from positions
status: open
depends: [002, 012]
---

## Goal

Fill the libero columns of the rally table where a team's middle blockers are known.

## Acceptance criteria

- [ ] Rule: the libero replaces each middle blocker in the back row (positions I, V, VI), except when that middle blocker serves
- [ ] Whether a libero may serve is a per-league setting in `impact.toml`
- [ ] Only applied when the team's middle blockers and libero are in the position list; otherwise the columns stay empty
- [ ] Filled rows get `libero_source = inferred`
- [ ] Check: each libero is on court for a plausible share of rallies (roughly 40–60 %); outliers are reported

## Notes

With two liberos on a roster, the position list must say who played; otherwise treat it as unknown.
