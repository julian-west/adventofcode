"""
Day 6: adventofcode.com/2020/day/6
"""
from collections import Counter


def load_input(file):
    """Load groups"""

    with open(file, "r") as f:
        lines = f.read()

    groups = lines.split("\n\n")
    return groups


def count_unique_letters(group):
    """Part 1 function: count number of unique questions in the group"""
    questions = "".join(group.split("\n"))
    letter_count = Counter(list(questions))

    return len(letter_count)


def count_all_yes_questions(group):
    """Part 2 function: count number of questions where everyone answered
    yes"""
    group = list(filter(None, group.split("\n")))
    num_individuals = len(group)
    questions = "".join(group)
    letter_count = Counter(list(questions))

    return sum(value == num_individuals for value in letter_count.values())


if __name__ == "__main__":
    groups = load_input("input.txt")

    # Part 1
    counts = []
    for group in groups:
        count = count_unique_letters(group)
        counts.append(count)

    print(sum(counts))

    # Part 2
    counts = []
    for group in groups:
        count = count_all_yes_questions(group)
        counts.append(count)

    print(sum(counts))
