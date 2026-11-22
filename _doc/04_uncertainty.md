# 04 · Uncertainty: how sure is each number?

## Bootstrap by match

Resample whole matches within the window about 200 times and refit. The 10th to 90th percentile of the results is the **80 % band** shown next to every rating. Resampling whole matches keeps the rallies of one match together, so the band isn't falsely narrow.

## Flags

| Flag | Rule | Shown as |
|---|---|---|
| Inseparable | Her on-court pattern correlates above 0.95 with a teammate's | "Rating shared with #x"; the band is wide |
| Small sample | Fewer than 100 rallies in the window | Rating greyed out |
| Libero | Player is a libero | "n/a, inside the team term τ" |
| Sufficient | None of the above | A small OK mark |
