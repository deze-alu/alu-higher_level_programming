#!/usr/bin/python3
"""Provides a base class for geometry shapes."""


class BaseGeometry:
    """Represents the base of every geometry shape."""

    def area(self):
        """Raises an exception because the area is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
