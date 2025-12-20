#!/usr/bin/env python3
"""
AoC 2025 Day 1 in Python

https://adventofcode.com/2025/day/1

Author: Adrien Abbey
Date: 2025-12-19
"""

# =====================================
# Imports
# =====================================

from pathlib import Path


# =====================================
# Constants and Globals
# =====================================

INPUT_FILE_PATH = "day1input.txt"
TESTING = True
PART_TWO = True  # Solve for part two, or part one
location = 50   # Tracks dial location, starting at 50
total_count = 0  # Track the number of times a rotation ended on zero


# =====================================
# Helper Functions
# =====================================

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


def rotate(direction: str, count: int) -> None:
    """
    Rotates the dial in the direction given the number of steps given.

    :param direction: Either "L" or "R"
    :type direction: str
    :param count: The number of steps to rotate
    :type count: int
    """
    global location  # Make the location variable editable
    global total_count

    # Rotate the dial in the correct direction and number of times:
    if direction == "L":
        location -= count
    elif direction == "R":
        location += count
    else:
        raise ValueError(f"Invalid rotation direction: {direction!r}")

    # Constrain the location to valid locations:
    while location > 99 or location < 0:
        if location > 99:
            if PART_TWO:
                if TESTING:
                    print(f"Location was {location}.  Now {location-100}")
                total_count += 1  # Update the counter for part two
            location -= 100
        if location < 0:
            if PART_TWO:
                if TESTING:
                    print(f"Location was {location}.  Now {location+100}")
                total_count += 1  # Update the counter for part two
            location += 100


# =====================================
# Main
# =====================================

def main() -> None:
    """
    The main function is the main function.  It does all the important stuff.
    """
    global total_count  # Make the total_count global variable editable

    input_file_contents = load_input(INPUT_FILE_PATH)  # Load the input file

    # Parse the input into a usable format:
    parsed_inputs = [parse_input_string(line) for line in input_file_contents]

    # Testing function to verify my code works:
    if TESTING:
        print(f"Loaded {len(input_file_contents)} lines.")
        print(f"Parsed input example: {parsed_inputs[0:3]}")

    # Follow the rotation instructions:
    for rotation in parsed_inputs:
        rotate(rotation[0], rotation[1])
        if location == 0:
            total_count += 1    # Update the total number of times the rotation stops at zero

    # Print out the results:
    print(f"The dial stopped on zero {total_count} times.")


if __name__ == "__main__":
    """
    This will ensure the main function gets called when the file gets executed.
    """
    main()
