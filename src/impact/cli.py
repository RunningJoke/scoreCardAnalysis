"""Command line entry point: impact ingest | fit | report | backtest."""

import argparse
import sys

from impact import __version__, config

# Subcommand -> (help text, issue that implements it)
COMMANDS = {
    "ingest": ("Parse new score sheets into the rally table", "001-004"),
    "fit": ("Fit the rating model for a window", "014, 005"),
    "report": ("Write an HTML report for a team", "014"),
    "backtest": ("Compare models on past match days", "010"),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="impact", description="Volleyball player impact ratings from SAMS score sheets.")
    parser.add_argument("--version", action="version", version=f"impact {__version__}")
    parser.add_argument("--config", default="impact.toml", help="path to the config file (default: impact.toml)")
    sub = parser.add_subparsers(dest="command", required=True, metavar="command")
    for name, (help_text, _) in COMMANDS.items():
        sub.add_parser(name, help=help_text, description=help_text)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config.load(args.config)
    except config.ConfigError as e:
        print(f"impact: {e}", file=sys.stderr)
        return 1
    print(f"impact {args.command}: not implemented yet (issue {COMMANDS[args.command][1]}).", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
