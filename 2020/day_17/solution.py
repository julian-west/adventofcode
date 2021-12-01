"""Day 17 solution"""

from itertools import product
from typing import Iterable, Tuple

import numpy as np
from tqdm import tqdm


def find_neighbours(coords: Tuple, matrix_shape: Tuple) -> Iterable:
    """Find the neighbour coordinates of a given target coordinate"""
    for transform in product((-1, 0, 1), repeat=len(matrix_shape)):
        if not all(i == 0 for i in transform):
            nb = tuple(coord + offset for coord, offset in zip(coords, transform))
            if all(i >= 0 for i in nb) and all(i < s for i, s in zip(nb, matrix_shape)):
                yield nb


def make_matrix(input_grid: str, extra_dims: Tuple) -> np.array:
    """Turn input string into a N dimensional np.array"""
    matrix = np.expand_dims([list(row) for row in input_grid.split()], axis=extra_dims)
    enc_matrix = (matrix == "#").astype(np.int)
    return enc_matrix


def run_iteration(enc_matrix: np.array) -> np.array:
    """Run an iteration and return new matrix"""
    pad_matrix = np.pad(enc_matrix, 1)
    new_matrix = pad_matrix.copy()

    for coord, value in np.ndenumerate(pad_matrix):
        neighbours = find_neighbours(coord, pad_matrix.shape)
        neighbours_sum = sum([pad_matrix[nb] for nb in neighbours])

        if value == 1:
            if neighbours_sum not in [2, 3]:
                new_matrix[coord] = 0
        else:
            if neighbours_sum == 3:
                new_matrix[coord] = 1

    return new_matrix


def run_simulation(input_grid: str, iterations: int, extra_dims: Tuple) -> int:
    """Return number of active cubes after a number of iterations"""
    matrix = make_matrix(input_grid, extra_dims)
    for _ in tqdm(range(iterations)):
        matrix = run_iteration(matrix)
    return np.sum(matrix)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        input_str = input_file.read()

    # Part 1
    print(run_simulation(input_str, iterations=6, extra_dims=(0,)))

    # Part 2
    print(run_simulation(input_str, iterations=6, extra_dims=(0, 1)))
