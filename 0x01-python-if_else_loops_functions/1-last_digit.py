#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number < 0:
    n = ((number * -1) % 10) * -1
print(f"Last digit of {number} is {n} ", end=" ")
if n > 5:
    print("and is greater than 5")
elif n == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
