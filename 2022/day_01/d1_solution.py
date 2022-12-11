"""Day 1 solution"""


def process_input(raw_elf_calories: str) -> list[list[str]]:
    """Read the text file and read into a list of lists containing calories for each elf"""
    calories = raw_elf_calories.split("\n\n")
    elf_calories = [list(filter(None, elf.split("\n"))) for elf in calories]

    return elf_calories


def aggregate_calories(elf_calories: list[list[str]]) -> list[int]:
    """Sum the calories for all elves"""
    return [sum(int(item) for item in calories) for calories in elf_calories]


def part_1(aggregated_calories: list[int]) -> int:
    """Max calories carried by an elf"""
    return max(aggregated_calories)


def part_2(aggregated_calories: list) -> int:
    """Return sum of top three calorie carrying elves"""
    sorted_elf_calories = sorted(aggregated_calories, reverse=True)
    top_3 = sorted_elf_calories[:3]
    return sum(top_3)


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as input_values:
        raw_elf_calories = input_values.read()

    elf_calories = process_input(raw_elf_calories)
    aggregated_calories = aggregate_calories(elf_calories)

    part_1_ans = part_1(aggregated_calories)
    print(part_1_ans)

    part_2_ans = part_2(aggregated_calories)
    print(part_2_ans)
