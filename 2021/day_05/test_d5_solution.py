"""Day 5 solution tests"""

import pytest
from d5_solution import (
    draw_lines,
    find_max_coordinate,
    get_interim_straight_line_coordinates,
    part_1,
    process_input_line,
)

example = [
    [(0, 9), (5, 9)],
    [(8, 0), (0, 8)],
    [(9, 4), (3, 4)],
    [(2, 2), (2, 1)],
    [(7, 0), (7, 4)],
    [(6, 4), (2, 0)],
    [(0, 9), (2, 9)],
    [(3, 4), (1, 4)],
    [(0, 0), (8, 8)],
    [(5, 5), (8, 2)],
]


part_1_expected = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
]


def test_process_input_line():
    assert process_input_line("608,828 -> 608,49\n") == [(608, 828), (608, 49)]


def test_find_max_coordinate():
    assert find_max_coordinate(example) == 9


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ((1, 1), (1, 3), [(1, 1), (1, 2), (1, 3)]),
        ((9, 7), (7, 7), [(9, 7), (8, 7), (7, 7)]),
    ],
)
def test_get_interim_straight_line_coordinates(start, end, expected):
    assert get_interim_straight_line_coordinates(start, end) == expected


def test_draw_lines():
    assert draw_lines(10, example) == part_1_expected


def test_part_1():
    assert part_1(example) == 5
