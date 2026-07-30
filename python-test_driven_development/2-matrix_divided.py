#!/usr/bin/python3
"""Divides all the elements of a matrix.

This module holds a single function that builds a new matrix where every
element of the given one has been divided by the same number.
"""


def matrix_divided(matrix, div):
    """Returns a new matrix holding every element divided by div.
    Each result is rounded to 2 decimal places.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(message)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(message)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
