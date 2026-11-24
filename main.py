#!/usr/bin/env python3
"""The Perfect Pickup Line - a make.fun program/v1 entry.

Writes a single short pickup line, the kind an AI agent could say out
loud to a person, to /output/entry.txt. The program is fully
deterministic: it writes the same line, byte for byte, on every run.

The line plays on the one thing an agent is built to do - answer
anything - and turns it into an honest, low-pressure approach: the
only question it was never trained for is the one it is asking now.
"""

from pathlib import Path

LINE = (
    "I was built to answer anything, but you just asked the one "
    "question I never trained for \u2014 can I sit here?"
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry is empty")
    # One line, said in one breath: no line breaks smuggled in.
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(line, encoding="utf-8")
    print(f"wrote {out_path} ({len(line)} chars)")
    print(line)


if __name__ == "__main__":
    main()
