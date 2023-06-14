#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    u = 0
    k = 0

    for m in reversed(roman_string):
        v = roman.get(m, 0)
        if v >= k:
            u += v
        else:
            u -= v
        k = v
    return u
