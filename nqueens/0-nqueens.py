#!/usr/bin/python3

"""
Answer to the N queens puzzle
"""

import sys


if __name__ == "__main__":
    """
    main function that init the algo
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    num_of_queens = int(sys.argv[1])
    if num_of_queens < 4:
        print("N must be at least 4")
        exit(1)

    res = []
    for i in range(num_of_queens):
        res.append([i, None])

    def clear_results(x):
        """
        Clear the res array, from x to num_of_queenss
        Args:
            x (int): The start
        """
        for i in range(x, num_of_queens):
            res[i][1] = None

    def possible(x, y):
        """
        Check if the queen do not attack another one
        Args:
            x (int): Position x
            y (int): Position y
        """
        for z in range(num_of_queens):
            if y == res[z][1]:
                return False
        i = 0
        while(i < x):
            if abs(res[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def nqueens(x):
        """
        Main prog
        """
        for y in range(num_of_queens):
            clear_results(x)
            if possible(x, y):
                res[x][1] = y
                if (x == num_of_queens - 1):
                    print(res)
                else:
                    nqueens(x + 1)

    nqueens(0)
