"""Day 2 solutions"""
from typing import Callable

SHAPE_SCORE = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
ROUND_SCORE = {"L": 0, "D": 3, "W": 6, "X": 0, "Y": 3, "Z": 6}

OUTCOMES = {
    "A X": "D",
    "A Y": "W",
    "A Z": "L",
    "B X": "L",
    "B Y": "D",
    "B Z": "W",
    "C X": "W",
    "C Y": "L",
    "C Z": "D",
}

REQUIRED_SELECTION = {
    "A X": "C",
    "A Y": "A",
    "A Z": "B",
    "B X": "A",
    "B Y": "B",
    "B Z": "C",
    "C X": "B",
    "C Y": "C",
    "C Z": "A",
}

RuleFunc = Callable[[str], int]


def part_1(moves: str) -> int:
    result = OUTCOMES[moves]
    my_move = moves[-1]
    return SHAPE_SCORE[my_move] + ROUND_SCORE[result]


def part_2(moves: str) -> int:
    result = moves[-1]
    my_move = REQUIRED_SELECTION[moves]
    return SHAPE_SCORE[my_move] + ROUND_SCORE[result]


def calc_total_score(strategy_guide: list[str], rule_func: RuleFunc) -> int:
    round_scores = []
    for moves in strategy_guide:
        round_score = rule_func(moves)
        round_scores.append(round_score)

    return sum(round_scores)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as input_file:
        raw_strategy_guide = input_file.readlines()
        strategy_guide = [line.strip() for line in raw_strategy_guide]

    part_1_ans = calc_total_score(strategy_guide, part_1)
    print(part_1_ans)

    part_2_ans = calc_total_score(strategy_guide, part_2)
    print(part_2_ans)
