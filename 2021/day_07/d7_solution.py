"""Day 7 Solution"""
from functools import lru_cache


@lru_cache(maxsize=2000)
def gauss(x):
    return x * (x + 1) // 2


def part_1(sorted_pos: list[int]) -> int:
    num_crabs = len(sorted_pos)
    mid = sorted_pos[num_crabs // 2]
    return sum(abs(x - mid) for x in sorted_pos)


def part_2(sorted_pos: list[int]) -> int:
    num_crabs = len(sorted_pos)
    mean = sum(sorted_pos) // num_crabs
    return sum(gauss(abs(x - mean)) for x in sorted_pos)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        sorted_pos = sorted([int(x) for x in input.read().split(",")])

    part_1_ans = part_1(sorted_pos)
    print(part_1_ans)

    part_2_ans = part_2(sorted_pos)
    print(part_2_ans)
