#!/usr/bin/python3
"""Provides a function checking the class family of an object."""


def is_kind_of_class(obj, a_class):
    """Returns True if an object belongs to the given class or a subclass."""
    return isinstance(obj, a_class)
