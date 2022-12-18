"""Day 13 solution"""
import ast
from functools import cmp_to_key
from itertools import zip_longest


def process_input(raw_input: str) -> list:
    processed_input = []
    for packet in raw_input.strip().split("\n\n"):
        processed_pair = list(map(ast.literal_eval, packet.split("\n")))
        processed_input.append(processed_pair)

    return processed_input


def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if left > right:
            return 1
        return
    elif isinstance(left, list) and isinstance(right, list):
        for new_left, new_right in zip_longest(left, right):
            if (result := compare(new_left, new_right)) is not None:
                return result
        return
    else:
        new_left = [left] if isinstance(left, int) else left
        new_right = [right] if isinstance(right, int) else right
        return compare(new_left, new_right)


def part_1(packets):
    results = [compare(*packet) for packet in packets]
    true_indices = [index + 1 for index, item in enumerate(results) if item == -1]
    return sum(true_indices)


def part_2(packets):
    div1, div2 = [[2]], [[6]]
    flat_list = [item for sublist in packets for item in sublist]
    sorted_packets = sorted([*flat_list, div1, div2], key=cmp_to_key(compare))
    return (sorted_packets.index(div1) + 1) * (sorted_packets.index(div2) + 1)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.read()

    packets = process_input(raw_input)

    part_1_ans = part_1(packets)
    print(part_1_ans)

    part_2_ans = part_2(packets)
    print(part_2_ans)
