#!/usr/bin/python3
"""
A function that returns a list of lists of integers
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle.
    """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        pop = [1]
        for m in range(len(triangle) - 1):
            pop.append(triangle[m] + triangle[m + 1])
        pop.append(1)
        triangles.append(pop)
    return triangles
