from pathlib import Path

import pytest

from impact import config

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "impact.toml"


@pytest.fixture
def cfg():
    return config.load(CONFIG)


@pytest.fixture
def score_sheets(cfg):
    """All score-sheet PDFs from the configured sources; skips the test on a fresh clone without data."""
    pdfs = [p for src in cfg["sources"] for p in sorted(src["folder"].glob("*.pdf"))]
    if not pdfs:
        pytest.skip("no score sheets in data/ (PDFs are git-ignored; copy them in to run this test)")
    return pdfs
