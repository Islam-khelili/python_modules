from typing import Union
from ex0.creature import Creature
from .strategy_base import BattleStrategy
from ex1.capabilities import TransformCapability, HealCapability


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        else:
            return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        transformCreature: Union[Creature, TransformCapability] = creature
        assert (
            isinstance(transformCreature, TransformCapability)
            and isinstance(transformCreature, Creature)
        )
        return "\n".join([
            transformCreature.transform(),
            transformCreature.attack(),
            transformCreature.revert(),
        ])


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}"
                " for this aggressive strategy"
                )
        HealCreature: Union[Creature, HealCapability] = creature
        assert (
            isinstance(HealCreature, Creature)
            and isinstance(HealCreature, HealCapability)
        )
        return "\n".join([
            HealCreature.attack(),
            HealCreature.heal()
        ])
