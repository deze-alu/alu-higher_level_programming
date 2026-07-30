#!/usr/bin/python3
"""Prints a square.

This module holds a single function that draws a square with the
character #.
"""


def print_square(size):
    """Prints a square of the given size with the character #.
    The size has to be an integer greater than or equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
