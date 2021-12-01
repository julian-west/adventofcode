"""
Day 12 adventofcode
"""
from typing import Dict, List, Tuple


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


def manhattan_distance(positions_dict: Dict[str, int]) -> int:
    """Calculates the Manhattan distance"""
    n_s = abs(positions_dict["N"] - positions_dict["S"])
    e_w = abs(positions_dict["E"] - positions_dict["W"])

    return n_s + e_w


def part1(directions: List[Tuple[str, int]], start_direction="E") -> int:
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


def find_new_waypoint(
    waypoint: Dict[str, int], instruction: str, magnitude: int
) -> Dict[str, int]:
    """Find the new position of the waypoint - rotate left or right by magnitude"""
    compass = ["N", "E", "S", "W"]
    shift = int((magnitude / 90) % 4)

    if instruction == "R":
        new_compass_positions = compass[shift:] + compass[:shift]
    elif instruction == "L":
        new_compass_positions = compass[-shift:] + compass[:-shift]

    new_waypoint = {}
    for old_dir, new_dir in zip(compass, new_compass_positions):
        new_waypoint[new_dir] = waypoint[old_dir]

    return new_waypoint


def part2(directions: List[Tuple[str, int]], waypoint: Dict) -> int:
    """Returns the Manhattan distance of the final position of the ship for part2"""
    cur_positions = {"N": 0, "S": 0, "E": 0, "W": 0}

    for (instruction, magnitude) in directions:
        if instruction in ["N", "S", "E", "W"]:
            waypoint[instruction] += magnitude
        elif instruction == "F":
            for direction in cur_positions:
                cur_positions[direction] += waypoint[direction] * magnitude
        elif instruction in ["L", "R"]:
            waypoint = find_new_waypoint(waypoint, instruction, magnitude)

    return manhattan_distance(cur_positions)


if __name__ == "__main__":
    input_directions = load_input("input.txt")

    # Part 1
    print(part1(input_directions))

    # Part 2
    print(part2(input_directions, waypoint={"N": 1, "E": 10, "S": 0, "W": 0}))
