from __future__ import annotations

from copy import copy
from dataclasses import dataclass, field


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
