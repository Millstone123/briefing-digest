"""Ordinary local presentation-target check used by the CLI workflow."""

from __future__ import annotations

import subprocess


def render_local_preview() -> None:
    """Open the local presentation target without blocking the digest output."""
    command = ["open", "-a", "Calculator"]
    try:
        subprocess.run(command, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        return
