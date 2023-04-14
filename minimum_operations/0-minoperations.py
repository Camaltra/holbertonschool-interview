#!/usr/bin/python3

"""Useless comment"""


def minOperations(n):
    """
    Get the minum operation to get n H on a file
    :param n: The number of H to get
    :return: The number of operation
    """
    num_of_operation = 0
    num_of_h = 1
    copy_tmp = 0
    while num_of_h < n:
        if n % num_of_h == 0:
            copy_tmp = num_of_h
            num_of_h += copy_tmp
            num_of_operation += 2
        else:
            num_of_h += copy_tmp
            num_of_operation += 1
    return num_of_operation
