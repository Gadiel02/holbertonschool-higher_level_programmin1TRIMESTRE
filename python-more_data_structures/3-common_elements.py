#!/usr/bin/python3
def common_elements(set_1, set_2):
    sets = list(set_1) + list(set_2)
    dupes = []
    uniq = []
    for thing in sets:
        if thing not in uniq:
            uniq.append(thing)
        else:
            dupes.append(thing)
    return dupes
