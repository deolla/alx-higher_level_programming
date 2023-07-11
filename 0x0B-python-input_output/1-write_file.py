#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)

    Args:
        filename: file to write into.
        text: text to be written.

    Raises:
        Exception: when file opens.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        write_data = f.write(text)
        print(write_data)
