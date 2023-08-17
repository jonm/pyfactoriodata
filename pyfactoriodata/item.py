import typing

from ingredient import Ingredient
from product import Product

class Item(Ingredient, Product):
    """Represents a solid entity in the game."""
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return "".join([
            "Item(",
            ", ".join([
                " = ".join(["name", self.name.__repr__()])
            ]),
            ")"])

    def __eq__(self, other):
        if type(other) != Item: return False
        return (self.name == other.name)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.name,))
            
