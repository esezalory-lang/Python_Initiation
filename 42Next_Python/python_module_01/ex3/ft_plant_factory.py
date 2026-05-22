#!/bin/python3

class Plant:
    total_growth = float(0)

    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.old = age

    def show(self: "Plant") -> None:
        print(f"Created: {self.name}: ", end="")
        print(f"{self.height:.1f}cm, {self.old} days old")

    def grow(self: "Plant", day: int) -> None:
        if day < 2:
            self.height += 0.6
            self.total_growth += 0.6
        elif day >= 2 and day <= 5:
            self.height += 0.4
            self.total_growth += 0.4
        else:
            self.height += 0.2
            self.total_growth += 0.2

    def age(self: "Plant") -> None:
        self.old += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30).show()
    Plant("Oak", 200, 365).show()
    Plant("Cactus", 5, 90).show()
    Plant("Sunflower", 80, 45).show()
    Plant("Fern", 15, 120).show()
