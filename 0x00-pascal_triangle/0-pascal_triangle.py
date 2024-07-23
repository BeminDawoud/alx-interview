# /usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    function to calculate full pacal triangle
    """
    from math import factorial

    if n <= 0:
        return []
    triangle = []
    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            row.append(int(factorial(i) / (factorial(j) * factorial(i - j))))
        triangle.append(row)
    return triangle
