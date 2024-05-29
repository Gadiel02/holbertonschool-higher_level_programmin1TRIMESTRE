#!/usr/bin/python3
"""Defines a function to load an object from a JSON file."""

import json

def load_from_json_file(filename):
    """Load an object from a JSON file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        object: The loaded object.
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
