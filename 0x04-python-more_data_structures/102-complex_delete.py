#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    remove_key = []
    for key, m in a_dictionary.items():
        if m == value:
            remove_key.append(key)

    for h in remove_key:
        del a_dictionary[h]
    return a_dictionary
