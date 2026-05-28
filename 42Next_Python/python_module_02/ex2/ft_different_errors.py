#!/bin/python3

def garden_operations(operation_number: int = 0) -> None:

    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("test.txt", "r")
    elif operation_number == 3:
        0 + "abc"
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    test_cases = [0, 1, 2, 3, 4]
    for i in test_cases:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as v:
            print(f"Caught ValueError: {v}")
        except ZeroDivisionError as z:
            print(f"Caught ZeroDivisionError: {z}")
        except FileNotFoundError as f:
            print(f"Caught FileNotFoundError: {f}")
        except TypeError as t:
            print(f"Caught TypeError: {t}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
