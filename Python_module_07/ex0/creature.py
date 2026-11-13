from abc import ABC, abstractmethod


class Creature(ABC):
    name: str
    type: str
    weapon: str

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    name = "Flameling"
    type = "Fire"
    weapon = "Ember"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"


class Pyrodon(Creature):
    name = "Pyrodon"
    type = "Fire/Flying"
    weapon = "Flamethrower"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"


class Aquabub(Creature):
    name = "Aquabub"
    type = "Water"
    weapon = "Water Gun"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"


class Torragon(Creature):
    name = "Torragon"
    type = "Water"
    weapon = "Hydro Pump"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"
