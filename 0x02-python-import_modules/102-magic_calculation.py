#!/usr/bin/python3

from magic_calculator_102 import add,sub

def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for m in range(4, 7):
            c = add (c, m)
        return (c)
    else:
        return sub(a, b)
