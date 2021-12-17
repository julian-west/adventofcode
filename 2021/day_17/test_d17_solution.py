"""Tests day 17"""
import pytest
from d17_solution import Target, part_1, part_2, process_input

example = "target area: x=20..30, y=-10..-5"


@pytest.fixture
def target():
    return process_input(example)


def test_process_input():
    assert process_input(example) == Target(min_x=20, max_x=30, min_y=-10, max_y=-5)


def test_part_1(target):
    assert part_1(target) == 45


def test_part_2(target):
    assert part_2(target) == 112
