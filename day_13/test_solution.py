"""
Tests for day 13
"""
from typing import List
import pytest
from solution import part1, part2

def test_part1():
    """Test part1 function"""
    assert part1(
        earliest_time = 939,
        bus_ids = ["7", "13", "x", "x", "59", "x", "31", "19"]
    ) == 295


@pytest.mark.parametrize(
    "bus_ids,expected",
    [
        (["7", "13", "x", "x", "59", "x", "31", "19"], 1068781),
        (["17", "x", "13", "19"], 3417),
        (["67", "7", "59", "61"], 754018),
        (["67", "x", "7", "59", "61"], 779210),
        (["67", "7", "x", "59", "61"], 1261476),
        (["1789", "37", "47", "1889"], 1202161486),
    ],
)
def test_part2(bus_ids: List[str], expected: int):
    """Test part2 function"""
    assert part2(bus_ids) == expected
