"""Day 13 solution"""

from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int


@dataclass
class Fold:
    axis: str
    val: int


def fold_grid(points: list[Point], fold: Fold) -> list[Point]:
    """Apply fold transformation to points on the grid"""
    points = points.copy()
    for i, point in enumerate(points):
        if fold.axis == "x" and point.x > fold.val:
            points[i] = Point(x=2 * fold.val - point.x, y=point.y)
        elif fold.axis == "y" and point.y > fold.val:
            points[i] = Point(x=point.x, y=2 * fold.val - point.y)
    return points


def find_max_xy(points: list[Point]) -> tuple[int, int]:
    """Find the maximum values for x and y on the current grid"""
    return max(point.x for point in points), max(point.y for point in points)


def print_grid(points: list[Point]) -> None:
    """Print the current state of the grid"""
    # get boundary coordinates for current grid
    max_x, max_y = find_max_xy(points)
    print(
        "\n".join(
            "".join("#" if Point(x, y) in points else "." for x in range(max_x + 1))
            for y in range(max_y + 1)
        )
    )


def part_1(points: list[Point], fold: Fold) -> int:
    """calc number of visible dots after first fold"""
    points = fold_grid(points, fold)
    return len(set(points))


def part_2(points: list[Point], folds: list[Fold]) -> None:
    """print the final code"""
    for fold in folds:
        points = fold_grid(points, fold)
    print_grid(points)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        points, folds = input.read().split("\n\n")
        points = [
            Point(*tuple(map(int, point.split(",")))) for point in points.splitlines()
        ]
        folds = [
            Fold(*(axis[-1], int(val)))
            for fold in folds.splitlines()
            for axis, val in [fold.split("=")]
        ]

    part_1_ans = part_1(points, folds[0])
    print(part_1_ans)

    part_2(points, folds)
