"""Day 5 solution"""


def find_max_coordinate(coordinates: list[list[tuple[int, int]]]) -> int:
    """Find the maximum coordinates from the list of coordinates"""
    flatten = [t for sublist in coordinates for li in sublist for t in li]
    return max(flatten)


def process_input_line(line: str) -> list[tuple[int, int]]:
    """convert raw input line string into list of tuples"""
    raw_coordinates = line.strip().split(" -> ")

    coordinates = []
    for coordinate in raw_coordinates:
        x, y = coordinate.split(",")
        coordinates.append((int(x), int(y)))

    return coordinates


def bresenham_algo(x0: int, y0: int, x1: int, y1: int) -> list[tuple[int, int]]:
    """Bresenham algo for finding point on a line

    Based off:
        en.wikipedia.org/wiki/Bresenham's_line_algorithm
        and
        https://github.com/encukou/bresenham/blob/master/bresenham.py
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
        if D >= 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy


def draw_lines(dim: int, coordinates: list[list[tuple[int, int]]]) -> list[list[int]]:
    """Draw lines on a grid"""
    grid = [[0] * dim for _ in range(dim)]
    for (x0, y0), (x1, y1) in coordinates:
        interim_coords = list(bresenham_algo(x0, y0, x1, y1))
        for coord in interim_coords:
            grid[coord[1]][coord[0]] += 1
    return grid


def calc_overlapping(grid: list[list[int]]) -> int:
    """Calculate number of overlapping lines"""
    flatten = [item for sublist in grid for item in sublist]
    return sum(i > 1 for i in flatten)


def solve(dim: int, coordinates: list[list[tuple[int, int]]]) -> int:
    """Calculate number of points where at least two lines overlap"""
    grid = draw_lines(dim, coordinates)
    return calc_overlapping(grid)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        lines = input.readlines()
        coordinates = [process_input_line(line) for line in lines]

    dim = find_max_coordinate(coordinates) + 1
    straightline_coords = list(
        filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], coordinates)
    )

    part_1_ans = solve(dim, straightline_coords)
    print(part_1_ans)

    part_2_ans = solve(dim, coordinates)
    print(part_2_ans)
