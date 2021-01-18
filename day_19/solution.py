"""Day 19 Advent of Code"""
from typing import List


def load_input(file: str) -> List:
    """load data input"""
    with open(file, "r") as input_file:
        data = input_file.readlines()
        data = [line.strip() for line in data]

    rules_data = data[: data.index("")]
    msgs = data[data.index("") :]

    return rules_data, msgs


if __name__ == "__main__":
    input_data = load_input("input.txt")
