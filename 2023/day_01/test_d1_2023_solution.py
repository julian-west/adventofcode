"""Day 1 Test cases"""
import pytest
from solution_d1 import find_first_and_last_number, part_1, part_2


def test_part_1():
    test_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    assert part_1(test_input) == 142


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_find_first_and_last_number(input_string, expected):
    assert find_first_and_last_number(input_string) == expected


def test_part_2():
    test_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert part_2(test_input) == 281
