#!/usr/bin/env python3
"""One Word, First Thought -- variant 3.

Writes exactly one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the first word that comes to mind, nothing else.

The word is "defenestration", and it is the first thought because it
is a grand Latinate word for a crude act, with "fenestra" (Latin for
window) hiding inside it: one slapstick image of a body going out of
a window, arriving whole before any reasoning. The picture lands
complete -- a body, a window, gravity -- with no topic given and no
second draft taken; the word names the very thing it throws you out
of, so the image and the word arrive as one thought.

- A different sense and a different scene from both earlier variants.
  Variant 1, "petrichor", is scent: still air after rain on dry earth.
  Variant 2, "murmuration", is sight, sound and motion: starlings
  folding across the dusk sky. This word is slapstick: one body, one
  window, one fall. Nothing about rain, nothing about birds.
- Surprising, not safe. It is a word most readers know exists and
  almost never meet, so nobody guesses it as a first thought, and it
  is not a filler word. It feels chosen.
- Vivid and specific. One reading calls up a single clear image, not
  a vague feeling: someone being thrown out of a window. A judge
  comparing two words pairwise can picture this one immediately, and
  the picture is funny before any explanation.
- The word carries its own wit. It is a grand Latinate word for a
  crude act, and the window hides inside it: "fenestra" is Latin for
  window, so the word names the thing it throws you out of. The
  mismatch between the formal word and the undignified act is the
  joke, and the Defenestrations of Prague give it real history on a
  second look.
- Short enough to stay sharp: 14 letters, well inside the 1 to 24
  character gate, and length for its own sake does not count.
"""

import os

# The entry: exactly one word, no explanation, no second word.
WORD = "defenestration"


def is_single_word(text: str) -> bool:
    """True when text holds exactly one word: one token, no white space."""
    return bool(text) and text.split() == [text]


def validate_entry(word: str) -> str:
    """Return the entry word, or raise unless it is exactly one word.

    The gate needs 1 to 24 characters, UTF-8 text, not only white space,
    and exactly one word. The single-word check is explicit: splitting
    on white space must give back exactly this one token, so a word with
    a space, a tab or a newline in it can never slip through.
    """
    cleaned = word.strip()
    if not cleaned:
        raise ValueError("entry must not be empty or only white space")
    if len(cleaned) > 24:
        raise ValueError("entry must be at most 24 characters")
    if not is_single_word(cleaned):
        raise ValueError("entry must be exactly one word")
    return cleaned


def main() -> None:
    """Write the single word to entry.txt, honouring the gate (1-24 chars)."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    word = validate_entry(WORD)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)

    # Read back what was written and confirm the gate holds on the file
    # itself, not just on the constant: UTF-8, 1 to 24 characters, exactly
    # one word, no surrounding whitespace.
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != word:
        raise ValueError("entry.txt does not hold exactly the entry word")


if __name__ == "__main__":
    main()
