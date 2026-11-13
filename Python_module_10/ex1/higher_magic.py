from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return 'Spell fizzled'
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_cast(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence_cast


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} for {power}"


if __name__ == "__main__":
    test_values = [14, 20, 9]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 14)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    strong_enough = conditional_caster(
        lambda target, power: power >= 50, fireball)
    print(f"Power 30: {strong_enough('Goblin', 30)}")
    print(f"Power 60: {strong_enough('Goblin', 60)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    for line in sequence("Wizard", 20):
        print(line)
