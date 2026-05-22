#!/bin/python3

my_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []
print(my_list)

for i in range(len(my_list)):
    if my_list[i] > 5:
        new_list.append(my_list[i])

for j in range(len(new_list)):
    new_list[j] += 2

newset = set((new_list))
print(newset)
