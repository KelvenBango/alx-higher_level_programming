#!/usr/bin/python3

"""0-add_integer module
This module provides a function for adding two integers or floats.

Functions:
    add_integer(a, b): Add two integers or floats
"""

def add_integer(a, b=98):
    """Add two integers or floats.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Defaults to 98.

    Raises:
        TypeError: If a or b is not integer or float.

    Returns:
        int: The addition of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError( 'b must be an integer')


    a = int(a)
    b = int(b)

    return a + b
