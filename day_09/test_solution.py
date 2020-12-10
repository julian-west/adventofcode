"""
Tests for day 9 python solution
"""
import pytest
from solution import part1, part2

# fmt: off
test_input = [ 35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
# fmt: on


def test_part1(test_input=test_input):
    """Test part 1 function"""
    assert part1(test_input, window=5) == 127


def test_part2(test_input=test_input):
    """Test part 2 function"""
    assert part2(test_input, target=127) == 62
