from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lower_case = ingredients.lower()

    if any(item in lower_case for item in allowed):
        return f'{ingredients} - VALID'
    else:
        return f'{ingredients} - INVALID'
