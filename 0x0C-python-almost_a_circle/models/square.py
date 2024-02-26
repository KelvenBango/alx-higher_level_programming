#!/usr/bin/python3
"""Defines the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square

        Args:
            size (size): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identifier of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def update(self, *args, *kwargs):
        """Method that assigns attributes

        Args:
            *args (list): The list of arguments - no-keyworded arguments
                - 1st argument represents the id attribute
                - 2nd argument represents the size attribute
                - 3rd argument represents the x attribute
                - 4th argument represents the y attribute
            **kwargs: keyworded arguments where each key represens an attribute
                    to the instance
        """

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width
                )
