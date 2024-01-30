#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for index, item in enumerate(matrix):
        new_matrix[index] = list(map(lambda item: item**2, item))
    return new_matrix
