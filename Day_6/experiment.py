from __future__ import annotations

from typing import List, Any, Protocol


class Fish(Protocol):
    """
    Protocol class for fish
    """

    def __init__(self):
        self.internal_counter = None

    @classmethod
    def from_str(cls, fish_str: str) -> Fish:
        """
        Create a fish from String
        :param fish_str:
        :return:
        """


def create_ages_from_fish(all_fish: List[Fish]):
    """
    ages ->
    { 0 : {
        "object": Fish,
        "count" : int
        },
    1 : {
        "object": Fish,
        "count" : int
        },
    }
    """
    ages = {}
    for f in all_fish:
        if f.internal_counter in ages:
            ages[f.internal_counter]["count"] += 1
        else:
            ages[f.internal_counter] = {"object": f,
                                        "count": 1}
    return ages


class Experiment:
    """
    Experiment class for population experiment
    """

    def __init__(self, all_fish: List[Fish]):

        self.ages: dict[int, dict[str:Any]] = create_ages_from_fish(all_fish)

    @classmethod
    def from_file(cls, file_path: str, fish_type: Fish) -> Experiment:
        """
        Create an experiment from file.
        Example File => 3,4,3,1,2
        :param file_path: str
        :param fish_type: Fish
        :return: Experiment
        """
        with open(file_path, encoding='utf-8') as fp:
            input_str = fp.readline()
            fish_str = input_str.split(",")
            all_fish = []
            for f in fish_str:
                all_fish.append(fish_type.from_str(f))
            return cls(all_fish)

    def run_days(self, num_days: int):
        """
        Runs multiple days movements on an experiment
        :param num_days:int
        """
        for _ in range(num_days):
            self.run_day()

    def run_day(self):
        """
        Runs a days movement on the experiment
        """
        new_ages = {}
        for _, age_dict in self.ages.items():
            fish = age_dict['object']
            new_f = fish.next_day()
            if fish.internal_counter in new_ages:
                new_ages[fish.internal_counter]['count'] += age_dict['count']
            else:
                new_ages[fish.internal_counter] = {"object": fish, "count": age_dict["count"]}
            if new_f:
                new_ages[new_f.internal_counter] = {"object": new_f, "count": age_dict["count"]}
        self.ages = new_ages

    def count_fish(self) -> int:
        """
        Counts the number of fish in the experiment currently
        :return:
        """
        fish_count = 0
        for _, data in self.ages.items():
            fish_count += data['count']
        return fish_count
