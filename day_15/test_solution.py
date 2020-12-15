"""Day 15 tests"""

import pytest

from solution import run_simulation


@pytest.mark.parametrize(
    "starting_seq, rounds, expected",
    [
        ([1, 3, 2], 2020, 1),
        ([2, 1, 3], 2020, 10),
        ([1, 2, 3], 2020, 27),
        ([2, 3, 1], 2020, 78),
        ([3, 2, 1], 2020, 438),
        ([3, 1, 2], 2020, 1836),
        ([0, 3, 6], 2020, 436),
        ([1, 3, 2], 30000000, 2578),
        ([2, 1, 3], 30000000, 3544142),
        ([1, 2, 3], 30000000, 261214),
        ([2, 3, 1], 30000000, 6895259),
        ([3, 2, 1], 30000000, 18),
        ([3, 1, 2], 30000000, 362),
        ([0, 3, 6], 30000000, 175594),
    ],
)
def test_run_simulation(starting_seq, rounds, expected):
    """Test part 1 and part 2"""
    assert run_simulation(starting_seq, rounds) == expected
