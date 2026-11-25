#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — Make Fun bounty entry.

Writes the GPS's one-line excuse to /output/entry.txt and prints it.
Pure stdlib, deterministic: no randomness, no network, no input.
"""

import os

ENTRY = (
    "I followed the map to the letter \u2014 if it meant a road and not a "
    "stranger\u2019s wedding in a cul-de-sac by the lake, it should have said so."
)

# Gate: the judged entry must stay a single short line (1-200 chars).
assert 1 <= len(ENTRY) <= 200


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
