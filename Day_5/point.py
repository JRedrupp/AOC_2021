from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Point:
    """
    Reference to a Point
    """
    x: int
    y: int

    @classmethod
    def from_str(cls, point_str: str) -> Point:
        """
        Returns a point from a string
        :param point_str:
        :return:
        """
        pos_xy = [int(x) for x in point_str.strip().split(",")]
        assert len(pos_xy) == 2
        return cls(*pos_xy)


def _get_dist_and_stride(end: Point, start: Point) -> tuple[int, int, int, int]:
    x_dist = end.x - start.x
    x_stride = -1 if x_dist < 0 else 1
    y_dist = end.y - start.y
    y_stride = -1 if y_dist < 0 else 1
    return x_dist, x_stride, y_dist, y_stride


def get_points_between_2_points(start: Point, end: Point) -> list[Point]:
    """
    Given 2 Points it will return all the points inbetween
    :param start:
    :param end:
    :return:
    """
    points: list[Point] = []
    if start.y == end.y:
        # Moving Horizontal
        dist = end.x - start.x
        if dist < 0:
            start, end = end, start
            dist = dist * -1
        for i in range(dist + 1):
            points.append(Point(x=start.x + i, y=start.y))
    elif start.x == end.x:
        # Moving Vertical
        dist = end.y - start.y
        if dist < 0:
            start, end = end, start
            dist = dist * -1
        for i in range(dist + 1):
            points.append(Point(x=start.x, y=start.y + i))
    else:
        # Diagonal Line
        x_dist, x_stride, y_dist, y_stride = _get_dist_and_stride(end, start)
        # We will then take the start point, increment it by 1 x and y and add each point on the way
        for i, j in zip(range(0, x_dist, x_stride), range(0, y_dist, y_stride)):
            points.append(Point(start.x + i, start.y + j))
        points.append(end)

    return points
