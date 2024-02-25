#!/usr/bin/python3
"""Defines a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object.

Function:
    class_to_json(obj)
"""


def class_to_json(obj):
    """Returns the dictionary witth simple data structure
    (list, dictionary, string, integer and boolean)

    Args:
        obj (object): an instance of a Class
    """
    return obj.__dict__
