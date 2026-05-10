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


def main():
    plants = [
        Plant("Rose", 15, 10),
        Plant("Oak", 200, 120),
        Plant("Cactus", 15, 120),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plants[0].show()
    print()
    plants[0].set_height(25)
    plants[0].set_age(30)
    print()
    plants[0].set_height(-10)
    plants[0].set_age(-5)
    print()
    print("Current state: ", end="")
    plants[0].show()


if __name__ == "__main__":
    main()
