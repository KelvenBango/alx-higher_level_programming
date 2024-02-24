#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout

Function:
    read_file(filename="")
"""


def read_file(filename=""):
    """Read text file and prints it text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as my_file:
        print(my_file.read(), end='')
