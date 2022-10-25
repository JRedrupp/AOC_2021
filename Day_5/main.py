"""
Main file for running AOC Day5
"""

from __future__ import annotations

from grid import Grid


def main(file_name: str):
    """
    Main Entrypoint
    :param file_name:
    :return:
    """
    grid = Grid.from_file(file_name)
    overlaps = grid.find_number_of_overlaps_gt_n(2)
    print(overlaps)
    print(f"Answer is {20500 == overlaps}")


if __name__ == '__main__':
    main('input.txt')
