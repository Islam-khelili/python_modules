class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        message = "Unknown garden error"


class PlantError(GardenError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        message = "Unknown plant error"


class WaterError(GardenError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        message = "Unknown water error"


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def test_garden_error() -> None:
    print("Testing catching all garden errors...")
    for error in [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    test_water_error()
    test_garden_error()
    print("\nAll custom error types work correctly!\n")
