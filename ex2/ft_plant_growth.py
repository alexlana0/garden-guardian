class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.total_days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.total_days} days old")

    def grow(self, cm: float) -> None:
        self.height += cm
        
    def age(self, day: int) -> None:
        self.total_days += day


def main():
    plants = [
                Plant("Rose", 25.0, 30),
                Plant("Sunflower", 80, 45),
                Plant("Cactus", 15, 120)
    ]
    growth_rate = 0.8
    print("=== Garden Plant Growth ===")
    plants[0].show()
    total_growth = 0
    for i in range(1, 8):
        plants[0].age(1)
        plants[0].grow(growth_rate)
        print(f"=== Day {i} ===")
        plants[0].show()
        total_growth += growth_rate
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()