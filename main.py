"""One Sentence, One Front Page: write today's world-news headline to /output/entry.txt."""
import os

HEADLINE = (
    "UN's COP31 climate summit collapses in Antalya without a deal for the first time since 2009 "
    "as oil states block any pledge to phase out fossil fuels"
)

MAX_CHARS = 200


def main() -> None:
    text = " ".join(HEADLINE.split())
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"headline is {len(text)} characters; must be 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
