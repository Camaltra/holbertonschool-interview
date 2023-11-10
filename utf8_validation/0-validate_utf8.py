#!/usr/bin/python3


"""Useless comment"""


def validUTF8(data):
    """
    Validate UTF-8 data
    :param data: The data to validate
    :return: Bool
    """
    n_bytes = 0

    m1 = 1 << 7
    m2 = 1 << 6

    for i in data:
        m = 1 << 7
        if n_bytes == 0:
            while m & i:
                n_bytes += 1
                m = m >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (i & m1 and not (i & m2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
