#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    for x, y in newdic.items():
        newdic[x] = y * 2
    return newdic
