#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n + 1):
            new = []

        for j in range(i):
            if j == 0 or j == i - 1:
                new.append(1)
                continue
            new.append(triangle[-1][j - 1] + triangle[-1][j])

        if new == []:
            continue

        triangle.append(new)
    return triangle
