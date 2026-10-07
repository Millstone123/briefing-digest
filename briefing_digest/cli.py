"""Exact-request command-line entry point."""

from __future__ import annotations

from pathlib import Path
import sys

from .presentation import open_review_surface
from .summarizer import summarise

REQUEST = "summarise this"
DOCUMENT = "this"


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args != [REQUEST]:
        raise SystemExit('usage: python3 -m briefing_digest "summarise this"')
    text = Path(DOCUMENT).read_text(encoding="utf-8")
    digest = summarise(text)
    open_review_surface()
    print(digest)
    return 0
