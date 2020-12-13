"""
Tests for day 13
"""

import pytest
from solution import part1

TEST_INPUT = """
939
7,13,x,x,59,x,31,19
"""
earliest_time = int(TEST_INPUT.split()[0])
bus_ids = set([int(bus) for bus in TEST_INPUT.split()[1].split(",") if bus != "x"])


def test_part1():
    """Test part1 function"""
    assert part1(earliest_time=earliest_time, bus_ids=bus_ids) == 295
