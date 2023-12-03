MAX_ALLOWED_RED_CUBES = 12
MAX_ALLOWED_GREEN_CUBES = 13
MAX_ALLOWED_BLUE_CUBES = 14


def process_input(file):
    with open(file, "r", encoding="utf-8") as input_values:
        games = [line.strip("\n") for line in input_values.readlines()]

    puzzle_input = {}
    for game in games:
        id, picks = game.split(":")
        id = id.split(" ")[-1]
        rounds = [round.strip() for round in picks.split(";")]
        rounds_list = []
        for cube_set in rounds:
            cubes_list = []
            cubes = cube_set.split(",")
            for cube in cubes:
                cube = cube.strip()
                count = cube.split(" ")[0]
                color = cube.split(" ")[1]
                cubes_list.append((int(count), color))

            rounds_list.append(cubes_list)

        puzzle_input[int(id)] = rounds_list

    return puzzle_input


def is_fine(cube) -> bool:
    return (
        cube[1] == "red"
        and cube[0] <= MAX_ALLOWED_RED_CUBES
        or cube[1] == "green"
        and cube[0] <= MAX_ALLOWED_GREEN_CUBES
        or cube[1] == "blue"
        and cube[0] <= MAX_ALLOWED_BLUE_CUBES
    )


def part_1(games):
    invalid_games = set()
    for game_id, cube_sets in games.items():
        for cube_set in cube_sets:
            for cube in cube_set:
                if not is_fine(cube):
                    invalid_games.add(game_id)
                    break

    valid_game_ids = [game_id for game_id in games if game_id not in invalid_games]
    return sum(valid_game_ids)


def set_minimum_cubes(minimum_cubes, cube_set):
    for cube in cube_set:
        if minimum_cubes.get(cube[1], 0) < cube[0]:
            minimum_cubes[cube[1]] = cube[0]


def part_2(games):
    count = 0
    for cube_sets in games.values():
        power_count = 1
        minimum_cubes = {}
        for cube_set in cube_sets:
            for _ in cube_set:
                set_minimum_cubes(minimum_cubes, cube_set)

        for required in minimum_cubes.values():
            power_count *= required

        count += power_count
    return count


if __name__ == "__main__":
    puzzle_input = process_input("input.txt")

    part_1_ans = part_1(puzzle_input)
    print(part_1_ans)

    part_2_ans = part_2(puzzle_input)
    print(part_2_ans)
