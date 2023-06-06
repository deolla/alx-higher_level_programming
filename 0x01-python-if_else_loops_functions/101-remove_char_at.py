#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return (str)
    else:
        pop = ""
        for m in range(len(str)):
            if m != n:
                pop += str[m]
        return (pop)
