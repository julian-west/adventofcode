"""
adventofcode.com/2020/day/5

The first 7 characters denote the row position
The last 3 characters denote the column position
"""
from typing import List, Tuple
import math


def load_input(file: str) -> List:
    with open(file, "r") as f:
        seats = f.read().splitlines()

    return seats


def find_number(string: str, min: int, max: int) -> int:

    for letter in string:
        if letter == "R" or letter == "B":
            min = math.ceil((max + min) / 2)
        if letter == "L" or letter == "F":
            max = (max + min) // 2
    assert max == min
    return max


def find_seat(string: str) -> Tuple:

    row_letters = string[:7]
    column_letters = string[7:]

    row = find_number(row_letters, min=0, max=127)
    column = find_number(column_letters, min=0, max=7)

    return row, column


def find_seat_id(row: int, column: int) -> int:
    return (row * 8) + column


def find_highest_seat_id(seats: List) -> int:

    seat_ids = []
    for seat in seats:
        row, column = find_seat(seat)
        seat_id = find_seat_id(row, column)
        seat_ids.append(seat_id)

    return max(seat_ids)


def get_possible_ids(max_rows: int = 127, max_columns: int = 7) -> List:

    seat_ids = []
    for row in range(max_rows):
        for col in range(max_columns):
            seat_ids.append(row * 8 + col)

    return seat_ids


def get_seat_ids(seats: List) -> List:

    seat_ids = []
    for seat in seats:
        row, column = find_seat(seat)
        seat_id = find_seat_id(row, column)
        seat_ids.append(seat_id)

    return seat_ids


if __name__ == "__main__":
    seats = load_input("input.txt")

    # part 1
    print(find_highest_seat_id(seats))

    possible_seat_ids = get_possible_ids()
    actual_seat_ids = get_seat_ids(seats)

    # part 2
    # your seat id is the seat id which does not have an adjacent id in this
    # list
    print(list(set(possible_seat_ids) - set(actual_seat_ids)))
