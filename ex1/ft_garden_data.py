class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.total_days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.total_days} days old")


def main():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
