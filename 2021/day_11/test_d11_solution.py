"""Tests day 11 solution"""
import pytest
from d11_solution import part_1, part_2

example = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


@pytest.mark.parametrize("steps,expected", [(10, 204), (100, 1656)])
def test_part_1(steps, expected):
    field = {}
    for i, row in enumerate(example):
        for j, val in enumerate(row.strip()):
            field[(i, j)] = int(val)
    assert part_1(field, steps) == expected


def test_part_2():
    field = {}
    for i, row in enumerate(example):
        for j, val in enumerate(row.strip()):
            field[(i, j)] = int(val)
    assert part_2(field) == 195
