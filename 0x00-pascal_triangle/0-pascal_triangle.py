#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Generates a Pascal's Triangle up to the nth row
        Returns an empty list when n <= 0
        Returns a list of lists containing the values"""

    if n <= 0:
        return []

    triangle = []

    # Iterate through rows starting from the 2nd row
    for i in range(1, n + 1):
        level = []
        first = 1
        for j in range(1, i + 1):
            level.append(first)
            first = first * (i - j) // j
        triangle.append(level)
    return triangle
