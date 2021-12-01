"""Day 18 solution"""
import operator
import re
from collections import deque
from math import prod
from typing import Callable, Dict, List

OPS = {"+": operator.add, "*": operator.mul}


def load_input(filepath: str) -> List:
    """load input into a list"""
    with open(filepath, "r") as input_file:
        data = input_file.read().splitlines()
    return data


def normal_precedence(eq: str, operators: Dict = OPS) -> int:
    """Evaluate a 'base' expression which does not contain any brackets"""
    tokens = deque(eq.split())
    result = int(tokens.popleft())
    while tokens:
        op, num = tokens.popleft(), int(tokens.popleft())
        result = operators[op](result, num)
    return result


def change_precedence(eq):
    """Change precedence so that '+' is evaluated before '*'"""
    return prod(map(normal_precedence, eq.split("*")))


def evaluate(eq: str, func: Callable) -> int:
    """Evaluate an equation and return the result"""
    inside_expressions = re.search(r"(\([^()]+\))", eq)
    # base case for recursion
    if not inside_expressions:
        return func(eq)

    inside_expression = inside_expressions.group(1)
    brackets_result = func(inside_expression.strip("()"))
    new_eq = eq.replace(inside_expression, str(brackets_result))
    return evaluate(new_eq, func)


if __name__ == "__main__":

    equations = load_input("input.txt")

    # part 1
    print(sum(evaluate(eq, normal_precedence) for eq in equations))

    # part 2
    print(sum(evaluate(eq, change_precedence) for eq in equations))
