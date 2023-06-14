#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary)
    for keys in sort_keys:
        print(keys, ":", a_dictionary[keys])
