"""
Tests for day 11
"""
from typing import Callable

import numpy as np
import pytest
from solution import (
    count_total_occupied_seats,
    fill_seats,
    get_adjacent_occupied_seats,
    get_visible_neighbours,
    is_seat_visible,
    run_simulation,
)

TEST_INPUT_1 = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

TEST_INPUT_2 = """
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
"""

TEST_INPUT_3 = """
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
"""

TEST_INPUT_4 = """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
"""


def load_raw_string(raw_string):
    """Load test string into matrix for testing"""
    return np.array([list(line) for line in raw_string.split("\n") if line])


test_input1_matrix = load_raw_string(TEST_INPUT_1)
test_input2_matrix = load_raw_string(TEST_INPUT_2)
test_input3_matrix = load_raw_string(TEST_INPUT_3)
test_input4_matrix = load_raw_string(TEST_INPUT_4)


@pytest.mark.parametrize(
    "matrix,x_pos,y_pos,expected",
    [
        (test_input1_matrix, 0, 0, 0),
        (test_input2_matrix, 0, 0, 1),
        (test_input2_matrix, 7, 0, 2),
    ],
)
def test_get_adjacent_occupied_seats(
    matrix: np.array, x_pos: int, y_pos: int, expected: int
) -> bool:
    """test get_adjacent_occupied_seats function"""
    assert get_adjacent_occupied_seats(matrix, x_pos, y_pos) == expected


@pytest.mark.parametrize(
    "matrix, x_pos, y_pos, expected",
    [
        (test_input1_matrix, 0, 0, 0),
        (test_input2_matrix, 3, 9, 1),
        (test_input2_matrix, 5, 4, 1),
        (test_input3_matrix, 3, 3, 0),
    ],
)
def test_get_visible_neigbours(matrix: np.array, x_pos: int, y_pos: int, expected: int):
    """test get_visible_neighbours function"""
    assert get_visible_neighbours(matrix, x_pos, y_pos) == expected


@pytest.mark.parametrize(
    "matrix, x_pos, y_pos, x_dir, y_dir, expected",
    [
        (test_input2_matrix, 9, 8, 0, 1, 1),
        (test_input3_matrix, 3, 3, 0, 1, 0),
        (test_input3_matrix, 1, 0, 1, 1, 1),
    ],
)
def test_is_seat_visible(
    matrix: np.array, x_pos: int, y_pos: int, x_dir: int, y_dir: int, expected: int
) -> bool:
    """test is_seat_visible function"""
    assert is_seat_visible(matrix, x_pos, y_pos, x_dir, y_dir) == expected


@pytest.mark.parametrize(
    "matrix, max_occ, neighbour_check_fn, expected",
    [(test_input1_matrix, 4, get_adjacent_occupied_seats, test_input2_matrix)],
)
def test_fill_seats(
    matrix: np.array, max_occ: int, neighbour_check_fn: Callable, expected: np.array
) -> bool:
    """test fill seats function"""
    first_pass = fill_seats(matrix, max_occ, neighbour_check_fn)
    assert np.array_equal(fill_seats(first_pass, max_occ, neighbour_check_fn), expected)


@pytest.mark.parametrize(
    "matrix, expected",
    [(test_input1_matrix, 0), (test_input2_matrix, 20), (test_input3_matrix, 24)],
)
def test_count_total_occupied_seats(matrix: np.array, expected: int):
    """test count_total_occupied_seats function"""
    assert count_total_occupied_seats(matrix) == expected


@pytest.mark.parametrize(
    "matrix, max_occ, neighbour_check_fn, expected",
    [
        (test_input1_matrix, 4, get_adjacent_occupied_seats, 37),
        (test_input1_matrix, 5, get_visible_neighbours, 26),
    ],
)
def test_run_simulation(
    matrix: np.array, max_occ: int, neighbour_check_fn: Callable, expected: np.array
):
    """test run_simulation function"""
    assert run_simulation(matrix, max_occ, neighbour_check_fn) == expected
