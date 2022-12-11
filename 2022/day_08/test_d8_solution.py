"""Test day 8 solution"""

import pytest
from d8_solution import (
    calc_scenic_score,
    check_visible,
    count_perimiter,
    create_grid,
    get_sight_lines,
    part_1,
    part_2,
)

test_input = """
30373
25512
65332
33549
35390
"""


@pytest.fixture
def grid():
    return create_grid(test_input)


def test_count_perimiter(grid):
    assert count_perimiter(grid) == 16


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1, 1, ([2], [5, 1, 2], [0], [5, 3, 5])),
        (2, 2, ([5, 6], [3, 2], [5, 3], [5, 3])),
    ],
)
def test_get_sight_lines(x, y, expected, grid):
    assert get_sight_lines(x, y, grid) == expected


@pytest.mark.parametrize(
    "height,sight_line,expected",
    [
        (1, ([2, 3], [1, 2, 3], [4, 4], [1]), False),
        (5, ([2, 3], [1, 2, 3], [4, 4], [1]), True),
        (5, ([3, 3], [9, 4], [3, 5, 3], [3]), True),
    ],
)
def test_check_visible(height, sight_line, expected):
    assert check_visible(height, sight_line) == expected


def test_part_1(grid):
    assert part_1(grid) == 21


@pytest.mark.parametrize(
    "height,sight_lines,expected",
    [
        (5, ([5, 2], [1, 2], [3], [3, 5, 3]), 4),
        (5, ([3, 3], [4, 9], [3, 5, 3], [3]), 8),
    ],
)
def test_calc_scenic_score(height, sight_lines, expected):
    assert calc_scenic_score(height, sight_lines) == expected


def test_part_2(grid):
    assert part_2(grid) == 8
