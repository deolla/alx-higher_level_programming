#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    import magic_calculator_102
    add = magic_calculator_102.add
    cub = magic_calculator_102.sub

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))
