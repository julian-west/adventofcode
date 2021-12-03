"""Day 3 solution"""
from collections import Counter


def find_gamma_rate(diagnostic_report: list[str]) -> str:
    """Find the gamma rate from input list of binary representations"""
    gamma_rate_binary = ""
    base = len(diagnostic_report[0])
    for index in range(base):
        index_value_counts = Counter(map(lambda x: x[index], diagnostic_report))
        mode = index_value_counts.most_common()[0][0]
        gamma_rate_binary += mode

    return gamma_rate_binary


def find_epsilon_rate(gamma_rate_binary: str) -> str:
    """Find epsilon rate given the gamma rate binary"""
    return "".join("1" if x == "0" else "0" for x in gamma_rate_binary)


def find_mode(values: list[str], criterion: str) -> str:
    """Find the most or least common binary value depending on the criterion"""
    most_common = Counter(values).most_common()

    if criterion == "most":
        if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
            return "1"
        else:
            return most_common[0][0]
    elif criterion == "least":
        if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
            return "0"
        else:
            return most_common[-1][0]
    else:
        raise ValueError(f"Criterion={criterion}. Must be one of 'most' or 'least'")


def find_rating_binary(
    diagnostic_report: list[str],
    index: int = 0,
    result: str = "",
    criterion: str = "most",
) -> str:
    """Use recursion to find the rating binary value"""

    if index == len(diagnostic_report[0]):
        return result

    bit_values = list(map(lambda x: x[index], diagnostic_report))
    mode = find_mode(bit_values, criterion)
    new_list = list(filter(lambda x: x[index] == mode, diagnostic_report))

    result += mode
    index += 1

    return find_rating_binary(new_list, index, result, criterion)


def part_1(input):
    gamma_rate = find_gamma_rate(input)
    epsilon_rate = find_epsilon_rate(gamma_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_2(input):
    o2_rating_binary = find_rating_binary(input, criterion="most")
    co2_rating_binary = find_rating_binary(input, criterion="least")
    return int(o2_rating_binary, 2) * int(co2_rating_binary, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        diagnostic_report = input.read().strip().split("\n")

    part_1_ans = part_1(diagnostic_report)
    print(part_1_ans)

    part_2_ans = part_2(diagnostic_report)
    print(part_2_ans)
