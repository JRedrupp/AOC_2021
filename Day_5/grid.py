from __future__ import annotations

from copy import copy
from dataclasses import dataclass
from typing import Tuple, Any

from vector import Vector
from point import Point


@dataclass
class Grid:
    vectors: list[Vector]

    def __post_init__(self):
        self.max_x, self.max_y = self.find_max_xy(self.vectors)
        self.board: list[list[int]] = self.create_board()

    @classmethod
    def from_file(cls, file_path: str) -> Grid:
        """
        Create a Grid from txt file
        Format:
            0,9 -> 5,9
            8,0 -> 0,8
        :param file_path:
        :return:
        """
        vectors: list[Vector] = []
        with open(file_path, "r", encoding='utf8') as file:
            for line in file:
                vectors.append(Vector.from_str(line))
        return cls.from_vectors(vectors)

    @classmethod
    def from_vectors(cls, vectors: list[Vector]) -> Grid:
        """
        Create a Grid from Vectors
        :param vectors:
        :return:
        """
        return cls(vectors)

    @staticmethod
    def find_max_xy(vectors: list[Vector]) -> tuple[int | Any, ...]:
        """
        Given a list of Vectors find the Max X and Y coordinate
        :param vectors:
        :return:
        """
        max_xy = [0, 0]
        for vec in vectors:
            for point in vec:
                if point.x > max_xy[0]:
                    max_xy[0] = point.x
                if point.y > max_xy[1]:
                    max_xy[1] = point.y

        return tuple(max_xy)

    def create_board(self) -> list[list[int]]:
        """
        Creates a board from scratch and fills with Vectors
        """
        board = [copy([0 for _ in range(self.max_x + 1)])
                 for _ in range(self.max_y + 1)]
        points: list[Point] = []
        for vec in self.vectors:
            all_points = vec.all_points()
            if all_points:
                points.extend(all_points)
        board = self._add_points_to_board(board, points)
        return board

    @staticmethod
    def _add_points_to_board(board: list[list[int]], points: list[Point]) -> list[list[int]]:
        p: Point
        for p in points:
            board[p.y][p.x] += 1
        return board

    def find_number_of_overlaps_gt_n(self, n: int) -> int:
        """
        finds the number of overlaps in the board with greater than or equal overlaps to n
        :type n: int
        :param n:
        :return number of positions overlapped: int
        """
        overlaps = 0
        for i in self.board:
            for j in i:
                if j >= n:
                    overlaps += 1

        return overlaps
