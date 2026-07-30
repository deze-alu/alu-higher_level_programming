#!/usr/bin/python3
"""Provides a function serializing an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON string representation of an object."""
    return json.dumps(my_obj)
