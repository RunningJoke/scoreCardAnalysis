---
id: 005
title: "rapm_sams: fit the rally model per window (season and form)"
status: open
depends: [010, 011]
---

## Goal

Estimate θ (impact), δ (sideout/break split), σ (serve) and τ (team/libero) from the rally table.

## Acceptance criteria

- [ ] Weighted logistic regression of "serving team wins rally" with the terms in [_doc/03_model.md](../../_doc/03_model.md)
- [ ] Separate L2 penalties per term group, shrinking θ and σ toward their priors
- [ ] λ values chosen by forward-chaining cross-validation
- [ ] Season window (all rallies up to match day d, prior = last season × ρ) and form window (last K matches, prior = season rating before the window)
- [ ] Outputs converted to points per 100 rallies

## Notes

Implements `RatingModel` as `rapm_sams` (`requires = {rallies, server}`), see [_doc/08_architecture.md](../../_doc/08_architecture.md). Leverage weights come from issue 006; until then, fit without weights.
