"""Day 1 Advent submission

Find two numbers in a list which add to 2,000 and multiply them together

"""
from itertools import combinations
import numpy as np


def load_input(file):
    """Load text file into a list"""
    input_list = []
    with open(file, "r") as f:
        lines = filter(None, f.read().split("\n"))
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
    numbers = load_input("input.txt")
    target_numbers = find_numbers(numbers, n=2, target=2020)

    if isinstance(target_numbers, tuple):
        print(f"the target numbers are: {target_numbers}")
        print(f"the product of these numbers are {np.prod(target_numbers)}")
