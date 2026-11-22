"""Load impact.toml."""

import tomllib
from pathlib import Path

MODELS = {"auto", "team_only", "plus_minus", "rapm_sams", "rapm_positions"}


class ConfigError(Exception):
    pass


def load(path: str | Path = "impact.toml") -> dict:
    path = Path(path)
    if not path.is_file():
        raise ConfigError(f"Config file not found: {path}. Run from the project folder or pass --config.")
    with path.open("rb") as f:
        cfg = tomllib.load(f)

    # Resolve folders against the config file's location, so the CLI works from any directory.
    base = path.resolve().parent
    for key in ("derived", "positions"):
        cfg["data"][key] = base / cfg["data"][key]
    for src in cfg.get("sources", []):
        src["folder"] = base / src["folder"]

    model = cfg["model"]
    for name in [model["default"], *model.get("leagues", {}).values()]:
        if name not in MODELS:
            raise ConfigError(f"Unknown model '{name}' in {path}. Choose one of: {', '.join(sorted(MODELS))}.")
    return cfg
