#!/usr/bin/python3
"""
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout:
    """
    if not filename:
        print("No filename provided.")
        return
    with open(filename, 'r', encoding="utf-8") as f:
        read_text_file = f.read()
        print(read_text_file, end='')
