"""Tests for day 14"""

import pytest
from solution import load_input, apply_mask, part1


def test_load_input():
    """Test the load_input function"""
    processed_input = load_input("input.txt")
    assert processed_input[:2] == [
        ("1001X0X00110011X01X1000110100011000X", 5228, 409649),
        ("1001X0X00110011X01X1000110100011000X", 64037, 474625),
    ]


@pytest.mark.parametrize(
    "mask, binary, expected",
    [
        (
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "000000000000000000000000000000001011",
            "000000000000000000000000000001001001",
        ),
        (
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "000000000000000000000000000001100101",
            "000000000000000000000000000001100101",
        ),
        (
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "000000000000000000000000000000000000",
            "000000000000000000000000000001000000",
        ),
    ],
)
def test_apply_mask(mask: str, binary: str, expected: str):
    """Test apply_mask function"""
    assert apply_mask(mask, binary) == expected


def test_part1():
    """Test part1 function"""
    input_instructions = [
        ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 8, 11),
        ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 7, 101),
        ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 8, 0),
    ]

    assert part1(input_instructions) == 165
