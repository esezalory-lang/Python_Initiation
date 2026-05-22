#!/bin/python3

print(f"Enter the first number:")
frst_numb = input()
print(f"Enter the second number:")
scnd_numb = input()
product = int(frst_numb) * int(scnd_numb) 
print(f"{frst_numb} x {scnd_numb} = {product}")

if product > 0 :
    print("The result is positive.")
elif product < 0 :
    print("The result is negative.")
else :
    print("The result is positive and negative.")