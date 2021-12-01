"""Day 1 Solution"""
import numpy as np


def part_1(measurements: list[int]) -> int:
    """Count number of measurements larger than previous"""
    result = [i2 > i1 for i1, i2 in zip(measurements, measurements[1:])]
    return sum(result)


def part_2(measurements: list[int], window: int) -> int:
    """Count number of time sliding window sum is greater than previous"""
    sliding_window_sum = np.convolve(measurements, np.ones(window, dtype=int), "valid")
    return part_1(list(sliding_window_sum))


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        input_values = [int(x) for x in input.read().split()]

    part_1_ans = part_1(input_values)
    print(part_1_ans)

    part_2_ans = part_2(input_values, window=3)
    print(part_2_ans)
