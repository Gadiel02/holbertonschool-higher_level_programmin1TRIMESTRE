#!/usr/bin/python3
"""Abstract Animal Class and its Subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Start of the class"""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Dog subclass"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat subclass"""
    def sound(self):
        return "Meow"