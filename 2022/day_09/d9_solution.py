"""Day 9 Solution"""


def process_input(input_string: str) -> list[tuple[str, int]]:
    instructions = [line.split(" ") for line in input_string.split("\n") if line]
    return [(d, int(n)) for [d, n] in instructions]


def move_tail(hx: int, hy: int, tx: int, ty: int) -> tuple[int, int]:
    dist = abs(hx - tx) + abs(hy - ty)
    if hx == tx and dist >= 2:
        return (tx, hy - 1 if hy > ty else hy + 1)
    if hy == ty and dist >= 2:
        return (hx - 1 if hx > tx else hx + 1, ty)
    if dist > 2:
        if hx > tx:
            return (tx + 1, ty + 1 if hy > ty else ty - 1)
        if hx < tx:
            return (tx - 1, ty + 1 if hy > ty else ty - 1)
    return tx, ty


def solve(instructions: list[tuple[str, int]], knots: int) -> int:
    history = {i: [(0, 0)] for i in range(knots + 1)}
    for direction, steps in instructions:
        for _ in range(steps):
            hx, hy = history[0][-1]
            match direction:
                case "R":
                    hx += 1
                case "L":
                    hx -= 1
                case "U":
                    hy += 1
                case "D":
                    hy -= 1
            history[0].append((hx, hy))
            for k in range(1, knots + 1):
                tx, ty = move_tail(*history[k - 1][-1], *history[k][-1])
                history[k].append((tx, ty))
    return len(set(history[knots]))


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        data = puzzle_input.read().strip()

    instructions = process_input(data)

    part_1_ans = solve(instructions, knots=1)
    print(part_1_ans)

    part_2_ans = solve(instructions, knots=9)
    print(part_2_ans)
