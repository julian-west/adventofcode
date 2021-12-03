"""Day 3 solution"""
from collections import Counter


def find_gamma_rate(diagnostic_report: list[str]) -> str:
    """Find the gamma rate from input list of binary representations"""
    gamma_rate_binary = ""
    base = len(diagnostic_report[0])
    for index in range(base):
        index_values = map(lambda x: x[index], diagnostic_report)
        counts = Counter(index_values)
        mode = counts.most_common()[0][0]
        gamma_rate_binary += mode

    return gamma_rate_binary


def find_epsilon_rate(gamma_rate_binary: str) -> str:
    """Find epsilon rate given the gamma rate binary"""
    return "".join("1" if x == "0" else "0" for x in gamma_rate_binary)


def part_1(input):
    gamma_rate = find_gamma_rate(input)
    epsilon_rate = find_epsilon_rate(gamma_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        diagnostic_report = input.read().strip().split("\n")

    part_1_ans = part_1(diagnostic_report)
    print(part_1_ans)
