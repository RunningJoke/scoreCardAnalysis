# 07 · Background: how other sports rate players

## Approaches by sport

| Sport | Main approach | Data it needs | Usable with score sheets? |
|---|---|---|---|
| Basketball | Plus-minus, then RAPM (regression adjusting for teammates and opponents), then hybrids with box-score stats (EPM, RAPTOR) | Who was on court for each possession | Yes: RAPM fits almost one to one |
| Ice hockey | Corsi (shot share while on ice), RAPM, GAR (goals above replacement) | Shifts, shots | Yes: the RAPM part |
| Soccer | Expected-goals models on every touch (xG, xT, VAEP); plus-minus barely works because so few goals are scored | Event tracking | No event data |
| Handball | Throw efficiency, save %, sometimes plus-minus | Per-throw stats | Mostly no |
| Volleyball (pro level) | DataVolley scouting: attack efficiency, reception %, serve rating | A live human scout | Only the serve is attributable |
| Chess, online gaming | Elo (one against one), TrueSkill (team rating = sum of players, updates shared out by uncertainty) | Results and line-ups | Yes |
| Baseball, cricket, NFL analytics | Win probability added: weight each play by how much it changed the chance of winning | Play by play | Yes: the score of every rally is known |

## Concepts considered

| # | Concept | Verdict |
|---|---|---|
| 1 | Match Elo shared by playing time | Rejected: two players who both play the full match always get the same number, so starters can't be separated |
| 2 | Rally-level Elo/TrueSkill (online) | Rejected in favour of windows: ratings are order-dependent and early-season noise is never corrected |
| 3 | RAPM per rally | **Chosen** as the core ([03_model.md](03_model.md)) |
| 4 | Serve impact | **Chosen** as the σ term |
| 5 | Leverage weighting | **Chosen** for the clutch measure |
| – | Rotation sideout/break analysis | **Chosen** for the scouting and line-up modules |

## Where the model's ideas come from

| Idea | Origin | Used here as |
|---|---|---|
| Plus-minus, on/off | Ice hockey, basketball | v0, and a backtest baseline |
| RAPM | Basketball, hockey | Core model |
| Prior-informed RAPM | Basketball multi-year RAPM | Season carry-over ρ; form shrinks toward season |
| Win probability added, leverage | Baseball, cricket, NFL | Leverage weights, clutch |
| Rotation analysis | Volleyball scouting (DataVolley) | Rotation table |
