"""Day 18 solution"""
from typing import List


def load_input(filepath: str) -> List:
    """load input into a list"""
    with open(filepath, "r") as input_file:
        data = input_file.read().splitlines()

    return [eq.replace(" ", "") for eq in data]


def evaluate(eq: str) -> int:
    """Evaluate an equation and return the result"""
    pass


if __name__ == "__main__":

    equations = load_input("input.txt")

    print(equations[:5])
