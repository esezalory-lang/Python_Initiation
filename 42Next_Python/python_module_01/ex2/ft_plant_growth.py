#!/bin/python3

class Plant:
    growth = float(0)

    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.old = age

    def show(slf: "Plant", day: int) -> None:
        if day == 7:
            print(f"{slf.name}: {slf.height:.1f}cm, {slf.old} days old")
            print(f"Growth this week: {slf.growth:.1f}cm")
        else:
            print(f"{slf.name}: {slf.height:.1f}cm, {slf.old} days old")

    def grow(self: "Plant", day: int) -> None:
        if day < 2:
            self.height += 0.6
            self.growth += 0.6
        elif day >= 2 and day <= 5:
            self.height += 0.4
            self.growth += 0.4
        else:
            self.height += 0.2
            self.growth += 0.2

    def age(self: "Plant") -> None:
        self.old += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 10, 30)
    for day in range(0, 7):
        if day == 0:
            print(f"=== Day {day + 1} ===")
            rose.show(day)
        else:
            print(f"=== Day {day + 1} ===")
            rose.grow(day + 1)
            rose.age()
            rose.show(day + 1)
