#!/usr/bin/python3
"""Provides a rectangle built on the base geometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initializes a new Rectangle after validating its two sides."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the current area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
