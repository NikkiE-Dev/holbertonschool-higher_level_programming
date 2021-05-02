#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = set(set_1) | set(set_2)
    b = set(set_1).intersection(set(set_2))
    return list(a - b)
