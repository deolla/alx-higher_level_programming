#!/usr/bin/python3

def magic_calculation(a, b, c):
    return c if a < b else (a + b - c) if a > b else (a * b)
