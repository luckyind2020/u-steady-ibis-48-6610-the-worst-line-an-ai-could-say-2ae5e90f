"""The Worst Line an AI Could Say -- make.fun entry.

Reads the single pickup line from entry.txt next to this file and writes
it to /output/entry.txt for the grader's gate scorer.
"""

from pathlib import Path

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")


def normalize(line: str) -> str:
    """Collapse runs of whitespace inside the line to single spaces."""
    return " ".join(line.split())


def read_line(source: Path) -> str:
    raw = source.read_text(encoding="utf-8")
    lines = [line for line in raw.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError(
            f"entry.txt must hold exactly one non-empty line, found {len(lines)}"
        )
    return normalize(lines[0])


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry line holds a control character")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars, over the {MAX_CHARS} limit"
        )


def main() -> None:
    line = read_line(Path(__file__).with_name("entry.txt"))
    validate(line)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
