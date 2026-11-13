from functools import partial, reduce, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == 'add':
        result = reduce(operator.add, spells)
    elif operation == 'multiply':
        result = reduce(operator.mul, spells)
    elif operation == 'max':
        result = reduce(max, spells)
    elif operation == 'min':
        result = reduce(min, spells)
    else:
        print(f"Unknown operation: {operation}")
        return 0

    return result


def partial_enchanter(
        base_enchantment: Callable) -> dict[str, Callable]:
    result: dict[str, Callable] = {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning")
    }
    return result


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f'{spell} damage'

    @dispatch.register
    def _(spell: str) -> str:
        return spell

    @dispatch.register
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer([10, 20, 30, 40], 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    caster = spell_dispatcher()
    print(f"Damage spell: {caster(42)}")
    print(f"Enchantment: {caster('fireball')}")
    print(f"Multi-cast: {caster([1, 2, 3])}")
    print(caster(3.14))
