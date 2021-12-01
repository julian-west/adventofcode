"""Adventofcode day 15"""

from typing import List


def run_simulation(starting_seq: List[int], rounds: int) -> int:
    """Run the simulation"""
    state = {
        "last_idx": dict(zip(starting_seq[:-1], range(len(starting_seq) - 1))),
        "last_num": starting_seq[-1],
        "len": len(starting_seq),
    }

    counter = len(starting_seq)
    while counter < rounds:
        last_num = state["last_num"]
        if last_num in state["last_idx"]:
            prev_idx = state["last_idx"][last_num]
            new_num = state["len"] - prev_idx - 1
        else:
            new_num = 0
        state["last_idx"][last_num] = state["len"] - 1
        state["len"] += 1
        state["last_num"] = new_num

        counter += 1
    return state["last_num"]


if __name__ == "__main__":
    puzzle_input = [1, 2, 16, 19, 18, 0]

    # Part 1
    print(run_simulation(puzzle_input, rounds=2020))

    # Part 2
    print(run_simulation(puzzle_input, rounds=30000000))
