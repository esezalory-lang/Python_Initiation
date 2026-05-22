#!/bin/python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    
    if temp >= 0 and temp <= 40:
        print(f"Temperature is now {int(temp_str)}°C\n")
    elif temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return int(temp_str)


def test_temperature() -> None:
    temperature = ["25", "abc", "100", "-50"]

    for temps in temperature:
        try:
            print(f"Input data is {temps}")
            input_temperature(temps)
        except ValueError as v:
            print(f"Caught input_temperature error: {v}\n")
        except TypeError as t:
            print(f"Caught input_temperature error: {t}\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
