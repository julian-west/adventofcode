"""Day 1 Advent submission

Find two numbers in a list which add to 2,000 and multiply them together

"""
from itertools import combinations

import numpy as np


def load_input(file):
    """Load text file into a list"""

    with open(file, "r") as input_file:
        lines = filter(None, input_file.read().split("\n"))
        numbers = [int(line) for line in lines]
    return numbers


def find_numbers(numbers, n=3, target=2020):
    """Finds 'n' numbers which sum to the target"""
    combs = combinations(numbers, n)
    for comb in combs:
        if sum(comb) == target:
            return comb
    return "No combinations found"


if __name__ == "__main__":
    input_list = load_input("input.txt")

    # Part 1
    target_numbers = find_numbers(input_list, n=2, target=2020)
    print(target_numbers, np.prod(target_numbers))

    # Part 2
    target_numbers = find_numbers(input_list, n=3, target=2020)
    print(target_numbers, np.prod(target_numbers))
