#!/usr/bin/python3
"""defines Pascal's Triangle function"""


def pascal_triangle(n):
    """represents Pascal's Triangle of the size n
    returns a list of lists of integers that represents the triangle
    """
    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tr = tris[-1]
        tmp = [1]
        for t in range(len(tr) - 1):
            tmp.append(tr[t] + tr[t + 1])
        tmp.append(1)
        tris.append(tmp)
    return tris
