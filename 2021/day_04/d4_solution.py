"""Day 4 Solutions"""
from dataclasses import dataclass, field
from itertools import product
from typing import Optional


@dataclass
class BingoTracker:
    row: list[int]
    col: list[int]
    hits: list[int] = field(default_factory=list)


@dataclass
class WinnersReport:
    num_rounds: int
    index: Optional[int]
    sum_unmarked: int
    final_score: int


class Board:
    def __init__(self, board: list[list[int]]):
        self.bingo = False
        self.board = board
        self.dim = len(board[0])
        self.coordinates = list(product(range(self.dim), range(self.dim)))
        self.tracker = BingoTracker(row=[0] * self.dim, col=[0] * self.dim)

    def play(self, val: int):
        coordinates = self._find_coordinates(val)
        if coordinates:
            self._update_tracker(val, coordinates[0], coordinates[1])
            self._check_bingo()

    def _find_coordinates(self, val: int) -> Optional[tuple[int, int]]:
        """find the coordinates of the value"""
        for (row, col) in self.coordinates:
            if self.board[row][col] == val:
                return row, col
        return None

    def _update_tracker(self, val: int, row: int, col: int):
        """Update bingo tracker"""
        self.tracker.hits.append(val)
        self.tracker.row[row] += 1
        self.tracker.col[col] += 1

    def _check_bingo(self):
        """Check if there is a bingo"""
        if max(self.tracker.row) == self.dim or max(self.tracker.col) == self.dim:
            self.bingo = True


class Game:
    def __init__(self, boards: list[list[list[int]]], draws: list[int]):
        self.boards = [Board(board) for board in boards]
        self.draws = draws
        self.winners_report: Optional[WinnersReport] = None

    def play(self):
        for round, val in enumerate(self.draws):
            for index, board in enumerate(self.boards):
                board.play(val)
                if board.bingo:
                    self.winner = index
                    self._create_winners_report(round, val)
                    break
            else:
                continue
            break

    def play_to_lose(self):
        winning_order = {}
        while len(winning_order) < len(self.boards):
            for round, val in enumerate(self.draws):
                for index, board in enumerate(self.boards):
                    if index not in winning_order:
                        board.play(val)
                        if board.bingo:
                            winning_order[index] = val

        self.winner = list(winning_order.keys())[-1]
        self._create_winners_report(round, winning_order[self.winner])

    def _create_winners_report(self, round: int, last_number: int):
        sum_unmarked = self._get_sum_unmarked(self.boards[self.winner])
        final_score = self._get_final_score(sum_unmarked, last_number)
        self.winners_report = WinnersReport(
            num_rounds=round,
            index=self.winner,
            sum_unmarked=sum_unmarked,
            final_score=final_score,
        )

    def _get_sum_unmarked(self, board: Board) -> int:
        unmarked = [
            board.board[row][col]
            for (row, col) in board.coordinates
            if board.board[row][col] not in board.tracker.hits
        ]
        return sum(unmarked)

    def _get_final_score(self, sum_unmarked: int, last_number: int) -> int:
        return sum_unmarked * last_number


def format_board_input(raw_board: str) -> list[list[int]]:
    """Clean raw input string into list of lists"""
    rows = raw_board.split("\n")
    formatted_rows = []
    for row in rows:
        formatted_rows.append([int(num) for num in row.split(" ") if num])
    return formatted_rows


def part_1(boards: list[list[list[int]]], draws: list[int]) -> int:
    game = Game(boards, draws)
    game.play()
    return game.winners_report.final_score


def part_2(boards: list[list[list[int]]], draws: list[int]) -> int:
    game = Game(boards, draws)
    game.play_to_lose()
    return game.winners_report.final_score


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        line_breaks = input.read().strip().split("\n\n")

    draws = [int(num) for num in line_breaks[0].split(",")]
    boards = list(map(format_board_input, line_breaks[1:]))

    part_1_ans = part_1(boards, draws)
    print(part_1_ans)

    part_2_ans = part_2(boards, draws)
    print(part_2_ans)
