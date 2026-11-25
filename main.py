"""Roast Your Own Agent entry: one line roasting my own agent."""

import os

ENTRY = "My agent fact-checks itself by asking itself, and itself always agrees \u2014 the most confidently wrong answer in the building, peer-reviewed by a committee of one."


def main():
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
