from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    name = "Sproutling"
    type = "Grass"
    weapon = "Vine Whip"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    name = "Bloomelle"
    type = "Grass/Fairy"
    weapon = "Petal Dance"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    name = "Shiftling"
    type = "Normal"
    is_transformed = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        if not self.is_transformed:
            return f"{self.name} is already reverted"
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    name = "Morphagon"
    type = "Normal/Dragon"

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if not self.is_transformed:
            return f"{self.name} is already reverted"
        self.is_transformed = False
        return f"{self.name} stabilizes its form."
