# 01 · What a score sheet gives us

Source: SAMS Score sheets (PDF with a text layer), one per match.

## Recorded

- Starting six per set in rotation order I–VI, for both teams
- Substitutions with the score at the change
- **Service rounds**: the score at which each server's turn ended. These rebuild every rally in order.
- Timeouts with score, set scores, set start and end times, home and away
- Roster: number, name, captain (C), liberos, used players (X), MVP
- Officials (referees, scorer), which are not needed for the model

## Not recorded

- Who scored or lost a point: no attack, block, reception or error stats
- Libero changes
- Playing positions (setter, opposite, middle, outside)

## Consequence

The only individual signal is **the server**. Everything else is inferred from who was on court when rallies were won or lost. About 180 rallies per match make that workable, compared with about 100 possessions in a basketball game and 2–3 goals in soccer.

## Practical notes

- `pdftotext -layout` extracts a usable text layer.
- Umlauts are broken in the raw text (for example `K�kten`) and must be repaired on read.
- Substitution scores are written from the substituting team's side. This was seen on the LL4 2026/27 sheets; confirm on 2025/26.
- The data in this repo is listed in [../data/README.md](../data/README.md).
