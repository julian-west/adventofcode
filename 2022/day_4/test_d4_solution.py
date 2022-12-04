"""Test day 4 solution"""

import pytest
from d4_solution import calc_total, part_1, part_2

test_input = [
    [2, 4, 6, 8],
    [2, 3, 4, 5],
    [5, 7, 7, 9],
    [2, 8, 3, 7],
    [6, 6, 4, 6],
    [2, 6, 4, 8],
]


@pytest.mark.parametrize(
    "l1_min,l1_max,l2_min,l2_max,expected",
    [
        (2, 4, 6, 8, False),
        (2, 3, 4, 5, False),
        (5, 7, 7, 9, False),
        (2, 8, 3, 7, True),
        (6, 6, 4, 6, True),
        (2, 6, 4, 8, False),
    ],
)
def test_part_1(l1_min, l1_max, l2_min, l2_max, expected):
    assert part_1(l1_min, l1_max, l2_min, l2_max) == expected


@pytest.mark.parametrize(
    "l1_min,l1_max,l2_min,l2_max,expected",
    [
        (2, 4, 6, 8, False),
        (2, 3, 4, 5, False),
        (5, 7, 7, 9, True),
        (2, 8, 3, 7, True),
        (6, 6, 4, 6, True),
        (2, 6, 4, 8, True),
    ],
)
def test_part_2(l1_min, l1_max, l2_min, l2_max, expected):
    assert part_2(l1_min, l1_max, l2_min, l2_max) == expected


@pytest.mark.parametrize(
    "sections,func,expected",
    [
        (test_input, part_1, 2),
        (test_input, part_2, 4),
    ],
)
def test_calc_total(sections, func, expected):
    assert calc_total(sections, func) == expected
