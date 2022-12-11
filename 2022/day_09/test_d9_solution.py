"""Test day 9 solution"""
import pytest
from d9_solution import process_input, solve

test_input_part_1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

test_input_part_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


@pytest.mark.parametrize(
    "raw_input,knots,expected",
    [
        (test_input_part_1, 1, 13),
        (test_input_part_2, 9, 36),
    ],
    ids=[
        "part_1",
        "part_2",
    ],
)
def test_solve(raw_input, knots, expected):
    instructions = process_input(raw_input)
    assert solve(instructions, knots) == expected
