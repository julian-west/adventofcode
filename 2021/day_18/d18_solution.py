"""Day 18 Solution"""

import functools


def add(proc_sn1: list[list[int]], proc_sn2: list[list[int]]) -> list[list[int]]:
    sum_sn = [[entry[0], entry[1] + 1] for entry in proc_sn1 + proc_sn2]
    updated = True
    while updated:
        updated = False
        for i in range(len(sum_sn)):
            depth = sum_sn[i][1]
            if depth >= 5 and depth == sum_sn[i + 1][1]:
                if i > 0:
                    sum_sn[i - 1][0] += sum_sn[i][0]
                if i < len(sum_sn) - 2:
                    sum_sn[i + 2][0] += sum_sn[i + 1][0]
                del sum_sn[i : i + 2]
                sum_sn.insert(i, [0, depth - 1])
                updated = True
                break
        if not updated:
            for i in range(len(sum_sn)):
                if sum_sn[i][0] > 9:
                    [val, depth] = sum_sn[i]
                    half_rounded_down = val // 2
                    half_rounded_up = val - val // 2
                    del sum_sn[i]
                    sum_sn.insert(i, [half_rounded_up, depth + 1])
                    sum_sn.insert(i, [half_rounded_down, depth + 1])
                    updated = True
                    break
    return sum_sn


def magnitude(proc_sn: list[list[int]]) -> int:
    while len(proc_sn) > 1:
        for i in range(len(proc_sn)):
            if i < len(proc_sn) - 1 and proc_sn[i][1] == proc_sn[i + 1][1]:
                depth = proc_sn[i][1]
                val = proc_sn[i][0] * 3 + proc_sn[i + 1][0] * 2
                del proc_sn[i : i + 2]
                proc_sn.insert(i, [val, depth - 1])
                break
    return proc_sn[0][0]


def process_lines(input_lines: list[str]) -> list:
    processed = []
    for line in input_lines:
        processed_line = []
        depth = 0
        for c in line:
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
            elif c == ",":
                pass
            else:
                processed_line.append([int(c), depth])
        processed.append(processed_line)

    return processed


def part_1(processed: list) -> int:
    return magnitude(functools.reduce(add, processed))


def part_2(processed: list) -> int:
    res = 0
    for i in range(len(processed) - 1):
        for j in range(i + 1, len(processed)):
            res = max(res, magnitude(add(processed[i], processed[j])))
            res = max(res, magnitude(add(processed[j], processed[i])))
    return res


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    processed = process_lines(lines)

    part_1_ans = part_1(processed)
    print(part_1_ans)

    part_2_ans = part_2(processed)
    print(part_2_ans)
