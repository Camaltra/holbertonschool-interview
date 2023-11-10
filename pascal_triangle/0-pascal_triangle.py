#!/usr/bin/env python3


"""Useless comment"""


def pascal_triangle(n):
    """
    Useless comment; function should be name build_pascal_triangle
    :param n: The number of expected row of the triangle
    :return: The triangle
    """
    if n <= 0:
        return []
    triangle = [[0 for _ in range(j + 1)] for j in range(n)]
    for row_i, row in enumerate(triangle):
        row[0] = 1
        row[-1] = 1
        for elem_i in range(1, len(row) - 1):
            row[elem_i] = triangle[row_i - 1][elem_i - 1] + \
                          triangle[row_i - 1][elem_i]

    return triangle
