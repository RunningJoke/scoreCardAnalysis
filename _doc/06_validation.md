# 06 · Validation, limits and settings

## Backtest before trusting a single rating

Fit on match days 1…d and predict day d+1, then roll forward through the season. Score with log-loss and Brier score on rallies, and accuracy on set winners.

| Model | Knows | Role |
|---|---|---|
| League rate | Break-point rate only | Floor |
| Team-only | One rating per team, no players | **The bar to beat.** If the player model doesn't beat it, the player differences are noise and the profiles say so. |
| v0 plus-minus | Raw on/off per player | The current method, for comparison |
| Rally impact model | All of the above, adjusted | Candidate |

## Known limits

- It measures a player's effect on rallies, not her actions. A great passer next to a weak hitter can look average.
- Positions are unknown, so a setter and an outside are compared on one scale.
- Liberos get no individual rating, and middles may carry a little of the libero's effect.
- Teams that never substitute give wide bands. Only cross-season and cross-team data can narrow them.
- Name matching can merge two different people with the same name. These cases go to manual review.

## Settings

| Setting | Start value | How set |
|---|---|---|
| λ_θ, λ_δ, λ_σ, λ_τ | from CV | Forward-chaining cross-validation |
| Form window K | 3 matches | Coach preference |
| Season carry-over ρ | 0.7 | Backtest on the second season |
| Min. rallies to show | 100 | Fixed |
| Bootstrap draws | 200 | Fixed |
| Leverage weights | On for clutch only | Fixed |
| Home term | On | Drop if about 0 |
