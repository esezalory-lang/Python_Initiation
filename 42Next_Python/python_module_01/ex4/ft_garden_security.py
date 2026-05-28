#!/bin/python3

class Plant:
    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self: "Plant", height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self: "Plant", age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self: "Plant") -> float:
        return self._height

    def get_age(self: "Plant") -> int:
        return self._age

    def get_name(self: "Plant") -> str:
        return self._name


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    height = rose.get_height()
    age = rose.get_age()
    name = rose.get_name()
    print(f"Plant created: {name}: {height:.1f}cm, {age} days old\n")
    rose.set_height(25)
    rose.set_age(30)
    print(f"Height updated: {height}cm")
    print(f"Age updated: {age} days\n")
    rose.set_height("-25")
    rose.set_age(-30)
    print()
    height = rose.get_height()
    age = rose.get_age()
    print(f"Current state: {name}: {height:.1f}cm, {age} days old")
