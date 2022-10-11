from __future__ import annotations

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

    def boards_status(self) -> list[bool]:
        status: list[bool] = []
        for i, board in enumerate(self.boards):
            status.append(board.is_finished())
        return status

    def play_turn(self):
        number_to_play = self.moves_to_play.pop(0)
        for board in self.boards:
            board.check_number(number_to_play)
        self.played_moves.append(number_to_play)

    def get_winning_score(self) -> int:
        status: list[bool] = self.boards_status()
        winning_board = [i for i, x in enumerate(status) if x][0]
        board = self.boards[winning_board]
        board_score: int = board.get_score()
        last_called: int = int(self.played_moves[-1])
        return board_score * last_called

    def get_specific_score(self, final_to_win: int) -> int:
        board = self.boards[final_to_win]
        board_score: int = board.get_score()
        last_called: int = int(self.played_moves[-1])
        return board_score * last_called

    @classmethod
    def play_pt_1(cls, file_path):
        print("--- Part 1 ---")
        game = cls.from_file(file_path)
        n_turns = 0
        while not any(game.boards_status()):
            game.play_turn()
            n_turns += 1
        score = game.get_winning_score()
        print(f"Game Over! Took {n_turns} turns.")
        print(f"Winning Score is {score}!")
        print(f"Winning Score is {score == 89001}!")

    @classmethod
    def play_pt_2(cls, file_path):
        final_to_win = -1
        print("--- Part 2 ---")
        game = cls.from_file(file_path)
        n_turns = 0
        while not all(game.boards_status()):
            game.play_turn()
            n_turns += 1
            if game.boards_status().count(False) == 1:
                final_to_win: int = [i for i, x in enumerate(game.boards_status()) if x is False][0]

        print(f"Final Board to win is {final_to_win}")

        # Play until Board is complete
        while game.boards_status()[final_to_win] is False:
            game.play_turn()
        score = game.get_specific_score(final_to_win)
        print(f"Last Board to win's Score is {score}!")
        print(f"Last Board to win's Score is {score == 7296}!")
