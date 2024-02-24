#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text
file (UTF-8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file"""
    with open(filename, 'a', enconding='utf-8') as f:
        return f.write(text)
