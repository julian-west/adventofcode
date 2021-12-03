"""Day 3 solution tests"""
from d3_solution import find_epsilon_rate, find_gamma_rate, part_1

example = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_find_gamma_rate():
    assert find_gamma_rate(example) == "10110"


def test_find_epsilon_rate():
    assert find_epsilon_rate("10110") == "01001"


def test_part_1():
    assert part_1(example) == 198
