""" Day 14 adventofcode """

from typing import List, Tuple
import re


def load_input(file: str) -> List[Tuple[str, int, int]]:
    """Load input into list of tuples

    [(mark, mem location, target number),(....)]
    """
    with open(file, "r") as input_file:
        raw = input_file.read()

    mask_sequences = [series.split("\n") for series in raw.split("mask")]

    processed_input = []
    for sequence in mask_sequences:
        mask = sequence[0][3:]
        for mem_instruction in sequence[1:-1]:
            mem_allocation, number = re.match(
                r"mem\[(\d+)\]\s=\s(\d+)", mem_instruction
            ).groups()

            processed_input.append((mask, int(mem_allocation), int(number)))

    return processed_input


def apply_mask(mask: str, binary: str) -> str:
    """Apply mask to a binary string"""
    return "".join(y if x == "X" else x for x, y in zip(mask, binary))


def part1(mask_sequences: List[Tuple[str, int, int]]) -> int:
    """Takes a list of sequences, applies mask and saves new number in a Dict

    Returns the sum of all numbers in the Dict
    """

    mem_storage = {}
    for instruction in mask_sequences:
        binary = "{:036b}".format(instruction[2])
        new_binary = apply_mask(mask=instruction[0], binary=binary)
        mem_storage[instruction[1]] = int(new_binary, 2)

    return sum(mem_storage.values())


if __name__ == "__main__":
    mask_instructions = load_input("input.txt")

    # Part 1
    print(part1(mask_instructions))

    # Part 2
