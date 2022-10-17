#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """ Function return a list of lists of integers"""
    if n <= 0:
        return []
    triangule = [[1]]
    for x in range(1, n):
        m = [1]
        for y in range(1, x):
            m.append(triangule[x-1][y-1] + triangule[x-1][y])
        m.append(1)
        triangule.append(m)
    return triangule
