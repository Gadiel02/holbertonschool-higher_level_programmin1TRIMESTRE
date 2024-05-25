#!/usr/bin/python3
"""Simple comments"""


class SwimMixin:
    """Allows swimming"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Allows flying"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""
    def roar(self):
        print("The dragon roars!")      
