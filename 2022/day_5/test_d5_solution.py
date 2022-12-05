"""Day 6 tests"""

from collections import deque

import pytest
from d5_solution import (
    parse_instructions_string,
    parse_stacks_string,
    part_1,
    part_2,
    solve,
)

test_input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

"""  # noqa: W291

stacks_string = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

"""  # noqa: W291

instructions_string = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

"""

stacks = {
    1: deque(["Z", "N"]),
    2: deque(["M", "C", "D"]),
    3: deque(["P"]),
}

instructions = [
    (1, 2, 1),
    (3, 1, 3),
    (2, 2, 1),
    (1, 1, 2),
]


def test_parse_stacks_string():

    expected = {
        1: deque(["Z", "N"]),
        2: deque(["M", "C", "D"]),
        3: deque(["P"]),
    }

    assert parse_stacks_string(stacks_string) == expected


def test_parse_instructions_string():
    # TODO: convert to named tuple or dataclass
    expected = [
        (1, 2, 1),
        (3, 1, 3),
        (2, 2, 1),
        (1, 1, 2),
    ]
    assert parse_instructions_string(instructions_string) == expected


@pytest.mark.parametrize(
    "stacks,instructions,move_crates,expected",
    [
        (stacks, instructions, part_1, "CMZ"),
        (stacks, instructions, part_2, "MCD"),
    ],
    ids=[
        "part_1",
        "part_2",
    ],
)
def test_solve(stacks, instructions, move_crates, expected):
    assert solve(stacks, instructions, move_crates) == expected
