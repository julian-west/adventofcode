"""Day 17 solution tests"""
import pytest
from solution import run_simulation

test_input = """
.#.
..#
###
"""


@pytest.mark.parametrize(
    "input_grid, iterations, extra_dims, expected",
    [(test_input, 6, (0,), 112), (test_input, 6, (0, 1), 848)],
)
def test_run_simulation(input_grid, iterations, extra_dims, expected):
    """Test simulation"""
    assert run_simulation(input_grid, iterations, extra_dims) == expected
