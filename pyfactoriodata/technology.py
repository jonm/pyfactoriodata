import typing

from ingredient import Ingredient

class Technology:
    """Represents a research goal in the game."""
    # TODO: cost_count only represents non-infinite research; the raw data
    # has formulas for calculating the cost of a given level of an
    # infinite research tech
    def __init__(self, name: str, cost_count: int, cycle_time_secs: int,
                 ingredients: dict[Ingredient, int],
                 prerequisites: list['Technology'] = []) -> None:
        self.name = name
        self.cost_count = cost_count
        self.cycle_time_secs = cycle_time_secs
        self.ingredients = ingredients
        self.prerequisites = prerequisites

    def __repr__(self):
        return "".join([
            "Technology(",
            ", ".join([
                " = ".join(["name",self.name.__repr__()]),
                " = ".join(["cost_count",self.cost_count.__repr__()]),
                " = ".join(["cycle_time_secs",self.cycle_time_secs.__repr__()]),
                " = ".join(["ingredients",self.ingredients.__repr__()]),
                " = ".join(["prerequisites",self.prerequisites.__repr__()])
            ]),
            ")"])

    def requires(self, other: 'Technology'):
        if len(self.prerequisites) == 0: return False
        if other in self.prerequisites: return True
        for prereq in self.prerequisites:
            if prereq.requires(other): return True
        return False

    def __eq__(self, other):
        if type(other) != Technology: return False
        return (self.name == other.name
                and self.cost_count == other.cost_count
                and self.cycle_time_secs == other.cycle_time_secs
                and self.ingredients == other.ingredients
                and self.prerequisites == other.prerequisites)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if type(other) != Technology: raise TypeError("comparing Technology to non-Technology")
        return other.requires(self)

    def __le__(self, other):
        if type(other) != Technology: raise TypeError("comparing Technology to non-Technology")
        return (self == other) or other.requires(self)

    def __gt__(self, other):
        if type(other) != Technology: raise TypeError("comparing Technology to non-Technology")
        return self.requires(other)

    def __ge__(self, other):
        if type(other) != Technology: raise TypeError("comparing Technology to non-Technology")
        return (self == other) or self.requires(other)

    def __hash__(self):
        return hash((self.name, self.cost_count, self.cycle_time_secs,
                     tuple(self.ingredients), tuple(self.prerequisites)))
