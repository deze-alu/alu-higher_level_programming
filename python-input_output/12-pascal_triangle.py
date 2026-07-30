#!/usr/bin/python3
"""Provides a function building the Pascal's triangle of a given size."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle."""
    triangle = []
    for _ in range(n):
        if not triangle:
            triangle.append([1])
            continue
        previous = triangle[-1]
        row = [1]
        for index in range(len(previous) - 1):
            row.append(previous[index] + previous[index + 1])
        row.append(1)
        triangle.append(row)
    return triangle
