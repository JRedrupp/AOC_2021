from __future__ import annotations

from game import Game


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
