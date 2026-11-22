---
id: 006
title: Set win-probability chain (leverage, line-up predictor)
status: open
depends: [005]
---

## Goal

Compute P(set win) from any score and serve state, given sideout and break rates.

## Acceptance criteria

- [ ] Markov chain over (score, serving team), to 25, or 15 in a fifth set, win by 2
- [ ] Leverage per rally: P(set | point won) − P(set | point lost), normalized to a mean of 1
- [ ] Callable with model-predicted rates for any two sixes (needed by the line-up predictor in issue 009)
- [ ] Check: equal rates at 0:0 give about 50 %

## Notes

See "Leverage weighting" in [_doc/03_model.md](../../_doc/03_model.md).
