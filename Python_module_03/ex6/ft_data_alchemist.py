import random

player_names = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    all_names = [name for name in player_names]
    print(f"Initial list of players: {all_names}")

    to_capitalized_names = [name.capitalize() for name in player_names]
    print(f"New list with all names capitalized: {to_capitalized_names}")
    only_capitalized = [name for name in player_names if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")

    score_dict = {
        name: random.randint(0, 1000) for name in to_capitalized_names
    }
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_score = {
        name: score
        for name, score in score_dict.items()
        if score > average
    }
    print(f"High score: {high_score}")
