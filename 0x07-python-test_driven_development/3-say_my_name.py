#!/usr/bin/python3

"""3-say_my_name module
This module provides a function for printing your name

Functions:
    say_my_name(first_name, last_name=""): prints
    My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: If ```first_name``` and ```last_name``` are not
                    string type with the message first_name must be a string
                    or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
