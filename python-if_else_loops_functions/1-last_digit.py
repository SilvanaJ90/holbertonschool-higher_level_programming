#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_last_1 = int(str(number)[-1])
if number > 5:
    print(f"Last digit of {number} is {number_last_1} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {number_last_1} and is 0")
elif number < 6 != 0:
    print(f"Last digit of {number} and is {-number_last_1} less than 6 and not 0")
