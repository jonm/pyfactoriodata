import typing

from ingredient import Ingredient
from item import Item
from product import Product
from technology import Technology

class Recipe:
    """Represents the process for crafting or producing something."""
    def __init__(self,
                 name: str,
                 results: dict[Product,int],
                 ingredients: dict[Ingredient,int],
                 crafting_time_secs: float=0.5,
                 crafted_only_in: Item = None,
                 enabled_by: Technology = None,
                 expensive_version: 'Recipe' = None) -> None:
        self.name = name
        self.results = results
        self.ingredients = ingredients
        self.crafting_time_secs = crafting_time_secs
        # if self.crafted_only_in is None, then this can be made in
        # any assembling machine or can be handcrafted
        self.crafted_only_in = crafted_only_in
        # if self.enabled_by is None, then it is available initially
        # before any research
        self.enabled_by = enabled_by
        self.expensive_version = expensive_version

    def __repr__(self):
        return "".join([
            "Recipe(",
            ", ".join([
                " = ".join(["name", self.name.__repr__()]),
                " = ".join(["results", self.results.__repr__()]),
                " = ".join(["ingredients", self.ingredients.__repr__()]),
                " = ".join(["crafting_time_secs", self.crafting_time_secs.__repr__()]),
                " = ".join(["crafted_only_in", self.crafted_only_in.__repr__()]),
                " = ".join(["enabled_by", self.enabled_by.__repr__()]),
                " = ".join(["expensive_version", self.expensive_version.__repr__()])
            ]),
            ")"])

    def __eq__(self, other):
        if type(other) != Recipe: return False
        return (self.name == other.name
                and self.results == other.results
                and self.ingredients == other.ingredients
                and self.crafting_time_secs == other.crafting_time_secs
                and self.crafted_only_in == other.crafted_only_in
                and self.enabled_by == other.enabled_by
                and self.expensive_version == other.expensive_version)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.name, tuple(self.results), tuple(self.ingredients),
                     self.crafting_time_secs, self.crafted_only_in,
                     self.enabled_by, self.expensive_version))
            
    

        
