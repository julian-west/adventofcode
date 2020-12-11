"""
Day 11 Advent of code
"""
from typing import Callable
import numpy as np


def load_input(file: str) -> np.array:
    """Load text file into matrix"""
    with open(file, "r") as input_file:
        lines = input_file.read().splitlines()

    matrix = np.array([list(line) for line in lines])
    return matrix


def get_adjacent_occupied_seats(matrix: np.array, x_pos: int, y_pos: int) -> int:
    """Find the number of adjacent occupied seats"""

    occupied = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and y == 0:
                continue
            y_idx = y + y_pos
            if y_idx < 0 or y_idx >= len(matrix):
                continue
            x_idx = x + x_pos
            if x_idx < 0 or x_idx >= len(matrix[0]):
                continue
            if matrix[y_idx][x_idx] == "#":
                occupied += 1
    return occupied


def get_visible_neighbours(matrix: np.array, x_pos: int, y_pos: int) -> int:
    """Get number of occupied seats which are visible from a given position"""
    occupied = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and y == 0:
                continue
            occupied += is_seat_visible(matrix, x_pos, y_pos, x, y)
    return occupied


def is_seat_visible(
    matrix: np.array, x_pos: int, y_pos: int, x_dir: int, y_dir: int
) -> int:
    """Checks if a seat is occupied within view"""
    x = x_pos + x_dir
    y = y_pos + y_dir
    while 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
        if matrix[y][x] == "#":
            return 1
        if matrix[y][x] == "L":
            return 0
        x += x_dir
        y += y_dir

    return 0


def fill_seats(
    matrix: np.array, max_occ: int, neighbour_check_fn: Callable
) -> np.array:
    """Return iteration of seat filling"""
    new_layout = np.empty(matrix.shape, dtype=str)
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "L":
                adj_occupied = neighbour_check_fn(matrix, x, y)
                if adj_occupied == 0:
                    new_layout[y][x] = "#"
                else:
                    new_layout[y][x] = matrix[y][x]
            elif matrix[y][x] == "#":
                adj_occupied = neighbour_check_fn(matrix, x, y)
                if adj_occupied >= max_occ:
                    new_layout[y][x] = "L"
                else:
                    new_layout[y][x] = matrix[y][x]
            else:
                new_layout[y][x] = matrix[y][x]

    return new_layout


def count_total_occupied_seats(matrix: np.array) -> int:
    """Count total number of occupied seats"""
    return (matrix == "#").sum()


def run_simulation(matrix: np.array, max_occ: int, neighbour_check_fn: Callable) -> int:
    """Run simulation until it converges and return count of occupied seats

    When the matrices converge, returns the number of iterations and the final
    number of occupied seats
    """
    old_matrix = matrix
    while True:
        new_matrix = fill_seats(old_matrix, max_occ, neighbour_check_fn)
        if np.array_equal(old_matrix, new_matrix):
            return count_total_occupied_seats(new_matrix)
        old_matrix = new_matrix


if __name__ == "__main__":
    input_matrix = load_input("input.txt")

    # Part 1
    p1_seat_count = run_simulation(
        input_matrix, max_occ=4, neighbour_check_fn=get_adjacent_occupied_seats
    )
    print(p1_seat_count)

    # Part 2
    p2_seat_count = run_simulation(
        input_matrix, max_occ=5, neighbour_check_fn=get_visible_neighbours
    )
    print(p2_seat_count)
