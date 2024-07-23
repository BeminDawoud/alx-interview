#!/usr/bin/python3
"""
Pascal Triangle
"""

from math import factorial


def element(n, k):
    """
    calculate element in pacal triangle row
    """
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def pascal_triangle_row(n):
    """
    calculate pacal triangle row
    """
    if n == 0:
        return [1]
    row = []
    for i in range(0, n + 1):
        row.append(element(n, i))
    return row


def pascal_triangle(n):
    """
    function to calculate full pacal triangle
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(0, n):
        triangle.append(pascal_triangle_row(i))
    return triangle
