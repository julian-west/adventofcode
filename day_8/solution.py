"""
Day 8
"""
from typing import List, Tuple


def load_input(file: str) -> List:
    """Load input into list of instructions"""
    with open(file, "r") as input_file:
        instructions = input_file.read().splitlines()

    return instructions


def part1(instructions: List) -> Tuple:
    """Return whether it is a valid set of instructions and the value of the acc

    The set of instructions are valid if the program terminates by trying to
    execute an instruction immediately after the final instruction in the file

    """

    acc = 0
    index = 0
    memo = set()
    while True:
        if index in memo:
            break
        memo.add(index)

        cmd, step = instructions[index].split()

        if cmd == "acc":
            acc += int(step)
            index += 1
        elif cmd == "jmp":
            index += int(step)
        elif cmd == "nop":
            index += 1

        if index == len(instructions):
            return True, acc
        if index > len(instructions):
            return False, acc

    return False, acc


def part2(instructions: List) -> int:
    """Brute force approach

    Sequentially swap and evaluate each instruction to get a valid set of
    instructions

    Returns the index of erroneous instruction and the value of the accumulator
    when the correct set of instructions are run

    """

    for index, instruction in enumerate(instructions):
        tmp_instructions = instructions.copy()

        cmd, step = instruction.split()

        if cmd == "jmp":
            tmp_instructions[index] = f"nop {step}"

        elif cmd == "nop":
            tmp_instructions[index] = f"nop {step}"

        valid, acc = part1(tmp_instructions)

        if valid:
            return index, acc

    return "No possible solution"


if __name__ == "__main__":
    boot_instructions = load_input("input.txt")

    # Part 1
    print(part1(boot_instructions))

    # Part 2
    print(part2(boot_instructions))
