#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """ Function return a list of lists of integers"""
    if n <= 0:
        return []
    triangule = [[1]]
    for line in range(1, n):
        row = [1]
        for i in range(1, line):
            row.append(triangule[line-1][i-1] + triangule[line-1][i])
        row.append(1)
        triangule.append(row)
    return triangule
