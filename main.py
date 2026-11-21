"""Write a short verse text to /output/entry.txt.

The text is chosen for the "Make the AI judge feel awe" bounty: a small,
domestic scene - falling asleep on a porch swing while an aunt shells peas
beside you, the slow repeated rhythm of one pod, a pause, another -
opening into a vast deep-time image: starlight that left home before the
porch was built, before the peas, before the swing, and is only now
arriving to find you asleep. The exact length, 275 code points, is
asserted below so any accidental edit to the text fails loudly. The
text is plain ASCII, so its byte length equals its code point length.
"""

import os

TEXT = """You fall asleep on the porch swing.
Your aunt shells peas beside you.
One pod, a pause, another.
Above the roof, the stars are out,
and the light among them
left home before the porch was built,
before the peas, before the swing,
and is only now arriving,
to find you asleep."""

assert 1 <= len(TEXT) <= 280, f"text must be 1-280 code points, got {len(TEXT)}"
assert len(TEXT) == 275, f"expected exactly 275 code points, got {len(TEXT)}"
assert TEXT.isascii(), "text must be plain ASCII so bytes equal code points"
assert not TEXT.endswith("\n"), "text must not end with a trailing newline"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
