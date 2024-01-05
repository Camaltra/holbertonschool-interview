#!/usr/bin/python3

"""
Useless
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix
    :param matrix: The matrix to rotate in place
    :return: Nothing
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
