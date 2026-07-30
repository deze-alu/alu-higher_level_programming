#!/usr/bin/python3
"""Provides a function printing the content of a text file."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints its whole content to stdout."""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
