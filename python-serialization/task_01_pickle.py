#!/usr/bin/python3
"""Custom Object Class Module for pickling"""


import pickle


class CustomObject:
    """Custom Object class for serialization"""

    def __init__(self, name="", age=0, is_student=None):
        """Instance definition of trhe custom class"""

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the class attribute values"""

        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize instance and save to the given file"""

        try:
            with open(filename, "wb") as pfile:
                pickle.dump(self, pfile)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Create an instance from the given pickle file"""

        try:
            with open(filename, "rb") as pfile:
                return pickle.load(pfile)
        except Exception:
            return None
