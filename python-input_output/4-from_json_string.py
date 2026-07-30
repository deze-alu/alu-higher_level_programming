#!/usr/bin/python3
"""Provides a function building an object out of a JSON string."""
import json


def from_json_string(my_str):
    """Returns the Python data structure represented by a JSON string."""
    return json.loads(my_str)
