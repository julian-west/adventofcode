"""
Tests for day 13
"""
from typing import List
import pytest
from solution import part1, part2

TEST_INPUT = """
939
7,13,x,x,59,x,31,19
"""
earliest_time, bus_ids = int(TEST_INPUT.split()[0]), TEST_INPUT.split()[1].split(",")


def test_part1():
    """Test part1 function"""
    assert part1(earliest_time=earliest_time, bus_ids=bus_ids) == 295


@pytest.mark.parametrize(
    "bus_ids,expected",
    [
        (bus_ids, 1068781),
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
