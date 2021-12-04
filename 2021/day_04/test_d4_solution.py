"""Day 4 Solution Tests"""

import pytest
from d4_solution import Board, format_board_input, part_1, part_2

# fmt:off
draws = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
# fmt: on

raw_board = (
    "62  5 77 94 75\n59 10 23 44 29\n93 91 63 51 74\n22 14 15  2 55\n78 18 95 58 57"
)

boards = [
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],
    [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ],
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
]


def test_format_board():
    """Test formatting the raw board input from string to list of lists"""
    assert format_board_input(raw_board) == [
        [62, 5, 77, 94, 75],
        [59, 10, 23, 44, 29],
        [93, 91, 63, 51, 74],
        [22, 14, 15, 2, 55],
        [78, 18, 95, 58, 57],
    ]


def test_dim():
    assert Board(boards[0]).dim == 5


@pytest.mark.parametrize(
    "board,value,expected",
    [
        (boards[0], 22, (0, 0)),
        (boards[0], 10, (3, 1)),
        (boards[0], 3, (3, 2)),
        (boards[0], 99, None),
    ],
)
def test__find_coordinates(board, value, expected):
    playing_board = Board(board)
    assert playing_board._find_coordinates(value) == expected


@pytest.mark.parametrize(
    "board,rounds,draws,expected",
    [
        (boards[0], 5, draws, [7, 4, 9, 5, 11]),
        (boards[1], 5, draws, [7, 4, 9, 5, 11]),
        (boards[1], 11, draws, [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21]),
    ],
)
def test_play(board, rounds, draws: list[int], expected: list[int]):
    """Check number of hits is correct after X rounds"""
    playing_board = Board(board)
    for val in draws[:rounds]:
        playing_board.play(val)
    assert playing_board.tracker.hits == expected


def test_part_1():
    assert part_1(boards, draws) == 4512


def test_part_2():
    assert part_2(boards, draws) == 1924
