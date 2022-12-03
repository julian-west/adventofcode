"""Day 3 tests"""
from d3_solution import calc_total_priority, split_into_compartments, split_into_groups

test_input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def test_part_1():
    assert calc_total_priority(test_input, split_into_compartments) == 157


def test_part_2():
    assert calc_total_priority(test_input, split_into_groups, n=3) == 70
