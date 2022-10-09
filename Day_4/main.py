from __future__ import annotations

from copy import copy
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BoardPlace:
    number: str = field(default_factory=str)
    picked: bool = False

    @classmethod
    def from_str(cls, number: str = "") -> BoardPlace:
        return cls(number)

    def check_number(self, number_to_play: str):
        if number_to_play == self.number:
            self.picked = True


@dataclass
class BingoBoard:
    board_places: list[list[BoardPlace]]

    def __post_init__(self):
        self.column_length: int = len(self.board_places[0])
        self.row_length: int = len(self.board_places)

    @classmethod
    def from_str(cls, board_str: str) -> BingoBoard:
        # Example board_str -> '\n 3 55 15 54 81\n56 77 20 99 25\n90 57 67  0 97\n28 45 69 84 14\n91 94 39 36 85'

        board_rows: list[str] = [x for x in board_str.split("\n") if x]

        base_board = cls.create_empty_board_array(len(board_rows))

        for row_index, row in enumerate(board_rows):
            numbers = [y for y in row.split(" ") if y]
            col_index: int
            for col_index, number in enumerate(numbers):
                base_board[row_index][col_index] = BoardPlace.from_str(number)
        return BingoBoard(board_places=base_board)

    @classmethod
    def create_empty_board_array(cls, board_len) -> list[list[BoardPlace]]:
        # initialise empty board
        base_first_row: list[BoardPlace] = [BoardPlace()] * board_len
        base_board = []
        for _ in range(board_len):
            base_board.append(copy(base_first_row))
        return base_board

    def is_finished(self) -> bool:
        """
        Work out if a board is finished.
        """
        if self.rows_finished():
            return True
        if self.columns_finished():
            return True
        return False

    def rows_finished(self) -> bool:
        for row in self.board_places:
            finished: list[bool] = [bp.picked for bp in row]
            if all(finished):
                return True
        return False

    def columns_finished(self) -> bool:
        for col_index in range(self.column_length):
            finished: list[bool] = [bp.picked for bp in self.extract_column(col_index)]
            if all(finished):
                return True
        return False

    def extract_column(self, col_index: int) -> list[BoardPlace]:
        return [row[col_index] for row in self.board_places]

    def check_number(self, number_to_play: str):
        # TODO: Add custom __iter__
        for row in self.board_places:
            for bp in row:
                bp.check_number(number_to_play)

    def get_score(self) -> int:
        score = 0
        # TODO: Add custom __iter__
        for row in self.board_places:
            for bp in row:
                if not bp.picked:
                    score += int(bp.number)
        return score


class Game:
    def __init__(self, moves_to_play=None, bingo_boards=None):
        if bingo_boards is None:
            bingo_boards = []
        if moves_to_play is None:
            moves_to_play = []
        self.moves_to_play: list[str] = moves_to_play
        self.played_moves: list[str] = []
        self.boards: list[BingoBoard] = bingo_boards

    @classmethod
    def from_file(cls, path: str) -> Game:
        bingo_boards: list[BingoBoard] = []
        with open(path, "r") as txt_file:
            instruction_set: list[str] = txt_file.readline().split(",")

            boards_to_parse: list[str] = txt_file.read().split("\n\n")
            for board_str in boards_to_parse:
                bingo_boards.append(BingoBoard.from_str(board_str))
        return Game(moves_to_play=instruction_set, bingo_boards=bingo_boards)

    def is_over(self) -> tuple[Optional[int], bool]:
        # TODO: Split this back out to separate responsibility
        for i, board in enumerate(self.boards):
            if board.is_finished():
                return i, True
        return None, False

    def play_turn(self):
        number_to_play = self.moves_to_play.pop(0)
        for board in self.boards:
            board.check_number(number_to_play)
        self.played_moves.append(number_to_play)

    def get_winning_score(self) -> int:
        winning_board, _ = self.is_over()
        board = self.boards[winning_board]
        board_score: int = board.get_score()
        last_called: int = int(self.played_moves[-1])
        return board_score * last_called


def main(file_path):
    game = Game.from_file(file_path)
    n_turns = 0
    while not game.is_over()[1]:
        game.play_turn()
        n_turns += 1
    score = game.get_winning_score()
    print(f"Game Over! Took {n_turns} turns.")
    print(f"Winning Score is {score}")


if __name__ == '__main__':
    main('input.txt')
