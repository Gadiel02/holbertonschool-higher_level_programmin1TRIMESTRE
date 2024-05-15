#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    sets = list(set_1) + list(set_2)
    uniq = []
    for thing in sets:
        if thing not in uniq:
            uniq.append(thing)
        else:
            uniq.remove(thing)
    return uniq