"""Day 9 Solution"""
import math


def get_adjacents(grid, i, j):
    adjacents = []
    if i + 1 < len(grid[0]):
        adjacents.append(grid[j][i + 1])
    if i - 1 >= 0:
        adjacents.append(grid[j][i - 1])
    if j + 1 < len(grid):
        adjacents.append(grid[j + 1][i])
    if j - 1 >= 0:
        adjacents.append(grid[j - 1][i])
    return adjacents


def part_1(grid: list[list[int]]) -> int:
    result = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[0])):
            if grid[j][i] < min(get_adjacents(grid, i, j)):
                result += 1 + grid[j][i]
    return result


def count_groups(grid, groups, i, j):
    if (
        j < 0
        or j >= len(grid)
        or i < 0
        or i >= len(grid[0])
        or grid[j][i] == 9
        or grid[j][i] == -1
    ):
        return
    grid[j][i] = -1
    groups[len(groups) - 1] += 1
    count_groups(grid, groups, i + 1, j)
    count_groups(grid, groups, i - 1, j)
    count_groups(grid, groups, i, j + 1)
    count_groups(grid, groups, i, j - 1)


def part_2(grid: list[list[int]]):
    groups = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            groups.append(0)
            count_groups(grid, groups, j, i)
    return math.prod(sorted(groups, reverse=True)[:3])


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        grid = [list(map(int, x)) for x in input.read().splitlines()]

    part_1_ans = part_1(grid)
    print(part_1_ans)

    part_2_ans = part_2(grid)
    print(part_2_ans)
