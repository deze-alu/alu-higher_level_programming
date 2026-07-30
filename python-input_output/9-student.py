#!/usr/bin/python3
"""Provides a student class able to describe itself with a dictionary."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student with a name and an age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description of the student."""
        return self.__dict__.copy()
