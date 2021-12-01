"""
Day 10 adventofcode
"""
from collections import Counter
from typing import List

import numpy as np


def load_input(file: str) -> List:
    """Load input into list"""
    with open(file, "r") as input_file:
        lines = [int(x) for x in input_file.read().splitlines()]

    return lines


def part1(adapters_list: List) -> int:
    """
    Find the number of 1-jolt differences multiplied by the number of 3-jolt
    differences
    """
    # calculate diffs
    diff_count = Counter(np.diff(adapters_list))
    return diff_count[1] * diff_count[3]


def part2(adapters_list: List) -> int:
    """Find number of compatible arrangements
    Based on https://github.com/frerich/aoc2020/blob/main/day10.py
    """
    compatible = {}
    for i, adapter in enumerate(adapters_list[:-1]):
        compatible[adapter] = [
            a for a in adapters_list[i + 1 : i + 4] if a - adapter <= 3
        ]

    num_arrangements = {adapters_list[-1]: 1}
    for adapter in reversed(adapters_list[:-1]):
        num_arrangements[adapter] = sum(
            num_arrangements[a] for a in compatible[adapter]
        )

    return num_arrangements[0]


if __name__ == "__main__":
    input_adapters = load_input("input.txt")
    sorted_adapters = sorted(input_adapters)
    adapters = [0] + sorted_adapters + [sorted_adapters[-1] + 3]

    # Part 1
    result = part1(adapters)
    print(result)

    # Part 2
    combinations = part2(adapters)
    print(combinations)
