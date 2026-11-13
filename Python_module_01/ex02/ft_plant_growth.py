class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def get_older(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm , {self.age} days old"


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(plant1.get_info())

    pervious_height = plant1.height

    for i in range(0, 7):
        plant1.get_older()
        plant1.grow()

    print("=== Day 7 ===")
    print(plant1.get_info())

    difference = plant1.height - pervious_height
    print(f"Growth this week: +{difference}cm")
