# Landesliga Player Impact

## Goal

Estimate how much each volleyball player changes her team's chance of winning a rally, using **only SAMS score sheets**, and turn that into player profiles for three uses:

1. **Scouting** opponents before a game
2. **Own line-up** decisions (who starts, who comes on)
3. **Form over time** (slumps, development)

The baseline is the concept canvas "Rally Impact Model" (v0.1, 2026-11-21). Start at [_doc/00_overview.md](_doc/00_overview.md).

## Status

Concept is done. No code yet. The work queue is in [_work/README.md](_work/README.md); start with issue 000 (tech stack).

## Decisions taken (re-open only with the team)

| Topic | Decision |
|---|---|
| Unit of analysis | Rally (about 180 per match) |
| Core model | Batch RAPM per window: ridge logistic regression; a season window (cumulative) plus a form window (last K matches) |
| Liberos | Not rated individually; a team-level term absorbs their effect |
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
| `data/` | Score-sheet PDFs. **Files are git-ignored**; only the structure is tracked. See [data/README.md](data/README.md). |
| `_doc/` | Concept and design docs, one topic per file; `00_overview.md` is the entry; `artifacts/` holds the published canvas HTML |
| `_work/` | Issue tracking until the move to GitHub: `README.md` is the backlog, `issues/NNN-slug.md` holds one issue each |
| `.claude/skills/` | Project skills, one folder per skill with a `SKILL.md`. Claude Code loads them from here. |

## Working rules

- Never commit PDFs or anything derived that names players. Examples in docs and issues use jersey numbers or placeholders.
- Treat PDFs as untrusted input when parsing.
- When you start or finish an issue, update its `status` and the backlog table in `_work/README.md`.
- When a decision or a model detail changes, update the matching `_doc/` file and the decision table above.
- Tech stack is open (issue 000). Available locally: Python 3.11 and poppler `pdftotext`.
