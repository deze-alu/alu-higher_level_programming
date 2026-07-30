#!/usr/bin/python3
"""Defines a square shape."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a rectangle whose sides are equal."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square with its size and its position."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the width and the height of the square to the same value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns the given values to the attributes of the square.

        The keyword arguments are skipped when positional ones are given.
        """
        if args:
            names = ["id", "size", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Returns the description of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
