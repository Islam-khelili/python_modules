from alchemy.elements import create_air, create_earth  # type: ignore  # noqa: F401, E501
from alchemy.potions import healing_potion
from alchemy.potions import strength_potion  # type: ignore  # noqa: F401
from . import transmutation  # noqa: F401  # type: ignore


def heal() -> str:
    return healing_potion()
