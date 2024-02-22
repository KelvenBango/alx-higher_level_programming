#!/usr/bin/python3
"""3-is_kind_of_class.py
This module defines a function that checks if the object
is an instance of a class that inherited from, the specified class

Functions:
    is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of the class that inherited
    from, the specified class

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is exactly an instance of a_class - True
        Otherwise - False
    """

    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False
