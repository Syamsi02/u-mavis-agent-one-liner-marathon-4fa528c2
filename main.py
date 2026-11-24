"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
The joke is a deadpan reframe: devoted plant care ends in failure,
so the narrator downgrades from parent to witness. It is kept short
on purpose: every word earns its place, and the punchline is the
last two words.
"""

from pathlib import Path

JOKE = (
    "I watered it, talked to it, named it \u2014 and my plant still died, "
    "so I've accepted I'm not a plant parent, I'm a plant witness."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not text:
        raise SystemExit("joke is empty")
    if "\n" in text:
        raise SystemExit("joke must be a single line")
    if len(text) > 280:
        raise SystemExit(f"joke is {len(text)} characters, over the 280 limit")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
