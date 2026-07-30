#!/usr/bin/python3
"""Defines a Square class whose instances can be compared."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square with the given size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validating its type and value."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Returns True if both squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Returns True if both squares have a different area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Returns True if this square has a smaller area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Returns True if this square has a smaller or equal area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Returns True if this square has a bigger area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Returns True if this square has a bigger or equal area."""
        return self.area() >= other.area()
