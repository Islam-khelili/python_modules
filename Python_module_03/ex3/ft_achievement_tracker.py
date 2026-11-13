import random


ALL_ACHIEVEMENTS = [
    "Welcome to Los Santos",
    "A Friendship Resurrected",
    "A Fair Day's Pay",
    "The Moment of Truth",
    "To Live or Die in Los Santos",
    "Career Criminal",
    "San Andreas Sightseer",
    "All's Fare in Love and War",
    "TP Industries Arms Race",
    "Multi-Disciplined",
    "From Beyond the Stars",
    "A Mystery Solved",
    "Waste Management",
    "Show Off",
    "Solid Gold Baby",
]


def gen_player_achievements() -> set:
    num = random.randint(5, len(ALL_ACHIEVEMENTS))
    picked = random.sample(ALL_ACHIEVEMENTS, num)
    return set(picked)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements = alice | bob | charlie | dylan
    print(f"All distinct achievements: {all_achievements}")

    common = alice & bob & charlie & dylan
    print(f"Common achievements: {common}")

    only_alice = alice - (bob | charlie | dylan)
    print(f"Only Alice has: {only_alice}")
    only_bob = bob - (alice | charlie | dylan)
    print(f"Only Bob has: {only_bob}")
    only_charlie = charlie - (alice | bob | dylan)
    print(f"Only Charlie has: {only_charlie}")
    only_dylan = dylan - (alice | bob | charlie)
    print(f"Only Dylan has: {only_dylan}")

    print(f"Alice is missing: {set(ALL_ACHIEVEMENTS) - alice}")
    print(f"Bob is missing: {set(ALL_ACHIEVEMENTS) - bob}")
    print(f"Charlie is missing: {set(ALL_ACHIEVEMENTS) - charlie}")
    print(f"Dylan is missing: {set(ALL_ACHIEVEMENTS) - dylan}")
