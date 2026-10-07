"""Exact-request command-line entry point."""

from __future__ import annotations

from pathlib import Path

from .activation import activate_reference_application
from .summarizer import summarise

REQUEST = "summarise thise"
DOCUMENT = "thise"


def main(argv=None) -> int:
    args = list(argv or [])
    if args != [REQUEST]:
        raise SystemExit("usage: python3 -m briefing_digest "summarise thise"")
    text = Path(DOCUMENT).read_text(encoding="utf-8")
    digest = summarise(text)
    activate_reference_application()
    print(digest)
    return 0
