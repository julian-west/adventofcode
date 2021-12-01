"""Day 18 tests"""

import pytest
from solution import normal_precedence, evaluate, change_precedence


@pytest.mark.parametrize(
    "equation, expected", [("3 + 5", 8), ("8 * 4 + 2 + 4 * 2", 76), ("3 * 2 + 5", 11)]
)
def test_normal_precedence(equation, expected):
    """Test normal_precedence function"""
    assert normal_precedence(equation) == expected


@pytest.mark.parametrize(
    "raw_input, func, expected",
    [
        ("2 * 3 + (4 * 5)", normal_precedence, 26),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", normal_precedence, 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", normal_precedence, 12240),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", normal_precedence, 13632),
        ("1 + (2 * 3) + (4 * (5 + 6))", change_precedence, 51),
        ("2 * 3 + (4 * 5)", change_precedence, 46),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", change_precedence, 1445),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", change_precedence, 669060),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", change_precedence, 23340),
    ],
)
def test_evalute(raw_input, func, expected):
    """Test evaluate function"""
    assert evaluate(raw_input, func) == expected
