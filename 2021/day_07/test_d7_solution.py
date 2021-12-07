"""Tests for day 7 solution"""

import pytest
from d7_solution import gauss, part_1, part_2

example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
sorted_example = sorted(example)


@pytest.mark.parametrize("x,expected", [(100, 5050), (50, 1275)])
def test_gauss(x, expected):
    assert gauss(x) == expected


def test_part_1():
    assert part_1(sorted_example) == 37


def test_part_2():
    assert part_2(sorted_example) == 170
