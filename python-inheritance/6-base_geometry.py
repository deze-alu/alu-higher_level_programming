#!/usr/bin/python3
"""Provides a base class for geometry shapes."""


class BaseGeometry:
    """Represents the base of every geometry shape."""

    def area(self):
        """Raises an exception because the area is not implemented yet."""
        raise Exception("area() is not implemented")
