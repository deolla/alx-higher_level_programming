#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit *= -1

print("Last_digit of {} is {} and is ".format(number, last_digit), end='')

if last_digit > 5:
    print("greater that 5\n")
elif last_digit == 0:
    print("0\n")
else:
    print("less than 6 and not 0\n")
