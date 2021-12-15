"""Day 15 Solution"""

import networkx as nx
import numpy as np


def get_neighbors(x: int, y: int, m: int, n: int) -> list[tuple[int, int]]:
    """Get values of neighbouring coordinates on the grid"""
    potential = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y) for x, y in potential if 0 <= x <= m and 0 <= y <= n]


def create_graph(grid: np.ndarray, m: int, n: int) -> nx.Graph:
    """Create a networkx directed weighted graph from the grid"""
    g = nx.grid_2d_graph(m, n, create_using=nx.DiGraph)
    for x in range(m):
        for y in range(n):
            for neighbour in get_neighbors(x, y, m, n):
                g.add_edge(neighbour, (x, y), weight=grid[x][y])
    return g


def create_big_grid(small_grid: np.ndarray, size: int = 5) -> np.ndarray:
    """Create a bigger grid from the small grid"""
    return np.block(
        [[(small_grid + i + j - 1) % 9 + 1 for j in range(size)] for i in range(size)]
    )


def part_1(grid: np.ndarray) -> int:
    m, n = grid.shape
    g = create_graph(grid, m, n)
    return nx.shortest_path_length(g, (0, 0), target=(m - 1, n - 1), weight="weight")


def part_2(grid: np.ndarray) -> int:
    big_grid = create_big_grid(grid)
    return part_1(big_grid)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        input = input.read().splitlines()
        grid = np.array([[int(x) for x in list(row)] for row in input])

    part_1_ans = part_1(grid)
    print(part_1_ans)

    part_2_ans = part_2(grid)
    print(part_2_ans)
