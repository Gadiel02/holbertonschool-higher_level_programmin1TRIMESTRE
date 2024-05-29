#!/usr/bin/python3
"""Defines a function to save an object to a JSON file."""

import json

def save_to_json_file(my_obj, filename):
    """Save the object to a JSON file.

    Args:
        my_obj: The object to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
