#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle():
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle object

        Args:
            width (int): the value to be set as width of the rectangle.
            height (int): the value to be set as height of the rectangle.

        Raises:
            TypeError: If the width is not integer with the message
                        `width must be an integer`
                        If the height is not integer with the message
                        `height must be an integer`

            ValueError: If width is less than 0, with the message
                        'width must be >= 0
                        If height is less than 0, with the message
                        'height must be >= 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width

        Args:
            value (int): the value to be set to the width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height

        Args:
            value (int): the value to be set to the height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
