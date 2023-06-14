#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {key: values * 2 for key, value in a_dictionary.item()}
    return(new_dict)
