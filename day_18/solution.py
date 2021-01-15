"""Day 18 solution"""
from typing import List
import operator

OPERATORS = {"+": operator.add, "*": operator.mul}


def load_input(filepath: str) -> List:
    """load input into a list"""
    with open(filepath, "r") as input_file:
        data = input_file.read().splitlines()

    return [eq.replace(" ", "") for eq in data]


def evaluate(eq: str) -> int:
    """Evaluate an equation and return the result"""
    inside_expressions = re.search(r"(\([^()]+\))", eq)
    # base case for recursion
    if not inside_expressions:
        return inner_eval()  # TODO
    pass


if __name__ == "__main__":

    equations = load_input("input.txt")

    print(equations[:5])
