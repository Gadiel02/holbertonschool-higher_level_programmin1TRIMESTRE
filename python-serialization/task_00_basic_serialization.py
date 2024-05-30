#!/usr/bin/python3
"""Basic serialization module from Python to JSON"""


import json


def serialize_and_save_to_file(data, filename):
    """Serializes and saves data to a file"""

    with open(filename, "w", encoding="utf-8") as jfile:
        json.dump(data, jfile)


def load_and_deserialize(filename):
    """Loads and deserializes data from a file"""

    with open(filename, "r", encoding="utf-8") as jfile:
        return json.load(jfile)