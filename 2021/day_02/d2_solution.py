"""Day 2 Solution"""
from typing import List, Tuple


def part_1(instructions: List[Tuple[str, int]]) -> int:

    hz, dp = 0, 0
    for ins in instructions:
        if ins[0] == "down":
            dp += ins[1]
        elif ins[0] == "up":
            dp -= ins[1]
        elif ins[0] == "forward":
            hz += ins[1]

    return hz * dp


def part_2(instructions: List[Tuple[str, int]]) -> int:

    hz, dp, aim = 0, 0, 0

    for ins in instructions:
        if ins[0] == "down":
            aim += ins[1]
        elif ins[0] == "up":
            aim -= ins[1]
        elif ins[0] == "forward":
            hz += ins[1]
            dp += aim * ins[1]

    return hz * dp


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        input_values = [line.split(" ") for line in input.read().strip().split("\n")]
        input_clean = [(ins[0], int(ins[1])) for ins in input_values]

    part_1_ans = part_1(input_clean)
    print(part_1_ans)

    part_2_ans = part_2(input_clean)
    print(part_2_ans)
