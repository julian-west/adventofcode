"""Day 14 Solution Tests"""

import pytest
from d14_solution import (
    get_answer,
    get_element_counts,
    polymerise,
    process_pairs,
    process_polymer,
    run_simulation,
)

example_polymer = "NNCB"

example_pairs = """
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

processed_polymer = process_polymer(example_polymer)
processed_pairs = process_pairs(example_pairs)

# fmt: off
example_step1_polymer_dict = {"NC": 1, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1}
example_step4_polymer_dict = {"NB": 9, "BB": 9, "BN": 6, "BC": 4, "CC": 2, "CN": 3, "NC": 1, "CB": 5, "BH": 3, "HC": 3, "HH": 1, "HN": 1, "NH": 1}
example_step1_element_counts = {'C': 2, 'B': 2, 'N': 2, 'H': 1}
example_step4_element_counts = {'B': 23, 'N': 11, 'H': 5, 'C': 10}
example_step10_element_counts = {'B': 1749, 'N': 865, 'H': 161, 'C': 298}
# fmt: on


def test_process_polymer():
    assert process_polymer(example_polymer) == {"NN": 1, "NC": 1, "CB": 1}


def test_process_pairs():
    assert process_pairs(example_pairs)["CH"] == "B"
    assert process_pairs(example_pairs)["CN"] == "C"


def test_get_element_counts():
    assert get_element_counts(processed_polymer) == {"C": 1, "N": 2, "B": 1}


@pytest.mark.parametrize(
    "polymer,pairs,steps,expected",
    [
        (processed_polymer, processed_pairs, 1, example_step1_polymer_dict),
        (processed_polymer, processed_pairs, 4, example_step4_polymer_dict),
    ],
)
def test_polymerise(polymer, pairs, steps, expected):
    assert polymerise(polymer, pairs, steps) == expected


@pytest.mark.parametrize(
    "element_counts,expected",
    [
        (example_step1_element_counts, 1),
        (example_step4_element_counts, 18),
        (example_step10_element_counts, 1588),
    ],
)
def test_get_answer(element_counts, expected):
    assert get_answer(element_counts) == expected


@pytest.mark.parametrize(
    "polymer,pairs,steps,expected",
    [
        (processed_polymer, processed_pairs, 10, 1588),
        (processed_polymer, processed_pairs, 40, 2188189693529),
    ],
)
def test_run_simulation(polymer, pairs, steps, expected):
    assert run_simulation(polymer, pairs, steps) == expected
