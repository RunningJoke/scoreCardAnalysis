import pytest

from conftest import CONFIG
from impact import cli, config


def test_help_lists_subcommands(capsys):
    with pytest.raises(SystemExit) as exit_info:
        cli.main(["--help"])
    assert exit_info.value.code == 0
    out = capsys.readouterr().out
    for name in ("ingest", "fit", "report", "backtest"):
        assert name in out


def test_stub_command_reports_not_implemented(capsys):
    assert cli.main(["--config", str(CONFIG), "fit"]) == 2
    assert "not implemented yet" in capsys.readouterr().err


def test_missing_config_is_a_clear_error(capsys, tmp_path):
    assert cli.main(["--config", str(tmp_path / "nope.toml"), "fit"]) == 1
    assert "Config file not found" in capsys.readouterr().err


def test_config_loads_and_resolves_paths(cfg):
    assert cfg["model"]["default"] == "auto"
    assert all(src["folder"].is_absolute() for src in cfg["sources"])


def test_unknown_model_is_rejected(tmp_path):
    bad = tmp_path / "impact.toml"
    bad.write_text('[data]\nderived="d"\npositions="p"\n[model]\ndefault="elo"\n', encoding="utf-8")
    with pytest.raises(config.ConfigError, match="Unknown model 'elo'"):
        config.load(bad)


def test_score_sheets_are_found(score_sheets):
    assert all(p.suffix == ".pdf" for p in score_sheets)
