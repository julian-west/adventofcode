"""Day 13 tests"""

import pytest
from d13_solution import compare, part_1, part_2, process_input

test_input = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


@pytest.fixture
def processed_input():
    return process_input(test_input)


@pytest.mark.parametrize(
    "packet,expected",
    [
        ([[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]], -1),
        ([[[1], [2, 3, 4]], [[1], 4]], -1),
        ([[9], [[8, 7, 6]]], 1),
        ([[[4, 4], 4, 4], [[4, 4], 4, 4, 4]], -1),
        ([[7, 7, 7, 7], [7, 7, 7]], 1),
        ([[], [3]], -1),
        ([[[[]]], [[]]], 1),
        ([[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]], 1),
    ],
)
def test_compare(packet, expected):
    assert compare(*packet) == expected


def test_part_1(processed_input):
    assert part_1(processed_input) == 13


def test_part_2(processed_input):
    assert part_2(processed_input) == 140
