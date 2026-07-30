#!/usr/bin/python3
"""Adds two integers.

This module holds a single function that casts both of its arguments
to integers before adding them together.
"""


def add_integer(a, b=98):
    """Returns the addition of two integers.
    Floats are casted to integers before the addition happens.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
