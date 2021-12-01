"""Day 1 Solution Tests"""
from d1_solution import part_1, part_2

example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_1(input=example, expected=7):
    assert part_1(input) == expected


def test_part_2(input=example, expected=5):
    assert part_2(input, window=3) == expected
