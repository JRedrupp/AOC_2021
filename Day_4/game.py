from __future__ import annotations

from typing import Optional

from models import BingoBoard


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
