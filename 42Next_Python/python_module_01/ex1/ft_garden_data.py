#!/bin/python3

class Plant:
    def __init__(self: "Plant", name: str, height: int, age: int) -> None:
        self.name = name
        self.height = int(height)
        self.age = int(age)

    def show(self: "Plant") -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.show()
    cactus = Plant("Cactus", 15, 120)
    cactus.show()
