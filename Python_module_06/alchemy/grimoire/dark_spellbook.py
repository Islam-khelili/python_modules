from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_dark_ingredients(ingredients)
    if result.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
