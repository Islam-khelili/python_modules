

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_by_power = sorted(artifacts, key=lambda p: p["power"], reverse=True)
    return sorted_by_power


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_by_power = list(filter(lambda n: n['power'] >= min_power, mages))
    return filtered_by_power


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = list(map(lambda t: '* ' + t + ' *', spells))
    return transformed


def mage_stats(mages: list[dict]) -> dict:
    max_power: int = max(mages, key=lambda m: m["power"])['power']
    min_power: int = min(mages, key=lambda n: n['power'])['power']
    avg_power: float = round(sum(a['power'] for a in mages) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Lightning Rod', 'power': 99, 'type': 'armor'},
        {'name': 'Crystal Orb', 'power': 104, 'type': 'accessory'},
        {'name': 'Storm Crown', 'power': 79, 'type': 'accessory'},
        {'name': 'Wind Cloak', 'power': 66, 'type': 'weapon'}
        ]
    mages = [
        {'name': 'Nova', 'power': 96, 'element': 'light'},
        {'name': 'Kai', 'power': 62, 'element': 'wind'},
        {'name': 'River', 'power': 60, 'element': 'fire'},
        {'name': 'River', 'power': 68, 'element': 'water'},
        {'name': 'Jordan', 'power': 80, 'element': 'light'}
        ]
    spells = ['flash', 'freeze', 'lightning', 'tornado']
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)")

    print("\nTesting power filter...")
    strong = power_filter(mages, 50)
    print([m["name"] for m in strong])

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(mage_stats(mages))
