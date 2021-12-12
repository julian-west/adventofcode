"""Day 12 solution tests"""

import pytest
from d12_solution import create_graph, part_1, part_2

example1 = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
example2 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

example3 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]


@pytest.mark.parametrize(
    "input,expected", [(example1, 10), (example2, 19), (example3, 226)]
)
def test_part_1(input, expected):
    graph = create_graph(input)
    assert part_1(graph) == expected


@pytest.mark.parametrize(
    "input,expected", [(example1, 36), (example2, 103), (example3, 3509)]
)
def test_part_2(input, expected):
    graph = create_graph(input)
    assert part_2(graph) == expected
