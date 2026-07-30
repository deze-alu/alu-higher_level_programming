#!/usr/bin/python3
"""Provides a student class able to filter its dictionary description."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student with a name and an age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description of the student.

        Only the attributes listed in attrs are kept when attrs is a list
        of strings, otherwise every attribute is returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(name, str) for name in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__.copy()
