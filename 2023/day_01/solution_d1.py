"""Day 1 Solution"""
import re


def part_1(calibration_lines: list[str]) -> int:
    # get list of calibration values
    calibration_values = []
    for line in calibration_lines:
        calibration_value = ""
        # first digit
        for char in line:
            if char.isnumeric():
                calibration_value += char
                break
        # last digit
        for char in line[::-1]:
            if char.isnumeric():
                calibration_value += char
                break
        calibration_values.append(int(calibration_value))
    return sum(calibration_values)


def find_first_and_last_number(line):
    WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    NUMBER_PAT = re.compile(f"(?=([0-9]|{'|'.join(WORDS)}))")

    matches = NUMBER_PAT.findall(line)
    first, last = matches[0], matches[-1]

    if first in WORDS:
        first = str(WORDS.index(first) + 1)

    if last in WORDS:
        last = str(WORDS.index(last) + 1)

    return int(first + last)


def part_2(calibration_lines: list[str]) -> int:
    calibration_values = []
    for line in calibration_lines:
        value = find_first_and_last_number(line)
        calibration_values.append(value)
    return sum(calibration_values)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as input_values:
        calibration_lines = [line.strip("\n") for line in input_values.readlines()]

    part_1_ans = part_1(calibration_lines)
    print(part_1_ans)

    part_2_ans = part_2(calibration_lines)
    print(part_2_ans)
