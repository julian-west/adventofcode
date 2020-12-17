"""Test day 16 solutions"""

import pytest

from solution import load_input, find_valid_ints, part1


@pytest.fixture
def test_input():
    """Load the test input for testing"""
    return load_input("test_input.txt")


def test_load_input():
    """Test load input function"""
    assert load_input("test_input.txt") == (
        {
            "class": [(1, 3), (5, 7)],
            "row": [(6, 11), (33, 44)],
            "seat": [(13, 40), (45, 50)],
        },
        [7, 1, 14],
        [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]],
    )


def test_find_valid_ints(test_input):
    """Test find_valid_ints"""
    # fmt: off
    expected = {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50} 
    # fmt: on
    assert find_valid_ints(test_input[0]) == expected


def test_part1(test_input):
    """Test part1 function"""
    assert part1(test_input[0], test_input[2]) == 71
