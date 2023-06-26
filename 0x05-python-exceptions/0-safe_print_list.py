#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    mp = 0

    try:
        for m in range(x):
            print(my_list[m], end="")
            mp += 1

    except IndexError:
        pass

    print()
    return mp
