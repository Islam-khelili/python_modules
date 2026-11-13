class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_area = self.trunk_diameter + 28
        print(f"{self.name} provides {shade_area} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str,
                 nutritional_value: str
                 ) -> None:
        super().__init__(name, height, age)
        self.season = season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "purple"),
    ]

    trees = [
        Tree("Oak", 500, 1251, 50),
        Tree("Apple", 625, 1874, 49),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "Vitamin C"),
        Vegetable("Carrot", 35, 75, "winter", "Vitmain A"),
    ]

    print("=== Garden Plant Types ===\n")
    for flower in flowers:
        print(
            f"{flower.name} (Flower): {flower.height}cm, "
            f"{flower.age} days, {flower.color}"
        )
        flower.bloom()

    for tree in trees:
        print(
            f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, "
            f"{tree.trunk_diameter} diameter"
        )
        tree.produce_shade()

    for vegetable in vegetables:
        print(
            f"{vegetable.name} (Vegetable): {vegetable.height}cm, "
            f"{vegetable.age} days, {vegetable.season} harvest"
        )
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}\n")
