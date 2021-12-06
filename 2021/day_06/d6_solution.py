"""Day 6 Solution"""
from collections import deque


def solve(
    initial_state: list[int],
    days: int,
    new_spawn_start_timer: int = 9,
    rejuvenate_start_timer: int = 6,
) -> int:
    fish_stats = [0] * new_spawn_start_timer

    for fish in initial_state:
        fish_stats[fish] += 1

    Q = deque(fish_stats)

    for _ in range(days):
        spawn = Q.popleft()
        Q[rejuvenate_start_timer] += spawn
        Q.append(spawn)

    return sum(Q)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        start_timers = [int(x) for x in input.read().split(",")]

    part_1_ans = solve(start_timers, 80)
    print(part_1_ans)

    part_2_ans = solve(start_timers, 256)
    print(part_2_ans)
