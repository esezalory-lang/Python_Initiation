#!/bin/python3

print("Enter a number less than 25")
i = input()
j = int(i)
if j > 25 :
    print("Error")
else :
    while j <= 25 :
        print(f"Inside the loop, my variable is {j}")
        j += 1
