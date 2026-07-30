#!/usr/bin/python3
"""Provides a function detecting a strict subclass relationship."""


def inherits_from(obj, a_class):
    """Returns True if an object belongs to a strict subclass of a class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
