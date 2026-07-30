#!/usr/bin/python3
"""Provides a function building an object out of a JSON file."""
import json


def load_from_json_file(filename):
    """Returns the Python data structure stored in a JSON text file."""
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
