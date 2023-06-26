#!/usr/bin/python3

def magic_calculation(a, b):
    score = 0

    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            score += (a ** b) / m
        except Exception:
            score = b + a
            break

    return score
