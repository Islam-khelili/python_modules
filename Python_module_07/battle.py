from ex0 import FlameFactory, AquaFactory, CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    for creature in (base, evolved):
        print(creature.describe())
        print(creature.attack())


def battle(
        flame_factory: CreatureFactory,
        aqua_factory: CreatureFactory
        ) -> None:
    print("Testing battle")
    fire_creature = flame_factory.create_base()
    water_creature = aqua_factory.create_base()

    print(f"{fire_creature.describe()}\n"
          f" vs.\n{water_creature.describe()}\n fight!")
    print(fire_creature.attack())
    print(water_creature.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()

    testing_factory(flame)
    print("\n")
    testing_factory(aqua)
    print("\n")
    battle(flame, aqua)
