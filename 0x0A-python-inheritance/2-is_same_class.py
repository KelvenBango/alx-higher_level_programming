#!/usr/bin/python3
"""2-is_same_class
This module provides a function that checks if the object
is exactly an instance of the specified class

Functions:
    is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class

    Args:
        obj: The object to be checked
        a_class: The class we want to verify

    Returns:
        Bool: True if the object is exactly an instance of tthe specified class
                otherwise False
    """

    return True if type(obj) == a_class else False
