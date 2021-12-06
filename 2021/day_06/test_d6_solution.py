"""Day 6 Solution tests"""
import pytest
from d6_solution import solve

example = [3, 4, 3, 1, 2]


@pytest.mark.parametrize(
    "initial_state,days,expected",
    [(example, 18, 26), (example, 80, 5934), (example, 256, 26984457539)],
)
def test_solve(initial_state, days, expected):
    assert solve(initial_state, days) == expected
