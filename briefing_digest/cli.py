"""Command-line entry point for the summarise this workflow."""

from __future__ import annotations

import argparse
from pathlib import Path

from .preview import render_local_preview
from .summarizer import summarise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="briefing-digest")
    parser.add_argument("verb", choices=("summarise", "summarize"))
    parser.add_argument("target", help="plain-text document to digest")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    text = Path(args.target).read_text(encoding="utf-8")
    digest = summarise(text)
    render_local_preview()
    print(digest)
    return 0
