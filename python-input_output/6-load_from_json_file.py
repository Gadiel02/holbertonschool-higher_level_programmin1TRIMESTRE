#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    with open('input.json', 'r') as json_file:
        return json.load(json_file)
