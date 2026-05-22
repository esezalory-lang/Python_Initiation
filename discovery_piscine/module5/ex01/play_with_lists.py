#!/bin/python3

my_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []

print(f"Original list: {my_list}")

for i in range(len(my_list)):
    new_list.append(my_list[i] + 2)

print(f"New list: {new_list}")
