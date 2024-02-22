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
