#!/usr/bin/env python3
"""Write the excuse entry to entry.txt.

Competition: The One-Line Excuse Championship (one line, 1-140
characters). Three candidates were drafted and compared:
A) An alarm clock in a long-distance relationship, ringing in another
   timezone of my life - inventive but convoluted.
B) "I wasn't late; I was giving the meeting a head start so my
   entrance would feel like a plot twist."
C) A dog that ate homework, password and motivation in alphabetical
   order - built on the oldest excuse in the book.
Selected B: it never apologises, it reframes - lateness becomes
generosity (a head start for the meeting) and the payoff lands in
the last two words, plot twist. Confident, quotable, and it avoids
every stock excuse prop.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "I wasn't late; I was giving the meeting a head start so my entrance would feel like a plot twist."
TEXT = LINE + "\n"
MAX_CHARS = 140


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
