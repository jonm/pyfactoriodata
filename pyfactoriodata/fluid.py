import typing

from ingredient import Ingredient
from product import Product

class Fluid(Ingredient, Product):
    """Represents liquid elements in the game (water, oil, etc.)."""
    def __init__(self, name: str,
                 default_temperature: int,
                 heat_capacity_kJ : float,
                 max_temperature: int = None,
                 gas_temperature: int = None) -> None:
        self.name = name
        self.default_temperature = default_temperature
        self.heat_capacity_kJ = heat_capacity_kJ
        self.max_temperature = max_temperature
        self.gas_temperature = gas_temperature

    def __repr__(self):
        return "".join([
            "Fluid(",
            ", ".join([
                " = ".join(["name", self.name.__repr__()]),
                " = ".join(["default_temperature", self.default_temperature.__repr__()]),
                " = ".join(["heat_capacity_kJ", self.heat_capacity_kJ.__repr__()]),
                " = ".join(["max_temperature", self.max_temperature.__repr__()]),
                " = ".join(["gas_temperature", self.gas_temperature.__repr__()])
            ]),
            ")"])

    def __eq__(self, other):
        if type(other) != Fluid: return False
        return (self.name == other.name
                and self.default_temperature == other.default_temperature
                and self.heat_capacity_kJ == other.heat_capacity_kJ
                and self.max_temperature == other.max_temperature
                and self.gas_temperature == other.gas_temperature)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.name, self.default_temperature,
                     self.heat_capacity_kJ, self.max_temperature,
                     self.gas_temperature))
            
    
