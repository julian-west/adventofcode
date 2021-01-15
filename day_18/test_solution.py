"""Day 18 tests"""

import pytest
from solution import inner_eval, evaluate


@pytest.mark.parametrize(
    "equation, expected", [("3 + 5", 8), ("8 * 4 + 2 + 4 * 2", 76), ("3 * 2 + 5", 11)]
)
def test_inner_eval(equation, expected):
    """Test inner_eval function"""
    assert inner_eval(equation) == expected


@pytest.mark.parametrize(
    "raw_input, expected",
    [
        ("2 * 3 + (4 * 5)", 26),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
    ],
)
def test_evalute(raw_input, expected):
    """Test evaluate function"""
    assert evaluate(raw_input) == expected
