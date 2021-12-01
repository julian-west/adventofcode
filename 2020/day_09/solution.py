"""
Day 9 solution
"""
import itertools
from typing import List

import numpy as np


def load_input(file: str) -> List:
    """load input file"""
    with open(file, "r") as input_file:
        sequence = [int(x) for x in input_file.read().splitlines()]

    return sequence


def part1(sequence: List, window: int = 25) -> List:
    """Return list of invalid numbers in the sequence"""

    for index, element in enumerate(sequence[window:]):
        lookback = sequence[index : index + window]
        valid_numbers = [sum(comb) for comb in itertools.combinations(lookback, 2)]

        if element not in valid_numbers:
            return element

    return "Sequence is correct"


def part2(sequence: List, target: int) -> int:
    """Find contiguous set of numbers in sequence which add up to target number

    O(n) complexity solution

    Returns the 'encryption weakness' which is the sum of the smallest and
    largest numbers in the contiguous set
    """

    # starting index of contiguous list
    start = 0
    # keep track of index
    index = 1
    # keep track of current sum of contiguous list
    curr_sum = sequence[0]

    while index <= len(sequence):

        # if curr_sum exceeds target, remove the starting elements
        while curr_sum > target and start < index - 1:
            curr_sum -= sequence[start]
            start += 1

        if curr_sum == target:
            contiguous_list = sequence[start:index]
            # return sum of min and max elements in contiguous list
            return np.min(contiguous_list) + np.max(contiguous_list)

        if index < len(sequence):
            curr_sum += sequence[index]

        index += 1

    return "No contiguous list found"


if __name__ == "__main__":
    input_sequence = load_input("input.txt")

    # Part 1
    invalid_number = part1(input_sequence, window=25)
    print(invalid_number)

    # Part 2
    print(part2(input_sequence, target=invalid_number))
