#!/usr/bin/python3

"""Define a class named Square. """


class Square:
    """Represents a Square"""

    def __init__(self, size):
        """Constructor

        Args:
            size (int): The size of the square

        Returns:
        """
        if not isinstance(size, int):
            raise TYpeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        def area(self):
            """
            Area Function

            Args:
                self: reference to the object it self

            Returns:
                (int) the current square area
            """

            return self.__area
