"""Day 5 solution tests"""

import pytest
from d5_solution import (
    bresenham_algo,
    draw_lines,
    find_max_coordinate,
    process_input_line,
    solve,
)

full_example = [
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

horizontal_only_example = [
    [(0, 9), (5, 9)],
    [(9, 4), (3, 4)],
    [(2, 2), (2, 1)],
    [(7, 0), (7, 4)],
    [(0, 9), (2, 9)],
    [(3, 4), (1, 4)],
]

horizontal_expected = [
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

full_expected = [
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
    [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
    [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
]


def test_process_input_line():
    assert process_input_line("608,828 -> 608,49\n") == [(608, 828), (608, 49)]


def test_find_max_coordinate():
    assert find_max_coordinate(full_example) == 9


@pytest.mark.parametrize(
    "x0,y0,x1,y1,expected",
    [
        (1, 1, 1, 3, [(1, 1), (1, 2), (1, 3)]),
        (9, 7, 7, 7, [(9, 7), (8, 7), (7, 7)]),
        (1, 1, 3, 3, [(1, 1), (2, 2), (3, 3)]),
        (9, 7, 7, 9, [(9, 7), (8, 8), (7, 9)]),
    ],
)
def test_bresenham_algo(x0, y0, x1, y1, expected):
    """test Bresenham algo"""
    assert list(bresenham_algo(x0, y0, x1, y1)) == expected


@pytest.mark.parametrize(
    "dim,coords,expected",
    [
        (10, horizontal_only_example, horizontal_expected),
        (10, full_example, full_expected),
    ],
)
def test_draw_lines(dim, coords, expected):
    assert draw_lines(dim, coords) == expected


@pytest.mark.parametrize(
    "dim,coords,expected", [(10, horizontal_only_example, 5), (10, full_example, 12)]
)
def test_solve(dim, coords, expected):
    assert solve(dim, coords) == expected
