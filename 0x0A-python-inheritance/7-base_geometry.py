#!/usr/bin/python3
"""This module provides a class with an public instance method

Functions:
    area(self)
"""


class BaseGeometry:
    """BaseGeometry class that defines a public instance method"""

    def area(self):
        """Public instance method

        Raises:
            Exception with the message `area() is not implemented`
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Function that validate value attribute

        Args:
            name (str): the name
            value (int): the value to be checked

        Raises:
            TypeError: If value is not an integer with the message
                        `<name> must be an integer`
            ValueError: If value is less or equal to 0 with the message
                        `<name> must be greater than 0`
        """

        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{}  must be greater than 0'.format(name))
