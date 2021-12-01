"""
Day 13 adventofcode
"""
from typing import Tuple, List
from functools import reduce


def load_input(file: str) -> Tuple[int, List[str]]:
    """Load input file"""
    with open(file, "r") as input_file:
        lines = input_file.read().splitlines()

    return int(lines[0]), lines[1].split(",")


def part1(earliest_time: int, bus_ids: List[str]) -> int:
    """Find the earliest bus you can take

    Return the bus ID by the number of minutes you have to wait
    """
    time = earliest_time
    bus_id_set = set(int(bus) for bus in bus_ids if bus != "x")
    while True:
        for bus in bus_id_set:
            if time % bus == 0:
                return bus * (time - earliest_time)
        time += 1


def part2(bus_ids: List[str]) -> int:
    """Find the earliest time that the buses depart sequentially

    This will take too long to run using brute force. Can use the Chinese
    Remainder Theorem as all the bus ids are prime numbers

    https://brilliant.org/wiki/chinese-remainder-theorem/

    """

    def crt(times: List[int], offsets: List[int]) -> int:
        """Chinese remainder theorem"""
        N = reduce(lambda a, b: a * b, times)
        x = sum(
            offset * (N // time) * pow(N // time, -1, time)
            for offset, time in zip(offsets, times)
        )

        return x % N

    buses = [(i, int(bus)) for i, bus in enumerate(bus_ids) if bus != "x"]
    offsets = [time - i for i, time in buses]
    times = [t for _, t in buses]

    return crt(times, offsets)


if __name__ == "__main__":
    earliest_time, bus_ids = load_input("input.txt")

    # Part 1
    print(part1(earliest_time, bus_ids))

    # Part 2
    print(part2(bus_ids))
