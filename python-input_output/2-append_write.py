#!/usr/bin/python3
"""Provides a function appending a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and returns the character count."""
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
