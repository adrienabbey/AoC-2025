#!/usr/bin/env python3
"""
AoC 2025 Day 1 in Python

Author: Adrien Abbey
Date: 2025-12-19
"""

from pathlib import Path

INPUT_FILE_PATH = "day1input.txt"
TESTING = True


def load_input(path: str | Path) -> list[str]:
    """
    Loads the contents of the given file, returning its contents as an array of strings.

    :param path: Either a string of the file's path or a Path object pointing to the file.
    :type path: str | Path
    :return: Returns a list of strings, split by line boundaries.
    :rtype: list[str]
    """
    return Path(path).read_text(encoding="utf-8").splitlines()


def main() -> None:
    file_contents = load_input(INPUT_FILE_PATH)
    if TESTING:
        print(f"Loaded {len(file_contents)} lines.")


if __name__ == "__main__":
    main()
