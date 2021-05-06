#!/usr/bin/python3
"""
This is to check and see if the
matrix contains a list of integers
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    if not all(isinstance(x, list) for x in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for num in matrix:
        if not all(isinstance(a, (int, float)) for a in num):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    row = len(matrix[0])
    for i in matrix:
        if row != len(i):
            raise TypeError(
                "Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    else:
        list1 = []
        list2 = []
        new_matrix = []
        for i in matrix[0]:
            qt = round((i / 3), 2)
            list1.append(qt)
        new_matrix.append(list1)
        for i in matrix[1]:
            qt = round((i / 3), 2)
            list2.append(qt)
        new_matrix.append(list2)
        return new_matrix
