from __future__ import annotations

from dataclasses import dataclass

from point import Point, get_points_between_2_points


@dataclass
class Vector:
    point_1: Point
    point_2: Point

    @classmethod
    def from_str(cls, vec_str: str) -> Vector:
        """
        Creates a Vector from a string
        :param vec_str:
        :return:
        """
        points: list[vec_str] = vec_str.split("->")
        assert len(points) == 2
        p1: Point = Point.from_str(points[0])
        p2: Point = Point.from_str(points[1])
        return cls(p1, p2)

    def __iter__(self) -> Point:
        yield self.point_1
        yield self.point_2

    def __len__(self):
        return 2

    def all_points(self) -> list[Point]:
        """
        Returns all Points that the Vector Passes through
        """
        app_points = get_points_between_2_points(self.point_1, self.point_2)
        return app_points
