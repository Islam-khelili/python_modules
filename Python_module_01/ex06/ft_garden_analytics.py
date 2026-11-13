class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def get_info(self) -> str:
        status = "blooming"
        if not self.is_blooming:
            status = "not blooming"
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers ({status})"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def count_plants(self, plants: list[Plant]) -> int:
            count = 0
            for plant in plants:
                count += 1
            return count

        def total_height(self, plants: list[Plant]) -> int:
            total = 0
            for plant in plants:
                total += plant.height
            return total

        def count_regular(self, plants: list[Plant]) -> int:
            count = 0
            for plant in plants:
                if (
                    plant.__class__ is Plant
                ):
                    count += 1
            return count

        def count_flowering(self, plants: list[Plant]) -> int:
            count = 0
            for plant in plants:
                if plant.__class__ is FloweringPlant:
                    count += 1
            return count

        def count_prize(self, plants: list[Plant]) -> int:
            count = 0
            for plant in plants:
                if plant.__class__ is PrizeFlower:
                    count += 1
            return count

    def __init__(self, gardener_name: str) -> None:
        self.gardener_name = gardener_name
        self.plants: list[Plant] = []
        self.stats = self.GardenStats()
        self.plants_added = 0
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.gardener_name}'s garden")

    def help_all_plants_grow(self) -> None:
        print(f"{self.gardener_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def show_report(self) -> None:
        print(f"=== {self.gardener_name}'s Garden Report ===\n")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(
            f"Plants added: {self.plants_added}, "
            f"Total growth: {self.total_growth}cm"
        )
        print(
            "Plant types: "
            f"{self.stats.count_regular(self.plants)} regular, "
            f"{self.stats.count_flowering(self.plants)} flowering, "
            f"{self.stats.count_prize(self.plants)} prize flowers\n"
        )

    def get_garden_score(self) -> int:
        score = self.stats.total_height(self.plants)
        for plant in self.plants:
            if plant.__class__ is PrizeFlower:
                score += plant.prize_points
        return score

    @classmethod
    def create_garden_network(cls) -> None:
        print("Garden network created successfully")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak_tree = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    fern = Plant("Fern", 40)

    alice_garden.add_plant(oak_tree)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(fern)

    print()

    alice_garden.help_all_plants_grow()
    print()
    alice_garden.show_report()

    print(
        f"Height validation test: "
        f"{GardenManager.validate_height(25)}"
    )

    print(
        f"Garden scores - Alice: {alice_garden.get_garden_score()}, "
        f"Bob: {bob_garden.get_garden_score()}"
    )

    print(f"Total gardens managed: {GardenManager.total_gardens}")
