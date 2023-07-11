#!/usr/bin/python3
"""
A function that returns an object represented by a JSON
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string:

    Args:
        my_str: THE STRING.

    Returns:
        returns an object.
    """
    return json.loads(my_str)
