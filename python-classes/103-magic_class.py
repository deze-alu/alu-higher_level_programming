#!/usr/bin/python3
"""Defines a MagicClass matching a given Python bytecode."""
import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass with the given radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the current area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the current circumference of the circle."""
        return 2 * math.pi * self.__radius
