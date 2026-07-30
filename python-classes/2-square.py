#!/usr/bin/python3
"""Defines a Square class with size validation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square, validating the type and value of size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
