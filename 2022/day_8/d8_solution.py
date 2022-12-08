"""Day 8 solution"""
from functools import reduce

SightLines = tuple[list[int], list[int], list[int], list[int]]
Grid = list[list[int]]


def create_grid(raw_string: str) -> Grid:
    lines = list(filter(None, raw_string.split("\n")))
    return [[int(height) for height in line] for line in lines]


def count_perimiter(grid: Grid) -> int:
    return ((len(grid) + len(grid[0])) * 2) - 4


def get_sight_lines(x: int, y: int, grid: Grid) -> SightLines:
    left = grid[y][:x][::-1]
    right = grid[y][x + 1 :]
    top = [row[x] for row in grid[:y]][::-1]
    bottom = [row[x] for row in grid[y + 1 :]]
    return left, right, top, bottom


def check_visible(height: int, sight_lines: SightLines) -> bool:
    return any([height > max(line) for line in sight_lines if line])


def part_1(grid: Grid) -> int:
    # outer trees always visible
    visible_count = count_perimiter(grid)
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            sight_lines = get_sight_lines(x, y, grid)
            height = grid[y][x]
            if check_visible(height, sight_lines):
                visible_count += 1
    return visible_count


def calc_scenic_score(height: int, sight_lines: SightLines) -> int:
    views = []
    for line in sight_lines:
        if line:
            for i, tree in enumerate(line):
                if tree >= height:
                    break
            views.append(len(line[: i + 1]))
    return reduce(lambda x, y: x * y, views)


def part_2(grid: Grid) -> int:
    max_scenic_score = 0
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            sight_lines = get_sight_lines(x, y, grid)
            height = grid[y][x]
            scenic_score = calc_scenic_score(height, sight_lines)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.read().strip()

    grid = create_grid(raw_input)
    part_1_ans = part_1(grid)
    print(part_1_ans)

    part_2_ans = part_2(grid)
    print(part_2_ans)
