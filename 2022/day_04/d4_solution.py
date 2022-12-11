"""Day 4 solutions"""

from typing import Callable

OverlapCondition = Callable[[int, int, int, int], int]


def part_1(l1_min: int, l1_max: int, l2_min: int, l2_max: int) -> bool:
    return ((l1_min <= l2_min) & (l1_max >= l2_max)) or (
        (l2_min <= l1_min) & (l2_max >= l1_max)
    )


def part_2(l1_min: int, l1_max: int, l2_min: int, l2_max: int) -> bool:
    return (l1_min <= l2_min <= l1_max) or (l2_min <= l1_min <= l2_max)


def calc_total(sections: list[list[int]], func: OverlapCondition) -> int:
    return sum(func(*item) for item in sections)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as input_data:
        pairs = [pair.strip() for pair in input_data.readlines()]
        sections = [[*map(int, pair.replace("-", ",").split(","))] for pair in pairs]

    part_1_ans = calc_total(sections, part_1)
    print(part_1_ans)

    part_2_ans = calc_total(sections, part_2)
    print(part_2_ans)
