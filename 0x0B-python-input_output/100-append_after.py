#!/usr/bin/python3
"""
A function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file.

    Args:
        filename: the file.
        search_string: the string to be searched.
        new_string: new string.
    """

    s = []
    with open(filename, "r", encoding="utf-8") as f:
        for pop in f:
            s += [pop]
            if pop.find(search_string) != -1:
                s += [new_string]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(s))
