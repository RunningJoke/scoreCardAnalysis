# 02 · Data preparation: sheet to rally table

```
0 Score sheets → 1 Parse → 2 Rebuild rallies → 3 Validate → 4 Identify players → 5 Fit → 6 Uncertainty → 7 Profiles & modules
```

Steps 5–7 are in [03_model.md](03_model.md), [04_uncertainty.md](04_uncertainty.md) and [05_outputs.md](05_outputs.md).

## 1 · Parse

- **In:** one SAMS PDF (text layer)
- **Out:** a match record with teams, home/away, date, league, season and game number. Per set: the starting six, substitutions, service-round end scores and timeouts. Roster as number → name with libero and captain flags.
- Fix the text encoding on read.

## 2 · Rebuild rallies

Walk each set from 0:0. The serving team keeps serving until the score in its service-round entry is reached, and then the other team wins the next point (a sideout) and rotates. Substitutions are applied at their recorded score. Each rally gets both on-court sixes, the server and the winner.

### Rally table schema

| Column | Example | Note |
|---|---|---|
| match | M014 | |
| set | 2 | |
| rally | 37 | Number within the set |
| score_before | 17:19 | Serving team : receiving team |
| serving_team | B | |
| server | B#9 | Player at position I of the serving team |
| serving_six | 9 14 33 23 41 25 | Player IDs after step 4 |
| receiving_six | 14 8 5 13 23 7 | |
| winner | A | |
| leverage | 0.92 | Added in step 5 (see 03_model.md) |

The example values are illustrative.

## 3 · Validate

A set enters the model only if all of these hold. Otherwise it is logged and left out, so one bad parse can't distort a rating.

- The rebuilt final score equals the printed set score
- Every substitution score lies on the rebuilt score path
- At most 6 substitutions per team per set; every number is on the roster
- The number of service rounds matches the number of sideouts

## 4 · Identify players

Jersey numbers are only valid within one match. A player ID is the normalized name (Unicode NFC, case-folded, "Surname, Firstname"). The same name on another team or in another season is treated as the same person, which carries information across promotion, relegation and transfers.

- Near-matches (one letter off, double names) go to a manual review list instead of being merged silently. The list contains names, so it stays under `data/`.
- Liberos are flagged and are not rated individually (see the team term in [03_model.md](03_model.md)).
