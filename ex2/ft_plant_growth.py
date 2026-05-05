class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.total_days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.total_days} days old")

    def grow(self, cm: float) -> None:
        self.height += cm
        
    def age(self, day: float) -> None:
        self.total_days += day


def main():
    plants = [
                Plant("Rose", 25, 30),
                Plant("Sunflower", 80, 45),
                Plant("Cactus", 15, 120)
    ]
    growth_rate = 0.5
    print(f"=== Garden Plant Growth ===")
    plants[2].show()
    total_growth = 0
    for i in range(1, 8):
        plants[2].age(1)
        plants[2].grow(growth_rate)
        print(f"=== Day {i} ===")
        plants[2].show()
        total_growth += growth_rate
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()