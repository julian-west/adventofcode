"""Test day 2 solution"""

import pytest
from d2_solution import calc_total_score, part_1, part_2

test_input = [
    "A Y",
    "B X",
    "C Z",
]


@pytest.mark.parametrize(
    "moves,expected",
    [
        ("A Y", 8),
        ("B X", 1),
        ("C Z", 6),
    ],
)
def test_part_1(moves, expected):
    assert part_1(moves) == expected


@pytest.mark.parametrize(
    "moves,expected",
    [
        ("A Y", 4),
        ("B X", 1),
        ("C Z", 7),
    ],
)
def test_part_2(moves, expected):
    assert part_2(moves) == expected


@pytest.mark.parametrize(
    "strategy_guide,rule_func,expected",
    [
        (test_input, part_1, 15),
        (test_input, part_2, 12),
    ],
)
def test_calc_total_score(strategy_guide, rule_func, expected):
    assert calc_total_score(strategy_guide, rule_func) == expected
