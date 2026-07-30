#!/usr/bin/python3
"""Defines a Square class that can compute its area."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square, validating the type and value of size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
