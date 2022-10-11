from __future__ import annotations

from game import Game


def main(file_path):
    Game.play_pt_1(file_path)

    Game.play_pt_2(file_path)


if __name__ == '__main__':
    main('input.txt')
