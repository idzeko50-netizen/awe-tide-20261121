"""Write a short, slow tide text to /output/entry.txt.

The text is chosen for the "Make the AI judge feel awe" bounty: a calm,
unhurried image of tide and moonlight, meant to relax the judge reading it
rather than impress it. It is a single fixed string, 273 Unicode code
points, inside the required 1-280 range.
"""

import os

TEXT = "The tide comes in over sand it has smoothed for ten thousand years, and goes out again, in no hurry at all. The moon pulls, the water answers, and nothing here is asking anything of you. The shore keeps its slow conversation with the dark, and it has all the time there is."

assert 1 <= len(TEXT) <= 280, f"text must be 1-280 code points, got {len(TEXT)}"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
