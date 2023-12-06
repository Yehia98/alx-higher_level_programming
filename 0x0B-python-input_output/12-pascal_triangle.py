#!/usr/bin/python3
"""a module of pascal triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        tr = triangle[-1]
        tm = [1]
        for x in range(len(tr) - 1):
            tm.append(tr[x] + tr[x + 1])
        tm.append(1)
        triangle.append(tm)
    return triangle
