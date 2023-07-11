#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8).
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    Args:
        filename: the file itself.
        text: the txt to be inputed.

    Raises:
        Exception: when file opens.
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_info = f.write(text)
        return (append_info)
