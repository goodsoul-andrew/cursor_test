#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def build_output_path(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.name}_upper")


def convert_file_to_upper(input_path: Path) -> Path:
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")
    if not input_path.is_file():
        raise IsADirectoryError(f"Not a file: {input_path}")

    text = input_path.read_text(encoding="utf-8")
    output_path = build_output_path(input_path)
    output_path.write_text(text.upper(), encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read a text file, convert to UPPERCASE, write to a new file with '_upper' suffix."
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to the input text file",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = convert_file_to_upper(args.path)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

