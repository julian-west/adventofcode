"""Day 2 test"""
from d2_solution import part_1, part_2

example = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]


def test_part_1():
    assert part_1(example) == 150


def test_part_2():
    assert part_2(example) == 900
