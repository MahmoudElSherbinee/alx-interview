#!/usr/bin/python3
"""
0-0x00-pascal_triangle
"""


def pascal_triangle(n):
    """
    a function def pascal_triangle(n): that returns
    a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return[]
    triangle = [[1]]    # Initialize the triangle with the first row
    for x in range(n - 1):
        row = [1]   # Start each row with a '1'
        for y in range(x):
            # Append the sum of the two elements above the current position
            row.append(triangle[-1][y] + triangle[-1][y + 1])
        row.append(1)   # End each row with a '1'
        triangle.append(row)    # Add the completed row to the triangle
    return triangle     # Return the completed triangle
