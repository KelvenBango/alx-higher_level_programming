#!/usr/bin/python3

"""1-matrix divided module
This module provides a function for dividing all elements of a matrix.

Functions:
    matrix_divided(matrix, div): Divide all elements of matrix
"""


def matrix_divided(matrix, div):
    """Divide all elements of the matrix

    Args:
        matrix (list of lists of int or float): The elements to be divided.
        div (int or float): The divisor of the matrix elements.

    Raises:
        TypeError: If a list of lists are not of integers or floats,
                    If each row of the matrix are not the same size, and
                    If the divisor is not integer or float

        ZeroDivisionError: If the divisor is equal to 0 (zero)

    Returns:
        a new matrix divided by div and rounded to 2 decimal places.
    """

    # Check if matrix is a list of lists
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, (int, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
                )

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Divide each element of the matrix by div,
    # rounding to 2 decimal places
    divided_matrix = [
            list(map(lambda x: round(x / div, 2), row)) for row in matrix
            ]

    return divided_matrix
