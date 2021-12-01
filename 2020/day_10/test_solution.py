"""
Tests for python solution
"""

import pytest
from solution import part1, part2

test_input_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

# fmt: off
test_input_2 = [ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3, ]
# fmt: on


@pytest.mark.parametrize(
    "input_adapters,expected", [(test_input_1, 35), (test_input_2, 220)]
)
def test_part1(input_adapters, expected):
    """Test part 1 function"""
    sorted_adapters = sorted(input_adapters)
    adapters = [0] + sorted_adapters + [sorted_adapters[-1] + 3]
    assert part1(adapters) == expected


@pytest.mark.parametrize(
    "input_adapters,expected", [(test_input_1, 8), (test_input_2, 19208)]
)
def test_part2(input_adapters, expected):
    """Test part 2 function"""
    sorted_adapters = sorted(input_adapters)
    adapters = [0] + sorted_adapters + [sorted_adapters[-1] + 3]
    assert part2(adapters) == expected
