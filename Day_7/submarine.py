"""
Submarine Class
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Submarine:
    x_pos: int

    @classmethod
    def from_str(cls, sub_str: str) -> Submarine:
        pos = int(sub_str)
        return cls(pos)

    def fuel_required(self, pos_x: int) -> int:
        distance = abs(pos_x - self.x_pos)
        return int(0.5 * ((distance + 1) * distance))
