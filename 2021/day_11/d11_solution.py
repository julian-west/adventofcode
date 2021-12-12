"""Day 11 Solution"""
from itertools import count


def neighbors(field: dict, point: tuple[int, int]):
    """gives points neighboring a given point"""
    x, y = point
    w = (-1, 0, 1)
    return filter(
        lambda point: point in field,
        ((x + dx, y + dy) for dx in w for dy in w if dx or dy),
    )


def iterate_field(field: dict) -> int:
    """iterate simulation return number of flashes"""
    stack = []
    flashes = set()

    def iter_point(point):
        field[point] += 1
        if field[point] > 9:
            flashes.add(point)
            stack.append(point)

    # increment each point once
    for point in field:
        iter_point(point)

    # increment each point by a flash until we've flashed all flashes
    while stack:
        for point in neighbors(field, stack.pop()):
            # skip points which have already flashed
            if point not in flashes:
                iter_point(point)
    # reset values of flashed out octopuses
    for flash in flashes:
        field[flash] = 0
    return len(flashes)


def part_1(grid: dict[tuple[int, int], int], steps: int = 100) -> int:
    return sum(iterate_field(grid) for _ in range(steps))


def part_2(grid: dict[tuple[int, int], int], steps: int = 100) -> int:
    return next(i for i in count(1) if iterate_field(grid) == steps)


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        field = {}
        for i, row in enumerate(data):
            for j, val in enumerate(row.strip()):
                field[(i, j)] = int(val)

    field_1 = field.copy()
    part_1_ans = part_1(field_1)
    print(part_1_ans)

    part_2_ans = part_2(field)
    print(part_2_ans)
