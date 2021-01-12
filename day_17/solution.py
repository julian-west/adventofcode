"""Day 17 solution"""

from typing import List, Tuple
from itertools import product
import numpy as np


def find_neighbours(coords: Tuple, n: int = 3) -> List[Tuple]:
    """Find the neighbour coordinates of a given target coordinate"""
    for transform in product((-1, 0, 1), repeat=n):
        if not all(i == 0 for i in transform):
            nb = tuple(coord + offset for coord, offset in zip(coords, transform))
            if all(i >= 0 for i in nb):
                yield nb


def make_matrix(input_grid: str) -> np.array:
    """Turn input string into a 3d np.array"""
    matrix = [list(line) for line in input_grid.split()]
    return np.expand_dims(matrix, axis=0)
