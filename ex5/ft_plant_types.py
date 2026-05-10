class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def grow(self, cm: float) -> None:
        self._height += cm

    def age(self, day: int) -> None:
        self._days += day

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


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color:
                 str) -> None:
        super().__init__(name, height, days)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, trunk_diameter:
                 float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}"
              f"cm long and {self._trunk_diameter:.1f}cm wide.")

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


def main():
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")

    rose.show()
    print(f"{rose.get_name()} has not bloomed yet")
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom()
    print()

    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
