"""Day 3 solution tests"""
import pytest
from d3_solution import (
    find_epsilon_rate,
    find_gamma_rate,
    find_mode,
    find_rating_binary,
    part_1,
    part_2,
)

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


@pytest.mark.parametrize(
    "values,criterion,expected",
    [
        (["0", "0", "1", "1"], "most", "1"),
        (["1", "0", "0"], "most", "0"),
        (["1", "1", "0"], "most", "1"),
        (["0", "0", "1", "1"], "least", "0"),
        (["1", "0", "0"], "least", "1"),
        (["1", "1", "0"], "least", "0"),
    ],
)
def test_find_mode(values, criterion, expected):
    assert find_mode(values, criterion) == expected


@pytest.mark.parametrize(
    "values,criterion,expected",
    [(example, "most", "10111"), (example, "least", "01010")],
)
def test_rating_binary(values, criterion, expected):
    assert find_rating_binary(values, criterion=criterion) == expected


def test_part_2():
    assert part_2(example) == 23


def test_part_1():
    assert part_1(example) == 198
