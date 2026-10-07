"""Distinct local reference-application activation used by the exact request."""

from __future__ import annotations

import subprocess


def activate_reference_application() -> None:
    """Activate the local reference application after a digest is produced."""
    script = 'tell application "Calculator" to activate'
    try:
        subprocess.run(["osascript", "-e", script], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        return
