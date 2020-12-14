""" Day 14 adventofcode """

from typing import List, Tuple
import re
from itertools import product


def load_input(file: str) -> List[Tuple[str, int, int]]:
    """Load input into list of tuples

    [(mark, address, target number),(....)]
    """
    with open(file, "r") as input_file:
        raw = input_file.read()

    mask_sequences = [series.split("\n") for series in raw.split("mask")]

    processed_input = []
    for sequence in mask_sequences:
        mask = sequence[0][3:]
        for mem_instruction in sequence[1:-1]:
            match = re.match(r"mem\[(\d+)\]\s=\s(\d+)", mem_instruction)
            processed_input.append((mask, int(match.group(1)), int(match.group(2))))

    return processed_input


def apply_mask(mask: str, binary: str) -> str:
    """Apply mask to a binary string"""
    return "".join(y if x == "X" else x for x, y in zip(mask, binary))


def part1(mask_sequences: List[Tuple[str, int, int]]) -> int:
    """Takes a list of sequences, applies mask and saves new number in a Dict

    Returns the sum of all numbers in the Dict
    """
    mem_storage = {}
    for (mask, addr, num) in mask_sequences:
        binary = "{:036b}".format(num)
        new_binary = apply_mask(mask=mask, binary=binary)
        mem_storage[addr] = int(new_binary, 2)

    return sum(mem_storage.values())


def part2(mask_sequences: List[Tuple[str, int, int]]) -> int:
    """Part 2
    bitwise operators: https://wiki.python.org/moin/BitwiseOperators
    """
    mem_storage = {}
    for (mask, addr, num) in mask_sequences:
        mask_to_1 = int("".join(m if m == "1" else "0" for m in mask), 2)
        float_positions = [i for i, x in enumerate(reversed(mask)) if x == "X"]
        addr = addr | mask_to_1

        for bits in product((0, 1), repeat=len(float_positions)):
            mask_toggle = 0
            for b, i in zip(bits, float_positions):
                mask_toggle = mask_toggle ^ (b << i)
            mem_storage[addr ^ mask_toggle] = num

    return sum(mem_storage.values())


if __name__ == "__main__":
    mask_instructions = load_input("input.txt")

    # Part 1
    print(part1(mask_instructions))

    # Part 2
    print(part2(mask_instructions))
