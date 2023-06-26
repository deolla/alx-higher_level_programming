#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for m in range(x):
            if isinstance(my_list[m], int):
                print("{:d}".format(my_list[m]), end="")
                count += 1

    except IndexError:
        pass

    print()
    return count
