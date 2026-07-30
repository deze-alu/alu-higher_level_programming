#!/usr/bin/python3
"""Indents a text.

This module holds a single function that prints a text with two new
lines after each of the characters ., ? and :
"""


def text_indentation(text):
    """Prints the given text with two new lines after ., ? and :
    The printed lines hold no leading or trailing space.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for character in text:
        line += character
        if character in ".?:":
            print(line.strip())
            print("")
            line = ""
    if line.strip() != "":
        print(line.strip(), end="")
