#!/usr/bin/python3

"""Print square
This module provides a function for printing a square with the character #

Function:
    print_square(size): prints a square with the character #
"""


def print_square(size):
    """Prints a square with character #

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: if size is not integer with the message `size must be an integer`
                    if size is a float and less than zero with the message
                    `size must be an integer`

        ValueError: if size is less than 0 (zero) with the message `size must be >= 0`
    """

    if not isinstance(size, int):
        raise TypeError('size must be integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >=0')

    number_of_character = size * size
    counter = 0
    
    for character in range(number_of_character):
        counter += 1
        print('#', end='')
        
        if counter == size:
            print()
            counter = 0
