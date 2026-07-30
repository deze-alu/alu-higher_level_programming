#!/usr/bin/python3
"""Prints the name of a person.

This module holds a single function that prints a first name followed by
a last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints the given first name followed by the given last name.
    Both names have to be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
