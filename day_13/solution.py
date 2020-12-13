"""
Day 13 adventofcode
"""
from typing import Tuple, Set


def load_input(file: str) -> Tuple[int, Set[int]]:
    """Load input file"""
    with open(file, "r") as input_file:
        lines = input_file.read().splitlines()

    earliest_time = int(lines[0])
    bus_ids = set(int(bus) for bus in lines[1].split(",") if bus != "x")
    return earliest_time, bus_ids


def part1(earliest_time: int, bus_ids: Set[int]) -> int:
    """Find the earliest bus you can take

    Return the bus ID by the number of minutes you have to wait
    """
    time = earliest_time
    while True:
        for bus in bus_ids:
            if time % bus == 0:
                return bus * (time - earliest_time)

        time += 1


if __name__ == "__main__":
    earliest_time, bus_ids = load_input("input.txt")

    # Part 1
    print(part1(earliest_time, bus_ids))
