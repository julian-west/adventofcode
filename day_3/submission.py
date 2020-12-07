"""
https://adventofcode.com/2020/day/3

- need to keep track of the modulus of the index to know where in the pattern
we are
- recursion?
- counter to count number of trees found
"""

import numpy as np


def load_input(file):
    """loads input into a list of lists"""

    with open(file, "r") as f:
        lines = f.read().splitlines()

    matrix = [list(line) for line in lines]
    return matrix


def count_trees(matrix, right, down):
    """Traverses the matrix according to the rule (right, down)"""
    pattern_len = len(matrix[0])

    trees = 0
    index = 0
    row = 0
    while row < len(matrix):
        if matrix[row][index] == "#":
            trees += 1
        index = (index + right) % pattern_len
        row += down
    return trees


if __name__ == "__main__":
    input_matrix = load_input("input.txt")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = []

    for (right, down) in slopes:
        trees = count_trees(input_matrix, right, down)
        results.append(trees)

    prod = np.prod(results)
    print(results)
    print(prod)
