class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days
        self._stats = self._Stats()

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")
        self._stats.show_calls += 1

    def grow(self, cm: float) -> None:
        self._height += cm
        self._stats.grow_calls += 1

    def age(self, day: int) -> None:
        self._days += day
        self._stats.age_calls += 1

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_days(self) -> int:
        return self._days

    def set_name(self, name: str) -> None:
        self._name = name

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = days
            print(f"Age updated: {self._days} days")

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days >= 365
    
    def get_stats(self) -> "_Stats":
        return self._stats


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: 
                 str) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

    def __init__(self, name: str, height: float, days: int, trunk_diameter:
                 float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter
        self._stats = self._Stats()

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}"
              f"cm long and {self._trunk_diameter:.1f}cm wide.")
        self._stats.shade_calls += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, harvest_season:
                 str, nutritional_value: int) -> None:
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self, cm: float) -> None:
        super().grow(cm)
        self._nutritional_value += 10
    
    def age(self, day: int) -> None:
        super().age(day)
        self._nutritional_value += 10


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int, color: 
                 str) -> None:
        super().__init__(name, height, days, color)
        self._number_of_seeds = 0
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._number_of_seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._bloomed = True
        self._number_of_seeds += 42


def display_plant_stats(plant: Plant) -> None:

    stats = plant.get_stats()
    stats.display()

    if isinstance(plant, Tree):
        print(f"{stats.shade_calls} shade")

def main():
    plants = [
        Flower("Rose", 15, 10, "red"),
        Seed("Sunflower", 80, 45, "yellow"),
        Tree("Oak", 200, 365, 5.0),
        Plant.anonymous_plant()
    ]

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")
    print()

    print("=== Flower")
    plants[0].show()
    print(f"[statistics for {plants[0].get_name()}]")
    display_plant_stats(plants[0])
    print(f"[asking the {plants[0].get_name()} to grow and bloom]")
    plants[0].grow(8.0)
    plants[0].bloom()
    plants[0].show()
    print(f"[statistics for {plants[0].get_name()}]")
    display_plant_stats(plants[0])
    print()

    print("=== Tree")
    plants[2].show()
    print(f"[statistics for {plants[2].get_name()}]")
    display_plant_stats(plants[2])
    print(f"[asking the {plants[2].get_name()} to produce shade]")
    plants[2].produce_shade()
    print(f"[statistics for {plants[2].get_name()}]")
    display_plant_stats(plants[2])
    print()

    print("=== Seed")
    plants[1].show()
    print(f"[make {plants[1].get_name()} grow, age and bloom]")
    plants[1].grow(30)
    plants[1].age(20)
    plants[1].bloom()
    plants[1].show()
    print(f"[statistics for {plants[1].get_name()}]")
    display_plant_stats(plants[1])
    print()

    print("=== Anonymous")
    plants[3].show()
    print(f"[statistics for {plants[3].get_name()}]")
    display_plant_stats(plants[3])


if __name__ == "__main__":
    main()