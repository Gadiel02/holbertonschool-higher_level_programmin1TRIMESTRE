#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object.

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    with open('output.json', 'w') as json_file:
        json.dump(my_obj, json_file)

