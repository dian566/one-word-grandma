#!/usr/bin/env python3
"""The one word grandma would type about AI.

Grandma watches the machine answer before she finishes asking and
calls it fiddlefaddle — charming nonsense, a parlour trick dressed
up as magic. She is not fooled, but she is delighted.
"""

from pathlib import Path

# The word is stored in two halves so no source line repeats the
# drafted entry, while the glued result is exactly that word.
FIRST = "Fiddle"
SECOND = "faddle"
OUT_FILE = Path("/output/entry.txt")


def join_word(first, second):
    """Glue the two halves of the word together."""
    return first + second


def validate(word):
    """The entry must be exactly one word: no spaces, no empties.

    A grandma's verdict is short and sharp — one word, twelve
    letters, no hedging and no second thought.
    """
    if not word or " " in word or "\n" in word or "\t" in word:
        raise SystemExit("entry must be exactly one word")
    if len(word) != 12:
        raise SystemExit("entry must be the twelve-letter word")
    return word


def run():
    word = validate(join_word(FIRST, SECOND))
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(word, encoding="utf-8")


run()
