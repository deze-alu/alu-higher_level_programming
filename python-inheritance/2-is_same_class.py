#!/usr/bin/python3
"""Provides a function comparing the exact type of an object."""


def is_same_class(obj, a_class):
    """Returns True if an object is exactly an instance of the given class."""
    return type(obj) is a_class
