"""
Tests for day 12
"""
from typing import Dict

import pytest
from solution import (
    find_new_direction,
    manhattan_distance,
    part1,
    find_new_waypoint,
    part2,
)

TEST_INPUT = """
F10
N3
F7
R90
F11
"""

test_input = [
    (instruction[0], int(instruction[1:])) for instruction in TEST_INPUT.split()
]


@pytest.mark.parametrize(
    "cur_direction, instruction, magnitude, expected",
    [("E", "R", 90, "S"), ("E", "L", 270, "S"), ("N", "R", 180, "S")],
)
def test_find_new_direction(
    cur_direction: str, instruction: str, magnitude: int, expected: str
) -> None:
    """Test find new direction function"""
    assert find_new_direction(cur_direction, instruction, magnitude) == expected


@pytest.mark.parametrize(
    "positions_dict, expected",
    [({"N": 0, "E": 10, "S": 4, "W": 5}, 9), ({"N": 20, "E": 10, "S": 4, "W": 1}, 25)],
)
def test_manhattan_distance(positions_dict: Dict[str, int], expected: int) -> None:
    """Test mahattan_distance function"""
    assert manhattan_distance(positions_dict) == expected


@pytest.mark.parametrize(
    "waypoint, instruction, magnitude, expected",
    [
        ({"N": 1, "E": 10, "S": 0, "W": 0}, "R", 90, {"N": 0, "E": 1, "S": 10, "W": 0}),
        ({"N": 1, "E": 10, "S": 0, "W": 0}, "L", 90, {"N": 10, "E": 0, "S": 0, "W": 1}),
    ],
)
def test_find_new_waypoint(
    waypoint: Dict[str, int], instruction: str, magnitude: int, expected: Dict[str, int]
):
    """Test find new waypoint"""
    assert find_new_waypoint(waypoint, instruction, magnitude) == expected


def test_part1():
    """Test part 1"""
    assert part1(directions=test_input, start_direction="E") == 25


def test_part2():
    """Test part 2"""
    assert (
        part2(directions=test_input, waypoint={"N": 1, "E": 10, "S": 0, "W": 0}) == 286
    )
