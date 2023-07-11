#!/usr/bin/python3
"""
A function that returns an object by a JSON string
"""
import json


def save_to_json_file(my_obj, filename):
    """
    returns an object (Python data structure) represented by a JSON string

    Args:
        my_obj: the object
        filename: the file.

    """
    with open(filename, "w", encoding="utf=8") as f:
        json.dump(my_obj, f)
