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

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
