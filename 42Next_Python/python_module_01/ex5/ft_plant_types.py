#!/bin/python3

class Plant:
    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def show(self: "Plant") -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

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


class Flower(Plant):
    did_it_bloom = 0

    def __init__(self: "Flower", name: str,
                 height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self.show_flower()

    def show_flower(self: "Flower") -> None:
        super().show()
        print(f" Color: {self._color}")
        if self.did_it_bloom == 0:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self: "Flower") -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self.did_it_bloom = 1
        self.show_flower()


class Tree(Plant):
    def __init__(self: "Tree", name: str,
                 height: float, age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        if diameter < 0:
            print("Invalid trunk diameter")
        else:
            self._trunk_diameter = diameter
        self.show_tree()

    def show_tree(self: "Tree") -> None:
        super().show()
        print(f" Trunk Diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self: "Tree") -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"{self.__class__.__name__} {self._name} ", end="")
        print(f"produces a shade of {self._height:.1f}cm ", end="")
        print(f"and {self._trunk_diameter:.1f}cm wide")


class Vegetable(Plant):
    def __init__(self: "Vegetable", name: str,
                 height: float, age: int, season: str, nutri_val: int) -> None:
        super().__init__(name, height, age)
        self._season = season
        if nutri_val < 0:
            print("Invalid nutritional value")
        else:
            self._nutrional_value = nutri_val

    def show_veggie(self: "Vegetable") -> None:
        super().show()
        print(f" Harvest season: {self._season}")
        print(f" Nutritional value: {self._nutrional_value}")

    def age(self: "Vegetable", days: int) -> None:
        if days < 0:
            print("Invalid number of days")
        else:
            self._age += days

    def grow(self: "Vegetable", growth: int) -> None:
        if growth < 0:
            print("Invalid growth data")
        else:
            self._nutrional_value += growth
            self._height += 42


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.bloom()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.show_veggie()
    print(f"[make {tomato.get_name().lower()} grow and age for 20 days]")
    tomato.grow(20)
    tomato.age(20)
    tomato.show_veggie()
