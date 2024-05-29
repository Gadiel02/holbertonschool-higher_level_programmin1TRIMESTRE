#!/usr/bin/python3
"""Module that defines a function for reading a text file."""


def read_file(filename=""):
    """Prints the contents of a UTF-8 encoded text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
