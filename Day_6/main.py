from __future__ import annotations

from experiment import Experiment
from fish import LanternFish

if __name__ == "__main__":
    exp = Experiment.from_file("input.txt", LanternFish)
    exp.run_days(256)
    print(exp.count_fish())
