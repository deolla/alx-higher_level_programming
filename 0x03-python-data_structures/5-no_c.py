#!/usr/bin/env python3

def no_c(my_string):
    brand_new_string = ""
    for h in my_string:
        if h != 'c' and h != 'C':
            brand_new_string += h
    return (brand_new_string)
