#!/bin/python3


class Plant:
    def __init__(self: "Plant", name: str = "Unknown plant",
                 height: float = 0, age: int = 0) -> None:
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)
        self._grow_counter = 0
        self._age_counter = 0
        self._show_counter = 0

    def set_name(self: "Plant", name: str) -> None:
        self._name = name

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

    def get_name(self: "Plant") -> str:
        return self._name

    def get_height(self: "Plant") -> float:
        return self._height

    def get_age(self: "Plant") -> int:
        return self._age

    def get_age_count(self: "Plant") -> int:
        return self._age_counter

    def get_show_count(self: "Plant") -> int:
        return self._show_counter

    def get_grow_count(self: "Plant") -> int:
        return self._grow_counter

    def show(self: "Plant") -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._show_counter += 1

    def grow(self: "Plant", day: int) -> None:
        if day < 2:
            self._height += 0.6
        elif day >= 2 and day <= 5:
            self._height += 0.4
        else:
            self._height += 0.2
        self._grow_counter += 1

    def age(self: "Plant") -> None:
        self._age += 1
        self._age_counter += 1

    @staticmethod
    def check_age(age: int) -> None:
        if age >= 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls()

    class Statistics:
        def __init__(self, main: "Plant") -> None:
            self._plant = main

        def show(self) -> None:
            print(f"Stats: {self._plant.get_grow_count()} grow, ", end="")
            print(f"{self._plant.get_age_count()} age, ", end="")
            print(f"{self._plant.get_show_count()} show")


class Flower(Plant):
    def __init__(self: "Flower", name: str,
                 height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._did_it_bloom = False

    def show(self: "Flower") -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._did_it_bloom is True:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self: "Flower") -> None:
        self._did_it_bloom = True


class Tree(Plant):
    def __init__(self: "Tree", name: str,
                 height: float, age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        if diameter < 0:
            print("Invalid trunk diameter")
        else:
            self._trunk_diameter = diameter
        self._shade_counter = 0

    def show(self: "Tree") -> None:
        super().show()
        print(f" Trunk Diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self: "Tree") -> None:
        print(f"{self.__class__.__name__} {self._name} ", end="")
        print(f"produces a shade of {self._height:.1f}cm ", end="")
        print(f"and {self._trunk_diameter:.1f}cm wide")
        self._shade_counter += 1

    def get_tree_shade(self: "Tree") -> int:
        return self._shade_counter

    class Statistics(Plant.Statistics):
        def __init__(self, main: "Tree") -> None:
            super().__init__(main)
            self._tree: Tree = main

        def show(self) -> None:
            super().show()
            print(f" {self._tree.get_tree_shade()} shade")


class Seed(Flower):
    def __init__(self: "Seed", name: str,
                 height: float, age: int,  color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed = 0

    def bloom(self: "Seed") -> None:
        super().bloom()
        self._seed = 42

    def show(self: "Seed") -> None:
        super().show()
        print(f" Seeds: {self._seed}")


def print_plant_statistics(plant_type: Plant) -> None:
    plant_type.Statistics(plant_type).show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    print("=== Check year-old")
    Plant.check_age(10)
    Plant.check_age(400)
    print()

    print("=== Flower")
    rose.show()
    rose_stats = rose.Statistics(rose)
    print("[asking the rose to grow and bloom]")
    for i in range(3):
        rose.grow(i)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose_stats.show()
    print()

    print("=== Tree")
    oak.show()
    oak_stats = oak.Statistics(oak)
    print("[statistics for Oak]")
    oak_stats.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak_stats.show()
    print()

    print("=== Seed")
    sunflower.show()
    sunflower_stats = sunflower.Statistics(sunflower)
    print("[make sunflower grow, age and bloom]")
    for i in range(20):
        sunflower.grow(i)
        sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower_stats.show()
    print()

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    anon_stats = anon.Statistics(anon)
    anon_stats.show()
