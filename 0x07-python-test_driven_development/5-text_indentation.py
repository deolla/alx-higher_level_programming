#!/usr/bin/python3

"""
A function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
     Print a text with 2 new lines after each occurrence of '.', '?', and ':' characters.

     Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    pop = text[:]
    signs = ".?:"

    for sign in signs:
        pop_s = pop.split(sign)
        pop = ""

        for m in pop_s:
            m = m.strip(" ")
            pop = m + sign if pop == "" else pop + "\n\n" + m + sign

    print(pop[:-3], end="")
