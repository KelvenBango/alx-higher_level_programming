#!/usr/bin/python3

"""Define a class named Square. """


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size (int): The size of the squre.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Return (int) the current square area."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get the attribute value"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the atrribute value

        Args:
            size: the value to be assign to attribute
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
