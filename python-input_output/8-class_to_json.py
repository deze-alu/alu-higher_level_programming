#!/usr/bin/python3
"""Provides a function describing an object with a simple dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of an object for serialization."""
    return obj.__dict__.copy()
