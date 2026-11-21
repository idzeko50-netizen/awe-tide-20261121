"""Write a short, warm winter text to /output/entry.txt.

The text is chosen for the "Make the AI judge feel awe" bounty: a small,
domestic scene - a kettle, a fogged window, snow falling the way it has
for a hundred winters - meant to give the judge a quiet moment of awe
rather than a vast cosmic one. The repeated "soft on the roof, soft on
the road, soft on everything that was in a hurry" is the core device:
the world slowing down, inside and out. It is a single fixed string,
229 Unicode code points, inside the required 1-280 range. The text is
plain ASCII, so its byte length equals its code point length.
"""

import os

TEXT = "The kettle sings, the window fogs, and outside the snow comes down the way it has for a hundred winters, soft on the roof, soft on the road, soft on everything that was in a hurry. Inside, the lamp is lit, and the night can wait."

assert 1 <= len(TEXT) <= 280, f"text must be 1-280 code points, got {len(TEXT)}"
assert TEXT.isascii(), "text must be plain ASCII so bytes equal code points"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
