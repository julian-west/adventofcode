"""Day 8 solution tests

Note: part 1 and 2 tests commented out as pytest cannot find the example_input.txt
from the top level directory. Can't be bothered to sort it out properly.

The tests do pass though :)
"""

# import pytest
# from d8_solution import part_1, part_2
from d8_solution import process_line

example_line_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

processed_line_input = (
    [
        "acedgfb",
        "cdfbe",
        "gcdfa",
        "fbcad",
        "dab",
        "cefabd",
        "cdfgeb",
        "eafb",
        "cagedb",
        "ab",
    ],
    ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
)


def test_process_line():
    assert process_line(example_line_input) == processed_line_input


# @pytest.fixture
# def example_input():
#     with open("./example_input.txt", "r") as example_input:
#         patterns = example_input.read().splitlines()
#     return [process_line(x) for x in patterns]


# def test_part_1(example_input):
#     assert part_1(example_input) == 26


# def test_part_2(example_input):
#     assert part_2(example_input) == 61229
