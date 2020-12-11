"""
Day 11 Advent of code
"""
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


def fill_seats(matrix: np.array, max_occ: int = 4) -> np.array:
    """Return iteration of seat filling"""
    new_layout = np.empty(matrix.shape, dtype=str)
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "L":
                adj_ocupied = get_adjacent_occupied_seats(matrix, x, y)
                if adj_ocupied == 0:
                    new_layout[y][x] = "#"
                else:
                    new_layout[y][x] = matrix[y][x]
            elif matrix[y][x] == "#":
                adj_ocupied = get_adjacent_occupied_seats(matrix, x, y)
                if adj_ocupied >= max_occ:
                    new_layout[y][x] = "L"
                else:
                    new_layout[y][x] = matrix[y][x]
            else:
                new_layout[y][x] = matrix[y][x]

    return new_layout


def count_total_ocupied_seats(matrix: np.array) -> int:
    """Count total number of occupied seats"""
    return (matrix == "#").sum()


def part1(matrix: np.array) -> int:
    """Run simulation until it converges and return count of occupied seats

    When the matrices converge, returns the number of iterations and the final
    number of occupied seats
    """
    counter = 0
    old_matrix = matrix
    while True:
        new_matrix = fill_seats(old_matrix)
        if np.array_equal(old_matrix, new_matrix):
            return counter, count_total_ocupied_seats(new_matrix)
        old_matrix = new_matrix
        counter += 1


if __name__ == "__main__":
    input_matrix = load_input("input.txt")

    # Part 1
    iterations, seat_count = part1(input_matrix)
    print(iterations, seat_count)
