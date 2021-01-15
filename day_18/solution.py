"""Day 18 solution"""
from typing import List, Dict
import re
from collections import deque
import operator

OPS = {"+": operator.add, "*": operator.mul}


def load_input(filepath: str) -> List:
    """load input into a list"""
    with open(filepath, "r") as input_file:
        data = input_file.read().splitlines()
    return data


def inner_eval(eq: str, operators: Dict = OPS) -> int:
    """Evaluate a 'base' expression which does not contain any brackets"""
    tokens = deque(eq.split())
    result = int(tokens.popleft())
    while tokens:
        op, num = tokens.popleft(), int(tokens.popleft())
        result = operators[op](result, num)
    return result


def evaluate(eq: str) -> int:
    """Evaluate an equation and return the result"""
    inside_expressions = re.search(r"(\([^()]+\))", eq)
    # base case for recursion
    if not inside_expressions:
        return inner_eval(eq)

    inside_expression = inside_expressions.group(1)
    brackets_result = inner_eval(inside_expression.strip("()"))
    new_eq = eq.replace(inside_expression, str(brackets_result))
    return evaluate(new_eq)


def part_1(equations: List) -> int:
    """Part 1 solution"""
    return sum(evaluate(eq) for eq in equations)


if __name__ == "__main__":

    equations = load_input("input.txt")

    # part 1
    print(part_1(equations))
