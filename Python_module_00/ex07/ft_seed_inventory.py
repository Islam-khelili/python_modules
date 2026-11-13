def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if seed_type == "tomato":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif seed_type == "carrot":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif seed_type == "lettuce":
        print(
            f"{seed_type.capitalize()} seeds: covers {quantity} square meters"
        )
    else:
        print(f"{seed_type.capitalize()} seeds: {quantity} unknown unit type")
