import math


def get_player_pos() -> tuple[float, float, float]:
    user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
    coords = user_input.split(",")

    if len(coords) != 3:
        print("Invalid syntax")
        return get_player_pos()

    result = []
    for part in coords:
        try:
            result.append(float(part))
        except ValueError as e:
            print(f"Error on parameter '{part}': {e}")
            return get_player_pos()

    return (result[0], result[1], result[2])


def distance_between_two_coords(pos1: tuple[float, float, float],
                                pos2: tuple[float, float, float]) -> float:
    distance = math.sqrt((pos2[0] - pos1[0])**2 +
                         (pos2[1] - pos1[1])**2 +
                         (pos2[2] - pos1[2])**2)
    return distance


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_coords = get_player_pos()
    print(f"Got a first tuple: {first_coords}")
    print(
        f"It includes: X={first_coords[0]}, "
        f"Y={first_coords[1]}, "
        f"Z={first_coords[2]}"
    )
    center = (0, 0, 0)
    print(f"Distance to center: "
          f"{distance_between_two_coords(first_coords, center):.4f}")
    print("Get a second set of coordinates")
    second_coords = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_between_two_coords(first_coords, second_coords):.4f}")
