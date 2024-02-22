#!/usr/bin/python3
"""4-inherits_from
This module provides a function that checks if the object is an instance
of a class that inherited (directly or indirectly) from the specified class

Functions:
    inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """checks if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is exactly an instance of a_class - True
        Otherwise - False
    """
    return True if (
            issubclass(type(obj), a_class) and type(obj) != a_class
            ) else False
