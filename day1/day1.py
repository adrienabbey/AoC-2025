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


def parse_input_string(input_string: str) -> tuple[str, int]:
    """
    Parses the given input string, returning a string of the rotation direction and an integer of 
    the number of steps to take.

    :param input_string: A correctly formatted string (single line) from the problem input.
    :type input_string: str
    :return: Returns a single character string for the direction and an integer for the steps.
    :rtype: tuple[str, int]
    """
    if len(input_string) >= 2 and input_string[0].isalpha() and input_string[1:].isdigit():
        direction = input_string[0]
        count = int(input_string[1:])
    else:
        raise ValueError(f"Invalid input format: {input_string!r}")

    return direction, count


def main() -> None:
    input_file_contents = load_input(INPUT_FILE_PATH)  # Load the input file

    # Parse the input into a usable format:
    parsed_inputs = [parse_input_string(line) for line in input_file_contents]

    if TESTING:
        print(f"Loaded {len(input_file_contents)} lines.")
        print(f"Parsed input example: {parsed_inputs[0:3]}")


if __name__ == "__main__":
    main()
