"""Day 5 solution"""

import re
from collections import defaultdict, deque
from copy import deepcopy
from typing import Callable

MoveCratesFunc = Callable[
    [dict[int, deque[str]], list[tuple[int, int, int]]], dict[int, deque[str]]
]


def parse_stacks_string(stacks_string: str) -> defaultdict[int, deque[str]]:
    stack_rows = stacks_string.split("\n")[:-1]
    stacks = defaultdict(deque)

    # start from bottom up
    for row in reversed(stack_rows):
        # parse through each row to extract letters
        for stack_num, crate in enumerate(row[1::4], start=1):
            if crate.isalpha():
                stacks[stack_num].append(crate)
    return stacks


def parse_instructions_string(instructions_string: str) -> list[tuple[int, int, int]]:
    instructions = []
    for instruction in instructions_string.split("\n"):
        if instruction.strip():
            numbers = [int(number) for number in re.findall(r"\d+", instruction)]
            instructions.append(tuple(numbers))
    return instructions


def process_input(
    raw_input: str,
) -> tuple[defaultdict[int, deque[str]], list[tuple[int, int, int]]]:
    """Split raw input into starting stacks and instructions"""
    stacks_string, instructions_string = raw_input.split("\n\n")
    stacks = parse_stacks_string(stacks_string)
    instructions = parse_instructions_string(instructions_string)
    return stacks, instructions


def solve(
    stacks: defaultdict[int, deque],
    instructions: list[tuple[int, int, int]],
    move_crates: MoveCratesFunc,
) -> str:
    stacks_copy = deepcopy(stacks)
    moved_stacks = move_crates(stacks_copy, instructions)
    return "".join([stack.pop() for stack in moved_stacks.values()])


def part_1(
    stacks: defaultdict[int, deque], instructions: list[tuple[int, int, int]]
) -> defaultdict[int, deque[str]]:
    """Cratemover 9000 stacking function"""
    for move, source, target in instructions:
        for _ in range(move):
            crate = stacks[source].pop()
            stacks[target].append(crate)
    return stacks


def part_2(
    stacks: defaultdict[int, deque], instructions: list[tuple[int, int, int]]
) -> defaultdict[int, deque[str]]:
    """Cratemover 9001 stacking function"""
    for move, source, target in instructions:
        group = []
        for _ in range(move):
            crate = stacks[source].pop()
            group.append(crate)
        stacks[target].extend(group[::-1])
    return stacks


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.read()

    stacks, instructions = process_input(raw_input)

    part_1_ans = solve(stacks, instructions, part_1)
    print(part_1_ans)

    part_2_ans = solve(stacks, instructions, part_2)
    print(part_2_ans)
