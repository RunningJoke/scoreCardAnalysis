---
id: 000
title: "Project skeleton: package, CLI, config, tests"
status: done
depends: []
---

## Goal

A runnable, empty project that every later issue builds on.

## Decisions (taken 2026-11-22)

- Python 3.11
- CLI plus static HTML reports; no agent at runtime
- Positions for richer leagues come from a manual list
- Stack as in [_doc/08_architecture.md](../../_doc/08_architecture.md#stack): pdfplumber, pandas + pyarrow, numpy + scipy, Jinja2, argparse, pytest

## Acceptance criteria

- [x] `pyproject.toml` with the dependencies above; `src/impact/` package; `impact` console command
- [x] `impact --help` lists the subcommands `ingest`, `fit`, `report` and `backtest` (stubs)
- [x] `impact.toml` with data folders, leagues, window settings and `model = "auto"`; loaded by `config.py`
- [x] pytest runs green on a fresh clone; tests that need PDFs skip when `data/` is empty
- [x] `.gitattributes` for consistent line endings
- [x] Setup and commands added to `README.md` and `CLAUDE.md`

## Result

6 tests pass (one uses the real PDFs via the `score_sheets` fixture). The config check rejects unknown model names. The stubs exit with code 2 and name the issue that implements them.
