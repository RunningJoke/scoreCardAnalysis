# 03 · Core model: regularized adjusted plus-minus per rally

Every rally is framed the same way: **does the serving team win this point (a break point)?** The probability depends on the twelve players on court, the server and both teams' baselines. This is basketball's RAPM, applied to rallies instead of possessions.

## Formula

```
logit P(serving team wins rally r) =
    β
  + h · home
  + Σ_{i ∈ serving six}   (θ_i + δ_i^srv)
  − Σ_{j ∈ receiving six} (θ_j + δ_j^rcv)
  + σ_server(r)
  + τ_serving team − τ_receiving team
```

## Terms

| Term | Meaning | Shrunk toward | Penalty |
|---|---|---|---|
| β | League break-point rate on the logit scale (typically 35–40 %) | – | free |
| h | Home advantage: +1 if the serving team is at home, −1 if away (optional) | 0 | free |
| θ_i | **Overall impact** of player i while on court | Prior rating | λ_θ |
| δ_i^srv, δ_i^rcv | Phase split: extra impact when her team serves (breaking) or receives (siding out) | 0 | λ_δ > λ_θ |
| σ_k | **Serve rating**: extra break chance on rallies player k serves herself | Prior rating | λ_σ |
| τ_t | **Team and libero term**: everything constant for a team that the listed six don't explain (libero, system, coaching) | 0 | λ_τ ≫ λ_θ |

## Fitting

- Minimize the weighted log-loss over all rallies in the window plus the ridge penalties:
  `λ_θ Σ(θ − θ_prior)² + λ_δ Σδ² + λ_σ Σ(σ − σ_prior)² + λ_τ Στ²`
- Choose the λ values by forward-chaining cross-validation: fit up to match day d, score the rallies of day d+1.
- λ_τ is kept large so team strength is credited to players wherever the data allows. τ only absorbs what can't be attributed, mainly the libero.
- Players who always play together can't be told apart. The ridge then splits their credit evenly instead of producing extreme values.

## Units people can read

| Output | Formula | Unit |
|---|---|---|
| Impact | `100 · 2 · (P(β+θ) − P(β))`, roughly `50·θ` | Point difference per 100 rallies compared with an average league player (same unit as v0) |
| Serve | `100 · (P(β+σ) − P(β))` | Extra break points per 100 own serves |
| Sideout and break impact | θ + δ^rcv and θ + δ^srv | Same unit as impact |

## Leverage weighting (optional)

Each rally gets a weight equal to how much it moves the chance of winning the set:

```
L(r) = P(set | point won) − P(set | point lost)
```

This comes from a set-level Markov chain that uses the league sideout and break rates and plays to 25 (15 in a fifth set), win by 2. Weights are normalized to a mean of 1. A rally at 23:23 counts about three times as much as one at 5:12.

**Clutch** = θ fitted with leverage weights − θ fitted without them.

The same chain turns predicted sideout and break rates into P(set win) for the line-up predictor ([05_outputs.md](05_outputs.md)).

## Windows: season and form

The model is fitted twice per match day d:

| Window | Rallies | Prior |
|---|---|---|
| **Season** | All up to day d | Last season's rating × ρ (start value 0.7); 0 for a new player |
| **Form** | Last K matches (start value 3) | Season rating from before the window |

**Form delta** = form − season.

```
match day:  1   2   3   4   5   6   7   8   9   10
Season:     [===========================]               (days 1–7)
Form K=3:                   [===========]               (days 5–7, prior = season @ day 4)
                                        ^ today = day 7
```
