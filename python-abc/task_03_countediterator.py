#!/usr/bin/python3
"""CountedIterator Class"""

class CountedIterator:
    """Iterator that counts items"""

    def __init__(self, data):
        """Initialize with an iterable and counter"""
        self.data = iter(data)
        self.counter = 0

    def get_count(self):
        """Return the current count"""
        return self.counter

    def __next__(self):
        """Return the next item and increment the counter"""
        try:
            item = next(self.data)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Return the iterator object itself"""
        return self

# Testing
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    counted_iterator = CountedIterator(data)

    for item in counted_iterator:
        print(f"Item: {item}, Count: {counted_iterator.get_count()}")
