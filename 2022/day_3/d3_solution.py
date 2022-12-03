"""Day 3 solution"""

import string
from typing import Protocol, Any


class GroupFunc(Protocol):
    def __call__(self, lst: list[str], **kwargs: Any) -> list[list[str]]:
        ...


def find_intersection(*item_strings) -> str:
    intersection = set.intersection(*map(set, item_strings))
    return intersection.pop()


def get_priority(letter: str) -> int:
    priority_order = string.ascii_lowercase + string.ascii_uppercase
    return priority_order.index(letter) + 1


def split_into_compartments(lst):
    def midpoint(lst):
        return len(lst) // 2
    return [[i[: midpoint(i)], i[midpoint(i) :]] for i in lst]


def split_into_groups(lst: list[str], n: int) -> list[list[str]]:
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def calc_total_priority(rucksacks: list[str], grouping_func: GroupFunc, **kwargs):

    groups = grouping_func(rucksacks, **kwargs)

    total = 0
    for group in groups:
        intersection = find_intersection(*group)
        priority = get_priority(intersection[0])
        total += priority
    return total


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as input_file:
        rucksacks = [rucksack.strip() for rucksack in input_file.readlines()]

    part_1_ans = calc_total_priority(rucksacks, split_into_compartments)
    print(part_1_ans)

    part_2_ans = calc_total_priority(rucksacks, split_into_groups, n=3)
    print(part_2_ans)
