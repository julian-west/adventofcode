"""Day 20 Solution"""
from functools import cache

die = 0


def roll():
    global die
    die += 1
    return die


@cache
def count_win(p1: int, p2: int, s1: int, s2: int):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    ans = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                new_p1 = (p1 + d1 + d2 + d3) % 10
                new_s1 = s1 + new_p1 + 1

                x1, y1 = count_win(p2, new_p1, s2, new_s1)
                ans = (ans[0] + y1, ans[1] + x1)
    return ans


def part_1(p1: int, p2: int, s1: int, s2: int) -> int:
    while True:
        m1 = roll() + roll() + roll()
        p1 = (p1 + m1) % 10
        s1 += p1 + 1
        if s1 >= 1000:
            break

        m2 = roll() + roll() + roll()
        p2 = (p2 + m2) % 10
        s2 += p2 + 1
        if s2 >= 1000:
            break
    return min(s1, s2) * die


def part_2(p1: int, p2: int, s1: int, s2: int) -> int:
    return max(count_win(p1, p2, s1, s2))


if __name__ == "__main__":

    # puzzle input
    p1, p2 = 6, 3

    part_1_ans = part_1(p1 - 1, p2 - 1, 0, 0)
    print(part_1_ans)

    part_2_ans = part_2(p1 - 1, p2 - 1, 0, 0)
    print(part_2_ans)
