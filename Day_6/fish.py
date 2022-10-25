from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Fish:
    internal_counter: int
    reproduction_rate: int = 7
    new_lag_time: int = 2

    @classmethod
    def from_str(cls, fish_str: str) -> Fish:
        internal_counter = int(fish_str)
        return cls(internal_counter)

    def next_day(self) -> Optional[Fish]:
        """
        Run a days population movement
        :return:
        """
        if self.internal_counter == 0:
            self.internal_counter = self.reproduction_rate - 1
            new_counter = self.reproduction_rate + self.new_lag_time - 1
            return self.__class__(new_counter)
        self.internal_counter -= 1
        return None


@dataclass
class LanternFish(Fish):
    reproduction_rate: int = 7
    new_lag_time: int = 2
