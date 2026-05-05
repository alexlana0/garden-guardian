class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self, cm: float) -> None:
        self.height += cm
        
    def age(self, day: float) -> None:
        self.days += day

def main():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 120),
        Plant("Cactus", 15, 120),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()