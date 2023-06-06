#!/usr/bin/python3

def fizzbuzz():
    for v in range(1,101):
        if v % 3 == 0 and v % 5 == 0:
            print("FizzBuzz", end=" ")
        elif v % 3 == 0:
            print("Fizz", end=" ")
        elif v % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(v, end=" ")
