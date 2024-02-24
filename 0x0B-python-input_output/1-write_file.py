#!/usr/bn/python3
"""Defines a function that writes a string to a text file (UTF-8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Returns:
        number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
