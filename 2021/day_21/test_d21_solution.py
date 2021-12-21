"""Tests day 20"""
from d21_solution import part_1, part_2

# example input
p1, p2 = 4, 8


def test_part_1():
    part_1(p1 - 1, p2 - 1, 0, 0) == 739785


def test_part_2():
    part_2(p1 - 1, p2 - 1, 0, 0) == 444356092776315
