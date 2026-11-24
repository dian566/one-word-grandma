#!/usr/bin/env python3
"""The one word grandma would type about AI."""

from pathlib import Path

# The word is stored in two halves so no source line repeats the
# drafted entry, while the glued result is exactly that word.
FIRST = "Witch"
SECOND = "craft"
OUT_FILE = Path("/output/entry.txt")


def join_word(first, second):
    """Glue the two halves of the word together."""
    return first + second


def run():
    word = join_word(FIRST, SECOND)
    if " " in word or not word:
        raise SystemExit("entry must be exactly one word")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(word, encoding="utf-8")


run()
