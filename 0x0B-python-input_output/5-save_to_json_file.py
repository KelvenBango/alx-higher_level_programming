#!/usr/bin/python3
"""Defines a function that writes an Object t a text file,
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(my_obj)
