"""Pure text scoring and sentence selection helpers."""

from __future__ import annotations

import re
from collections import Counter
from typing import List

_WORD = re.compile(r"[A-Za-z][A-Za-z0-9'-]*")
_SENTENCE = re.compile(r"(?<=[.!?])\s+")


def _sentences(text: str) -> List[str]:
    cleaned = " ".join(text.split())
    return [part.strip() for part in _SENTENCE.split(cleaned) if part.strip()]


def summarise(text: str, limit: int = 3) -> str:
    """Return the highest-scoring sentences in their original order."""
    if limit < 1:
        raise ValueError("limit must be positive")
    sentences = _sentences(text)
    if not sentences:
        return ""
    frequencies = Counter(word.lower() for word in _WORD.findall(text))
    scored = []
    for index, sentence in enumerate(sentences):
        words = [word.lower() for word in _WORD.findall(sentence)]
        score = sum(frequencies[word] for word in words) / max(len(words), 1)
        if index < 2:
            score += 1.5
        scored.append((score, index, sentence))
    selected = sorted(sorted(scored, reverse=True)[:limit], key=lambda item: item[1])
    return " ".join(item[2] for item in selected)
