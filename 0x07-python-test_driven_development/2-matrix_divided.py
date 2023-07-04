#!/usr/bin/python3

"""
A function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all element of a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list of lists containing int and floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with all elements divided by the given number
        rounded to 2 decimal places.

    Raises:
        TypeError:  If matrix is not list of int/float. 
                    If matrix is not of the same size.
                    If the div is not a number (integer or float).

        ZeroDivisionError: If div is zero.
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    count = 0
    for p in matrix:
        if not p or not isinstance(p, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers"
            "/floats")
        if count != 0 and len(p) != count:
            raise TypeError("Each row of the matrix must have the same size")

        for num in p:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")
        count = len(p)
    matrix_divide = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (matrix_divide)
