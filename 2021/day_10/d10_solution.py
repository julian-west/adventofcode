"""Day 10 Solution"""
from collections import deque

TRANS_TABLE = str.maketrans("([{<", ")]}>")
SYNTAX_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPL_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def check(s: str) -> tuple[int, int]:
    stack = deque()

    for c in s:
        if c in "([{<":
            stack.append(c.translate(TRANS_TABLE))
        elif stack.pop() != c:
            return SYNTAX_SCORE[c], 0

    score2 = 0
    while stack:
        score2 *= 5
        score2 += COMPL_SCORE[stack.pop()]

    return 0, score2


def part_1(lines: list[str]) -> int:

    tot_syntax = 0
    for line in lines:
        score1, _ = check(line)
        tot_syntax += score1

    return tot_syntax


def part_2(lines: list[str]) -> int:
    autocompl_scores = []
    for line in lines:
        _, score2 = check(line)
        if score2 > 0:
            autocompl_scores.append(score2)
    autocompl_scores_sorted = sorted(autocompl_scores)
    return autocompl_scores_sorted[len(autocompl_scores) // 2]


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        lines = input.read().splitlines()

    part_1_ans = part_1(lines)
    print(part_1_ans)

    part_2_ans = part_2(lines)
    print(part_2_ans)
