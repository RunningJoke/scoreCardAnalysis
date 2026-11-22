# 05 · Outputs: player profile and modules

## Player profile

One card per player and window. The canvas shows a mock-up with made-up values.

| Field | Content |
|---|---|
| Impact | Points per 100 rallies, with the 80 % band |
| Sideout | Impact when her team receives |
| Break | Impact when her team serves |
| Serve | Extra break points per 100 own serves, with the number of serves |
| Clutch | Leverage-weighted impact − plain impact |
| Playing time | Rallies, share of team rallies, sets, starts |
| Form curve | Season rating (with band) and form rating per match day |
| Partners (exploratory) | Model residual while both are on court, shrunk by rallies together; top and bottom 3 |
| Flags | See [04_uncertainty.md](04_uncertainty.md) |
| Position | Not recorded; shown as unknown |

## Modules

### Scouting an opponent

Used for the next game's game plan.

- Players ranked by impact, with band and flags
- Best and weakest servers (σ)
- **Rotation table**: sideout % and break % in each of their 6 rotations, observed vs expected. The weakest sideout rotation is where to serve hardest.
- Their usual starting six and substitution habits (who comes on when trailing)

### Our own line-up

Used to decide who starts and who comes on.

- **Line-up predictor**: pick any six and an opponent. The model gives sideout % and break %, and the Markov chain ([03_model.md](03_model.md)) turns them into P(set win).
- Compare candidates side by side, for example "#12 instead of #18 against Team C: +6 % set-win chance".
- Our own rotation table, to place strong servers and passers

### Form over time

Used to spot slumps and development.

- Season and form curves per player, refreshed after every match day
- An alert when form leaves the season band two match days in a row
- Team view: whose form moved most since the last report
