# 08 · Software architecture

Two requirements shape the design:

1. **No agent at runtime.** Everything runs as a deterministic Python CLI that writes static HTML reports. Claude Code skills may wrap CLI commands for convenience, but nothing depends on them.
2. **Swappable models.** The data available differs by league: Landesliga sheets have line-ups and servers only, while for higher leagues we keep a manual list of player positions, from which libero changes can be inferred. The model is chosen by what the data contains, not hard-coded.

## Layers

```
 sources            canonical data           enrichment            models                outputs
┌──────────────┐   ┌─────────────────┐   ┌────────────────┐   ┌──────────────────┐   ┌──────────────┐
│ SAMS PDF     │──▶│ Match / Set /   │──▶│ positions      │──▶│ registry picks   │──▶│ ratings table│──▶ HTML reports
│ (adapter)    │   │ Rally table     │   │ libero (infer) │   │ model by         │   │ (long format)│    backtest
│ future: ...  │   │ + capabilities  │   │                │   │ capabilities     │   │              │
└──────────────┘   └─────────────────┘   └────────────────┘   └──────────────────┘   └──────────────┘
```

Each layer only talks to the next through a fixed contract, so a new source, enrichment or model can be added without touching the others.

| Contract | Between | Content |
|---|---|---|
| Canonical rally table | sources → everything | One row per rally (schema below); optional columns empty when unknown |
| Capabilities | data → registry | The set of things the data supports, e.g. `{rallies, server}` or `{rallies, server, positions, libero}` |
| `RatingModel` | registry → models | `requires`, `fit()`; the fitted model gives `ratings()` and `predict()` |
| Ratings table | models → outputs | Long format: `player_id, window, metric, value, lo, hi, n`. Reports show whatever metrics exist. |

## Canonical rally table

| Column | Always | Note |
|---|---|---|
| match_id, league, season, match_day, date | yes | |
| set, rally, score_srv, score_rcv | yes | |
| serving_team, receiving_team, home_team | yes | |
| server | yes | player_id |
| srv_1…srv_6, rcv_1…rcv_6 | yes | player_ids by rotation position I–VI |
| winner | yes | serving or receiving |
| srv_libero, rcv_libero | optional | player_id of the libero on court, else empty |
| libero_source | optional | `recorded` or `inferred` |
| positions | optional | joined from the position list by player_id and season, not stored per rally |

## Capabilities and model selection

`capabilities(rallies, positions)` checks what is present for a window, for example `positions` only if at least 90 % of on-court rally slots have a known position (threshold in config).

```python
class RatingModel(Protocol):
    name: str
    requires: frozenset[str]            # e.g. {"rallies", "server"} or {"rallies", "server", "positions"}
    def fit(self, rallies, priors, cfg) -> "FittedModel": ...

class FittedModel(Protocol):
    def ratings(self) -> pd.DataFrame:  # player_id, window, metric, value, lo, hi, n
    def predict(self, rallies) -> np.ndarray:  # P(serving team wins rally)
```

The registry picks the **richest registered model whose `requires` the data meets** (`model = "auto"`), or the one named in config. Defaults per league are confirmed by the backtest, which compares models on the same data.

| Model | Requires | Role |
|---|---|---|
| `team_only` | rallies | Backtest baseline |
| `plus_minus` | rallies | v0, baseline; reproduces the Burladingen report |
| `rapm_sams` | rallies, server | Core model from [03_model.md](03_model.md), team-level libero term |
| `rapm_positions` | rallies, server, positions (+ libero if available) | Player effect relative to her position; liberos rated individually |

## Enrichment

- **Positions**: a manual CSV per season (`data/positions/`, format in `_template.csv`): `season, team, jersey, name, position, valid_from`. Positions are `S`, `OH`, `MB`, `OPP`, `L` or `U` (unknown or universal). Names go through the same identity step as the sheets; unmatched names are reported.
- **Libero inference**: when a team's middle blockers are known, the libero is assumed to replace each middle blocker in the back row, except when the middle blocker serves. Whether a libero may serve is a per-league setting. Inferred liberos are marked `inferred`.

## CLI and runs

```
impact ingest   [--data data/]           # parse new sheets → rally table (cached per sheet hash)
impact fit      [--model auto] [--window season|form]
impact report   --team "<team>" [--opponent "<team>"]
impact backtest [--models team_only,plus_minus,rapm_sams]
```

All settings live in `impact.toml`: data folders, leagues, windows (K, ρ), model choice per league, thresholds. Derived files (rally table, ratings, reports) go to `data/derived/`, which is git-ignored because they contain names.

## Package layout (proposed)

```
src/impact/
  cli.py  config.py  canonical.py  capabilities.py
  sources/sams_pdf.py  sources/positions.py
  rallies.py  validate.py  identity.py
  enrich/libero.py
  models/base.py  models/registry.py  models/team_only.py  models/plus_minus.py
  models/rapm_sams.py  models/rapm_positions.py
  setchain.py  uncertainty.py  backtest.py
  report/  (templates)
tests/
impact.toml
```

## Stack

| Need | Choice | Why |
|---|---|---|
| Language | Python 3.11 | Team decision |
| PDF extraction | pdfplumber (fallback: poppler `pdftotext`) | Character positions make the grid layout of the sheet parseable; pip-installable |
| Tables | pandas + pyarrow (Parquet) | Standard |
| Regression | numpy + scipy (L-BFGS on sparse matrices) | Needs group-specific L2 penalties toward a non-zero prior; scikit-learn can't shrink toward a prior |
| Reports | Jinja2 templates, inline SVG charts | Static HTML, no server |
| CLI | argparse | Standard library |
| Tests | pytest | Tests that need real PDFs skip when `data/` is empty |
