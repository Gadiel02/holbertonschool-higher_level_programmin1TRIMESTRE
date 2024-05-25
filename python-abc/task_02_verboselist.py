#!/usr/bin/python3
"""Extending the Python List with Notifications"""
from abc import ABC, abstractmethod

class NotifiableList(ABC):
    """Abstract Base Class for Notifiable List"""

    @abstractmethod
    def append(self, object):
        pass

    @abstractmethod
    def extend(self, iterable):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def pop(self, index=-1):
        pass


class VerboseList(list, NotifiableList):
    """VerboseList Class implementing NotifiableList"""

    def append(self, object):
        print(f"Added [{object}] to the list.")
        return super().append(object)

    def extend(self, iterable):
        print(f"Extended the list with [{len(iterable)}] items.")
        return super().extend(iterable)

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        return super().remove(value)

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)


# Example Usage
if __name__ == "__main__":
    vl = VerboseList()
    vl.append(1)
    vl.extend([2, 3])
    vl.remove(2)
    vl.pop()
