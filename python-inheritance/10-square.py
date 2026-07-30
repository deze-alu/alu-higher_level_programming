#!/usr/bin/python3
"""Provides a square built on the rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new Square after validating its size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
