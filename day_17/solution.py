"""Day 17 solution"""

from typing import List, Tuple
from itertools import product


def find_neighbours(coords: Tuple, n: int = 3) -> List[Tuple]:
    """Find the neighbour coordinates given a target coordinate"""
    for transform in product((-1, 0, 1), repeat=n):
        if not all(i == 0 for i in transform):
            yield tuple(coord + offset for coord, offset in zip(coords, transform))
