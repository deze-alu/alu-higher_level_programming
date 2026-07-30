#!/usr/bin/python3
"""Defines a Square class that can be printed directly."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square with the given size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validating its type and value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square after validating it."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the square drawn with the character # at its position."""
        if self.__size == 0:
            return ""
        rows = [""] * self.__position[1]
        rows += [" " * self.__position[0] + "#" * self.__size
                 for _ in range(self.__size)]
        return "\n".join(rows)

    def my_print(self):
        """Prints the square with the character # at its position."""
        print(self)
