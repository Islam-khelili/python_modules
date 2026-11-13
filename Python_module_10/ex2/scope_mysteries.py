from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def count_increasement() -> int:
        nonlocal count
        count += 1
        return count

    return count_increasement


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulate_power(amount: int) -> int:
        nonlocal total_power

        total_power += amount
        return total_power

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def describe_enchantment(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'

    return describe_enchantment


def memory_vault() -> dict[str, Callable]:
    storage: dict[str, int] = {}

    def store(key: str, value: int) -> str:
        storage[key] = value
        return f"save {value} under {key}"

    def recall(key: str) -> str | int:
        if key not in storage:
            return 'Memory not found'
        return storage[key]

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    initial_powers = [76, 24, 66]
    power_additions = [12, 19, 6, 17, 6]
    enchantment_types = ["Radiant", "Frozen", "Dark"]
    items_to_enchant = ["Staff", "Sword", "Armor", "Amulet"]

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(initial_powers[0])
    print(f"Base {initial_powers[0]}, add {power_additions[0]}: "
          f"{acc(power_additions[0])}")
    print(f"Base {initial_powers[0]}, add {power_additions[1]}: "
          f"{acc(power_additions[1])}")

    print("\nTesting enchantment factory...")
    radiant = enchantment_factory(enchantment_types[0])
    frozen = enchantment_factory(enchantment_types[1])
    print(radiant(items_to_enchant[0]))
    print(frozen(items_to_enchant[1]))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print(vault["store"]("secret", 42))
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
