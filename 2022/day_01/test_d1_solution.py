"""Test day 1 solution"""
import pytest
from d1_solution import aggregate_calories, part_1, part_2, process_input

test_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


@pytest.fixture
def elf_calories():
    return process_input(test_input)


@pytest.fixture
def aggregated_calories(elf_calories):
    return aggregate_calories(elf_calories)


def test_process_input():
    expected = [
        ["1000", "2000", "3000"],
        ["4000"],
        ["5000", "6000"],
        ["7000", "8000", "9000"],
        ["10000"],
    ]
    assert process_input(test_input) == expected


def test_aggregate_calories(elf_calories):
    expected = [6000, 4000, 11_000, 24_000, 10_000]
    assert aggregate_calories(elf_calories) == expected


def test_part_1(aggregated_calories):
    assert part_1(aggregated_calories) == 24000


def test_part_2(aggregated_calories):
    assert part_2(aggregated_calories) == 45000
