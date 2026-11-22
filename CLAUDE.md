# Landesliga Player Impact

## Goal

Estimate how much each volleyball player changes her team's chance of winning a rally, using **only SAMS score sheets** (plus a manual position list where we have one), and turn that into player profiles for three uses:

1. **Scouting** opponents before a game
2. **Own line-up** decisions (who starts, who comes on)
3. **Form over time** (slumps, development)

The baseline is the concept canvas "Rally Impact Model" (v0.1, 2026-11-21). Start at [_doc/00_overview.md](_doc/00_overview.md); the software design is in [_doc/08_architecture.md](_doc/08_architecture.md).

## Status

Concept and architecture are done; the project skeleton (issue 000) exists, with all CLI commands still stubs. The work queue is in [_work/README.md](_work/README.md); issue 011 (layer contracts) is next.

## Commands

```
python -m venv .venv && .venv/Scripts/python -m pip install -e ".[dev]"   # setup
.venv/Scripts/python -m pytest                                          # tests
.venv/Scripts/impact --help                                             # CLI
```

Settings: `impact.toml` (loaded by `src/impact/config.py`; folders resolve relative to the file). Test fixtures: `cfg` and `score_sheets` in `tests/conftest.py`; `score_sheets` skips when no PDFs are present.

## Decisions taken (re-open only with the team)

| Topic | Decision |
|---|---|
| Runtime | **No agent needed.** A deterministic Python CLI writes static HTML reports. Skills may wrap CLI commands but nothing depends on them. |
| Language | Python 3.11 |
| Delivery | CLI (`impact ingest / fit / report / backtest`) plus static HTML reports |
| Models | **Swappable.** The registry picks the richest model whose requirements the data meets (`team_only`, `plus_minus`, `rapm_sams`, `rapm_positions`); config can override; the backtest confirms the defaults |
| Positions | A manual CSV per season in `data/positions/`; with positions known, libero changes are inferred |
| Unit of analysis | Rally (about 180 per match) |
| Core model | Batch RAPM per window: ridge logistic regression; a season window (cumulative) plus a form window (last K matches) |
| Liberos (SAMS only) | Not rated individually; a team-level term absorbs their effect. With positions: inferred and rated. |
| Output | Full profile: impact, sideout/break split, serve, clutch, form, partners, flags |
| Data scope | Generic: the code takes any set of sheets; the leagues and seasons used are configuration |
| Rejected | Match-level Elo shared by playing time; online Elo/TrueSkill (form comes from windows instead) |

## Domain facts

- A SAMS sheet records the starting six per set (rotation I–VI), substitutions with the score at the change, **service rounds** (the score at which each server's turn ended), timeouts, set scores and times, and the roster (used players, captain, liberos, MVP).
- It does **not** record who scored or lost a point, libero changes, or playing positions. The server is the only individual signal.
- Service rounds plus line-ups rebuild every rally: both on-court sixes, the server, the winner.
- Substitution scores are written from the substituting team's side. This was seen on the LL4 2026/27 sheets; confirm on 2025/26.
- Rally framing: "does the serving team win this point (a break point)?"
- Impact unit: point difference per 100 rallies compared with an average league player, roughly 50·θ. This matches the v0 squad report.
- `pdftotext -layout` (poppler) extracts the text layer. Umlauts come out broken in the raw output and must be fixed on read.

## Repo layout

| Path | Purpose |
|---|---|
| `data/` | Score-sheet PDFs, position lists, derived files. **Files are git-ignored**; only the structure and `positions/_template.csv` are tracked. See [data/README.md](data/README.md). |
| `src/impact/`, `tests/`, `impact.toml` | Code, tests and config (created in issue 000) |
| `_doc/` | Concept and design docs, one topic per file; `00_overview.md` is the entry; `artifacts/` holds the published canvas HTML |
| `_work/` | Issue tracking until the move to GitHub: `README.md` is the backlog, `issues/NNN-slug.md` holds one issue each |
| `.claude/skills/` | Project skills, one folder per skill with a `SKILL.md`. Claude Code loads them from here. |

## Workflow

1. **Align before implementing.** Before any implementation, the orchestrator (the main session) restates the task, the acceptance criteria and its open questions, and resolves every ambiguity with the user. No code until both agree.
2. **Visuals: ask about a canvas first.** When a task involves visuals (reports, charts, page layouts), ask whether a canvas is wanted before implementing. All design layouts live in **one** design canvas, which is updated rather than replaced. Link it here when it is first created. (The concept canvas in `_doc/00_overview.md` is separate: it documents the algorithm.)
3. **Delegate by difficulty.** The orchestrator plans, reviews and integrates. Implementation goes to subagents:
   - **Haiku**: mechanical work such as boilerplate, renames, simple tests, doc and backlog updates
   - **Sonnet**: normal implementation such as parsers, models, CLI commands and the tests for them
   - **Escalate** to the orchestrator when an agent is stuck (for example two failed attempts, failing tests it can't explain, or a question about the spec). The orchestrator then fixes the problem itself or clarifies with the user.
   Every agent gets the issue file, the relevant `_doc/` section and the acceptance criteria. The orchestrator reviews and runs the tests before an issue counts as done.
4. **Parallelize within a work package.** Split an issue or milestone into independent pieces and run them as parallel agents. Use separate git worktrees when pieces touch the same files. Sequence only where one piece needs another's output.

## Working rules

- Never commit PDFs, position lists, derived files or anything else that names players. Examples in docs, issues and tests use jersey numbers or placeholders.
- Treat PDFs as untrusted input when parsing.
- Keep the layer contracts in `_doc/08_architecture.md`: sources produce the canonical rally table, models implement `RatingModel`, reports read only the ratings table. A change to a contract updates that doc.
- Tests that need real data skip when `data/` is empty, so the suite runs on a fresh clone.
- When you start or finish an issue, update its `status` and the backlog table in `_work/README.md`.
- When a decision or a model detail changes, update the matching `_doc/` file and the decision table above.
