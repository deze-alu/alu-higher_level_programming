#!/usr/bin/python3
"""Provides a function saving an object to a file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation."""
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
