from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from submarine import Submarine


@dataclass
class Fleet:
    submarines: list[Submarine]

    @classmethod
    def from_file(cls, file_path: str) -> Fleet:
        with open(file_path, 'r', encoding='utf-8') as fp:
            line = fp.readline()
        sub_strs = line.split(',')
        subs = []
        for sub_str in sub_strs:
            subs.append(Submarine.from_str(sub_str))
        return cls(subs)

    def distance_from(self, pos_x: int) -> int:
        """
        Given a position returns the total fuel required for the fleet to get there
        :param pos_x:
        :return:
        """
        fuel_required = 0
        for sub in self.submarines:
            fuel_required += sub.fuel_required(pos_x)
        return fuel_required

    def furthest_distance_ship(self) -> int:
        """Returns the furthest distance from the origin"""
        furthest_distance = 0
        for sub in self.submarines:
            furthest_distance = sub.x_pos if furthest_distance < sub.x_pos else furthest_distance

        return furthest_distance

    def get_position_with_least_fuel(self) -> int:
        fuel_positions = [self.distance_from(x) for x in range(self.furthest_distance_ship())]
        return int(np.argmin(fuel_positions))

    def get_minimal_fuel_to_align(self) -> int:
        fuel_positions = [self.distance_from(x) for x in range(self.furthest_distance_ship())]
        return min(fuel_positions)
