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


def get_interim_straight_line_coordinates(
    start: tuple[int, int],
    finish: tuple[int, int],
) -> list[tuple[int, int]]:
    """Get list of coordinates between two points"""
    fixed_axis = 0 if start[0] == finish[0] else 1
    floating_axis = 0 if fixed_axis == 1 else 1
    direction = -1 if finish[floating_axis] - start[floating_axis] < 0 else 1

    interim_coords = []
    for val in range(
        start[floating_axis], finish[floating_axis] + direction, direction
    ):
        coord = [0, 0]
        coord[fixed_axis] = start[fixed_axis]
        coord[floating_axis] = val
        interim_coords.append(tuple(coord))

    return interim_coords


def draw_lines(dim: int, coordinates: list[list[tuple[int, int]]]) -> list[list[int]]:
    """Draw lines on a grid"""
    grid = [[0] * dim for _ in range(dim)]

    for coordinate in coordinates:
        if coordinate[0][0] == coordinate[1][0] or coordinate[0][1] == coordinate[1][1]:
            interim_coords = get_interim_straight_line_coordinates(
                coordinate[0], coordinate[1]
            )

            for coord in interim_coords:
                grid[coord[1]][coord[0]] += 1

    return grid


def part_1(coordinates: list[list[tuple[int, int]]]) -> int:
    """Calculate number of points where at least two lines overlap"""
    dim = find_max_coordinate(coordinates) + 1
    grid = draw_lines(dim, coordinates)
    flatten = [item for sublist in grid for item in sublist]
    return sum(i > 1 for i in flatten)


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        lines = input.readlines()
        coordinates = [process_input_line(line) for line in lines]

    part_1_ans = part_1(coordinates)
    print(part_1_ans)
