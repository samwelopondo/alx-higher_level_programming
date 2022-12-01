#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)

if int(num[-1]) > 5:
    var = "and is greater than 5"

elif int(num[-1]) == 0:
    var = "and is 0"

elif int(num[-1]) < 6 and not 0:
    var = "and is less than 6 and not 0"

print(f"Last digit of {number} is {num[-1]} {var}")
