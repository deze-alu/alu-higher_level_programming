#!/usr/bin/python3
"""Provides a function writing a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file and returns the character count."""
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
