"""
Day 12 adventofcode
"""
from typing import List, Tuple, Dict


def load_input(file: str) -> List[Tuple[str, int]]:
    """Load input into list"""
    with open(file, "r") as input_file:
        directions = input_file.read().splitlines()

    directions = [(instruction[0], int(instruction[1:])) for instruction in directions]

    return directions


def find_new_direction(cur_direction: str, instruction: str, magnitude: int) -> str:
    """find the new direction of the ship after rotation"""
    compass_degrees = {"N": 0, "E": 90, "S": 180, "W": 270}
    if instruction == "L":
        new_heading = (compass_degrees[cur_direction] - magnitude) % 360
    else:
        new_heading = (compass_degrees[cur_direction] + magnitude) % 360

    return [k for k, v in compass_degrees.items() if v == new_heading][0]


def manhattan_distance(positions_dict: Dict):
    """Calculates the Manhattan distance"""
    n_s = abs(positions_dict["N"] - positions_dict["S"])
    e_w = abs(positions_dict["E"] - positions_dict["W"])

    return n_s + e_w


def part1(directions: List[Tuple[str, int]], start_direction="E"):
    """Returns the Manhattan distance of the final position of the ship"""
    cur_direction = start_direction
    cur_positions = {"N": 0, "S": 0, "E": 0, "W": 0}

    for (instruction, magnitude) in directions:
        if instruction in ["N", "S", "E", "W"]:
            cur_positions[instruction] += magnitude
        elif instruction == "F":
            cur_positions[cur_direction] += magnitude
        elif instruction in ["L", "R"]:
            cur_direction = find_new_direction(cur_direction, instruction, magnitude)

    return manhattan_distance(cur_positions)


if __name__ == "__main__":
    input_directions = load_input("input.txt")

    # Part 1
    print(part1(input_directions))
