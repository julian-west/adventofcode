"""Test day 12"""
import numpy as np
import pytest
from d12_solution import build_graph, get_node, part_1, part_2

test_input = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


@pytest.fixture
def area():
    return np.array([list(line) for line in test_input.split("\n") if line])


@pytest.fixture
def graph(area):
    return build_graph(area)


def test_part_1(area, graph):
    start = get_node(area, "S")
    dest = get_node(area, "E")
    assert part_1(graph, start, dest) == 31


def test_part_2(area, graph):
    dest = get_node(area, "E")
    assert part_2(graph, area, dest) == 29
